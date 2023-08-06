


'''
import DLA34
import DPN92
import efficient_net_b0
import Xception
import InceptionV3
import ResNeXt
import VisionTransformer

from DLA34 import dla34
from DPN92 import DPN92
from efficient_net_b0 import efficient_net_b0
from Xception import Xception
from InceptionV3 import inceptionV3
from ResNeXt import resNeXt
from VisionTransformer import visionTransformer

'''
from .DLA34 import dla34
from .DPN92 import DPN92
from .efficient_net_b0 import efficient_net_b0
from .Xception import Xception
from .InceptionV3 import inceptionV3
from .ResNeXt import resNeXt
from .VisionTransformer import visionTransformer



def list_models():
    print("models list: dla34 \n DPN92 \n efficient_net_b0 \n Xception  \n inceptionV3 \n resNeXt \n visionTransformer")
        
    return 

def create_model(name, classes):
    if name == "dla34":
        model = dla34(10)
        return model
        
    elif name == "DPN92":
        model = DPN92(10)
        return model
        
    elif name == "efficient_net_b0":
        model = efficient_net_b0(10)
        return model
        
    elif name == "Xception":
        model = Xception(10)
        return model
        
    elif name == "inceptionV3":
        model = inceptionV3(10)
        return model
    
    elif name == "resNeXt":
        model = resNeXt(10)
        return model
    
    elif name == "visionTransformer":
        model = visionTransformer(10)
        return model
        
    print("models list: dla34 \n DPN92 \n efficient_net_b0 \n Xception  \n inceptionV3 \n resNeXt \n visionTransformer")
        
    return 

'''
#model = resNeXt(10)

model = create_model('resNeXt', 10)
model.summary()

list_models()
'''


