import cPickle as pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import time
import random

net = buildNetwork(2, 3, 1)
ds = SupervisedDataSet(2, 1)

for i in range (0,100):
    ds.addSample((0, 0), (0,))
    ds.addSample((0, 1), (1,))
    ds.addSample((1, 0), (1,))
    ds.addSample((1, 1), (0,))

