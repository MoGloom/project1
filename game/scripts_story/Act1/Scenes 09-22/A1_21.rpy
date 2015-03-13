###############
label A1_21:


  $ persistent.scene_number = "A1_21" # current scene
  "Anne-marie trackes Erik down after his session with Faber."

  if persistent.scene_a1_08_flag == 3:
    "Erik interrupts when she shows up to ask if she knows him."
  else:
    "She comments subtly on the player's choices. As she leaves, she calls him Watson."

  $ persistent.scene_number = "A1_22"
  "Erik goes back to his room and checks his computer before bed."
  "There's an e-mail from Edna asking Erik to stop by her office in the morning."
  if persistent.scene_a1_11_flag == 2:
    "There's also a reminder about school pictures."

  $ persistent.scene_number = "A1_23"
  "Erik visits Edna's office before class and is introduced to Jeanne as Erik's new study partner."
  if persistent.scene_a1_17_flag == 2:
    "Jeanne smiles and replies that they have already met."
  "They agree to meet after class."

  $ persistent.scene_number = "A1_24"
  "In class, Erik notices Annaliese has pulled up her hood and looks to be listening to music."
  "During the downtime between periods, he tries to ask what she's listening to. She doesn't hear him."
  "Across the room, Fran laughs and shakes her head."

  "How do I get her attention?"
###############
  menu:
    "Give up":
      $ persistent.i_tot += 1
      $ persistent.scene_a1_24_flag = 1
      jump A1_24a

    "Tap her on the shoulder":
      $ persistent.l_tot += 2
      $ persistent.scene_a1_24_flag = 2
      jump A1_24b

    "Pass a note" if persistent.a_tot > 0:
      $ persistent.a_tot += 2
      $ persistent.scene_a1_24_flag = 3
      jump A1_24c

###############
##############################
## Up to scene 46, some common scenes are called as subroutines
##############################
###############
