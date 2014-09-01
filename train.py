import cPickle as pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import time
import random

inpts = pickle.load(open("data/coordinates.p","rb"))
targets = pickle.load(open("data/favorites.p","rb"))
for i in range (0,len(targets)):
    targets[i] = float(''.join(targets[i].split(',')))

##for i in range (0,len(inpts)):
##    inpts[i] = inpts[i][:1]

dim = len(inpts[0])
num_hidden = 65
net = buildNetwork(dim,num_hidden,1,bias=True)
ds = SupervisedDataSet(dim,1)

for i in range (0,len(inpts),4000):
    ds.addSample(inpts[i],targets[i])

trainer = BackpropTrainer(net,ds)
begin = time.time()
out = trainer.trainUntilConvergence(maxEpochs=10000,validationProportion=0.25,continueEpochs=100) #dataset=None, maxEpochs=None, verbose=None, continueEpochs=10, validationProportion=0.25
end = time.time()
print 'Time:',end-begin
print 'Error:',min(out[1]) # minimum error
print ''
pickle.dump(net,open("data/neuralnet.p",'wb'))
print(net.activate(inpts[0]))
print(net.activate(inpts[1000]))
