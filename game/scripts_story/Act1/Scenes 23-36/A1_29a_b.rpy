
###############
label A1_29a_b_jump:

  call A1_30aa from A1_30aa_ret
  if persistent.nh_tot < 1:
    call A1_30aa2 from A1_30aa2_ret
    jump A1_31a_b_jump
  else:
    call A1_30ab from A1_30ab_ret

label A1_30_Q:
    fran "\"Wanna get out of here?\""
###############
    menu:
      "I already have plans.":
        $ persistent.scene_a1_30_flag = 1
        jump A1_31a_b_jump

      "Sure.":
        $ persistent.j_tot -= 1
        $ persistent.i_tot -= 1
        $ persistent.scene_a1_30_flag = 2
        jump A1_36a_jump

label A1_31a_b_jump:
  call A1_31a_b from A1_31a_b_ret
label A1_32_jump:
  call A1_32    from A1_32_ret

  "What do I do about this?"
###############
  menu:
    "Call Lena out." if persistent.l_tot > 0:
      $ persistent.l_tot += 1
      call A1_32a from A1_32a_ret
      call A1_33  from A1_33_ret
      call A1_34  from A1_34_ret
      # Now need to branch depending how we got here
      if persistent.scene_a1_24_flag < 3:
        call A1_37a from A1_37a_ret
      else:
        call A1_37b from A1_37b_ret
      # Now need to branch depending how we got here
      if persistent.scene_a1_29_flag == 1:
        call A1_40a from A1_40a_ret

        "Choose your fate."
        ###############
        menu:
          "Newspaper":
            $ persistent.l_tot += 1
            $ persistent.j_tot -= 2
            call A1_41a from A1_41a_ret

            label A1_41a_Q:
            lena "\"Well? Ask me a question.\""
            ###############
            menu:
              "What's with the mask?":
                $ persistent.l_tot += 1
                call A1_41a2 from A1_41a2_ret

              "Why reporting?":
                call A1_41b2 from A1_41b2_ret

            call A1_41 from A1_41_ret
            jump A1_46_jump

          "Study group":
            label A1_42a_jump:
            call A1_42a from A1_42a_ret

            jeanne "\"Oh, j-just grab a chair from that table.\""
            ###############
            menu:
              "Sit next to Jeanne":
                $ persistent.j_tot += 1
                jump A1_42a2_jump

              "Sit next to Isolda":
                jump A1_42a2_jump

              "Sit across from them":
                $ persistent.i_tot += 1

            label A1_42a2_jump:
            call A1_42a2 from A1_42a2_ret
            label A1_44_jump:
            call A1_44 from A1_44_ret

            "Should I..."
            ###############
            menu:
              "Join the Frenchies":
                $ persistent.j_tot += 1
                $ persistent.i_tot += 1
                call A1_45a_b_c from A1_45a_b_c_ret

              "Talk to her":
                $ persistent.a_tot += 2
                call A1_44a_b_c from A1_44a_b_c_ret

            jump A1_46_jump

      else: # scene_a1_29_flag == 2:
        call A1_40b from A1_40b_ret
        call A1_41b from A1_41b_ret
        jump A1_41a_Q

    "Stay quiet.":
      $ persistent.k_tot += 1
      call A1_32b from A1_32b_ret
      call A1_35  from A1_35_ret
      # Now need to branch depending how we got here
      if persistent.scene_a1_29_flag == 1:
        call A1_38a from A1_38a_ret
        jump A1_42a_jump
      else: # scene_a1_29_flag == 2:
        call A1_38b from A1_38b_ret

        "What to do..."
        ###############
        menu:
          "Give the club another shot":
            $ persistent.l_tot += 1
            call A1_41c from A1_41c_ret
            jump A1_41a_Q

          "Go somewhere quiet":
            $ persistent.a_tot += 1
            call A1_43a_b from A1_43a_b1_ret
            jump A1_44_jump

