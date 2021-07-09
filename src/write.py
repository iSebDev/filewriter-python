import time

import datetime

from time import sleep as wait

def __WRITE__(file=None, text=None):
  
  if not file:
    
    print("Please, set a file in config.py")
   
  elif(file == None):
    
    print("Please, set a file in config.py")
    
  else:
    
    with open(file, 'w') as f:
      
      f.write(text)
      
      
