import cPickle as pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import time
import random
inpts = pickle.load(open("data/coordinates.p","rb"))
targets = pickle.load(open("data/favorites.p","rb"))
net = pickle.load(open("data/neuralnet.p","rb"))
print net.activate(inpts[0])[0]
