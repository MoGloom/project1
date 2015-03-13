

label __virgin_init_variables:
  python:
    # First-time init, or
    # reinit entire game if persistent.virgin_first == True
    if (persistent.virgin_first == None or persistent.virgin_first == True):
        # Reset start of game flag
        persistent.started = 0
        # TEMP select UI and/or screen rez
        if (persistent.menu_ui != 6 and not (persistent.menu_ui < 0)):
          persistent.menu_ui = 0
          persistent.show_scene_number = False
          persistent.show_girl_totals = False
          persistent.screen_width = 0
          persistent.screen_height = 0
          persistent.i_tot = 1
          persistent.j_tot = 1
          persistent.l_tot = 1
          persistent.k_tot = 1
          persistent.a_tot = 1
          persistent.nl_tot = 1
          persistent.nh_tot = 1
          persistent.am_tot = 0
  return


label __init_variables:

  # Declare characters used by this game.

  return


