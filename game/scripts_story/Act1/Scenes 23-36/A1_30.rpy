
###############
##############################
##############################
###############
label A1_30_jump:
  call A1_30b from A1_30b_ret

  "What to do..."
###############
  menu:
    "Check out the newspaper club.":
      $ persistent.l_tot += 1
      label A1_31c_d_jump:
      call A1_31c_d from A1_31c_d_ret
      jump A1_32_jump

    "See if I can find Fran.":
      call A1_30b2 from A1_30b2_ret
      jump A1_30_Q

