###############
label A1_16a_b:


  $ persistent.scene_number = "A1_16a_b" # current scene

  "Before classes start, Erik runs into the Twins at breakfast."
  $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'meet')
  $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'meet')
  if persistent.scene_a1_08_flag == 3:
    "Erik mentions this girl who might be stalking him."

  $ persistent.scene_number = "A1_17a/b"
  "Erik has a pretty ordinary day until he goes to PE and gets knocked over by Jeanne. She gets a nosebleed."
  $ persistent.j_menu = menu_chibi(persistent.j_menu,'meet')
  if persistent.scene_a1_11_flag == 1:
    "Hertha recognized Erik."

  if persistent.j_tot > 0:
    $ persistent.scene_number = "A1_17a"
    $ persistent.scene_a1_17_flag = 1
    "Erik offers to take Jeanne to the infirmary, Hertha accepts his help."
  else:
    $ persistent.scene_number = "A1_17b"
    $ persistent.scene_a1_17_flag = 2
    "Erik leaves it to Ertha. She leaves with Jeanne."

  $ persistent.scene_number = "A1_18"
  "Erik goes back to his room and does homework."
  "Next day, he daydreams his way through class. At lunch Ela check up on him."


  ela "How are you doing?"

###############
  menu:
    "\"I'd like to meet people. Maybe join a club.\"":
      $ persistent.l_tot += 1
      $ persistent.nh_tot += 1
      $ persistent.nl_tot += 1
      $ persistent.scene_number = "A1_18a"
      $ persistent.scene_a1_18_flag = 1
      "Ela suggest the newspaper club."
      jump A1_19

    "\"I'm fine.\"":
      $ persistent.k_tot += 1
      $ persistent.a_tot += 1
      $ persistent.scene_number = "A1_18b"
      $ persistent.scene_a1_18_flag = 2
      "Satisfied, Ela talks about the upcoming festival and says she might need help."
      jump A1_19

    "\"I'm worried I might fall behind.\"":
      $ persistent.j_tot += 1
      $ persistent.scene_number = "A1_18c"
      $ persistent.scene_a1_18_flag = 3
      "Ela mentions a couple of her friends have a study group."
      jump A1_19

    "\"It's a little overwhelming.\"":
      $ persistent.i_tot += 2
      $ persistent.scene_number = "A1_18d"
      $ persistent.scene_a1_18_flag = 4
      ela "\"Really? I love it here.\""
      jump A1_19

