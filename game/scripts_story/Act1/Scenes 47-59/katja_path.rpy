#############################################
################## KATJA ####################
#############################################
label katja_path:
  $ persistent.k_menu = menu_chibi(persistent.k_menu,'path')

  "Erik tells Ela he'll try to find Katja at the chapel."

  $ persistent.scene_number = "A1_50"
  "Looking to apologize to Katja and recruit her, Erik tracks her down in the chapel and listens to her sing. She says she'll consider helping if Erik delivers a letter to Nell."

  $ persistent.scene_number = "A1_51"
  "Erik delivers the letter and meets Nell. When he returns to the chapel, he and Katja have a more casual conversation. She agrees to help Ela."

  $ persistent.scene_number = "A1_56"
  "Katja joins Ela and Erik to work on open house stuff."

  if club_flag == 1:
    $ persistent.scene_number = "A1_61a"
    "Lena corners Erik on his way to lunch. She makes a show of interrogating him on where he's been, but she doesn't really care."

  $ persistent.scene_number = "A1_65b"
  "Beatrice calls to say she and Hilda will be attending the open house in their parents stead. The call reminds Erik that he never finished unpacking..."

  $ persistent.scene_number = "A1_66b"
  "Final day of preparations. Ela is acting strange today. She seems annoyed about something but says it's nothing."

  $ persistent.scene_number = "A1_67"
  "Katja invites Erik to come to the garden. She tries to be honest about her condition but goes loopy again. Erik tells her he'll go to the gala with her."

  $ persistent.scene_number = "A1_70b"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_71"
  "Erik wakes up to meowing and finds Nell searching for Cat."

  $ persistent.scene_number = "A1_73"
  "Erik sees Katja sing with the choir at the commencement ceremony. He talks to her afterward and finds she's upset with their performance. She drags him into coming to the practice the next morning."

  $ persistent.scene_number = "A1_78"
  "Erik watches the choir practice."

  $ persistent.scene_number = "A1_82b"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83b"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_85"
  "Erik and Katja go to the gala. They don't have a chance to dance before she has to join the choir on the stage. After a song, she runs offstage and Erik follows."

  "END ACT 1 (Katja path)"
  menu:
    "Bad ending Katja":
      jump end_act_1
    "Good ending Katja":
      $ persistent.k_menu = menu_chibi(persistent.k_menu,'good')
      jump end_act_1
    "100%% ending Katja":
      $ persistent.k_menu = menu_chibi(persistent.k_menu,'100%')
      jump end_act_1

