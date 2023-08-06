import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import os
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import RandomFlip
from tensorflow.keras.layers import DepthwiseConv2D,Layer
from tensorflow.keras.preprocessing import image_dataset_from_directory


import keras

from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, Model,load_model
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint
from tensorflow.keras.layers import Dropout,ReLU,Layer, Input, add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D,MaxPool2D
from tensorflow.keras.preprocessing import image
from tensorflow.keras.initializers import glorot_uniform

# Model Checks
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score


import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc, roc_auc_score
from itertools import cycle

#Model Graphs
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from keras.layers import Activation, Lambda,GlobalAveragePooling2D,concatenate
import math
from tensorflow.keras.layers import DepthwiseConv2D
from keras.layers import SeparableConv2D,Add,GlobalAvgPool2D
from keras.layers import Resizing
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_addons as tfa

def DualPathNetwork(input_shape=None,
                    in_filters=64,
                    depth=[3, 4, 20, 3],
                    filter_increment=[16, 32, 24, 128],
                    cardinality=32,
                    width=3,
                    input_tensor=None,
                    classes=1000):

    if input_tensor is None:
        img_input = Input(shape=(128,128,3))

    x = DPN(classes, in_filters, filter_increment, depth, cardinality, width)(img_input)

    model = Model(img_input, x, name='dpn')

    # load weights

    return model

###################################################

def DPN92(input_shape=None,
          input_tensor=None,
          classes=1000):
    
    return DualPathNetwork(classes=classes)

#####################################################

class BasicBnConv(Layer):
    def __init__(self, in_filters):
        super(BasicBnConv, self).__init__()
        self.conv = Conv2D(in_filters, (7, 7), padding='same', use_bias=False, strides=(2, 2))
        self.bn = BatchNormalization()
        self.relu = ReLU()
        self.maxpool = MaxPooling2D((3, 3), strides=(2, 2), padding='same')

    def call(self, inputs):
        x = self.conv(inputs)
        x = self.bn(x)
        x = self.relu(x)
        x = self.maxpool(x)
        
        return x
    
###############################################################


class ActBnConv(Layer):
    def __init__(self, filters, cardinality=1, kernel=(3, 3), stride=(1, 1)):
        super(ActBnConv, self).__init__()
        self.conv = Conv2D(filters, kernel, padding='same', use_bias=False,  strides=stride, groups=cardinality)
        self.bn = BatchNormalization()
        self.relu = ReLU()

    def call(self, inputs):
        x = self.conv(inputs)
        x = self.bn(x)
        x = self.relu(x)
        
        return x

################################################################

class DualPathBlock(Layer):
    def __init__(self, filters_1x1_a, filters_grouped_b, filters_1x1_c, filter_increment, cardinality, block_type='normal'):
        
        super(DualPathBlock, self).__init__()
        if block_type == 'projection':
            stride = (1, 1)
            self.projection = True
        elif block_type == 'downsample':
            stride = (2, 2)
            self.projection = True
        elif block_type == 'normal':
            stride = (1, 1)
            self.projection = False
            
        if self.projection:
            self.projection_path = ActBnConv(filters=filters_1x1_c + 2 * filter_increment, kernel=(1, 1), stride=stride)
            self.input_residual_path = Lambda(lambda z: z[:, :, :, :filters_1x1_c])
            self.input_dense_path = Lambda(lambda z: z[:, :, :, filters_1x1_c:])
            
        self.c_1x1_a = ActBnConv(filters=filters_1x1_a, kernel=(1, 1))
        self.c_3x3_b = ActBnConv(filters=filters_grouped_b, cardinality=cardinality, stride=stride)
        self.c_1x1_c = ActBnConv(filters=filters_1x1_c + filter_increment, kernel=(1, 1))
        
        self.output_residual_path = Lambda(lambda z: z[:, :, :, :filters_1x1_c])
        self.output_dense_path = Lambda(lambda z: z[:, :, :, filters_1x1_c:])

    def call(self, inputs):
        n_in = concatenate(inputs, axis=3) if isinstance(inputs, list) else inputs
        
        if self.projection:
            proj_path = self.projection_path(n_in)
            in_res_path = self.input_residual_path(proj_path)
            in_dense_path = self.input_dense_path(proj_path)
        else:
            in_res_path = inputs[0]
            in_dense_path = inputs[1]
            
        x = self.c_1x1_a(n_in)
        x = self.c_3x3_b(x)
        x = self.c_1x1_c(x)
        out_res_path = self.output_residual_path(x)
        out_dense_path = self.output_dense_path(x)
        
        residual_path = add([in_res_path, out_res_path])
        dense_path = concatenate([in_dense_path, out_dense_path], axis=3)

        return [residual_path, dense_path]
    
    
######################################################

class DPN(Layer):
    def __init__(self, nb_classes, in_filters, filter_increment, depth, cardinality=32, width=3):
        
        super(DPN, self).__init__()
        self.depth_list = depth #list(depth)
        self.base_filters = 256
        self.filter_list = filter_increment
        self.filters = int(cardinality * width)
        self.filter_inc = filter_increment[0]
        
        self.basic_bn_conv = BasicBnConv(in_filters)
        
        self.gap = GlobalAveragePooling2D()
        self.max = GlobalMaxPooling2D()
        self.flatten = Flatten()
        self.dense_1 = Dense(1000, use_bias=False)
        self.dense_2 = Dense(10, use_bias=False, activation='softmax')
        
    def dualBlocks(self, filters, base_filters, filter_inc, cardinality, block_type):
        block = DualPathBlock(filters_1x1_a=filters,
                              filters_grouped_b=filters,
                              filters_1x1_c=base_filters,
                              filter_increment=filter_inc,
                              cardinality=cardinality,
                              block_type=block_type)
        return block
            
        
    def call(self, inputs):
        
        deptht = self.depth_list
        base_filters = self.base_filters
        filter_list = self.filter_list
        filters = self.filters
        
        x = self.basic_bn_conv(inputs)
        
        filter_inc = self.filter_list[0]
        
        x = self.dualBlocks(filters, base_filters, filter_inc, 32, 'projection')(x)
        
        for i in range(deptht[0] - 1):
            x = self.dualBlocks(filters, base_filters, filter_inc, 32, 'normal')(x)

        for k in range(1, len(deptht)):
            filter_inc = self.filter_list[k]
            filters *= 2
            base_filters *= 2
            
            x = self.dualBlocks(filters, base_filters, filter_inc, 32, 'downsample')(x)

            for i in range(deptht[k] - 1):
                x = self.dualBlocks(filters, base_filters, filter_inc, 32, 'normal')(x)

        x = concatenate(x, axis=-1)


        x = self.gap(x)
        #max = self.max(x)
        #x = add([avg, max])
        #x = Lambda(lambda z: 0.5 * z)(x)
        #x = Lambda(lambda z: 0.5 * z)(avg)
        #x = self.flatten(x)
        x = self.dense_1(x)
        x = self.dense_2(x)


        return x


























