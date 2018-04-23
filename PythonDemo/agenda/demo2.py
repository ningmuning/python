# -*- coding: utf8 -*-
__author__ = 'yuan'

import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD


def fib():
    from sklearn.datasets import load_iris
    iris=load_iris
    print(iris['target'])
    from sklearn.preprocessing import LabelBinarizer
    print(LabelBinarizer().fit_transform(iris['target']))

if __name__ == '__main__':
    fib()
