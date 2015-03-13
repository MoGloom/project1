# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
label main_menu_reset:
screen main_menu:

  # This ensures that any other menu screen is replaced.
  tag menu

  if (persistent.menu_ui == 6):
    use main_menu_kev
  else:
    # The background of the main menu.
    window:
        style "mm_root"

    python:
      # BG stars
      ui.frame(xpos=config.screen_width/2,ypos=config.screen_height/2, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
      ui.imagebutton(im.Scale("images/menus/realstars3.png",config.screen_width, config.screen_height, bilinear=True),"images/menus/realstars3.png")


    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5

        has vbox
        textbutton _("June 9, 2013 flowchart test") action None
        textbutton _("Select test UI") action None
        textbutton _("Main Menu") action Jump("kev_ui2")
        textbutton _(" ") action None
        textbutton _("Reset all to new game") action Jump("reset_all")
        textbutton _(" ") action None
        if persistent.show_scene_number:
          textbutton _("scene number on") action Jump("tog_scene_number")
        else:
          textbutton _("scene number off") action Jump("tog_scene_number")
        if persistent.show_girl_totals:
          textbutton _("girl totals on") action Jump("tog_girl_totals")
        else:
          textbutton _("girl totals off") action Jump("tog_girl_totals")
        textbutton _("Set Starting Act") action Jump ("set_act")
        textbutton _("Set Girl Totals") action Jump ("set_girls")
        textbutton _(" ") action None
        textbutton _("800 x 450") action Jump("rez_800_450")
        textbutton _("1280 x 720") action Jump("rez_1280_720")
        textbutton _("1600 x 900") action Jump("rez_1600_900")
        textbutton _("2560 x 1440") action Jump("rez_2560_1440")
        textbutton _(" ") action None
        textbutton _("Quit") action Quit(confirm=False)

    # HOW TO ANIMATE MAIN MENU
image movie = Movie(size=(config.screen_width, config.screen_height))

init python:
    style.mm_root.background = None

label main_menu:
    scene movie

    python:
      if persistent.menu_ui == 5:
        renpy.music.play("video/starz4.ogg", channel="movie", loop=True)
      elif persistent.menu_ui == 6:
        renpy.music.play("video/background720p.webm", channel="movie", loop=True)
        renpy.music.play("music/mainmenumusic.ogg", channel="music", loop=True)
        renpy.music.set_volume(0.1, channel="music")
    jump main_menu_screen



screen main_menu_kev:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    python:
      if (persistent.k_menu > 2):
        ui.frame(xpos=524*config.screen_width/1200,ypos=154*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar1.png", 40*config.screen_width/1200, 40*config.screen_height/675, bilinear=True),"images/menus/kstar1.png")
      if (persistent.a_menu > 2):
        ui.frame(xpos=615*config.screen_width/1200,ypos=208*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar2.png", 30*config.screen_width/1200, 26*config.screen_height/675, bilinear=True),"images/menus/kstar2.png")
      if (persistent.l_menu > 2):
        ui.frame(xpos=752*config.screen_width/1200,ypos=158*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar3.png", 44*config.screen_width/1200, 39*config.screen_height/675, bilinear=True),"images/menus/kstar3.png")
      if (persistent.j_menu > 2):
        ui.frame(xpos=706*config.screen_width/1200,ypos=42*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar5.png", 22*config.screen_width/1200, 22*config.screen_height/675, bilinear=True),"images/menus/kstar5.png")
      if (persistent.i_menu > 2):
        ui.frame(xpos=663*config.screen_width/1200,ypos=87*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar5.png", 38*config.screen_width/1200, 38*config.screen_height/675, bilinear=True),"images/menus/kstar5.png")
      if (persistent.nl_menu > 2):
        ui.frame(xpos=638*config.screen_width/1200,ypos=22*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar6.png", 17*config.screen_width/1200, 17*config.screen_height/675, bilinear=True),"images/menus/kstar6.png")
      if (persistent.nh_menu > 2):
        ui.frame(xpos=647*config.screen_width/1200,ypos=13*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar6.png", 17*config.screen_width/1200, 17*config.screen_height/675, bilinear=True),"images/menus/kstar6.png")
      if (persistent.am_menu > 2):
        ui.frame(xpos=752*config.screen_width/1200,ypos=103*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/menus/kstar4.png", 27*config.screen_width/1200, 27*config.screen_height/675, bilinear=True),"images/menus/kstar4.png")

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .02

        has vbox
        textbutton _("Start") action Start()
        textbutton _("Resume") action Start("start0")
        # textbutton _("Resume") action ShowMenu("resume")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Options") action ShowMenu("preferences")
        textbutton _("Extras") action ShowMenu("preferences")
        textbutton _("Set UI") action Jump("reset_ui")
        # textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)



init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"
    style.mm_button_text.font = "Bebas.ttf"
    style.mm_button_text.size = 14

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
        if persistent.show_girl_totals:
          if persistent.am_tot == 0:
            text ("{size=11} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] {/size}")
          else:
            text ("{size=11} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] Anne-Marie:[persistent.am_tot]{/size}")
        if persistent.show_scene_number:
            text ("{size=11} [persistent.scene_number]{/size}")


init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"

    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

label reset_all:
  $ persistent.virgin_first = True
  $ persistent.menu_ui = -4
  $ virgin_init_variables()  # Init "first time run" variables
  $ init_variables()         # Init "startup" variables
  jump main_menu_reset

label reset_ui:
  $ persistent.menu_ui = -4
  return False

label set_act:
    $ persistent.start_act = renpy.input("Enter scene to start at (example: A1_04a): ")
    jump main_menu_reset

label set_girls:
    python:
      persistent.a_tot = None
      persistent.i_tot = None
      persistent.j_tot = None
      persistent.l_tot = None
      persistent.k_tot = None
      persistent.nh_tot = None
      persistent.nl_tot = None
      persistent.am_tot = None
      ints_list = []
      girllist = renpy.input("Enter a,i,j,l,k,nh,nl,am as e.g. 1,5,6,1,1,1,-1,5: ")
      if (len(girllist) > 0):
        ints_list = map(int, girllist.strip().split(','))
        if (len(ints_list) > 0):
          persistent.a_tot = ints_list[0]
        if (len(ints_list) > 1):
          persistent.i_tot = ints_list[1]
        if (len(ints_list) > 2):
          persistent.j_tot = ints_list[2]
        if (len(ints_list) > 3):
          persistent.l_tot = ints_list[3]
        if (len(ints_list) > 4):
          persistent.k_tot = ints_list[4]
        if (len(ints_list) > 5):
          persistent.nh_tot = ints_list[5]
        if (len(ints_list) > 6):
          persistent.nl_tot = ints_list[6]
        if (len(ints_list) > 7):
          persistent.am_tot = ints_list[7]

    jump main_menu_reset


label kev_ui2:
    $ persistent.menu_ui = -6
    return False

label tog_scene_number:
    $ persistent.show_scene_number = not persistent.show_scene_number
    $ renpy.call_in_new_context("main_menu")
    return False

label tog_girl_totals:
    $ persistent.show_girl_totals = not persistent.show_girl_totals
    $ renpy.call_in_new_context("main_menu")
    return False

label rez_800_450:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 800
    $ persistent.screen_height = 450
    $ renpy.set_physical_size((800,450))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_1280_720:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 1280
    $ persistent.screen_height = 720
    $ renpy.set_physical_size((1280,720))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_1600_900:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 1600
    $ persistent.screen_height = 900
    $ renpy.set_physical_size((1600,900))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_2560_1440:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 2560
    $ persistent.screen_height = 1440
    $ renpy.set_physical_size((2560,1440))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

