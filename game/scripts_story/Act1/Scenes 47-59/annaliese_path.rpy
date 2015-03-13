#############################################
################ ANNALIESE ##################
#############################################
label annaliese_path:
  $ persistent.a_menu = menu_chibi(persistent.a_menu,'path')

  "Erik tells Ela he'll ask Annaliese in class tomorrow."

  $ persistent.scene_number = "A1_53"
  "Annaliese doesn't seem terribly excited about it and declines."

  $ persistent.scene_number = "A1_49b"
  "Erik meets up with Ela, telling her that Lena wasn't interested. Isolda shows up and the three of them work on decorations."

  $ persistent.scene_number = "A1_58"
  "At lunch, Annaliese approaches Erik. She doesn't have anything to eat, so he offers her something from his own lunch that he hasn't touched yet."
  "He asks her if any of her family is coming to the open house, and she looks flustered. She leaves in a rush."
  "After class, Erik heads off to meet Ela and Isolda again."

  if persistent.club_flag == 1:
    $ persistent.scene_number = "A1_61c"
    "Lena corners Erik on his way to lunch. She makes a show of interrogating him on where he's been, but she doesn't really care."

  $ persistent.scene_number = "A1_63"
  "Erik goes straight to the dorm after Ela calls it a night. Lying in bed, he gets an apology from Anna in the form of a text message."

  $ persistent.scene_number = "A1_65d"
  "Beatrice calls to say she and Hilda will be attending the open house in their parents stead. The call reminds Erik that he never finished unpacking..."

  $ persistent.scene_number = "A1_66d"
  "Final day of preparations. Ela is acting strange today. She seems annoyed about something but says it's nothing."

  $ persistent.scene_number = "A1_68"
  "Ela pesters Erik about finding a date for the gala. After he leaves her, he finally texts Anna back, asking if she wants to hang out over the weekend."

  $ persistent.scene_number = "A1_70d"
  "AM stops Erik on his way back from preparations with Ela. She tells him something has come up and she needs his help. Erik says he's way too tired."

  $ persistent.scene_number = "A1_75"
  "Erik goes to the dinner and brings some leftovers to Annaliese afterward."

  $ persistent.scene_number = "A1_80"
  "Erik and Annaliese explore a few booths, ending up at a performance by the Music Club. He asks her if she's enjoying herself and she says yes."

  $ persistent.scene_number = "A1_82d"
  "Erik meets up with Ela to do the last bit of decorating for the gala."

  $ persistent.scene_number = "A1_83d"
  "And then a few more bits in the morning... Afterward, Hilda and Beatrice arrive."

  $ persistent.scene_number = "A1_87"
  "Erik spends part of the gala with his sisters, then leaves to meet up with Annaliese to listen to music and play vidya."

  "END ACT 1 (Annaliese path)"
  menu:
    "Bad ending Annaliese":
      jump end_act_1
    "Good ending Annaliese":
      $ persistent.a_menu = menu_chibi(persistent.a_menu,'good')
      jump end_act_1
    "100%% ending Annaliese":
      $ persistent.a_menu = menu_chibi(persistent.a_menu,'100%')
      jump end_act_1

