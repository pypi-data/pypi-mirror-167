
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


class conv2d_bn(tf.keras.layers.Layer):

    def __init__(self, filters, kernel_size, strides=1):
        super(conv2d_bn, self).__init__()
        self.conv = Conv2D(filters=filters,
                           kernel_size=kernel_size,
                           strides=strides,
                           padding='same',
                           use_bias=False)
        self.bn= BatchNormalization()

    def call(self, inputs):
        x = self.conv(inputs)
        x = self.bn(x)
        return x
    
    
#####################################################################

class sep_bn(tf.keras.layers.Layer):
    def __init__(self, filters, kernel_size, strides=1):
        super(sep_bn, self).__init__()
        self.SepConv2D = SeparableConv2D(filters=filters,
                                         kernel_size=kernel_size,
                                         strides=strides,
                                         padding='same',
                                         use_bias=False)
        self.bn= BatchNormalization()

    def call(self, inputs):
        x = self.SepConv2D(inputs)
        x = self.bn(x)
        return x
    
##################################################################


class EntryFlow(tf.keras.layers.Layer):
    def __init__(self):
        super(EntryFlow, self).__init__()
        self.conv2d_bn_0 = conv2d_bn(filters=32, kernel_size=3, strides=2)
        self.relu = ReLU()
        self.conv2d_bn_1 = conv2d_bn(filters=64, kernel_size=3)
        self.sep_bn_0 = sep_bn(filters=128, kernel_size=3)
        self.sep_bn_00 = sep_bn(filters=128, kernel_size=3)
        self.maxPool2D = MaxPool2D(pool_size=3, strides=2, padding='same')
        self.conv2d_bn_2 = conv2d_bn(filters=128, kernel_size=1, strides=2)
        self.sep_bn_1 = sep_bn(filters=256, kernel_size=3)
        self.sep_bn_11 = sep_bn(filters=256, kernel_size=3)
        self.sep_bn_2 = sep_bn(filters=728, kernel_size=3)
        self.sep_bn_22 = sep_bn(filters=728, kernel_size=3)
        self.conv2d_bn_3 = conv2d_bn(filters=256, kernel_size=1, strides=2)
        self.conv2d_bn_4 = conv2d_bn(filters=728, kernel_size=1, strides=2)
        
    def call(self, inputs):
        x = self.conv2d_bn_0(inputs)
        x = self.relu(x)
        x = self.conv2d_bn_1(x)
        x_res = self.relu(x) ##
        x = self.sep_bn_0(x_res)
        x = self.relu(x)
        x = self.sep_bn_00(x)
        x = self.maxPool2D(x)
        x_res = self.conv2d_bn_2(x_res)
        x = Add()([x_res, x])
        x = self.relu(x)
        x = self.sep_bn_1(x)
        x = self.relu(x)
        x = self.sep_bn_11(x)
        x = self.maxPool2D(x)
        x_res = self.conv2d_bn_3(x_res)
        x = Add()([x_res, x])
        x = self.relu(x)
        x = self.sep_bn_2(x)
        x = self.relu(x)
        x = self.sep_bn_22(x)
        x = self.maxPool2D(x)
        x_res = self.conv2d_bn_4(x_res)
        x = Add()([x_res, x])
        
        return x
    
#############################################################################

class MiddleFlow(tf.keras.layers.Layer):
    def __init__(self):
        super(MiddleFlow, self).__init__()
        self.relu = ReLU()
        self.sep_bn = sep_bn(filters=728, kernel_size=3)

    def call(self, inputs):
        for i in range(8):
            x = self.relu(inputs)
            x = self.sep_bn(x)
            x = self.relu(x)
            x = self.sep_bn(x)
            x = self.relu(x)
            x = self.sep_bn(x)
            inputs = Add()([inputs, x])
            
        return inputs
    
    
########################################################################


class ExitFlow(tf.keras.layers.Layer):
    def __init__(self, classes):
        super(ExitFlow, self).__init__()
        self.relu = ReLU()
        self.sep_bn_0 = sep_bn(filters=728, kernel_size=3)
        self.sep_bn_1 = sep_bn(filters=1024, kernel_size=3)
        self.maxPool2D = MaxPool2D(pool_size=3, strides=2, padding='same')
        self.conv2d_bn = conv2d_bn(filters=1024, kernel_size=1, strides=2)
        self.sep_bn_2 = sep_bn(filters=1536, kernel_size=3)
        self.sep_bn_3 = sep_bn(filters=2048, kernel_size=3)
        self.GAP2D = GlobalAvgPool2D()
        self.drop = Dropout(0.5)
        self.dense = Dense(classes, activation='softmax')

    def call(self, inputs):
        x = self.relu(inputs)
        x = self.sep_bn_0(x)
        x = self.relu(x)
        x = self.sep_bn_1(x)
        x = self.maxPool2D(x)
        
        inputs = self.conv2d_bn(inputs)
        x = Add()([inputs, x])
        x = self.sep_bn_2(x)
        x = self.relu(x)
        x = self.sep_bn_3(x)
        x = self.relu(x)
        x = self.GAP2D(x)
        x = self.drop(x)###
        x = self.dense(x)
            
        return x
    
    
########################################################################


def Xception(classes=1000):
    input_layer = Input(shape = [128, 128, 3])
    x = EntryFlow()(input_layer)
    x = MiddleFlow()(x)
    x = ExitFlow(classes)(x)
    
    return Model(input_layer, x)



