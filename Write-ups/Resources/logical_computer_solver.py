import torch
import numpy as np
import pandas as pd

layer1_bias = np.load("layer1_bias.npy")
layer1_weight = np.load("layer1_weight.npy")
layer2_weight = np.load("layer2_weight.npy")
# print(layer2_weight)

ans = [0 for _ in range(160)]
for i in range(1280):
    if layer2_weight[0][i]==1:
        temp = layer1_weight[i]
        for j in range(len(temp)):
            if temp[j]==1:
                ans[j]=1

print(ans)

def bintostr(s):  # reverse tensorize()
  power = 0
  temp = 0
  res = ''
  for x in s:
    if int(x)==1:
      temp+=2**power
    power = (power+1)%8
    if power==7:
      res+=chr(temp)
      temp = 0
  return res

print(bintostr(ans))
