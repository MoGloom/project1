
label A1_36a_jump:
  # Now need to branch depending how we got here
  if persistent.scene_a1_24_flag < 3:
    call A1_36a from A1_36a_ret
  else:
    call A1_36b from A1_36b_ret
  # Now need to branch depending how we got here
  if persistent.scene_a1_29_flag == 1:
    call A1_39a from A1_39a_ret
    call A1_42b from A1_42b_ret
    call A1_42b2 from A1_42b2_ret
    jump A1_44_jump
  else: # scene_a1_29_flag == 2:
    call A1_39b from A1_39b_ret

    "What to do..."
    ###############
    menu:
      "Go somewhere quiet":
        $ persistent.a_tot += 1
        call A1_43a_b from A1_43a_b2_ret
        jump A1_44_jump

      "Check out the newspaper club":
        $ persistent.l_tot += 1
        call A1_41d from A1_41d_ret
        jump A1_41a_Q

