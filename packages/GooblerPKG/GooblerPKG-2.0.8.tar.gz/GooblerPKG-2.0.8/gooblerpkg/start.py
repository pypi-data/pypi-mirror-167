###################
### Goobler 2022 ##
###################
# Scripts made by Eric #

class Colour():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Storage:
  newClient = True

if Storage.newClient == True:
  print(Colour.HEADER + 'Setting up bot client...')
  newClient=False