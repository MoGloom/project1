

# The game starts here.

    # Adding about button to main menu
    #$ config.main_menu.insert(3, ('About', _intra_jumps("about", "main_game_transition"), "True"))


init python:
    # Function to set main menu "stars" correctly
    # Call with girl's define and a parameter, meaning:
    # (0) means hidden path, (1) means not hidden
    # 'meet' = have met the girl (2)
    # 'path' = have opened her path to Act 2 (3)
    # 'good' = have gotten her good ending (4)
    # '100%' = have gotten all of her endings (5)
    # Do NOT have 'meet' part of Anne-Marie's hidden path
    def menu_chibi(girl,mode):
      # global a_menu,i_menu,j_menu,l_menu,k_menu,nl_menu,nh_menu,am_menu
      if (mode == 'meet'):
        if (girl == 1):
          girl = 2
      elif (mode == 'path'):
        if (girl == 2):
          girl = 3
      elif (mode == 'good' or mode == '100%'):
        if (girl == 3 or girl == 4):
          if (persistent.am_menu == 0):
            persistent.am_menu = 1
          # Since the last 'good' hasn't copied yet,
          # check for all 4s or 5s except one 3
          # This will change Anne-Marie to 'meet'
          if (persistent.am_menu == 1 and girl == 3 and persistent.i_menu>2 and persistent.j_menu>2 and persistent.l_menu>2 and persistent.k_menu>2 and persistent.a_menu>2 and persistent.nl_menu>2 and persistent.nh_menu>2):
            tot = 0
            if (persistent.i_menu==3): tot += 1
            if (persistent.j_menu==3): tot += 1
            if (persistent.l_menu==3): tot += 1
            if (persistent.k_menu==3): tot += 1
            if (persistent.a_menu==3): tot += 1
            if (persistent.nl_menu==3): tot += 1
            if (persistent.nh_menu==3): tot += 1
            if (tot == 1):
              persistent.am_menu = 2
          if (mode == 'good' and girl < 5):
            girl = 4
          else:
            girl = 5
      else:
        renpy.error("MS: unknown chibi menu mode: %s" % mode)

      return girl



#  layout.imagemap_main_menu("images/menus/menu1.jpg", "images/menus/starnames.png", [
#    (550, 1, 680 ,130, "Start Game"),
#    (111, 313, 392, 378, "Load Game"),
#    (48, 432, 237, 529, "Preferences"),
#    (48,529,237,576, "Quit"),
#    (48, 435, 237, 482, "Help"),
#    ])


# About box
#label about:
#    python hide:
#        renpy.transition(config.intra_transition)
#        ui.window(style=style.gm_root)
#        ui.frame(ymargin=10, xmargin=10, style=style.menu_frame)
#        ui.side(['t', 'c', 'r', 'b'], spacing=2)
#
#        # Here you put the title of your VN
#        layout.label("My visual novel", None)
#
#        vp = ui.viewport(mousewheel=True)
#
#        # This is where the text will go. You can use all the usual tags.
#        ui.text("This is my first visual novel, be gentle, thank you.. :)")
#        ui.bar(adjustment=vp.yadjustment, style='vscrollbar')
#
#        layout.button(u"Return to menu", None, clicked=ui.jumps("main_menu_screen"))
#        ui.close()
#        ui.interact()
#    return

label splashscreen:
  image white = Solid("#fff")
  scene black
  $ renpy.pause(1)
  $ renpy.movie_cutscene("video/Somnova_Intro.webm")
  show movie
  play movie "video/Somnova_Intro.webm"

  return

label start:
  if (persistent.menu_ui < 0):
    $ persistent.menu_ui = -persistent.menu_ui
    return

  $ persistent.i_tot = 1
  $ persistent.j_tot = 1
  $ persistent.l_tot = 1
  $ persistent.k_tot = 1
  $ persistent.a_tot = 1
  $ persistent.nl_tot = 1
  $ persistent.nh_tot = 1
  $ persistent.am_tot = 0

