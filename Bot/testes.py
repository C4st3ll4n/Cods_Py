from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.supervised.trainers.backprop import BackpropTrainer


ds = SupervisedDataSet(2,1)

ds.addSample((0.5, 0.6), 1.0)
ds.addSample((0.6, 0.7), 0.4)
ds.addSample((0.8, 0.3), 0.6)
ds.addSample((0.3, 0.3), 0.4)
ds.addSample((0.8, 0.2), 0.3)

nn = buildNetwork(2, 4, 1, bias=True)

t = BackpropTrainer(nn, ds)

for i in range(3000):
    t.train()
