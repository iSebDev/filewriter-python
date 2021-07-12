from src.variables import vars as v 

## v.variable_name
## Config variables in .src/variables.py

class config:
  
  FILE="paraadads.txt" ## FILE NAME + EXTENSION || example.txt || or other extension
  OS_ALIAS="my os aliases"
  
class message:
  TEXT = f"""
  Hi1
  HI + 2
  Hi 3 _
  Example 1 2 3 {v.variable1}
  {v.variable2}
  {v.variable3}
  {v.variable4}
  {v.variable5}
  {v.variable6}
  """ 

class options:
  
  history = False
  os_aliases = True
