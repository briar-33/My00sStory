# Этот файл можно назвать my_screens.rpy
# Здесь будут жить все ваши кастомные экраны

# =============================
# CREDITS SYSTEM FOR REN'PY
# =============================

#default images_on_screen = []

init python:
    def spawn_credit_image(images_on_screen, credits_images):
        images_on_screen.append(
            (
                renpy.random.choice(credits_images),
                renpy.random.choice([
                    renpy.random.uniform(0.05, 0.3),
                    renpy.random.uniform(0.7, 0.95)
                ]),
                renpy.random.uniform(0.2, 0.8),
                renpy.random.uniform(-10, 10)
            )
        )
        
init python:
    def full_restart_game():
        renpy.full_restart()

# --- DATA ---

# --- RANDOM POSITION HELPER ---
init python:
    import random
    def random_pos():
        return (random.random(), random.random())

# --- TRANSFORMS ---
transform smooth_scale:
    zoom 1
    subpixel True
    nearest False  # Отключает ближайший сосед, включает билинейную фильтрацию
    
transform photo_appear(xpos=0.5, ypos=0.5, rot=0):
    anchor (0.5, 0.5)  # Якорь в центре картинки
    pos (xpos, ypos)   # Позиция на экране (где будет якорь)
    rotate rot
    alpha 0.0
    zoom 1
    linear 2.5 alpha 1.0
    pause 3.5
    linear 2.0 alpha 0.0
    subpixel True
    nearest False

transform text_fade:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0


# --- SCREEN ---
screen credits(from_game_end=False):
   
    default images_on_screen = []
    default credits_images = [
    "images/titles/t1.png",
    "images/titles/t2.png",
    "images/titles/t3.png",
    "images/titles/t4.png",
    "images/titles/t5.png",
    "images/titles/t6.png",
    "images/titles/t7.png",
    "images/titles/t8.png",
    "images/titles/t9.png",
    "images/titles/t10.png",
    "images/titles/t11.png",
    "images/titles/t12.png",
    "images/titles/t13.png",
    "images/titles/t14.png",
    "images/titles/t15.png",
    "images/titles/t16.png"        
    ]
    
    default credits_pages = [
    [_("Сценарий и тексты"), "briar33"],
    [_("Программирование"), "AI / briar33"],    
    [_("Арт"), _("AI")],
    [_("Музыка"), _("AI")],
    [_("Звук"), _("Библиотеки бесплатных звуков")],  
    [_("Контакты"), "{a=mailto:briar33@proton.me}briar33@proton.me{/a}"],
    [_("{a=https://donatepay.ru/don/briar33}Поддержать{/a}"), ""]
    ]
    
    tag menu
    
    default active = True
    
    on "show" action [SetVariable("images_on_screen", []), Play("music", "audio/bg_music_s_menu.ogg", fadein=1.0), SetScreenVariable("active", True)]
    on "hide" action [SetVariable("images_on_screen", []), SetScreenVariable("active", False)]
    

    default page = 0
    
    # Background
    add Solid("#000")    
      
    # Кнопка "Назад" с условным действием
    # if from_game_end:
        # textbutton _("Назад") align (0.5, 0.95) action [Hide("credits"), Function(full_restart_game)]
    # else:
        # textbutton _("Назад") align (0.5, 0.95) action [Hide("credits"), Return()]

    
    for img_data in images_on_screen:
        $ img, xpos, ypos, rot = img_data
        
        add img at photo_appear(xpos, ypos, rot):
            # fit "contain"
            # xysize (500, 300)
            subpixel True
            nearest False               

    # --- TEXT ---
    vbox:
        align (0.5, 0.4)
        spacing 7
        for title, name in credits_pages:
            vbox:
                spacing 5
                xalign 0.5
                xmaximum 1200
                
                text title:
                    size 42
                    color "#0099cc"
                    xalign 0.5
                
                if name != "":
                    text name:
                        size 36
                        color "#FFFFFF"
                        xalign 0.5
                
                null height 20
        add "images/titles/qr_donate.png" xalign 0.5 zoom 0.25

    # --- ADD NEW RANDOM IMAGE (бесконечный цикл) ---
    
    if from_game_end:
        textbutton _("Назад") align (0.5, 0.95) action [Hide("credits"), Function(full_restart_game)]
    else:
        textbutton _("Назад") align (0.5, 0.95) action [Hide("credits"), Return()]
    
    # timer 3.5 repeat active and True action Function(
        # lambda: images_on_screen.append((
            # renpy.random.choice(credits_images),
            # renpy.random.choice([renpy.random.uniform(0.05, 0.3), renpy.random.uniform(0.7, 0.95)]),  # Только левая (0-0.3) или правая (0.7-1) часть
            # renpy.random.uniform(0.2, 0.8),  # ypos может быть любым, но не уходим слишком вверх/вниз
            # renpy.random.uniform(-10, 10)
        # ))
    # )
    
    timer 3.5 repeat True action Function(
    spawn_credit_image,
    images_on_screen,
    credits_images
)
    
screen black_with_text(message):
    default can_continue = False

    add Solid("#000000")
    
    # Основной текст
    text message:
        size 50
        color "#ffffff"
        xalign 0.5
        yalign 0.5
        
        # Ограничиваем ширину (например, 80% от ширины экрана)
        xsize 1400 
        # Выравниваем строки внутри текстового блока по центру
        text_align 0.5 
        
        at text_appear

    timer 1.5 action SetScreenVariable("can_continue", True)

    if can_continue:
        text _(_("нажмите для продолжения")):
            size 20
            color "#888888"
            xalign 0.5
            yalign 0.95
            at text_appear
            
    key "dismiss" action Return()
    key "game_menu" action Return()
    key "K_SPACE" action Return()
    key "mouseup_1" action Return()
    
transform text_appear:
    alpha 0.0
    linear 0.5 alpha 1.0

screen choice_lower(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.7
        for i in items:
            textbutton i.caption action i.action


transform dots_anim:
    alpha 0.3
    linear 0.3 alpha 1.0
    linear 0.3 alpha 0.3
    repeat

transform dots_anim_2:
    pause 0.2
    alpha 0.3
    linear 0.3 alpha 1.0
    linear 0.3 alpha 0.3
    repeat

transform dots_anim_3:
    pause 0.4
    alpha 0.3
    linear 0.3 alpha 1.0
    linear 0.3 alpha 0.3
    repeat

screen waiting_dots():
    hbox:
        spacing 4
        xalign 0.0
        yalign 0.0
        xoffset 20
        yoffset 20

        text "." at dots_anim
        text "." at dots_anim_2
        text "." at dots_anim_3
    
