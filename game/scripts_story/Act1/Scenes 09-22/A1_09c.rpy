
label A1_09c:

  $ persistent.scene_number = "A1_09c" # current scene

###############

  "She ends up not needing his help, but appreciates the offer."

  $ persistent.scene_number = "A1_09c" # current scene
  "Erik meets Claes, who takes him to class. There, Erik gives an awkward introduction and is seated next to Annaliese."
  $ persistent.a_menu = menu_chibi(persistent.a_menu,'meet')
  "He tries to talk to her but she ignores him."

  $ persistent.scene_number = "A1_10c" # current scene
  "Fran introduces him/herself after noticing Erik's failed attempt at socialization. Invites him to lunch with the twins."

  jump A1_11
