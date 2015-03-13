###############
label A1_14a_b:

  if persistent.scene_a1_08_flag == 3:
    "Anne-Marie drops by"

  "After school, Erik receives an e-mail from Dr. Faber. He goes to bed with it fresh on his mind..."


  $ persistent.scene_number = "A1_15" # current scene
  "Erik has a nightmare about meeting Faber. Since the sun is already comping up, he goes outside."
  "He meets Katja."
  $ persistent.k_menu = menu_chibi(persistent.k_menu,'meet')

  "She's looking into the sun..."
###############
  menu:
    "\"You know that hurts your eyes, right?\"":
      $ persistent.i_tot += 1
      $ persistent.j_tot += 1
      jump A1_16a_b

    "(Try it)":
      $ persistent.k_tot += 2
      $ persistent.nh_tot += 1
      $ persistent.nl_tot += 1
      jump A1_16a_b

###############
