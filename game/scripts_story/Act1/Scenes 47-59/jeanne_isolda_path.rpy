#############################################
############# JEANNE + ISOLDA ###############
#############################################
label jeanne_isolda_path:
  "Ela says she knows Isolda and Jeanne and will ask them to help out, since Erik isn't sure when he'll see them next."

  $ persistent.scene_number = "A1_54"
  "Isolda and Jeanne are already helping Ela out when Erik arrives. They work on banners."

  $ persistent.scene_number = "A1_59"
  "Erik goes with Jeanne to gather materials. They go to Hertha to see if she can help get what they need."

  if persistent.club_flag == 1:
    $ persistent.scene_number = "A1_61d"
    "Lena corners Erik on his way to lunch. She makes a show of interrogating him on where he's been, but she doesn't really care."

  $ persistent.scene_number = "A1_64"
  "The three girls and Erik make way better progress than any of the above groups. To celebrate, they put off the finishing touches until tomorrow and all go to dinner together."

  $ persistent.scene_number = "A1_65e"
  "Beatrice calls to say she and Hilda will be attending the open house in their parents stead. The call reminds Erik that he never finished unpacking..."

  $ persistent.scene_number = "A1_66e"
  "Final day of preparations. Ela is acting strange today. She seems annoyed about something but says it's nothing."

  $ persistent.scene_number = "A1_69"
  "Jeanne is looking especially tired. Ela sends Erik to walk her home, hinting that he should take the opportunity to ask her to the gala."

  "Well?"
###############
  menu:
    "Ask her." if persistent.j_tot > 2:
      jump A1_70e
    "Not now." if persistent.i_tot > 2:
      jump A1_70f

label A1_70e:
  $ persistent.j_menu = menu_chibi(persistent.j_menu,'path')

  $ persistent.scene_number = "A1_70e"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_76a"
  "Erik, Jeanne, Isolda, and Ela hang out at the dinner. Jeanne acts more nervous than usual, but she seems happy."

  $ persistent.scene_number = "A1_81a"
  "Jeanne and Isolda have to work the Astronomy Club booth, but Erik visits them for a while."

  $ persistent.scene_number = "A1_82e"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83e"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_88"
  "The sisters insist on being introduced to Erik's tutor at the gala. Jeanne is overwhelmed with unexpected praise. She tries to teach Erik to dance."

  "END ACT 1 (Jeanne path)"
  menu:
    "Bad ending Jeanne":
      jump end_act_1
    "Good ending Jeanne":
      $ persistent.j_menu = menu_chibi(persistent.j_menu,'good')
      jump end_act_1
    "100%% ending Jeanne":
      $ persistent.j_menu = menu_chibi(persistent.j_menu,'100%')
      jump end_act_1

#############################################

label A1_70f:
  $ persistent.i_menu = menu_chibi(persistent.i_menu,'path')

  $ persistent.scene_number = "A1_70f"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_76b"
  "Erik, Jeanne, Isolda, and Ela hang out at the dinner. Jeanne seems distant."

  $ persistent.scene_number = "A1_81b"
  "Jeanne and Isolda have to work the Astronomy Club booth, but Erik visits them for a while."

  $ persistent.scene_number = "A1_82f"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83f"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_89"
  "Ela has to ditch at the last minute, saying something important came up."
  "Erik keeps Isolda company during the gala, but she eventually has to leave when she gets too uncomfortable with the crowd. Erik takes her back to her dorm."

  "END ACT 1 (Isolda path)"
  menu:
    "Bad ending Isolda":
      jump end_act_1
    "Good ending Isolda":
      $ persistent.i_menu = menu_chibi(persistent.i_menu,'good')
      jump end_act_1
    "100%% ending Isolda":
      $ persistent.i_menu = menu_chibi(persistent.i_menu,'100%')
      jump end_act_1

