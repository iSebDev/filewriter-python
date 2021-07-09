from config import message
from time import sleep as wait
import datetime
from src import write
import os

def run():
  write.__WRITE__(file=config.FILE, text=message.TEXT)
  wait(5)
  print(f"File: {str(os.path.isfile(config.FILE))}")
  print("The file '{}' was written as {} by {} !".format(config.FILE, datetime.datetime.utcnow(), os.name))
  wait(10)
        
run()
