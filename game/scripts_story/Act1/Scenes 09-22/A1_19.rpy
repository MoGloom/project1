###############
label A1_19:


  $ persistent.scene_number = "A1_19" # current scene
  "To kill time between class and his appointment with Faber, Erik wanders around the campus and decides to visit the chapel."
  "He finds Katja and Father Max there."


  $ persistent.scene_number = "A1_20" # current scene
  "After school, Erik meets Isolda in waiting area of Faber's office. She panics, thinking she needs to see a different doctor."

  "What should I do??"
###############
  menu:
    "Calm her down":
      $ persistent.nh_tot += 1
      $ persistent.nl_tot += 1
      $ persistent.scene_number = "A1_20a"
      "She feels better and eventually leaves. Erik and Faber chat."
      jump A1_21

    "Get some help":
      $ persistent.i_tot += 1
      $ persistent.scene_number = "A1_20b"
      "Faber talks to her. She leaves. Erik and Faber chat."
      jump A1_21

###############
