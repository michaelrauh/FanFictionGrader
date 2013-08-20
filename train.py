import pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

inpts = pickle.load(open("data/coordinates.p","rb"))
targets = pickle.load(open("data/favorites.p","rb"))
for i in range (0,len(targets)):
    targets[i] = float(''.join(targets[i].split(',')))
dim = len(inpts[0])
num_hidden = dim
net = buildNetwork(dim,num_hidden,1,bias=True)
ds = SupervisedDataSet(dim,1)

for i in range (0,len(inpts)):
    ds.addSample(inpts[i],targets[i])
    
trainer = BackpropTrainer(net,ds)
out = trainer.trainUntilConvergence(maxEpochs = 2,verbose = False) #dataset=None, maxEpochs=None, verbose=None, continueEpochs=10, validationProportion=0.25
print (min(out[1])) # minimum error
