from config import config as conf
from config import message
from config import options
from time import sleep as wait
import datetime
from src import write
import os
import json

def run():
  write.__WRITE__(file=conf.FILE, text=message.TEXT)
  wait(5)
  print(f"File: {str(os.path.isfile(conf.FILE))}")
  if options.os_aliases == True:
    print("The file '{}' was written as {} by {} !".format(conf.FILE, datetime.datetime.utcnow(), conf.OS_ALIAS))
  else:
    print("The file '{}' was written as {} by {} !".format(conf.FILE, datetime.datetime.utcnow(), os.name))
  wait(10)
        
run()
