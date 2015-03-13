#############################################
############## END OF ACT ONE ###############
#############################################
label end_act_1:


# label endofgame:
#   menu:
#     "Set all paths to 100%%":
#       $ persistent.a_menu = menu_chibi(persistent.a_menu,'meet')
#       $ persistent.i_menu = menu_chibi(persistent.i_menu,'meet')
#       $ persistent.l_menu = menu_chibi(persistent.l_menu,'meet')
#       $ persistent.k_menu = menu_chibi(persistent.k_menu,'meet')
#       $ persistent.j_menu = menu_chibi(persistent.j_menu,'meet')
#       $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'meet')
#       $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'meet')
#       $ persistent.am_menu = menu_chibi(persistent.am_menu,'meet')
#       $ persistent.a_menu = menu_chibi(persistent.a_menu,'path')
#       $ persistent.i_menu = menu_chibi(persistent.i_menu,'path')
#       $ persistent.l_menu = menu_chibi(persistent.l_menu,'path')
#       $ persistent.k_menu = menu_chibi(persistent.k_menu,'path')
#       $ persistent.j_menu = menu_chibi(persistent.j_menu,'path')
#       $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'path')
#       $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'path')
#       $ persistent.am_menu = menu_chibi(persistent.am_menu,'path')
#       $ persistent.a_menu = menu_chibi(persistent.a_menu,'100%')
#       $ persistent.i_menu = menu_chibi(persistent.i_menu,'100%')
#       $ persistent.l_menu = menu_chibi(persistent.l_menu,'100%')
#       $ persistent.k_menu = menu_chibi(persistent.k_menu,'100%')
#       $ persistent.j_menu = menu_chibi(persistent.j_menu,'100%')
#       $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'100%')
#       $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'100%')
#       $ persistent.am_menu = menu_chibi(persistent.am_menu,'100%')
#     "no":
#       $ None

  if persistent.am_tot > 0:
    # "States am=[persistent.am_menu] i=[persistent.i_menu] a=[persistent.a_menu] j=[persistent.j_menu] l=[persistent.l_menu] k=[persistent.k_menu] twins=[persistent.nl_menu]"
    "Totals am=[persistent.am_tot] i=[persistent.i_tot] a=[persistent.a_tot] j=[persistent.j_tot] l=[persistent.l_tot] k=[persistent.k_tot] twins=[persistent.nl_tot]"
  else:
    # "States i=[persistent.i_menu] a=[persistent.a_menu] j=[persistent.j_menu] l=[persistent.l_menu] k=[persistent.k_menu] twins=[persistent.nl_menu]"
    "Totals i=[persistent.i_tot] a=[persistent.a_tot] j=[persistent.j_tot] l=[persistent.l_tot] k=[persistent.k_tot] twins=[persistent.nl_tot]"

  return

