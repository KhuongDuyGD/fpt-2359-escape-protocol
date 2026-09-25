# Self-contained 1280x720 UI. The default Ren'Py keyboard and mouse bindings
# still supply normal advance, rollback, skip, and auto-forward behavior.

screen say(who, what):
    # Keep the speaker and every wrapped line inside one fixed dialogue panel.
    # Reserving the name row also keeps narrator text aligned with dialogue.
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1240
        ysize 204
        xpadding 30
        ypadding 20
        background Solid("#101827f2")
        vbox:
            xfill True
            spacing 8
            if who is not None:
                text who id "who" size 26 color "#ffd37b"
            else:
                null height 31
            text what id "what" xsize 1180 size 27 color "#f4f6fb" text_align 0.0
    use quick_menu


screen choice(items):
    modal True
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 18
        for item in items:
            textbutton item.caption:
                action item.action
                xminimum 640
                text_size 28
                padding (24, 14)
                background Solid("#253659ef")
                hover_background Solid("#426195")
    use quick_menu


screen quick_menu():
    zorder 90
    frame:
        xalign 0.5
        yalign 0.685
        xpadding 16
        ypadding 5
        background Solid("#101827e8")
        hbox:
            spacing 14
            textbutton "Back" action Rollback() text_size 16
            textbutton "History" action ShowMenu("history") text_size 16
            textbutton "Skip" action Skip() text_size 16
            textbutton "Auto" action Preference("auto-forward", "toggle") text_size 16
            textbutton "Save" action ShowMenu("save") text_size 16
            textbutton "Load" action ShowMenu("load") text_size 16
            textbutton "Prefs" action ShowMenu("preferences") text_size 16


screen stats_hud():
    zorder 80
    frame:
        xalign 0.99
        yalign 0.02
        xpadding 16
        ypadding 10
        background Solid("#0c1421dc")
        vbox:
            spacing 2
            text "ENERGY  [energy]" size 20 color "#b2f5cb"
            text "SANITY  [sanity]" size 20 color "#d2c5ff"
            text "PENDING TASKS  [pending_tasks]" size 20 color "#ffcf9c"
            text "ESCAPE POINTS  [escape_point]" size 20 color "#91ddff"


screen boss_title(title, subtitle):
    modal True
    zorder 100
    add Solid("#090e1bf4")
    vbox:
        xalign 0.5
        yalign 0.48
        spacing 24
        text "BOSS ENCOUNTER" xalign 0.5 size 26 color "#ff6577"
        text title xalign 0.5 size 66 bold True color "#ffffff"
        text subtitle xalign 0.5 size 23 color "#ffcf86"
    text "Click to continue" xalign 0.5 yalign 0.91 size 18 color "#9faec3"
    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        background None
        action Return()


screen main_menu():
    tag menu
    add "bedroom_gaming"
    add Solid("#080e1dbb")
    vbox:
        xpos 95
        yalign 0.42
        spacing 16
        text "FPT: 23:59" size 68 bold True color "#ffffff"
        text "ESCAPE PROTOCOL" size 38 color "#ffbd70"
        null height 20
        textbutton "Start Game" action Start() text_size 27
        textbutton "Load Game" action ShowMenu("load") text_size 27
        textbutton "Ending Gallery" action ShowMenu("ending_gallery") text_size 27
        textbutton "Preferences" action ShowMenu("preferences") text_size 27
        textbutton "Quit" action Quit(confirm=True) text_size 27


screen menu_navigation():
    hbox:
        xalign 0.5
        yalign 0.91
        spacing 26
        textbutton "Return" action Return() text_size 21
        textbutton "Save" action ShowMenu("save") text_size 21
        textbutton "Load" action ShowMenu("load") text_size 21
        textbutton "History" action ShowMenu("history") text_size 21
        textbutton "Preferences" action ShowMenu("preferences") text_size 21
        textbutton "Gallery" action ShowMenu("ending_gallery") text_size 21
        textbutton "Main Menu" action MainMenu(confirm=True) text_size 21


screen save():
    tag menu
    add Solid("#11192b")
    text "SAVE GAME" xalign 0.5 ypos 40 size 42 bold True
    use file_slot_grid("save")
    use menu_navigation


screen load():
    tag menu
    add Solid("#11192b")
    text "LOAD GAME" xalign 0.5 ypos 40 size 42 bold True
    use file_slot_grid("load")
    use menu_navigation


screen file_slot_grid(mode):
    grid 3 2:
        xalign 0.5
        yalign 0.47
        spacing 22
        for slot in range(1, 7):
            frame:
                xsize 355
                ysize 230
                background Solid("#263651")
                if mode == "save":
                    button:
                        xfill True
                        yfill True
                        action FileSave(slot)
                        vbox:
                            spacing 8
                            text "SLOT [slot]" size 23
                            add FileScreenshot(slot) xsize 310 ysize 145
                            text FileTime(slot, format="%d/%m/%Y %H:%M", empty="Empty") size 17
                else:
                    button:
                        xfill True
                        yfill True
                        action FileLoad(slot)
                        sensitive FileLoadable(slot)
                        vbox:
                            spacing 8
                            text "SLOT [slot]" size 23
                            add FileScreenshot(slot) xsize 310 ysize 145
                            text FileTime(slot, format="%d/%m/%Y %H:%M", empty="Empty") size 17


