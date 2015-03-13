###############
label A1_11:


  $ persistent.scene_number = "A1_11" # current scene

  "After school, Edna asks Erik if he's had his school picture taken."

  edna "\"You'll do it promptly, I hope?\""
###############
  menu:
    "\"Yeah, sure.\"":
      $ persistent.j_tot += 1
      $ persistent.l_tot += 1
      $ persistent.scene_a1_11_flag = 1
      jump A1_12

    "\"I'll do it when I can.\"":
      $ persistent.k_tot += 1
      $ persistent.a_tot += 1
      $ persistent.scene_a1_11_flag = 2
      jump A1_14a_b

#