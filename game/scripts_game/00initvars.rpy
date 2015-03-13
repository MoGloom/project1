

# this adds a function that sequentially calls
# all __virgin_init_variables labels defined in your *.rpy
# files ONLY on the first play, or if
# persistent.virgin_first == True

init python:
  def virgin_init_variables():
    if (persistent.virgin_first == None or persistent.virgin_first == True):
      initvarlabels = [label for label in renpy.get_all_labels() if label.endswith('__virgin_init_variables') ]
      for l in initvarlabels:
        renpy.call_in_new_context(l)
    persistent.virgin_first = False

# this adds a function that sequentially calls
# all __init_variables labels defined in your *.rpy
# files

init python:
  def init_variables():
    initvarlabels = [label for label in renpy.get_all_labels() if label.endswith('__init_variables') ]
    for l in initvarlabels:
      renpy.call_in_new_context(l)
      

# Uncomment this bit for better 'pickle' error messages
init python:
    config.use_cpickle = False
