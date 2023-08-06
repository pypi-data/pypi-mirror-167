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

class BasicBlock(Layer):
    def __init__(self, out_channels, stride=1):
        super(BasicBlock, self).__init__()
        self.conv1 = Conv2D(out_channels, kernel_size=3, strides=stride, padding='SAME', use_bias=False)
        self.bn1 = BatchNormalization()
        self.relu = ReLU()
        self.conv2 = Conv2D(out_channels, kernel_size=3, strides=1, padding='SAME', use_bias=False)
        self.bn2 = BatchNormalization()
        
        self.stride = stride
        self.out_channels = out_channels
        self.downsample = MaxPooling2D(pool_size=stride, strides=stride)
        self.project_conv = Conv2D(out_channels, kernel_size=1, strides=1, use_bias=False)
        self.project_bn = BatchNormalization()

    def call(self, inputs, residual=None):
        if residual is None:
            residual = inputs
            if self.stride > 1:
                residual = self.downsample(residual)
            if self.out_channels != inputs.shape[3]:
                residual = self.project_conv(residual)
                residual = self.project_bn(residual)

        x = self.conv1(inputs)
        x = self.bn1(x)
        x = self.relu(x)

        x = self.conv2(x)
        x = self.bn2(x)

        x = add([x, residual])
        x = self.relu(x)

        return x

####################################################

class Root(Layer):
    def __init__(self, out_channels):
        super(Root, self).__init__()
        self.conv = Conv2D(out_channels, kernel_size=1, strides=1, use_bias=False)
        self.bn = BatchNormalization()
        self.relu = ReLU()

    def call(self, *inputs):
        x = tf.concat(inputs, axis=3)
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)

        return x
    
####################################################

class Tree(Layer):
    def __init__(self, levels, block, out_channels, stride=1, level_root=False):
        super(Tree, self).__init__()

        self.levels = levels
        self.level_root = level_root

        if levels == 1:
            self.tree1 = block(out_channels, stride)
            self.tree2 = block(out_channels, 1)
        else:
            self.tree1 = Tree(levels - 1, block, out_channels, stride)
            self.tree2 = Tree(levels - 1, block, out_channels, 1)

        if levels == 1:
            self.root = Root(out_channels)

        self.downsample = None
        if stride > 1:
            self.downsample = MaxPooling2D(pool_size=stride, strides=stride)

    def call(self, inputs, children=None):
        children = [] if children is None else children
        bottom = self.downsample(inputs) if self.downsample else inputs
        if self.level_root:  
            children.append(bottom)
        x1 = self.tree1(inputs)
        if self.levels == 1:
            x2 = self.tree2(x1)
            x1 = self.root(x1, x2, *children)
        else:
            children.append(x1)
            x1 = self.tree2(x1, children=children)
        return x1

####################################################

class DLA(Model):
    def __init__(self, levels, channels, classes=1000, block=BasicBlock, return_levels=False):
        super(DLA, self).__init__()
        self.channels = channels
        self.return_levels = return_levels
        self.base_layer = Sequential([
            Conv2D(channels[0], kernel_size=7, strides=1, padding='SAME', use_bias=False),
            BatchNormalization(),
            ReLU()
        ])
        self.level0 = Sequential([
            Conv2D(channels[0], kernel_size=3, strides=1, padding='SAME', use_bias=False),
            BatchNormalization(),
            ReLU()
        ])
        self.level1 = Sequential([
            Conv2D(channels[1], kernel_size=3, strides=2, padding='SAME', use_bias=False),
            BatchNormalization(),
            ReLU()
        ])
        self.level2 = Tree(levels[2], block, channels[2], stride=2, level_root=False)
        self.level3 = Tree(levels[3], block, channels[3], stride=2, level_root=True)
        self.level4 = Tree(levels[4], block, channels[4], stride=2, level_root=True)
        self.level5 = Tree(levels[5], block, channels[5], stride=2, level_root=True)

        self.avgpool = AveragePooling2D()
        self.flatten = Flatten()
        self.dense = Dense(classes, activation='softmax')
        
    def call(self, inputs):
        y = []
        x = self.base_layer(inputs)
        x = self.level0(x)
        y.append(x)
        x = self.level1(x)
        y.append(x)
        x = self.level2(x)
        y.append(x)
        x = self.level3(x)
        y.append(x)
        x = self.level4(x)
        y.append(x)
        x = self.level5(x)
        y.append(x)
        if self.return_levels:
            return y
        else:
            x = self.avgpool(x)
            x = self.flatten(x)
            x = self.dense(x)
            return x


####################################################

def dla34(pretrained=None,classes=1000, **kwargs):
    
    
    img_input = Input(shape=(128,128,3))
    
    x = DLA([1, 1, 1, 2, 2, 1],
                [16, 32, 64, 128, 256, 512],
                classes=classes,
                block=BasicBlock, **kwargs)(img_input)
    
    model = Model(img_input, x, name='dla34')
    
    return model






























