
##############################
############################################################
## Subroutines for the above calls are here, then the more normal layout continues from scene 46
############################################################
##############################

label A1_27a_b:
  $ persistent.scene_number = "A1_27a/b"
  if persistent.scene_a1_11_flag == 2:
    "After class, Erik decides to get the school picture out of the way. He meets Lena for the first time."
    $ persistent.l_menu = menu_chibi(persistent.l_menu,'meet')
    if persistent.scene_a1_17_flag == 1:
      "Upon seeing Erik enter, Hertha thanks him again."
    "Hertha says he can come back any time to help out, since they always need a hand."
  return

label A1_28a:
  $ persistent.scene_number = "A1_28a"
  "Erik goes to the library for a tutoring session with Jeanne. Isolda is there too."
  "He's still feeling a little awkward after the encounters with Annaliese and the twins."
  if persistent.scene_a1_17_flag == 2 and scene_a1_18_flag == 2:
    "Erik wonders if this is worth anyone's time..."
  return

label A1_28b:
  $ persistent.scene_number = "A1_28b"
  "Erik goes to the library for a tutoring session with Jeanne. Isolda is there too."
  "He's still feeling a little awkward after the encounters with Annaliese and the twins."
  if persistent.scene_a1_17_flag == 2 and scene_a1_18_flag == 2:
    "Erik wonders if this is worth anyone's time..."
  return

label A1_29a:
  $ persistent.scene_number = "A1_29a"
  "The next day, Erik goes to class. He feels like he's doing better after Jeanne's help."
  return

label A1_29b:
  $ persistent.scene_number = "A1_29b"
  "The next day, Erik goes to class. He feels like he's doing better after Jeanne's help. He wonders if he should have stuck with it."
  return

label A1_29c:
  $ persistent.scene_number = "A1_29c"
  "The next day, Erik goes to class. He feels like he's doing better after Jeanne's help. Annaliese gives him a list of albums she thinks he might like."
  return

label A1_29d:
  $ persistent.scene_number = "A1_29d"
  "The next day, Erik goes to class. He feels like he's doing better after Jeanne's help. He wonders if he should have stuck with it."
  "Annaliese gives him a list of albums she thinks he might like."
  return

label A1_30aa:
  $ persistent.scene_number = "A1_30aa"
  "Erik crosses paths with the twins and Fran after class."
  return

label A1_30aa2:
  $ persistent.scene_number = "A1_30aa"
  "Erik assumes it's a lost cause."
  return

label A1_30ab:
  $ persistent.scene_number = "A1_30ab"
  "Erik decides to apologize again for the other day. Fran razzes him for a bit, then tells him the three of them are going into town to do some drinking."
  return

label A1_30b:
  $ persistent.scene_number = "A1_30b"
  "With classes done for the day, Erik considers his options."
  return

label A1_30b2:
  $ persistent.scene_number = "A1_30b"
  "Erik finds Fran and the twins, who tell him the three of them are going into town to do some drinking."
  return

label A1_31a_b:
  $ persistent.scene_number = "A1_31a/b"
  $ club_flag = 1
  "Erik realizes he has nothing to do tonight. He decides to take Hertha up on her offer."
  "At the Newspaper Club meeting, Erik is asked to investigate something by Lena. After doing some research, Erik finds rumors of a 'werewolf' on campus."
  "Before he mentions it to Lena, Katja drops in..."
  return

label A1_31c_d:
  $ persistent.scene_number = "A1_31c/d"
  $ club_flag = 1
  "Erik decides to take Hertha up on her offer. At the Newspaper Club meeting, Erik is asked to investigate something by Lena."
  "After doing some research, Erik finds rumors of a 'werewolf' on campus. Before he mentions it to Lena, Katja drops in..."
  return

label A1_32:
  $ persistent.scene_number = "A1_32"
  "Katja comes to discuss something with Lena and to have some pictures taken. Lena ends up berating Katja for an article she was supposed to have written."
  return

label A1_32a:
  $ persistent.scene_number = "A1_32a"
  "For the remainder of the meeting, Lena treats Erik even more harshly."
  return

label A1_32b:
  $ persistent.scene_number = "A1_32b"
  "For the remainder of the meeting, Lena completely ignores Erik. He passive-agressively leaves the club early, unsure if he'll come back."
  return

label A1_33:
  $ persistent.scene_number = "A1_33"
  "Later that night, Erik heads to the woods, hoping to prove himself to Lena. AM stops him to give him a \"torch\" and to complain about her article being rejected."
  return

label A1_34:
  $ persistent.scene_number = "A1_34"
  "In the woods, Erik gets lost and trips over something, scraping himself up. Lena appears, naked, and brings him back to her room to nurse his wounds."
  "Hertha lets them into the dorm and Erik stays the night."
  return

label A1_35:
  $ persistent.scene_number = "A1_35"
  "AM stops Erik on his way back to the dorm to complain about her article being rejected."

label A1_36a:
  $ persistent.scene_number = "A1_36a"
  "Natasha and Natalya argue over whether to go out drinking or to a cafe. When pressed by Fran if he'd drink with them, Erik says \"Sure, I guess.\""
  "Fran and Natasha outvote Natalya, and they go to pick up some booze."
  if persistent.nh_tot > 1:
    "Erik manages not to embarrass himself."
    $ persistent.nh_tot = 9
    $ persistent.nl_tot = 9
  return

label A1_36b:
  $ persistent.scene_number = "A1_36b"
  "Natasha and Natalya argue over whether to go out drinking or to a cafe. When pressed by Fran if he'd drink with them, Erik says he'd rather not."
  "Fran and Natasha outvote Natalya, and they go to pick up some booze."
  if persistent.nh_tot > 1:
    "Erik manages not to embarrass himself."
    $ persistent.nh_tot = 9
    $ persistent.nl_tot = 9
  return

