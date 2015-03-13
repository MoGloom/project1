
label A1_09b:

  $ persistent.scene_number = "A1_09b" # current scene

###############

  "Erik escapes."

  $ persistent.scene_number = "A1_09b" # current scene
  "Erik meets Claes, who takes him to class. He's seated next to Annaliese, but isn't sure how to introduce himself."
  $ persistent.a_menu = menu_chibi(persistent.a_menu,'meet')

  $ persistent.scene_number = "A1_10b" # current scene
  "Fran introduces him/herself after noticing Erik's failed attempt at socialization. Invites him to lunch with the twins."

  jump A1_11

