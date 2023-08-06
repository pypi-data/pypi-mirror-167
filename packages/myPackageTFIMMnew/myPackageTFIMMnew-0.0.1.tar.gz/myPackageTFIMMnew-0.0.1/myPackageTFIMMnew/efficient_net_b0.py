
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

def swish(x):
    return tf.keras.activations.swish(x)


def round_filters(filters, multiplier):
    depth_divisor = 8
    min_depth = None
    min_depth = min_depth or depth_divisor
    filters = filters * multiplier
    new_filters = max(min_depth, int(filters + depth_divisor / 2) // depth_divisor * depth_divisor)
    if new_filters < 0.9 * filters:
        new_filters += depth_divisor
    return int(new_filters)


def round_repeats(repeats, multiplier):
    if not multiplier:
        return repeats
    return int(math.ceil(multiplier * repeats))


class SEBlock(tf.keras.layers.Layer):
    def __init__(self, input_channels, ratio=0.25):
        super(SEBlock, self).__init__()
        self.num_reduced_filters = max(1, int(input_channels * ratio))
        self.pool = GlobalAveragePooling2D()
        self.reduce_conv = Conv2D(filters=self.num_reduced_filters,
                                                  kernel_size=(1, 1),
                                                  strides=1,
                                                  padding="same")
        self.expand_conv = Conv2D(filters=input_channels,
                                                  kernel_size=(1, 1),
                                                  strides=1,
                                                  padding="same")

    def call(self, inputs, **kwargs):
        branch = self.pool(inputs)
        branch = tf.expand_dims(input=branch, axis=1)
        branch = tf.expand_dims(input=branch, axis=1)
        branch = self.reduce_conv(branch)
        branch = swish(branch)
        branch = self.expand_conv(branch)
        branch = tf.nn.sigmoid(branch)
        output = inputs * branch
        return output
    
###################################################################


class MBConv(tf.keras.layers.Layer):
    def __init__(self, in_channels, out_channels, expansion_factor, stride, k, drop_connect_rate):
        super(MBConv, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.stride = stride
        self.drop_connect_rate = drop_connect_rate
        self.conv1 = Conv2D(filters=in_channels * expansion_factor,
                                            kernel_size=(1, 1),
                                            strides=1,
                                            padding="same")
        self.bn1 = BatchNormalization()
        self.dwconv = DepthwiseConv2D(kernel_size=(k, k),
                                                      strides=stride,
                                                      padding="same")
        self.bn2 = BatchNormalization()
        self.se = SEBlock(input_channels=in_channels * expansion_factor)
        self.conv2 = Conv2D(filters=out_channels,
                                            kernel_size=(1, 1),
                                            strides=1,
                                            padding="same")
        self.bn3 = BatchNormalization()
        self.dropout = Dropout(rate=drop_connect_rate)

    def call(self, inputs, training=None, **kwargs):
        x = self.conv1(inputs)
        x = self.bn1(x, training=training)
        x = swish(x)
        x = self.dwconv(x)
        x = self.bn2(x, training=training)
        x = self.se(x)
        x = swish(x)
        x = self.conv2(x)
        x = self.bn3(x, training=training)
        if self.stride == 1 and self.in_channels == self.out_channels:
            if self.drop_connect_rate:
                x = self.dropout(x, training=training)
            x = tf.keras.layers.add([x, inputs])
        return x
    
####################################################################

def build_mbconv_block(in_channels, out_channels, layers, stride, expansion_factor, k, drop_connect_rate):
    block = tf.keras.Sequential()
    for i in range(layers):
        if i == 0:
            block.add(MBConv(in_channels=in_channels,
                             out_channels=out_channels,
                             expansion_factor=expansion_factor,
                             stride=stride,
                             k=k,
                             drop_connect_rate=drop_connect_rate))
        else:
            block.add(MBConv(in_channels=out_channels,
                             out_channels=out_channels,
                             expansion_factor=expansion_factor,
                             stride=1,
                             k=k,
                             drop_connect_rate=drop_connect_rate))
    return block


class EfficientNet(tf.keras.Model):
    def __init__(self,classes, width_coefficient, depth_coefficient, dropout_rate, drop_connect_rate=0.2):
        super(EfficientNet, self).__init__()
        self.NUM_CLASSES = classes
        self.conv1 = Conv2D(filters=round_filters(32, width_coefficient),
                                            kernel_size=(3, 3),
                                            strides=2,
                                            padding="same")
        self.bn1 = BatchNormalization()
        self.block1 = build_mbconv_block(in_channels=round_filters(32, width_coefficient),
                                         out_channels=round_filters(16, width_coefficient),
                                         layers=round_repeats(1, depth_coefficient),
                                         stride=1,
                                         expansion_factor=1, k=3, drop_connect_rate=drop_connect_rate)
        self.block2 = build_mbconv_block(in_channels=round_filters(16, width_coefficient),
                                         out_channels=round_filters(24, width_coefficient),
                                         layers=round_repeats(2, depth_coefficient),
                                         stride=2,
                                         expansion_factor=6, k=3, drop_connect_rate=drop_connect_rate)
        self.block3 = build_mbconv_block(in_channels=round_filters(24, width_coefficient),
                                         out_channels=round_filters(40, width_coefficient),
                                         layers=round_repeats(2, depth_coefficient),
                                         stride=2,
                                         expansion_factor=6, k=5, drop_connect_rate=drop_connect_rate)
        self.block4 = build_mbconv_block(in_channels=round_filters(40, width_coefficient),
                                         out_channels=round_filters(80, width_coefficient),
                                         layers=round_repeats(3, depth_coefficient),
                                         stride=2,
                                         expansion_factor=6, k=3, drop_connect_rate=drop_connect_rate)
        self.block5 = build_mbconv_block(in_channels=round_filters(80, width_coefficient),
                                         out_channels=round_filters(112, width_coefficient),
                                         layers=round_repeats(3, depth_coefficient),
                                         stride=1,
                                         expansion_factor=6, k=5, drop_connect_rate=drop_connect_rate)
        self.block6 = build_mbconv_block(in_channels=round_filters(112, width_coefficient),
                                         out_channels=round_filters(192, width_coefficient),
                                         layers=round_repeats(4, depth_coefficient),
                                         stride=2,
                                         expansion_factor=6, k=5, drop_connect_rate=drop_connect_rate)
        self.block7 = build_mbconv_block(in_channels=round_filters(192, width_coefficient),
                                         out_channels=round_filters(320, width_coefficient),
                                         layers=round_repeats(1, depth_coefficient),
                                         stride=1,
                                         expansion_factor=6, k=3, drop_connect_rate=drop_connect_rate)

        self.conv2 = Conv2D(filters=round_filters(1280, width_coefficient),
                                            kernel_size=(1, 1),
                                            strides=1,
                                            padding="same")
        self.bn2 = BatchNormalization()
        self.pool = GlobalAveragePooling2D()
        self.dropout = Dropout(rate=dropout_rate)
        self.fc = Dense(units=self.NUM_CLASSES,
                                        activation=tf.keras.activations.softmax)
        
        
        
    def call(self, inputs, training=None, mask=None):
        x = self.conv1(inputs)
        x = self.bn1(x, training=training)
        x = swish(x)

        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        x = self.block4(x)
        x = self.block5(x)
        x = self.block6(x)
        x = self.block7(x)

        x = self.conv2(x)
        x = self.bn2(x, training=training)
        x = swish(x)
        x = self.pool(x)
        x = self.dropout(x, training=training)
        x = self.fc(x)

        return x

###################################################
def get_efficient_net(classes,width_coefficient, depth_coefficient, resolution, dropout_rate):
    net = EfficientNet(classes=classes,width_coefficient=width_coefficient,
                       depth_coefficient=depth_coefficient,
                       dropout_rate=dropout_rate)
    net.build(input_shape=(None, resolution, resolution, 3))

    return net

###########################################

def efficient_net_b0(classes=1000):
    input_layer = Input(shape=(128,128,3,))
    x = get_efficient_net(classes,1.0, 1.0, 224, 0.2)(input_layer)
    model = Model(inputs=input_layer, outputs=x)
    return model