label A1_37a:
  $ persistent.scene_number = "A1_37a"
  "The next day, Alfons is already spreading rumors about Erik and Lena. He gives them a \"special edition\" of the Weekly Autist."
  return

label A1_37b:
  $ persistent.scene_number = "A1_37b"
  "The next day, Alfons is already spreading rumors about Erik and Lena. He gives them a \"special edition\" of the Weekly Autist."
  return

label A1_38a:
  $ persistent.scene_number = "A1_38a"
  "After an exceedingly ordinary day of classes, Erik remembers he has an appointment with Jeanne."
  return

label A1_38b:
  $ persistent.scene_number = "A1_38b"
  "After an exceedingly ordinary day of classes, Erik has to decide what to do for the rest of the day."
  return

label A1_39a:
  $ persistent.scene_number = "A1_39a"
  "Erik skips Saturday classes to mope around his room with a hangover."
  "AM checks up on him, saying the inspector sent her after noticing he wasn't in class. She reminds him to drink lots of water."
  "By the afternoon, Erik is feeling a bit better. Except he forgot about the study group. Damn."
  return

label A1_39b:
  $ persistent.scene_number = "A1_39b"
  "Erik skips Saturday classes to mope around his room with a hangover."
  "AM checks up on him, saying the inspector sent her after noticing he wasn't in class. She reminds him to drink lots of water."
  "By the afternoon, Erik is feeling a bit better."
  return

label A1_40a:
  $ persistent.scene_number = "A1_40a"
  "After an awkward day of class, Erik realizes he can only make his appointment with Jeanne and Isolda if he skips on the newspaper gig."
  return

label A1_40b:
  $ persistent.scene_number = "A1_40b"
  "After an awkward day of class, Erik takes refuge in the Newspaper Club room."
  return

label A1_41a:
  $ persistent.scene_number = "A1_41a"
  "Lena grills Erik on what he's learned, then gives him an impromptu lesson in journalism. He wonders if Jeanne will be upset that he ditched her."
  return

label A1_41a2:
  $ persistent.scene_number = "A1_41a"
  "Lena applauds him on getting to the point. Doesn't answer his question, though."
  return

label A1_41b:
  $ persistent.scene_number = "A1_41b"
  "Lena grills Erik on what he's learned, then gives him an impromptu lesson in journalism."
  return

label A1_41b2:
  $ persistent.scene_number = "A1_41b"
  "Lena gives a generic answer."
  return

label A1_41c:
  $ persistent.scene_number = "A1_41c"
  "Lena doesn't mention anything about Erik leaving last night. She grills him on what he's learned, then gives him an impromptu lesson in journalism."
  return

label A1_41d:
  $ persistent.scene_number = "A1_41d"
  "Erik decides to take Hertha up on her offer to help out at the Newspaper Club."
  "Hertha isn't there, but Lena is happy to put him to work pasting some articles together. Then she quizzes him."
  return

label A1_41:
  $ persistent.scene_number = "A1_41" # Should be after the other 41s
  "Later, the two get into a heated argument about the placement of an article. Eventually, Erik leaves in a huff."
  "He realizes that he was probably in the wrong, and plans to apologize later."
  "In the meantime, he gets some food from the lounge and goes back to his room."
  return

label A1_42a:
  $ persistent.scene_number = "A1_42a"
  "Erik goes to the next group study session to find the girls at a different table. There's no third chair."
  return

label A1_42a2:
  $ persistent.scene_number = "A1_42a"
  "Study study study. Jeanne mentions that she and Isolda are going to get dinner and says Erik is welcome to come. They leave ahead of him."
  return

label A1_42b:
  $ persistent.scene_number = "A1_42b"
  "Erik arrives for the tail end of the study session. Jeanne and Isolda have already pulled up a chair for him."
  return

label A1_42b2:
  $ persistent.scene_number = "A1_42b"
  "Jeanne summarizes what they've gone over so far. She mentions that she and Isolda are going to get dinner and says Erik is welcome to come."
  "His stomach still feels iffy, but he figures he'll make an appearance. They leave ahead of him."
  return

label A1_43a_b:
  $ persistent.scene_number = "A1_43a/b"
  "Erik goes to the library and finds Annaliese in the music section. He tries to make small talk, but she doesn't seem that interested. He sticks around and reads a book after she leaves."
  if persistent.scene_a1_24_flag == 2:
    "At first, Annaliese doesn't look too pleased to see Erik."
  return

label A1_44:
  $ persistent.scene_number = "A1_44"
  "Erik goes to dinner. On the way, he spots Annaliese by herself."
  return

label A1_44a_b_c:
  if persistent.scene_a1_24_flag < 3 and scene_a1_29_flag == 1:
    $ persistent.scene_number = "A1_44a/b"
    "He ends up buying her dinner."
    if persistent.scene_a1_24_flag == 2:
      "At first, Annaliese doesn't look too pleased to see Erik."
    return
  else:
    $ persistent.scene_number = "A1_44c"
    "He ends up buying her dinner."
  return

label A1_45a_b_c:
  if persistent.scene_a1_29_flag == 1:
    if persistent.scene_a1_30_flag == 1:
      $ persistent.scene_number = "A1_45a"
      "For the first time, the three of them talk about something other than their studies."
      return
    else: # scene_a1_30_flag == 2:
      $ persistent.scene_number = "A1_45b"
      "For the first time, the three of them talk about something other than their studies."
      return
  else: # scene_a1_29_flag == 2:
    $ persistent.scene_number = "A1_45c"
    "Erik finds Jeanne and Isolda in the cafeteria. He joins them."
    return


##############################
############################################################
## Normal layout continues from scene 46
############################################################
##############################
