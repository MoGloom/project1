
###############
label A1_24c:

  $ persistent.scene_number = "A1_24c"
  "Erik tries passing a note asking what she's listening to. She takes the head phones off so he can hear it."
  "Erik asks her name and she gives him a note of her own. He spends a little too long looking at the note and Claes snatches it away from him."
  "She calls Erik to her desk when the class breaks for lunch but lets Annaliese go without a word."

  $ persistent.scene_number = "A1_26"
  "At lunch, Erik notices that Annaliese isn't in the cafeteria. After grabbing some food, he wanders the halls in hopes of maybe running into her."
  "He finds AM instead. \"Have you lost something?\""

label A1_25a_b_jump:
  call A1_27a_b from A1_27a_b_ret
  # Now need to branch depending how we got here
  if persistent.scene_a1_24_flag < 3:
    call A1_28a from A1_28a_ret
  else:
    call A1_28b from A1_28b_ret

  jeanne "\"Should we meet again over the weekend?\""
###############
  menu:
    "\"Saturday, then?\"":
      $ persistent.j_tot += 2
      $ persistent.scene_a1_29_flag = 1
      # Now need to branch depending how we got here
      if persistent.scene_a1_24_flag < 3:
        call A1_29a from A1_29a_ret
      else:
        call A1_29b from A1_29b_ret
      jump A1_29a_b_jump

    "\"I'm all set\"":
      $ persistent.a_tot += 1
      $ persistent.scene_a1_29_flag = 2
      # Now need to branch depending how we got here
      if persistent.scene_a1_24_flag < 3:
        call A1_29c from A1_29c_ret
      else:
        call A1_29d from A1_29d_ret
      jump A1_30_jump

