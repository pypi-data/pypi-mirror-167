import sys
sys.path.append("/home/shb/SpikingNeuralNetwork/") 

from SNN import event as ev
from SNN.utils import transformer
import numpy as np
print(np.random.randint(1))
a = [1,2,3,4,5]
a[2:] = [5,6,7]
t = ev.loadaerdat("/home/shb/datasets/CIFAR10DVS/extract/airplane/cifar10_airplane_0.aedat")
print(t['x'])
print(t['y'])
t1 = transformer.EventReverse(transformer.EventReverse.x)(t)
print(t1['x'])
print(t1['y'])