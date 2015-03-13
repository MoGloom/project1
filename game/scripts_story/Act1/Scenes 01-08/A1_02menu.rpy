

label A1_02menu:
###############


  beatrice "What do you want to do?"
###############
  menu:
    "\"I'd like to go outside.\"":
      $ persistent.l_tot += 1
      $ persistent.nh_tot += 1
      $ persistent.nl_tot += 1
      $ persistent.j_tot += 1
      jump A1_02a

    "\"I don't care.\"":
      $ persistent.a_tot += 1
      $ persistent.i_tot += 1
      jump A1_02b

###############

