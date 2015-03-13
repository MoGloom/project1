#############################################
################## TWINS ####################
#############################################
label twins_path:

  "Erik tells Ela he'll ask Fran at lunch tomorrow."

  $ persistent.scene_number = "A1_52"
  "Natalya is eager to help, but Fran and Natasha aren't. After some debate, Natalya leaves with Erik and Natasha is follows reluctantly."
  "Erik, Natalya, Ela, and Isolda work hard, but Natasha bugs Natalya the whole time."

  $ persistent.scene_number = "A1_57"
  "No help from the twins today. Erik, Ela, and Isolda continue working."

  if persistent.club_flag == 1:
    $ persistent.scene_number = "A1_61b"
    "Lena corners Erik on his way to lunch. She makes a show of interrogating him on where he's been, but she doesn't really care."

  $ persistent.scene_number = "A1_62"
  "Having convinced Natasha to give it another shot, Natalya arrives to help out again. Natasha tries to be slightly useful."

  $ persistent.scene_number = "A1_65c"
  "Beatrice calls to say she and Hilda will be attending the open house in their parents stead. The call reminds Erik that he never finished unpacking..."

  $ persistent.scene_number = "A1_66c"
  "Final day of preparations. Ela is acting strange today. She seems annoyed about something but says it's nothing."

  $ persistent.scene_number = "A1_70c"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_74"
  "In class, Fran suggests Erik ditch the formal dinner with her the twins and go party. He does."

  $ persistent.scene_number = "A1_79"
  "Erik goofs off with the twins and Fran all day."

  $ persistent.scene_number = "A1_82c"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83c"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_86"
  "Erik hangs out with the twins at the gala for a bit before they all ditch for the rave. And get tanked."

  "END ACT 1 (twins path)"
  menu:
    "Bad ending Natasha":
      $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'path')
      jump end_act_1
    "Good ending Natasha":
      $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'path')
      $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'good')
      jump end_act_1
    "100%% ending Natasha":
      $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'path')
      $ persistent.nh_menu = menu_chibi(persistent.nh_menu,'100%')
      jump end_act_1
    "Bad ending Natalya":
      $ persistent.nh_menu = menu_chibi(persistent.nl_menu,'path')
      jump end_act_1
    "Good ending Natalya":
      $ persistent.nh_menu = menu_chibi(persistent.nl_menu,'path')
      $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'good')
      jump end_act_1
    "100%% ending Natalya":
      $ persistent.nh_menu = menu_chibi(persistent.nl_menu,'path')
      $ persistent.nl_menu = menu_chibi(persistent.nl_menu,'100%')
      jump end_act_1


