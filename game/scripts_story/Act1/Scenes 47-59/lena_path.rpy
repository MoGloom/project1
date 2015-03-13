#############################################
################### LENA ####################
#############################################
label lena_path:
  $ persistent.l_menu = menu_chibi(persistent.l_menu,'path')

  "Erik tells Ela he'll ask Lena at the next club meeting."

  $ persistent.scene_number = "A1_48"
  "Lena says no. \"And you'd better not skip any club meetings for this.\""

  $ persistent.scene_number = "A1_49a"
  "Erik meets up with Ela, telling her that Lena wasn't interested. Isolda shows up and the three of them work on decorations."

  $ persistent.scene_number = "A1_55"
  "Erik struggles to juggle club duties and still help Ela and Isolda with the preparations for the open house."

  $ persistent.scene_number = "A1_60"
  "Tensions come to a head. Erik and Lena have another argument. He holds his ground."
  "Lena tells him he's going to have to help her report on the open house in order to make up for being a moron."

  $ persistent.scene_number = "A1_65a"
  "Beatrice calls to say she and Hilda will be attending the open house in their parents stead. The call reminds Erik that he never finished unpacking..."

  $ persistent.scene_number = "A1_66a"
  "Final day of preparations. Ela is acting strange today. She seems annoyed about something but says it's nothing."

  $ persistent.scene_number = "A1_70a"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_72"
  "Lena reminds Erik he's got work to do. He goes with her to the formal dinner. Lena takes pictures while Erik takes notes."

  $ persistent.scene_number = "A1_77"
  "Erik and Lena visit the booths for the article and meet most of the girls in the process."
  "Isolda and Jeanne are at the Astronomy Club booth, Katja at the Gardening Club, Fran and the twins causing mischief, and Ela making some last-minute adjustments to the decorations."

  $ persistent.scene_number = "A1_82a"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83a"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_84"
  "Lena and Erik meet up for the gala. They interview students and take lots of pictures. Afterward, they go to a rave and Erik takes E because he's feeling manly."
  "Probably should have made sure it wouldn't react with his medication. He wakes up in the hospital with Lena and his sisters."


  "END ACT 1 (Lena path)"
  menu:
    "Bad ending Lena":
      jump end_act_1
    "Good ending Lena":
      $ persistent.l_menu = menu_chibi(persistent.l_menu,'good')
      jump end_act_1
    "100%% ending Lena":
      $ persistent.l_menu = menu_chibi(persistent.l_menu,'100%')
      jump end_act_1


