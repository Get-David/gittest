import gym
import numpy as np
import time

def figitize_state(observation):
    p,v,a,w = observation
    d = num_digitized
    pn = np.digitize(p,np.linespace(-2.4,2.4,d+1)[1:-1])
    return 