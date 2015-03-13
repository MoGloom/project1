
label A1_09a:

  $ persistent.scene_number = "A1_09a" # current scene

###############

  "AM says she doesn't have time explain and runs off."

  $ persistent.scene_number = "A1_09a" # current scene
  "Erik meets Claes, who takes him to class. Erik sits down next to Annaliese."
  $ persistent.a_menu = menu_chibi(persistent.a_menu,'meet')
  "He notices her headphones and compliments them. She acknowledges him, at least."

  $ persistent.scene_number = "A1_10a" # current scene
  "Fran introduces him/herself after noticing Erik sucks at socializing. Invites him to lunch with the twins."

  jump A1_11

