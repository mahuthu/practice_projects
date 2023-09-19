import sys

def linux_interaction():
  assert('linux' in sys.platform)
  print ("doing something")
try:
  linux_interaction()
except AssertionError as error:
  print(error)


try:
  with open('file.log') as file:
    read_file = file.read()
except FileNotFoundError as fnferror:

  print(fnferror)







