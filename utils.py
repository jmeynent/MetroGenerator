import numpy as np
import random

def generate_line(number_stop=None, random_number=True):
    if not isinstance(random_number, bool):
        raise ValueError("Please choose a boolean for random_number")
    if random_number==False:
        try:
            int(number_stop)
        except:
            raise ValueError('Choose a int for number_stop value')
    if random_number==True:
        binomiale = np.random.binomial(50, 0.5, 1000)
        number_stop = random.choice(binomiale)