screen preferences():
    tag menu
    add Solid("#11192b")
    text "PREFERENCES" xalign 0.5 ypos 40 size 42 bold True
    frame:
        xalign 0.5
        yalign 0.43
        xsize 820
        xpadding 40
        ypadding 30
        background Solid("#263651")
        vbox:
            spacing 20
            hbox:
                spacing 25
                text "Display" size 24
                textbutton "Window" action Preference("display", "window")
                textbutton "Fullscreen" action Preference("display", "fullscreen")
            text "Text Speed" size 24
            bar value Preference("text speed") xsize 720
            text "Auto Speed" size 24
            bar value Preference("auto-forward time") xsize 720
            text "Music Volume" size 24
            bar value Preference("music volume") xsize 720
            text "Sound Volume" size 24
            bar value Preference("sound volume") xsize 720
    use menu_navigation


screen history():
    tag menu
    add Solid("#11192b")
    text "DIALOGUE HISTORY" xalign 0.5 ypos 35 size 42 bold True
    frame:
        xpos 110
        ypos 105
        xsize 1060
        ysize 520
        background Solid("#263651")
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            vbox:
                spacing 18
                for entry in _history_list:
                    if entry.who:
                        text entry.who size 21 color "#ffcf83"
                    text entry.what size 23 substitute False xmaximum 965
    use menu_navigation


screen ending_gallery():
    tag menu
    add Solid("#11192b")
    text "ENDING GALLERY" xalign 0.5 ypos 52 size 46 bold True
    hbox:
        xalign 0.5
        yalign 0.46
        spacing 28
        frame:
            xsize 500
            ysize 280
            background Solid("#20443b" if persistent.good_ending_unlocked else "#29303c")
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 17
                text "GOOD ENDING — ESCAPE SUCCESSFUL" size 27 xalign 0.5 xmaximum 450 text_align 0.5
                if persistent.good_ending_unlocked:
                    textbutton "View ending" action Show("gallery_detail", ending="good") xalign 0.5
                else:
                    text "LOCKED" size 22 color "#9ba6b7" xalign 0.5
        frame:
            xsize 500
            ysize 280
            background Solid("#512d38" if persistent.bad_ending_unlocked else "#29303c")
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 17
                text "BAD ENDING — FPT HAS CONSUMED YOU" size 27 xalign 0.5 xmaximum 450 text_align 0.5
                if persistent.bad_ending_unlocked:
                    textbutton "View ending" action Show("gallery_detail", ending="bad") xalign 0.5
                else:
                    text "LOCKED" size 22 color "#9ba6b7" xalign 0.5
    use menu_navigation


screen gallery_detail(ending):
    modal True
    zorder 120
    add Solid("#080d18ed")
    vbox:
        xalign 0.5
        yalign 0.47
        spacing 25
        if ending == "good":
            text "GOOD ENDING — ESCAPE SUCCESSFUL" xalign 0.5 size 45 color "#a7f0be"
            text "Student Status: ALIVE\nEnergy: ENOUGH FOR ONE MORE GAME\nTomorrow: PROBLEM FOR TOMORROW" xalign 0.5 text_align 0.5 size 26
        else:
            text "BAD ENDING — FPT HAS CONSUMED YOU" xalign 0.5 size 45 color "#ff8190"
            text "Student Status: DECEASED*\n*Vẫn phải đi học ngày mai.\nSanity: SEGMENTATION FAULT" xalign 0.5 text_align 0.5 size 26
        textbutton "Close" action Hide("gallery_detail") xalign 0.5


screen ending_card(kind, subtitle, details):
    modal True
    add Solid("#080d18")
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 26
        text kind xalign 0.5 size 54 bold True color ("#a7f0be" if kind == "GOOD ENDING" else "#ff8190")
        text subtitle xalign 0.5 size 37 color "#ffffff"
        text details xalign 0.5 text_align 0.5 size 24 color "#dce4ef"
        textbutton "Continue" action Return() xalign 0.5 text_size 23


screen post_ending_actions():
    modal True
    add Solid("#080d18df")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22
        text "THE END" xalign 0.5 size 52 bold True
        textbutton "Start New Game+" action Jump("new_game_plus") xalign 0.5 text_size 28
        textbutton "Return to Main Menu" action MainMenu(confirm=False) xalign 0.5 text_size 28


screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#080d18df")
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 45
        ypadding 35
        background Solid("#263651")
        vbox:
            spacing 25
            text message size 26
            hbox:
                xalign 0.5
                spacing 30
                textbutton "Yes" action yes_action
                textbutton "No" action no_action


screen notify(message):
    zorder 210
    frame:
        xalign 0.99
        yalign 0.07
        background Solid("#314460ed")
        text message size 20
    timer 2.5 action Hide("notify")
