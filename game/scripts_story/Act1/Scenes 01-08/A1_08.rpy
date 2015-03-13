

###############
label A1_08:

  $ persistent.scene_number = "A1_08a" # current scene

  annemarie "\"I just need you to...\""
###############
  menu:
    "\"Who are you again?\"":
      $ persistent.a_tot += 1
      $ persistent.l_tot += 1
      $ persistent.scene_a1_08_flag = 1
      jump A1_09a

    "\"Maybe some other time.\"":
      $ persistent.i_tot += 1
      $ persistent.k_tot += 1
      $ persistent.scene_a1_08_flag = 2
      jump A1_09b

    "\"Uh... alright.\"":
      $ persistent.j_tot += 1
      $ persistent.scene_a1_08_flag = 3
      jump A1_09c

