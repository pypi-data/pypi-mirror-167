
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

    def __init__(self):
        super(conv2d_bn, self).__init__()
        self.conv_0 = Conv2D(128, (1, 1),strides=(2, 2), padding = 'same')
        self.bn_0 = BatchNormalization(axis=3)
        self.act_0 = Activation('relu')
        self.conv_1 = Conv2D(64, (3, 3),strides=(1, 1), padding = 'same')
        self.bn_1 = BatchNormalization(axis=3)
        self.act_1 = Activation('relu')
        self.conv_2 = Conv2D(32, (3, 3),strides=(1, 1), padding = 'same')
        self.bn_2 = BatchNormalization(axis=3)


    def call(self, inputs):
        x = self.conv_0(inputs)
        x = self.bn_0(x)
        x = self.act_0(x)
        x = self.conv_1(x)
        x = self.bn_1(x)
        x = self.act_1(x)
        x = self.conv_2(x)
        x = self.bn_2(x)
        return x
    
###############################################################

class parallel_blocks(tf.keras.layers.Layer):

    def __init__(self, conv_block=None):
        super(parallel_blocks, self).__init__()
        if conv_block is None:
            conv_block = conv2d_bn
        
        self.layers_parallel = list()
        self.cardinality = 4

    def call(self, inputs):
        for i in range(cardinality) :
          # conv2d_bn can be called many times
            parallel = conv_block(inputs)
            self.layers_parallel.append(parallel)

        return concatenate(layers_parallel)
###############################################################

class ResNeXt(Model):

    def __init__(self, classes):
        super(ResNeXt, self).__init__()
        self.classes = classes
        
        #self.block_1 = parallel_blocks()
        self.conv_0 = Conv2D(128, (1, 1),strides=(2, 2), padding = 'same')
        self.bn_0= BatchNormalization(axis=3)
        
        self.act_0 = Activation('relu')
        
        self.gap_pool_2D_0 = GlobalAveragePooling2D()
        self.drop = Dropout(.3)
        self.dense_0 = Dense(128, activation='relu')
        self.dense_1 = Dense(classes, activation='softmax')

    def call(self, inputs):
        x = inputs
        # Block 1
        #x = self.block_1(x_input)
        x = parallel_blocks(inputs)

        # 1*1conv layer to transform the input shape

        x2 = inputs
        x2 = self.conv_0(x2)
        x = self.bn_0(x2)

        # Residual connection
        x = Add()([x, x2])     
        x = self.act_0(x)
    
        x = self.gap_pool_2D_0(x)
        x = self.drop(x)
        x = self.dense_0(x)
        x = self.dense_1(x)
        
        return x

###############################################################


def resNeXt(classes=1000):
    
    input_layer = Input(shape=(128,128,3,))
    x = ResNeXt(classes)(input_layer)
    
    return Model(inputs=input_layer, outputs=x)