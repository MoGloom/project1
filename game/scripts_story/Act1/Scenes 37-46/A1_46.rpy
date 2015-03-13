
label A1_46_jump:
  $ persistent.scene_number = "A1_46"
  "It's the end of the school week, at last. Erik wanders around the grounds to gather his thoughts and reflect on the week that's gone by."
  "He ends up in the garden and has a run- in with Katja, who leaves upset. Later, Max asks Erik if he's  seen her."

  fathermax "\"I just want to make sure she's alright.\""

  menu:
    "\"I'm sure she's fine.\"" if persistent.k_tot > 1:
      $ None
    "\"I just saw her in the garden.\"":
      $ persistent.k_tot = 0

  "Erik returns to his room."

  $ persistent.scene_number = "A1_47"
  "Ela shows up at Erik's dorm room and the two of them talk about what's been going on last week."
  "Ela mentions that she needs a few extra hands to get materials and set things up for the Open House this coming week."


  ela "Do you know anyone who could help?"
###############
  menu:
    "\"There's this one girl from the Newspaper Club...\""     if persistent.l_tot > 3:
      jump lena_path
    "\"I know someone in the choir...\""                       if persistent.k_tot > 2:
      jump katja_path
    "\"There are these crazy twins and their friend...\""      if persistent.nh_tot == 9:
      jump twins_path
    "\"There's a quiet girl who sits next to me in class...\"" if persistent.a_tot > 3:
      jump annaliese_path
    "\"The girls I studied with...\""                          if persistent.j_tot + persistent.i_tot > 4:
      jump jeanne_isolda_path

