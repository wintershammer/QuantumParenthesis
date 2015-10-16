import numpy as np
import random

def stateComp(states):
    compositeState = states[0]
    for state in states[1:]:
        compositeState =  np.kron(compositeState,state)
    return compositeState

def pick_random(distribution):
  for (x,y) in distribution:
      print("Probability of state", x, "is" , y)
      
  r, s = random.random(), 0
  for num in distribution:
    s += num[1]
    if s >= r:
      print("System collapsed to state:",num[0])
      return num[0]

def measure(state):
    x = list()
    i = 0
    for amplitude in state:
        x.append([i,np.absolute(state[i])**2/np.linalg.norm(state)**2])
        i += 1
    return (pick_random(x))


