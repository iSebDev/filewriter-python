import datetime
import random

class vars:
    variable1 = 1+1 # Simple sum in variable
    variable2 = "Hi" # Simple str var
    variable3 = "Hi {}".format(15-5) # Variables in str of var
    variable4 = datetime.datetime.utcnow() # Get time
    variable5 = random.randint(1,100) # Get random number variable
    variable6 = random.choice([variable1,variable2,variable3]) # Get random variable