label start0:
  if (persistent.menu_ui < 0):
    $ persistent.menu_ui = -persistent.menu_ui
    return

  # Debug info
  $ persistent.scene_number = "startup" # current scene

  $ virgin_init_variables()  # Init "first time run" variables
  $ init_variables()         # Init "startup" variables

  define erik = Character('Erik', color="#5d5d5d")
  define isolda = Character('Isolda', color="#5ABF90")
  define jeanne = Character('Jeanne', color="#ED0202")
  define lena = Character('Lena', color="#808000")
  define katja = Character('Katja', color="#FE8A8A")
  define annaliese = Character('Annaliese', color="#22374c")
  define natalya = Character('Natalya', color="#FF8A00")
  define natasha = Character('Natasha', color="#FABE28")
  define annemarie = Character('Anne-Marie', color="#964820")

  #Side
  define drfaber = Character('Dr. Faber', color="#BF8000")
  define principalben = Character('Principal Ben', color="#")
  define fathermax = Character('Father Max', color="#E6E6E6")
  define hertha = Character('Miss Hertha Wieck', color="#D909BA")
  define edna = Character('Miss Edna Claes', color="#D90936")
  define ela = Character('Ela', color="#683849")
  define karin = Character('Karin van Lieropp', color="#00FF00")
  define alfons = Character('Alfons Metzl', color="#")
  define fran = Character('Fran Dragovic', color="#703D6F")

  #Family Related
  #Erik
  define mark = Character('Mark Wilhelm', color="#9d9d9d")
  define father = Character('Father', color="#9d9d9d")
  define johanna = Character('Johanna Wilhelm', color="#9d9d9d")
  define mother = Character('Mother', color="#9d9d9d")
  define mom = Character('Mother', color="#9d9d9d")
  define woman = Character('Woman', color="#9d9d9d")
  define gustav = Character('Gustav Wilhelm', color="#9d9d9d")
  define hilda = Character('Brunhilde Wilhelm', color="#9d9d9d")
  define beatrice = Character('Beatrice Wilhelm', color="#9d9d9d")
  define girl = Character('Girl', color="#9d9d9d")

  #Lena
  define gunther = Character('Gunther Forst', color="#007FFF")
  define flora = Character('Flora Ackermann', color="#E48400")

  #Jeanne
  define adrienne = Character ('Adrienne Lefevre', color="#2020DE")
  define gaston = Character ('Gaston Lefevre', color="#2E0D20")

  define Voice = Character('Voice', color="#9d9d9d")

  image bg black="#000000"
  scene bg black
  with fade

  # flag that game has been started
  $ persistent.started = 1

  # Girl influence totals
  if (persistent.i_tot == None):
    $ persistent.i_tot = 1
  if (persistent.j_tot == None):
    $ persistent.j_tot = 1
  if (persistent.l_tot == None):
    $ persistent.l_tot = 1
  if (persistent.k_tot == None):
    $ persistent.k_tot = 1
  if (persistent.a_tot == None):
    $ persistent.a_tot = 1
  if (persistent.nl_tot == None):
    $ persistent.nl_tot = 1
  if (persistent.nh_tot == None):
    $ persistent.nh_tot = 1
  if (persistent.am_tot == None):
    $ persistent.am_tot = 0
  $ j_help = 0

  python:
    if (persistent.start_act == None or persistent.start_act == ""):
      persistent.start_act = "A1_01"

  # Act 1 misc flags
  $ club_flag = 0        # Default is to not have been to the club
  $ scene_a1_30_flag = 1 # This needs to be set as default in case the question is skipped

  # image movie = Movie(size=(1024, 768))

  stop movie

  # Debug info
  $ persistent.scene_number = "no scene" # current scene

  jump expression persistent.start_act.upper()[:3] + persistent.start_act.lower()[3:]

