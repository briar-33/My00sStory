# ░ ▒ ▓ █ ▄ ▀ ■ ▚ ▞ ▒
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    renpy.music.register_channel("music2", "music", True, True)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)

init:
    
    default is_waiting = False
    
    # Фоны
    image bg_cinema_future = "images/bg/bg_cinema_future_1.png"      # Фон    
    image bg_cinema_future_entrance = "images/bg/bg_cinema_future_entrance.png"      # Фон    
    image bg_city_street = "images/bg/bg_city_street_1.png"      # Фон    
    image bg_dima_busstop = "images/bg/bg_dima_busstop.png"      # Фон
    image bg_dima_flat_corridor = "images/bg/bg_dima_flat_corridor_1.png"      # Фон
    image bg_dima_flat_corridor_dark = "images/bg/bg_dima_flat_corridor_dark_1.png"      # Фон
    image bg_dima_flat_room = "images/bg/bg_dima_flat_room.png"      # Фон
    image bg_dima_flat_room_evn = "images/bg/bg_dima_flat_room_evn.png"      # Фон    
    image bg_dima_flat_room_screen = "images/bg/bg_dima_flat_room_screen_1.png"      # Фон    
    image bg_dima_flat_room_screen_evng = "images/bg/bg_dima_flat_room_screen_2_evng.png"      # Фон    
    image bg_forest_field_dark = "images/bg/bg_forest_field_dark.png"      # Фон    
    image bg_hospital_dark = "images/bg/bg_hospital_dark_1.png"      # Фон        
    image bg_inside_bus = "images/bg/bg_inside_bus_1.png"      # Фон
    image bg_inside_bus_dark = "images/bg/bg_inside_bus_dark_1.png"      # Фон    
    image bg_inside_cafe_dark = "images/bg/bg_inside_cafe_dark_1.png"      # Фон        
    image bg_river_park_1 = "images/bg/bg_river_park_1.png"      # Фон    
    image bg_river_park_1_dark = "images/bg/bg_river_park_1_dark.png"      # Фон        
    image bg_river_park_2 = "images/bg/bg_river_park_2.png"      # Фон    
    image bg_river_park_bench = "images/bg/bg_river_park_bench.png"      # Фон    
    image bg_river_park_bench_dark = "images/bg/bg_river_park_bench_dark.png"      # Фон            
    image bg_road_to_busstop = "images/bg/bg_road_to_busstop_1.png"      # Фон        
    image bg_spring_city_street = "images/bg/bg_spring_city_street.png"      # Фон
    image bg_unvst_auditorium = "images/bg/bg_unvst_auditorium_1.png"      # Фон
    image bg_unvst_auditorium_dark = "images/bg/bg_unvst_auditorium_dark.png"      # Фон        
    image bg_unvst_busstop = "images/bg/bg_unvst_busstop.png"      # Фон
    image bg_unvst_busstop_dark = "images/bg/bg_unvst_busstop_dark_1.png"      # Фон    
    image bg_unvst_corridor = "images/bg/bg_unvst_corridor_1.png"      # Фон
    image bg_unvst_corridor_dark = "images/bg/bg_unvst_corridor_dark.png"      # Фон    
    image br_forest_field = "images/bg/br_forest_field_1.png"      # Фон    
    image bg_dima_flat_room_phone = "images/bg/bg_dima_flat_room_phone.png"      # Фон    
    image bg_epilogue = "images/bg/bg_epilogue.png"      # Фон    
        
    # Сцены                    
    image scn_cinema_inside = "images/scenes/scn_cinema_inside.png"
    image scn_dima_flat_telephone = "images/scenes/scn_dima_flat_telephone.png"    
    image scn_dima_masha_street = "images/scenes/scn_dima_masha_street.png"    
    image scn_hand_in_hand_bridge = "images/scenes/scn_hand_in_hand_bridge.png"    
    image scn_hand_in_hand_river_park = "images/scenes/scn_hand_in_hand_river_park.png"    
    image scn_river_park_on_bench = "images/scenes/scn_river_park_on_bench.png"    
    image scn_river_park_on_bench2 = "images/scenes/scn_river_park_on_bench2.png"        
    image scn_cellphone_andrey = "images/scenes/scn_university_andrey_call.png"    
    image scn_university_fight_dark = "images/scenes/scn_university_fight_dark.png"
    image scn_university_handshake = "images/scenes/scn_university_handshake_1.png"   
    image scn_dima_bed = "images/scenes/scn_dima_bed.png"   
    
    # Персонажи
    image masha = "images/chars/char_maria_1_2.png"
    image masha_reversed = "images/chars/char_maria_1_2_reversed.png"
    image dima = "images/chars/char_dima_2.png"
    image dima_home = "images/chars/char_dima_home.png"
    image pasha = "images/chars/char_pasha_2.png"
    image pasha_dark = "images/chars/char_pasha_dark.png"
    image andrey = "images/chars/char_andrey_2.png"
    image andrey_dark = "images/chars/char_andrey_dark.png"
    image sergey = "images/chars/char_sergey_2.png"    
    image sergey_dark = "images/chars/char_sergey_dark.png"        
    image tanya = "images/chars/char_tanya_12.png"       
    image tanya_dark = "images/chars/char_tanya_22.png"       
    image tanya_dark2 = "images/chars/char_tanya_dark_21.png"       
    image tanya_dark3 = "images/chars/char_tanya_dark_24.png"       
    image masha_dark1 = "images/chars/char_maria_1_2_dark1.png"       
    image masha_dark2 = "images/chars/char_maria_1_2_dark2.png"       
    image dima_epilogue = "images/chars/char_dima_epilogue.png"       
        
    image black = Solid("#000000")
    
    transform char_scale:
        zoom 0.90
        yoffset 5        
    
    transform slow_rotation:
        subpixel True
        align (0.5, 0.5)
        around (0.5, 0.5)
        
        # Добавляем увеличение
        zoom 1.7 
        
        rotate 0
        linear 60.0 rotate 360
        repeat

        
#персонажи
#со спрайтами
define dima = Character(_("Дима"), image="dima", who_color="#99ccff")
define dima_home = Character(_("Дима"), image="dima_home", who_color="#99ccff")
define dima_desmond = Character("Desmond", image="dima_home", who_color="#99ccff")
define masha = Character(_("Мария"), image="masha", who_color="#ffb3b3")
define masha_velvetmoon = Character("VelvetMoon", image="masha", who_color="#ffb3b3")
define mama = Character(_("Мама"), who_color="#ffcc99")
define pasha = Character(_("Паша"), who_color="#ffff00")
define andrey = Character(_("Андрей"), who_color="#c8ffc8")
define sergey = Character(_("Сергей"), who_color="#ff0000")
define tanya = Character(_("Таня"), who_color="#FF7F50")
#без спрайтов
define girls = Character(_("Девушки-одногруппницы"), who_color="#ab813a")
define teacher = Character(_("Преподаватель"), who_color="#485b61")
define voice_darkside = Character(_("Го▒▓с из ни▒▓куда"), who_color="#ffcc00")
define tatiana_online = Character("Tatiana", who_color="#FF7F50")

default darkside_voice_greeting = True
default day_one_darkside = False
default day_two_darkside = False
default day_three_darkside = False

label dark_voice_message1(darkside_voice_greeting):
    
    # if not darkside_voice_greeting:
       # return
    voice_darkside "{color=#ffb3b3}..это очень ин▓ █есное место.. о░нь инт ▚ ▞ сное{/color}"    
    $ darkside_voice_greeting = False
    
    return
    
label dark_voice_message2(darkside_voice_greeting):
    
    # if not darkside_voice_greeting:
       # return
    voice_darkside "{color=#ffb3b3}..тут ты можешь уз▀ ■ать то, что еще не произошло..{/color}"
    voice_darkside "{color=#ffb3b3}..а также узнать то, чего н▒гда не узнаешь..{/color}"
    $ darkside_voice_greeting = False
    
    return

# The game starts here.

label start:

# Стартутаем игру с черных экранов
    $ darkside_voice_greeting = True
    $ day_one_darkside = False
    $ day_two_darkside = False
    $ save_name = "День 1"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Сейчас мы часто называем это время \"нулевые\" или просто \"00-вые\""))
    call screen black_with_text(_("А тогда это была просто жизнь. Прошли годы, но некоторые ее картины до сих пор всплывают в памяти."))    
# День 1
# Просыпаемся и встаем
label day1:    
    call screen black_with_text(_("День 1"))
    
    $ quick_menu = True

    play music "audio/bg_music_s_gameplay1.ogg" volume 0.5
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    "( голос из коридора )"    
    mama "..Дим! Димаа!! Давай вставай уже! Опять вчера поздно лег!"    
    show dima_home at center, char_scale
    with fade
    dima_home "АААА!! Как спать хочется.. Да! Встаю уже, встаю!"    
    stop sound fadeout 1.0
    "( голос из коридора )"    
    mama "Ты чего орешь? Учебу пропустишь, давай, поднимайся, завтрак на столе..! Мы с отцом ушли на работу."    
    dima_home "Да-да, я помню, спасибо..! Уже поднимаюсь."    
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.7
    
    call wait(1.0) from _call_wait
    
    dima_home "...Ушли. Да, надо побыстрее собраться и в универ."
    dima_home "А там сегодня опять лекции бесконечные, а еще этот семинар по экономтеории, а еще лабу не сделал..."
    dima_home "И зачем мне вообще все это? Не интересно совершенно. Да и терпеть эту ерунду уже не могу, а еще 2 с половиной курса этой бодяги. Жесть."
    dima_home "Учить то, что не интересно, чтобы потом работать на работе, которую ненавидишь. Кайф."
    
    call wait(1.0) from _call_wait_1

label waking_up:
    
    dima_home "Вот бы еще поваляться полчасика... Но нельзя."
    dima_home "Прогуливать я не привык. Хотя, может и стоило бы уже научиться..."

    menu (screen="choice_lower"):
        "Еще поваляться":
            call wait(3.0) from _call_wait_2
            jump waking_up
        
        "Встать и собираться в универ":            
            pause 0.0
    dima_home "Эх, поехали."
    call wait(1.0) from _call_wait_3

    #Коридор и сборы
    scene bg_dima_flat_corridor    
    call wait(2.0) from _call_wait_4
    
    show dima_home at center, char_scale
    with fade
    dima_home "Ладно, быстро в душ, поесть, переодеться и бежать."
    
    menu (screen="choice_lower"):
        "Привести себя в порядок и собраться":
            call wait(1.0) from _call_wait_5
    
    hide dima_home
    play sound "audio/sound_morning_preparations_1.ogg" volume 1
    call wait(6.0) from _call_wait_6    
    show dima at center, char_scale
    stop sound fadeout 1.0
    dima "Все, теперь на остановку."    
    call wait(3.0) from _call_wait_7
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(1.0) from _call_wait_8
    #Путь на остановку
    scene bg_road_to_busstop
    with fade
    play sound "audio/bg_sound_street_1.ogg"
    dima "Утро.. На улице еще не жарко, но к середине дня точно начнет припекать. Вот бы просто гулять, а не бежать куда-то ради унылых пар..."
    dima "Универ почти что на другом конце города. Город хоть и небольшой, но, все же, это минут сорок пути на маршрутке через центр."
    dima "А в такое время все, что идет в центр, набито студентами, людьми едущим на работу и прочая и прочая..."
    dima "Схема такая - каждый день двадцать минут иду до конечной своей маршрутки - а это пешком через весь микрорайон. Зато потом почти всегда занимаю сидячее место у окна. Стратегия проверенная 2 годами универа."
    dima "Хорошо, что сейчас весна. Вот зимой ветер, холод, тьма, недосып, брррр - подобные приключения по утру основательно портят настрой. Впрочем, настроение и сейчас практически на нуле."
    dima "Почти добрался..."
    stop sound fadeout 2.0
    call wait(2.0) from _call_wait_9
    #Остановка маршрутки
    play sound "audio/bg_sound_street_2.ogg" volume 1.5 loop
    scene bg_dima_busstop    
    with fade
    dima "А вот и остановка..."
    call wait(1.0) from _call_wait_10
    show dima at center, char_scale
    with dissolve
    dima "На месте. А вот и мой ПАЗик подъезжает, повезло."
    call wait(1.0) from _call_wait_11
    scene black
    with fade
    call wait(1.0) from _call_wait_12
    
    #Маршрутка
    
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1.5 loop
    dima "А теперь 40 минут можно дремать или смотреть в окно на проплывающий мимо пейзаж, давно выученный наизусть."
    dima "Хотя не всегда это работает именно так.. Иногда в голову лезут мысли."
    dima "Например, обо всем этом беспровестном унынии в которое погружаешься и, кажется, конца и края этому не видно..."
    dima "Хотя это, конечно, детство какое-то.. И сильно пахнет попытками жалеть себя."
    dima "Вот еще на днях Андрей дал диск с \"Бойцовским Клубом\". Классное кино! Вот бы быть как Тайлер - ни о чем не думать, ничего не бояться, просто делать что хочешь"
    dima "Но тут есть две проблемы. Первая - таким надо родиться, а вторая - это в кино, а я здесь."
    dima "А еще можно рассматривать пассажироов маршрутки. Помимо вездесущих пенсионеров здесь есть студенты, которые, также как я, разъезжаются по своим бесполезным ВУЗам."
    dima "Учиться профессиям, которые никому не нужны. Кажется, многих из нас кто-то крепко обманул."
    dima "А среди студентов есть девушки. И иногда даже очень симпатичные девушки."
    dima "Сколько раз день начинался с мыслей - \"вот бы сегодня что-то хорошее взяло и случилось\""
    dima "Вот просто раз и произошло, как в фильме."
    dima "Например, я бы встретил симпатичную девушку и мы бы с ней познакомились."
    dima "Ну может же хоть раз в жизни повезти? Как в кино."
    dima "Но как в кино бывает только в кино. Сколько не витай в розовых фантазиях - жить приходится в реальном мире."
    dima "А в реальном мире - кому я, к черту, сдался? Некрасивый, неумный, несмелый. Да все ясно, о чем говорить?"
    dima "Правда, есть еще Таня... Но Таня - это больной вопрос, думать об этом не хочется."
    dima "Зато вчера в локалке скачал NFS:Most Wanted. Вот это шикарные гонки, скорее бы домой вернуться и погоняться с полицией, кайф..."
    dima "Вот только лабы несделанные кто сдавать будет? Ну и тоска."
    dima ". . ."
    dima "В полудреме время пролетает незаметно... Вот и моя остановка, надо пробиваться к выходу."
    stop sound fadeout 1.0   
    
    #Остановка университет
    
    play sound "audio/bg_sound_street_3.ogg" volume 1.2 loop
    scene bg_unvst_busstop    
    with fade
    show dima at center, char_scale
    with dissolve
    dima "А вот и он. Факультет экономики и финансов. А также юридический."
    dima "На самом деле это просто здание заводоуправления советского завода."
    dima "В начале 90х производство резко перестало быть нужным, зато понадобились новые модные профессии, а высшее образование стало возможно получить за деньги"
    dima "ВУЗ просто выкупил себе большую часть здания, назвал новым учебным корпусом и превратил бывшие кабинеты и бюро в аудитории для новосозданных факультетов."
    dima "О прошлом напоминало лишь то, что никто из студентов не называл этом место корпусом или университетом. Все говорили просто - \"Электроприбор\""
    dima "Прямо напротив остановки находилось в кафе в котором регулярно зависали все местные прогульщики"
    dima "Очень удобно"
    dima "Я не был в их числе"
    call wait(1.0) from _call_wait_13
    menu (screen="choice_lower"):
        "Вперед на пары":
            call wait(2.0) from _call_wait_14    
    stop sound fadeout 2.0        
    # Коридор университета
    scene bg_unvst_corridor
    with fade    
    play sound "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    show dima at center, char_scale
    with dissolve
    dima "Проходная, вестибюль, меньше десятка этажей на лифте вверх и вот я здесь."
    dima "В глубине длинного коридора уже виднелись знакомые силуэты моих одногруппников, ожидавших возможности войти и рассесться в аудитории."
    dima "Я направился к знакомым фигурам."
    call wait(1.0) from _call_wait_15   
    hide dima
    call wait(1.0) from _call_wait_16
    show pasha at left, char_scale
    with dissolve
    call wait(1.0) from _call_wait_17
    pasha "...так вот. Ну ты знаешь как он любит говорить \"Я накрыл этот стол\" и бухой уже совсем в неадеквате. "
    pasha "Ну, в общем, Игорек его тащит, а он там зацепился с какими-то... "
    show andrey at right, char_scale
    with dissolve
    andrey "...Лан, Паш, хорош свою пургу нести. Смотри кто идет."
    pasha "Опа. Диман, ты что ли.."
    hide pasha
    with dissolve
    show dima at left, char_scale
    with dissolve
    dima "Здорово. Ну что вы тут третесь, а?"
    show scn_university_handshake
    andrey "Паш, что ты тут трешься? Паша как обычно рассказывает свои обрыганские истории."
    hide scn_university_handshake
    hide dima
    with dissolve
    show pasha at left, char_scale
    with dissolve
    hide andrey
    with dissolve
    pasha "Я тебе ща врежу, обрыганские истории. Диман, кстати, давай деньги."
    show dima at right, char_scale
    with dissolve
    dima "Какие деньги, ты что, пьяный?"
    pasha "Сам ты пьяный. Ты у меня занимал, да и помнишь - я тогда угощал когда мы в кафе пили. Твоя очередь проставляться."
    dima "Да-да, начинай. Я вообще не пью. С кем ты там пил? Отстань."
    "( комическим громким шепотом в сторону Андрея )"
    pasha "Не прокатило, Андрюха."
    pasha "Ладно, короче, но ты мне должен."
    dima "Да-да, Паш, конечно."
    pasha "А ты, кстати, вчера зря уехал, мы там договорились по физре пропуски закрыть с Андрюхой."
    dima "Да вы чего, серьезно? Без меня?"
    hide pasha
    with dissolve
    show andrey at left, char_scale
    with dissolve
    andrey "Ну да, закрыли."
    dima "Блин. Ну вы крысы, конечно. Могли бы хоть позвонить..."
    andrey "Ну а чего мы сделаем, там все решалось за минуты. Сам разберешься, не парься."
    dima "Н-да. Ну это обида страшная."    
    hide andrey
    with dissolve
    show pasha at left, char_scale
    with dissolve
    pasha "Да не бухти, Диман. Надо было вертеться, а не дома откисать."
    dima "Понятно все с вами."    
    hide pasha
    with dissolve
    show andrey at left, char_scale
    with dissolve
    andrey "Ладно, хватит тебе, обижаешься как девочка. Пошли внутрь, вон препод уже с ключом идет..."
    hide dima
    with dissolve
    hide andrey
    with dissolve
    call wait(1.0) from _call_wait_18
    # Аудитория
    scene bg_unvst_auditorium
    with fade
    show andrey at right, char_scale
    with dissolve
    show dima at left, char_scale
    with dissolve
    dima "Вот, принес обратно..."
    "( садясь за парту ближе к концу аудитории )"
    andrey "О, \"Бойцовский Клуб\", ну как тебе?"
    "( садясь за ту же парту )"
    dima "Шикарное кино. Вот так надо бороться с системой. Надо книжку где-нибудь скачать и почитать... Я слышал, фильм по книге снят."
    andrey "С системой? От тебя я другого ответа и не ждал. Как думаешь, давай свой бойцовский клуб забабахаем?"
    dima "Чего?"
    andrey "Ну да. Сначала будем с тобой драться до крови за гаражами. Потом раскидаем объявления где-нибудь в инете, наберем еще сторонников. Пашу подтянем. Как тебе?"
    dima "Блин, ну что ты несешь?"
    andrey "Понятно, так и знал что ты бесхребетный.."
    hide andrey
    with dissolve
    show sergey at right, char_scale
    with fade
    with hpunch
    play sound2 "audio/sound_surprise_fx.ogg" volume 1
    call wait(1.0) from _call_wait_19
    "( приземляясь за пустую парту спереди )"
    sergey "Кто это тут у нас?! Диман!"    
    "( выхватывает тетрадь с парты и начинает листать не глядя )"
    sergey "Что вы тут делаете?"    
    sergey "Опять Дима и Андрейка - два голобука, да? Вы там это не того-этого?"
    "( повернувшись и громко к аудитории в виде сидящих впереди девушек )"
    sergey "А то я за тобой слежу!"
    sergey "Смотри у меня, не закончил еще с тобой!"
    girls "Хах-хаха Хи-хи"    
    dima "Серег, отвали.."        
    "( выхватив тетрадь обратно и вернув на парту )"
    sergey "Чт.."
    hide dima
    with dissolve
    hide sergey
    with dissolve
    with hpunch
    call wait(1.0) from _call_wait_20
    play sound "audio/sound_surprise_fx.ogg" volume 1
    teacher "Эй там, на галерке! Вообще-то лекция уже началась! По местам и тихо! Или за дверь - никого не держу.."
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("Начался бесконечный учебный день..."))
    call screen black_with_text(_("Но все когда-нибудь заканчивается."))
    $ quick_menu = True
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1.3 loop
    dima "...Спать уже хочется невероятно"    
    dima "А еще физра эта... Как они так взяли и закрыли все, а мне теперь одному в главный таскаться."    
    menu (screen="choice_lower"):
        "Да плевать, разберусь...":
            pause 0
        "Обидно на самом деле. Просто так сделали все без меня и даже не позвонили.":
            dima "Вот так вот. А у кого-то есть настоящие друзья. Или это все только в книжках и кино?"
            dima "Читал я где-то, что дружбы нет и все это очередные сказки."
            dima "Ну, по крайней мере, у меня друзей настоящих точно нет - это я знаю."
            dima "Сидим за одной партой, но по факту это так... Товарищи по несчастью."
            dima "Да и о чем я? Настоящую дружбу надо заслужить. А я заслужил чем-то?"
            dima "Неа, обычный эгоист. Ничем не лучше других."
            $ day_one_darkside = True
    $ quick_menu = False
    stop sound fadeout 1.0
    scene black
    with dissolve
    call screen black_with_text(_("Домашние дела, учеба, ужин. Время до позднего вечера пролетело незаметно."))    
    $ quick_menu = True
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop    
    scene bg_dima_flat_room
    with fade
    show dima_home at center, char_scale
    with dissolve
    dima "Ух, наконец, закончил. Ну все, можно на компе поиграть или позаниматься своими делами..."
    dima "А можно еще в аське посидеть. Не так давно GPRS себе настроил на телефоне, трафик дорогой, а, при отсутствии своих источников дохода, любые траты - это лишний разговор с родителями..."
    dima "Но плюс оплаты мобильного интернета по трафику в том, что аська очень мало его жрет... Можно весь вечер просидеть ничего не качая, а потратить копейки."
    dima "А еще в ICQ можно искать девушек. Где-то прочитал про такой способ."
    dima "Я проверял - по поиску можно найти кучу женских анкет в городе. Вот это прикол."
    dima "Может это шанс?"
    dima "Давно понятно, что \"нормальным способом\"  мне никого себе найти.. Попробуем. В очередной раз."
    dima "Правда, с Таней я тоже познакомился в аське..."
    menu (screen="choice_lower"):
        "Початиться в аське":
            pause 0        
    scene bg_dima_flat_room_screen
    with dissolve
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop
    dima "Так. Вобьем в поиск.. Город.. Пол - женский, само собой. Возраст, нууу, поставим 18-20 лет. И поставить галочку, что контакт в онлайне... Готово."
    dima "Ну вот и целый список. Реально, много кто сидит в аське сейчас. Кому бы написать..?"
    dima "Так. Ну тут по описанию все ясно, тут ник пошлый, а вот.."
    dima "Вот {color=#ffb3b3}VelvetMoon{/color}. Прикольный ник, правда, описание пустое. Но у меня тоже пустое, какая разница."
    dima_desmond "Привет"
    call wait(3.0) from _call_wait_21
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    masha_velvetmoon "Привет"
    dima_desmond "Как дела? Ты тоже из ... ?"
    "(называет город)"
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    masha_velvetmoon "Даа, у меня же в анкете написано :)"
    dima_desmond "На всякий случай спросил))"
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    masha_velvetmoon "Понятно)"
    masha_velvetmoon "Дела неплохо, после универа музыку слушаю. А ты что делаешь?"
    dima_desmond "Отдыхаю, я-то думал домашки все остались в школе, но не все так очевидно :(("
    dima_desmond "Прикольно, а где ты учишься?"
    masha_velvetmoon "..."
    "( называет название моего университета )"
    dima_desmond "Серьезно?"
    masha_velvetmoon "Даа, а что?"
    dima_desmond "Просто я там учусь тоже."
    masha_velvetmoon "Правда? На каком факультете?"
    dima_desmond "Финансы экономика, а ты?"
    masha_velvetmoon "Юридический"
    masha_velvetmoon "Я пока на втором курсе только и мы обычно в главном учимся, а потом должны на \"Электроприбор\" перейти"
    masha_velvetmoon "А экономисты же тоже там учатся, да? Ты на каком курсе?"
    dima_desmond "На 3м. Да, все так, там и учимся. Получается, будем вместе с тобой учиться :) Только на разных этажах в основном."
    masha_velvetmoon "Точно! Прикольно :)"
    masha_velvetmoon "Кстати, а что значит твой ник?"
    dima_desmond "Нууу, на самом деле ничего не значит, мне просто понравилось ;)"
    dima_desmond "Зато твой говорит сам за себя"
    masha_velvetmoon "Даа? И что же говорит? :) на самом деле там долгая история, потом расскажу"
    dima_desmond "Ладно :) ты говорила, что музыку слушаешь, а ка..."
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("..так незаметно пролетела пара часов.."))    
    $ quick_menu = True
    stop sound fadeout 1.0
    scene bg_dima_flat_room_evn    
    with fade
    with hpunch
    play sound "audio/sound_surprise_fx.ogg" volume 1
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 0.3 loop
    stop sound2 fadeout 1.0
    show dima_home at center, char_scale
    "( из коридора )"
    mama "Дим, ты чего не ложишься? Двенадцать уже, а у тебя свет горит. Опять завтра будешь кричать, что не выспался..."
    dima "Ладно, мам, сейчас.."
    scene bg_dima_flat_room_screen_evng
    with dissolve
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop
    dima_desmond "Мне спать пора.. Завтра на пары"
    masha_velvetmoon "Блин, а мне тоже вообще-то. Давай завтра спишемся тогда ближе к вечеру, хорошо? Очень понравилось с тобой общаться :) А тут обычно люди двух слов связать не могут"
    dima_desmond "Мне тоже понравилось :) Обязательно. Спокойной ночи"
    masha_velvetmoon "Спокойной ночи :)"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene bg_dima_flat_room_evn
    with fade    
    show dima_home at center, char_scale
    dima "И правда, уже темно, даже не заметил..."
    dima "Не ожидал просто так зайти и сразу встретить кого-то из своего универа..."
    dima "И общаться приятно, чувствуется, что мы на одной волне..."
    dima "Что-то я немного не в себе, очень нервный..."
    dima "Пора спать. Может просто показалось и завтра я уже не буду ей интересен... Кто знает?"
    menu (screen="choice_lower"):
        "Лечь спать":
            pause 0   
    hide dima_home
           
    $ quick_menu = False
    stop sound fadeout 1.0
    scene black
    with dissolve
    call screen black_with_text(_("Заснуть еще долго не удавалось, но все-таки усталость взяла свое..."))    
    $ quick_menu = True
    stop sound3 fadeout 1.0
    
    if not day_one_darkside:
       jump day2

#День 1 - Темная сторона
label day1_darkside:
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    play music "audio/bg_music_dark1.ogg" volume 1    
    scene bg_dima_flat_corridor_dark   
    with dissolve
    call wait(2.0) from _call_wait_22
    scene black
    call wait(1.0) from _call_wait_23
    scene bg_dima_flat_corridor_dark   
    with fade
    call wait(4.0) from _call_wait_24
    dima "...Чт...?"
    call wait(3.0) from _call_wait_25
    call dark_voice_message1(darkside_voice_greeting) from _call_dark_voice_message1
    call wait(2.0) from _call_wait_26
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0   
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(3.0) from _call_wait_27
    scene bg_inside_bus_dark
    with dissolve
    call wait(2.0) from _call_wait_28
    call dark_voice_message2(darkside_voice_greeting) from _call_dark_voice_message2
    call wait(3.0) from _call_wait_29
    dima "...куда я еду..? Вс▒█мнил... У меня же за▒█т.. Нужно привезти сде▒█анные лабы"
    dima "...надо успеть ин▒█че иначе"
    dima "..Но ведь.."
    dima "я уже не учусь там 10 лет.. я даже не живу в этом г▒█оде"
    scene bg_unvst_busstop_dark
    with dissolve
    dima "...мес█о знакомое, но поч▒му ночь.. сейчас же н▒ зима.. а в универе в темноте я бываю только зимой.. или"    
    dima "...зимой должен быть снег"    
    dima "...каж▒тся, я█знаю это кафе"    
    dima "...но оно назыв█ось как-то иначе"    
    dima "...за это время все мог█ло поме▒яться"    
    dima "надо про█ерить.."
    call wait(3.0) from _call_wait_30
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0       
    call wait(3.0) from _call_wait_31
    scene bg_inside_cafe_dark
    with dissolve
    call wait(2.0) from _call_wait_32
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    show pasha_dark at center
    with dissolve
    with hpunch
    dima "Паша?"
    call wait(3.0) from _call_wait_33
    pasha "..я воо▒ще не пон▀маю что он с то▒ой тусит"
    pasha "ты же реально лузер"
    pasha "пр▀сто он добрый сл▒шком чт▒бы перестать"
    pasha "ты же вре▒ный, много го▀оришь, мало делаешь"
    pasha "даже не пьешь с нами, типа сл▀▒ком умным себя считаешь?"
    pasha "я мно▒о таких как ты видел"
    pasha "с тобой обща▒ся западло, понял?"
    call wait(3.0) from _call_wait_34    
#День 2    
label day2:
    $ save_name = "День 2"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 2"))
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade   
    stop sound fadeout 1.0
    dima "Ухх... Опять утро что ли.."
    dima "Снилось что-то странное сегодня... Что-то про универ. А потом..."
    dima "Не помню."
    dima "Сегоня не к первой паре, родители уже ушли..."
    dima "Но и я встал позже, уже время собираться и выходить."
    scene bg_dima_flat_corridor
    with fade
    menu (screen="choice_lower"):
        "Привести себя в порядок и собраться":
            call wait(1.0) from _call_wait_35
    
    hide dima_home
    play sound "audio/sound_morning_preparations_1.ogg" volume 1
    call wait(6.0) from _call_wait_36    
    show dima at center, char_scale
    stop sound fadeout 1.0
    dima "Все, теперь на остановку."    
    pause
    hide dima
    with dissolve
    call wait(3.0) from _call_wait_37
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(1.0) from _call_wait_38    
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1.5 loop
    dima ". . ."   
    play sound "audio/bg_sound_street_3.ogg" volume 1.2 loop
    scene bg_unvst_busstop    
    with fade
    stop sound fadeout 1.0        
    call wait(3.0) from _call_wait_39
    scene bg_unvst_corridor
    with fade    
    play sound "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    call wait(3.0) from _call_wait_40
    scene bg_unvst_auditorium
    with fade
    show dima at left, char_scale
    show andrey at right, char_scale
    andrey "...Диман, ты слышал Паша рассказывает интересное?"
    dima "А?"
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "Андрюх, да блин, молчи ты..."
    hide pasha
    with dissolve
    show andrey at right, char_scale
    with dissolve
    andrey "Да стой ты.. Короче, смотри, Паша нашел себе женщину..."
    andrey "Она, короче, на десять лет..."
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "Не на десять, а на пять!"
    hide pasha
    with dissolve
    show andrey at right, char_scale
    with dissolve
    andrey "..на пять лет старше него. И у нее еще ребенок."
    dima "Может, она еще и замужем?"
    andrey "Может она замужем, Паш?"
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "Да не замужем она, холостая!"
    dima "Хах-хаха"
    hide pasha
    with dissolve
    show andrey at right, char_scale
    with dissolve
    andrey "Как это там называется - \"разведенка с прицепом\"?"
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "Я бы попросил побольше уважения! Вы вообще не понимаете плюсов зрелых женщин..."
    dima "Да, вкусные борщи и вот это все..."
    pasha "Именно! Дима шарит - у тебя тоже, что ли, была разведенка, а? Колись!"
    hide pasha
    with dissolve
    show andrey at right, char_scale
    with dissolve
    andrey "Ну ты вообще планируешь с ней в итоге оформить отношения? Жениться, усыновить ребенка..."
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "А это вот не вашего ума дело!"
    hide pasha
    with dissolve
    show andrey at right, char_scale
    with dissolve
    andrey "Ну все понятно с тобой. Несерьезный ты человек, морочишь голову зрелой женщине.."   
    dima "Аха-хаха"
    hide andrey
    with dissolve
    show pasha at right, char_scale
    with dissolve
    pasha "Схлопнитесь! У меня вот есть женщина, которая накормит, подогреет, а вашу личную жизнь мы еще даже не нач..."
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("День в универе прошел"))
    $ quick_menu = True        
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1.3 loop
    dima "Все-таки кайф ехать после универа домой..."    
    dima "Одно из немногих доступных удовольствией."    
    dima "Как в том анекдоте, где: - Зачем же вы носите ботинки которые вам малы?"    
    dima "- Зато когда я прихожу домой и их снимаю... Я самый счастливый человек на свете."    
    dima "Примерно такие ощущения."    
    call wait(2.0) from _call_wait_41
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop    
    scene bg_dima_flat_room
    with fade
    call wait(1.0) from _call_wait_42
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.7
    call wait(2.0) from _call_wait_43
    show dima_home at center, char_scale
    with dissolve
    dima_home "Наконец, дома. Родители еще до вечера на работе - полная свобода."
    dima_home "Зайду в аську, может... Хм, я только что понял, что даже не спросил имя у вчерашней девушки.."
    dima_home "Только ник {color=#ffb3b3}VelvetMoon{/color} и все. Надо это обязательно исправить."
    dima_home "А потом, может, в линейку погоняю... Трафик сожрет, конечно, быстрее аськи, но..."
    hide dima
    call wait(2.0) from _call_wait_44
    scene bg_dima_flat_room_screen
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop    
    with dissolve
    play sound "audio/sound_messenger_online.ogg" volume 0.3
    call wait(2.0) from _call_wait_45
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    dima_home "Только успел запустить - уже кто-то пишет..."
    tatiana_online "Привет, Дима"
    "( я тяжело вздохнул )"
    "( с Таней я познакомился в аське месяца два назад. Она как раз готовилась поступать в универ на фармацевта )"
    "( оказалось, что она живет со мной в одном районе )"
    "( из минусов - я ей понравился, но это не было взаимно и у меня не хватало смелости ей прямо об этом сказать )"
    "( я чувствовал себя человеком пойманным в ловушку )"
    "( невежественный в этих делах, но при этом со свалившейся сверху ответсвенностью за чувства человека еще более неопытного )"
    "( логика подсказывала жестко прекратить эти странные взаимоотношения )"
    "( но что-то мне мешало )"
    dima_desmond "Привет"
    tatiana_online "Как ты? Давно мне не писал)"
    dima_desmond "Слушай, все хорошо, а как ты?"
    tatiana_online "Тоже, вот к вступительным готовлюсь, правда, не уверена, что мне интересно то чем придется заниматься"
    dima_desmond "Я тоже был не уверен. И вот через три года я уверен точно."
    tatiana_online ":)"
    tatiana_online "Может пойдем погуляем? А то мне уже надоело дома сидеть."
    "( вот тут мне надо было бы отказаться, но... )"
    dima_desmond "Хорошо, давай."
    tatiana_online "Давай через полчаса на полпути до моего дома, пойдет?"
    dima_desmond "Да, помню, хорошо."
    tatiana_online "Как всегда немногословный))"
    dima_desmond "Человек дела)"   
    tatiana_online "Ладно, я отключусь, мне еще прибраться надо."
    dima_desmond "Хорошо, через полчаса."   
    stop sound2 fadeout 1.0    
    scene bg_dima_flat_room
    with fade
    call wait(1.0) from _call_wait_46    
    show dima_home at center, char_scale
    with dissolve
    dima "Чувствую себя виноватым. Получается, морочу ей голову, а она еще совсем как ребенок."
    dima "Ощущение, что все мы в этом возрасте готовы любить первого человека, который отнесется к нам хорошо."
    dima "Я сам, кажется, чувствовал что-то подобное раньше, а сейчас я что - загоняю в подобную ловушку другого человека? Который ни в чем не виноват."
    dima "Почему все всегда происходит с какими-то душевными метаниями? И каждый раз виноват в них ты сам..."
    dima ". . ."
    
    hide dima_home
    scene bg_dima_flat_corridor
    stop sound3 fadeout 1.0
    call wait(1.0) from _call_wait_47
    play sound "audio/sound_morning_preparations_1.ogg" volume 1
    call wait(6.0) from _call_wait_48
    show dima at center, char_scale
    stop sound fadeout 1.0
    menu (screen="choice_lower"):
        "Пойти гулять":
            call wait(1.0) from _call_wait_49
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.7
    
    scene black
    with fade
    $ quick_menu = False
    call screen black_with_text(_("На улице еще жарко, но к вечеру духота пошла на спад.."))
    $ quick_menu = True
    call wait(2.0) from _call_wait_50
    scene bg_road_to_busstop
    play sound "audio/bg_forest_ambience.ogg" loop
    with fade
    call wait(2.0) from _call_wait_51
    show dima at left, char_scale
    with dissolve
    call wait(1.0) from _call_wait_52
    show tanya at right, char_scale
    with dissolve
    
    tanya "Привет!"
    dima "Привет! Ну как ты там? Готовишься в универ?"
    tanya "Даа, замучалась совсем."
    dima "Понимаю. Я когда поступал тоже чуть нервный срыв не заработал, мне кажется.."
    tanya "Серьезно?"
    dima "Даа.. Зато теперь учусь за родительские деньги на коммерческом. Вот так вот."
    "( до сих по не избавился от чувства неполноценности по этому поводу, хотя какое мне должно быть дело спустя 3 года )"
    tanya "Ну на экономике большой конкурс, я слышала."
    dima "Да.."
    dima "Может пойдем? Прогуляемся до опушки где спорткомплекс.."
    tanya "Пойдем."
    
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Мы не спеша направились по еще жарким улицам своего микрорайона.."))
    call screen black_with_text(_("Таня рассказывала мне свои абитуриентские дела, а я все больше отмалчивался"))    
    call screen black_with_text(_("Так незаметно солнце стало катиться к горизонту, а мы пришли к опушке леса"))    
    call screen black_with_text(_("С одной стороны к обширной слегка запущенной поляне примыкало футбольное поле с лавочками"))    
    call screen black_with_text(_("Место традиционно было своего рода заменой парку - жители микрорайона гуляли здесь"))    
    call screen black_with_text(_("А на лавочках и ближе к опушке часто располагались пьющие компании"))    
    $ quick_menu = True
    
    scene br_forest_field
    with dissolve
    call wait(3.0) from _call_wait_53    
    show dima at left, char_scale
    with dissolve
    show tanya at right, char_scale
    with dissolve
    tanya "Ой, красивое солнце сегодня..."
    dima "Да, давно тут не был на закате. Пойдем сядем."
    "( мы расположились на видавшей виды лавочке у футбольного поля )"
    tanya "..А ты так и не рассказал как у тебя дела. На учебе."    
    tanya "..или в личной жизни.."    
    dima ". . ."
    dima "Да все хорошо, на самом деле, стабильно. Без изменений."
    tanya "Ничего мне не рассказываешь про себя.."    
    tanya "Кстати, не пробовал себе кого-нибудь найти в аське..?"    
    dima "Хм..."
    tanya "Мне вот часто пишут парни там.."    
    dima "И что ты?"
    tanya "Ну они все какие-то.. Пошлые.. И вторым сообщением предлагают в гости зайти."    
    dima "Ха.. Ничего удивительного."
    tanya "А еще все такие неграмотные. Пишут с ошибками и без знаков препинания."    
    tanya "Я вот когда с тобой начала общаться - сразу поняла, что ты другой."    
    dima "Думаешь?"
    tanya "Да..."    
    tanya "Знаешь.. Мы с тобой уже давно общаемся.."    
    dima "?"
    tanya "Я хотела тебя спросить."    
    call wait(2.0) from _call_wait_54
    tanya "Я тебе нравлюсь как девушка..?"    
    with hpunch
    play sound2 "audio/sound_surprise_fx.ogg" volume 1
    "( похоже, этот разговор настиг меня раньше, чем я рассчитывал )"
    call wait(2.0) from _call_wait_55
    dima "..."
    call wait(1.0) from _call_wait_56
    menu (screen="choice_lower"):
        "Тянуть время и дальше":
            jump tanya_dialogue_ending_1
        "Сказать честно":            
            jump tanya_dialogue_ending_2
            $ day_two_darkside = True    
            
label tanya_dialogue_ending_1:
    call wait(2.0) from _call_wait_57
    dima "Понимаешь... Честно говоря, я сейчас не готов отвечать на этот вопрос."
    dima "У меня довольно сложный период сейчас. И я сам не знаю что мне нужно."
    dima "Прости, что так."
    tanya "..."
    $ day_two_darkside = True
    jump day_2_evening
    
label tanya_dialogue_ending_2:    
    call wait(2.0) from _call_wait_58
    dima "Таня, скажу тебе честно."
    dima "У нас ничего не получится. Извини, что не признался раньше, но не хочу тебя обманывать."
    dima "Я могу тебе солгать и попытаться использовать тебя примерно как те ребята которые пишут тебе в аське."
    dima "Но это неправильно."
    dima "Вот так."
    tanya "..."    
    jump day_2_evening
    
label day_2_evening:    
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Я проводил Таню домой. По пути мы больше не развивали эту тему и говорили и незначащих вещах."))
    call screen black_with_text(_("Но я чувствовал, что она отвечат отстраненно, будто думает о чем-то другом."))
    call screen black_with_text(_("Чувство смутной вины навалилось на меня пока я шел домой по вечерним улицам."))
    $ quick_menu = True
    
    stop sound fadeout 1.0
    scene bg_dima_flat_room_evn    
    with fade
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 0.2 loop
    show dima_home at center, char_scale
    with dissolve
    
    "( добавшись домой и поужинав с родителями я уселся за компьютер ) "
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop
    dima "Надо как-то отвлечься... Может, наконец, поиграю в NFS"
    "( запуская аську ) "
    call wait(3.0) from _call_wait_59
    scene bg_dima_flat_room_screen_evng
    with dissolve
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    with hpunch
    masha_velvetmoon "Привет)"
    call wait(3.0) from _call_wait_60
    dima "Она мне написала..."    
    "( почувствовал как участился пульс )"
    dima_desmond "Привет :)"
    masha_velvetmoon "А я тебя жду, а тебя все нет)"
    dima_desmond "Правда ждешь?) Мне приятно. Были дела"
    masha_velvetmoon "Правда) Как у тебя день? Я была в универе, а потом с подругами встречалась"
    dima_desmond "Я тоже в универе, а потом лабы делал дома и всякое такое..."
    "( рассказывать про Таню совсем не хотелось )"
    dima_desmond "Слушай, я только сейчас вспомнил, что сделал ошибку"
    masha_velvetmoon "Это какую??"
    dima_desmond "Я до сих пор не представился и не узнал как тебя зовут))"
    masha_velvetmoon "Ааа)"
    dima_desmond "Я Дима. А тебя как зовут?"
    masha_velvetmoon "Маша )"
    dima_desmond "Мария, получается)"
    masha_velvetmoon "Да) Только не шути про \"Маша - три рубля и наша\""
    masha_velvetmoon "А то много любителей)"
    dima_desmond "Хахах смешно, не бу.." 
        
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Время в чате с Машей бежал незаметно"))
    call screen black_with_text(_("Мы заболтались за полночь и..."))    
    $ quick_menu = True
    
    scene bg_dima_flat_room_evn
    stop sound2 fadeout 1.0
    
    with dissolve    
    menu (screen="choice_lower"):
        "Лечь спать":
            call wait(3.0) from _call_wait_61
    stop sound3 fadeout 1.0
    
    scene black
    with dissolve    
    
    call wait(5.0) from _call_wait_62
    
    if not day_two_darkside:
       jump day3

#День 2 - Темная сторона
label day2_darkside:
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    play music "audio/bg_music_dark1.ogg" volume 1    
    scene bg_dima_flat_corridor_dark   
    with dissolve
    call wait(2.0) from _call_wait_63
    scene black
    call wait(1.0) from _call_wait_64
    scene bg_dima_flat_corridor_dark   
    with fade    
    dima "..Я з░есь, но все нем▀го не так как дожно быть.."
    call dark_voice_message1(darkside_voice_greeting) from _call_dark_voice_message1_1
    call dark_voice_message2(darkside_voice_greeting) from _call_dark_voice_message2_1    
    call wait(2.0) from _call_wait_65
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    scene bg_inside_bus_dark
    with fade
    call wait(2.0) from _call_wait_66
    dima "...ехать да░ко.. стра░но.. будто мне некомф▀ртно, я почти боюсь, но не знаю чего"
    dima "...я никогда ран░ше не ездил на этой мар░рутке..."
    dima "и не вы▀одил на этой ост▀новке"    
    call wait(1.0) from _call_wait_67
    scene bg_inside_bus_dark
    call wait(3.0) from _call_wait_68
    scene bg_hospital_dark_1
    with fade
    call wait(3.0) from _call_wait_69
    voice_darkside "{color=#ffb3b3}..я в░с слушаю...?{/color}"
    dima "я..."    
    voice_darkside "{color=#ffb3b3}..?{/color}"
    dima "..Это здесь.. Люди.. С про░лемами..? Мне надо.."    
    voice_darkside "{color=#ffb3b3}Тише, мо░одой человек, не шумите...{/color}"
    voice_darkside "{color=#ffb3b3}Вы пос░титель? К кому?{/color}"
    "( называю имя и фамилию )"
    voice_darkside "{color=#ffb3b3}Сейчас.. Минуту, я п░зову.. подожд░те здесь{/color}"
    " . . . "
    scene bg_hospital_dark_1
    call wait(5.0) from _call_wait_70    
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    show tanya_dark2 at center
    with dissolve
    call wait(2.0) from _call_wait_71
    tanya "Дима, Привет.."
    dima "Оо Привет"
    tanya "Я рада, что ты пришел. Норма▓льно добрался?"
    dima "Да, все хорошо.."
    dima "Как ты?"
    tanya "Все хо▓ошо. Пойдем по▓уляем?"
    dima "А тебя выпускают?"
    tanya "Даа, ты чего, это же не тюрьма."
    dima "Пойдем, к▓нечно."
    hide tanya_dark2
    with dissolve
    call wait(5.0) from _call_wait_72
    scene bg_forest_field_dark
    show tanya_dark2 at center
    with dissolve
    dima "..стран░но.. я думал, что мы.."
    tanya "Да░но мы тут не были, да?"
    dima "..да, давно.."
    tanya "Если ты хочешь меня спросить как я..."
    tanya "Все норм▒ьно. Там много хор▒ших девочек, мы с ним об▓аемся, даже поем под гитару..."
    tanya "И меня скоро выпустят все равно"
    dima "Я просто хот▒ел тебе сказать, что мы с тобой так давно общаемся"
    dima "И чт▓бы ты не делала всяких глу▒остей, ты понимаешь.."
    tanya "Да, я пони▒маю, прости, я знаю, что напугала тебя.. И родителей"
    dima "...У тебя нет причин для вс▒го этого, ведь вся жизнь впереди и все буд.."
    tanya "Дима.. Просто.."
    dima "?"
    tanya "Просто, пони▒аешь, когда я тебе тогда написала..."
    tanya "Мне кажется, я никому не нужна.. Я не нра░люсь никому, я не нра░юсь тебе"
    tanya "Я некрасивая, мне каж▒тся, меня никто не полюбит.."
    dima "Таня.."
    tanya "...Что?"
    tanya "...что"
    tanya "...ЧТО??"
    tanya "..."
    show tanya_dark3 at center
    with dissolve
    call wait(5.0) from _call_wait_73    
    hide tanya_dark2
    with dissolve
    hide tanya_dark3
    with dissolve
    call wait(3.0) from _call_wait_74    
    dima "...у те▒я будет все хорошо.."
    dima "...ты всегда общ▒лась с людьми лучше чем я и до░рее чем я.."
    dima "...я даже буду нем▚ого завидовать тебе из-за этого.."
    dima "...у тебя будет куча подруг.."
    dima "...ты на░чишься играть на г▒таре так как я ни▚когда не научусь.."
    dima "...у тебя будут отношения, у тебя будет своя семья.."
    dima "...у тебя все получ▒ится, получится гораздо лучше, чем у меня.."    
    call wait(3.0) from _call_wait_75 

#День 3
label day3:
    
    $ save_name = "День 3"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 3"))
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade       
    "( зевает и потягивается )"
    dima "Мммм..."
    dima "Снилась какая-то ерунда..."
    dima "Я где-то читал, что за ночь нам снится несколько снов"
    dima "Но помним мы только последний"
    stop sound fadeout 1.0        
    dima "И то не всегда..."
    dima "Может оно и к лучшему?"
    stop sound3 fadeout 1.0 
    scene bg_dima_flat_corridor
    with fade
    
    menu (screen="choice_lower"):
        "Привести себя в порядок и собраться":
            call wait(1.0) from _call_wait_76
    
    hide dima_home
    play sound "audio/sound_morning_preparations_1.ogg" volume 1
    call wait(6.0) from _call_wait_77        
    show dima at center, char_scale
    stop sound fadeout 1.0
    dima "Все, теперь на остановку."    
    call wait(1.0) from _call_wait_78
    hide dima
    with dissolve
    call wait(2.0) from _call_wait_79
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(1.0) from _call_wait_80    
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1 loop
    dima ". . ."   
    play sound "audio/bg_sound_street_3.ogg" volume 1.2 loop
    scene bg_unvst_busstop    
    with fade
    stop sound fadeout 1.0        
    call wait(3.0) from _call_wait_81
    scene bg_unvst_corridor
    play sound2 "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    with fade        
    call wait(3.0) from _call_wait_82
    scene bg_unvst_auditorium
    play sound2 "audio/bg_crowd_ambience_1.ogg" volume 0.6 loop
    with fade
    show dima at left, char_scale
    show andrey at right, char_scale
    dima "...Жаль, аську не поставить на мою нокию"
    andrey "Да? Ты проверял? Ты же гений-хакер."
    dima "Ну да, конечно. Телефон нужен другой. Количество памяти, поддерживаемые версии джавы, ну ты понял.."
    andrey "Ничего не понял, но я тебе верю."
    dima "Не смотрел документалку про Кевина Митника? На НТВ на днях была"
    andrey "Неа."
    dima "Один из первых известных хакеров."
    andrey "Как считаешь, ты на него похож? Ну внешне там, походкой."
    dima "Чего ты несешь вообще?"
    hide dima
    with dissolve
    hide andrey
    with dissolve
    $ quick_menu = False
    call screen black_with_text(_("Медленно тянулись часы лекций и семинаров"))    
    $ quick_menu = True
    "( я почуствовал, что кто-то постучал меня сзади по спине с соседней парты )"   
    with hpunch    
    play sound "audio/sound_surprise_fx.ogg" volume 1
    play sound2 "audio/bg_crowd_ambience_1.ogg" volume 0.4 loop
    play music "audio/bg_music_tension1.ogg" volume 2
    show sergey at right, char_scale
    with fade
    dima "Чего?"    
    sergey "(передразнивая) Чего?"    
    "( я отвернулся медленно закипая, уже было понятно к чему все идет )"   
    "( по спине повторно постучали )"   
    dima "Серег, что тебе надо?"    
    sergey "Мне надо? Чего ты ко мне пристал. Эй, чего он ко мне пристал вообще??"    
    dima "Это ты что ко мне прицепился? Что тебе от меня надо?"        
    sergey "Достать тебя хочу, не видно что ли?"    
    "( издевательская ухмылка стала еще шире )"   
    dima "Может выйдем, поговорим?"        
    sergey "Давай!"    
    hide dima
    hide sergey
    menu (screen="choice_lower"):
        "Выйти в коридор":            
            $ day_three_darkside = True    
        "Промолчать":            
            jump sergey_dialogue_ending_1
    call wait(3.0) from _call_wait_83
    scene bg_unvst_corridor
    with fade    
    play sound2 "audio/bg_crowd_ambience_1.ogg" volume 0.6 loop
    call wait(3.0) from _call_wait_84
    show dima at left, char_scale
    show sergey at right, char_scale
    sergey "Ну что, давай прямо здесь? Ну, давай."    
    "( он снял и убрал в карман очки будто действительно готовясь к драке )"
    "( по коридору мимо нас проходили студенты и персонал деканата, некоторые оглядывались обращая внимание на повышенные тона )"
    dima ". . ."    
    "( мое дыхание и пульс участились )"
    "( желание резким ударом локтя врезать по ухмыляющемуся лицу было невероятным )"
    dima ". . ."    
    dima "Нет, обойдешься"
    "( я повернулся и пошел обратно в аудиторию )"
    hide dima
    sergey "Ну я так и знал, что ты слабак!"    
    stop sound2 fadeout 1.0        
    
label sergey_dialogue_ending_1:
    scene black
    with dissolve
    $ quick_menu = False
    call screen black_with_text("")    
    $ quick_menu = True
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1 loop
    call wait(3.0) from _call_wait_85
    dima "...козел, дерьмо, с&ка.."
    call wait(5.0) from _call_wait_86
    scene bg_dima_flat_room
    with fade
    call wait(1.0) from _call_wait_87
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.7
    call wait(2.0) from _call_wait_88
    $ quick_menu = False
    call screen black_with_text(_("Наступил вечер..."))    
    $ quick_menu = True
    scene bg_dima_flat_room_evn
    with fade
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 0.3 loop
    show dima_home at center, char_scale
    with dissolve
    
    menu (screen="choice_lower"):
        "Посидеть за компом":
            call wait(3.0) from _call_wait_89
    scene bg_dima_flat_room_screen_evng
    with dissolve
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop    
    dima "Теперь включая аську все время думаю про Машу."
    call wait(3.0) from _call_wait_90
    play sound "audio/sound_messenger_online.ogg" volume 0.6
    call wait(1.0) from _call_wait_91    
    dima "Это она в онлайне..."
    dima "Я будто упиваюсь ожиданием - напишет она мне перевая или не напишет."
    call wait(2.0) from _call_wait_92
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    call wait(1.0) from _call_wait_93    
    masha_velvetmoon "Привет!"
    dima "Написала.."
    dima "Так хочется ощущаться себя нужным. Я реально просто сидел и выжидал, чтобы она сделала это первой."
    dima "Кошмар."
    call wait(2.0) from _call_wait_94
    dima_desmond "Привет)) Как ты?"
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    call wait(1.0) from _call_wait_95    
    masha_velvetmoon "Все ок, только освободилась и решила сразу тебе написать) а ты?"
    dima_desmond "Тоже все ок, учился как обычно, все достало)"
    "( почему я никогда никому ничего не рассказываю про свою жизнь? стесняюсь или боюсь быть навязчивым? что-то в этом не то )"
    call wait(2.0) from _call_wait_96
    $ quick_menu = False
    call screen black_with_text(_("Мы как обычно долго болтали..."))    
    $ quick_menu = True
    dima_desmond "Я вот раньше у тебя не спрашивал... У тебя есть парень?"
    masha_velvetmoon "Нет.. А у тебя есть кто-нибудь?"
    dima_desmond "Нет, я один"
    masha_velvetmoon "Как-то это ты грустно написал)"
    dima_desmond "Думаешь? Случайно вышло..)"
    call wait(3.0) from _call_wait_97
    masha_velvetmoon "Помнишь, мы тогда говорили про музыку... И я хотела скинуть тебе где скачать"
    masha_velvetmoon "Мне очень нравится эта группа. И они из нашего города)) Я прямо подсела на них когда-то"
    masha_velvetmoon "И на всех концертах бываю)"
    masha_velvetmoon "Вот, я нашла ссылку на сайте где можно скачать.."
    "( Маша прислала ссылку на чей-то сайт на narod.ru )"
    masha_velvetmoon "Вот, обязательно послушай эту, мне очень нравится"
    dima_desmond "Ого. Прикольно. Я из наших местных никого не слышал почти"
    dima_desmond "Только другую группу, ........ кажется называется"
    masha_velvetmoon "Ну блин их все знают, я не люблю)) Там их фронтмен он слишком много о себе думает"
    masha_velvetmoon "Их я тоже раньше слушала, но надоело)"
    dima_desmond "Ого. Я просто никогда не ходил на концерты."   
    masha_velvetmoon "Почему? Это же очень прикольно"
    dima_desmond "Не знаю, мне не с кем."   
    masha_velvetmoon "..Почему? С друзьями."
    " . . . "
    dima_desmond "Если честно - у меня нет друзей."   
    stop music fadeout 2.0
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    call wait(1.0) from _call_wait_98    
    masha_velvetmoon "Как так?? С тобой так прикольно общаться, как у тебя не может быть друзей?"
    dima_desmond "Наверное, не так уж прикольно на самом деле... Так получилось"   
    masha_velvetmoon "Ну Диима, не кисни, хочешь я буду с тобой дружить?)))"
    dima_desmond "Конечно))"   
    masha_velvetmoon "Договорились!"
    masha_velvetmoon "Ты скачай и обязательно послушай .... трек, мне он очень нравится сейчас"
    menu (screen="choice_lower"):
        "Скачать mp3":
            call wait(2.0) from _call_wait_99
    "( в уме я прикинул хватит ли мне трафика на музыку в 128 и нажал на ссылку )"
    "0%% [[--------------------]"
    masha_velvetmoon "А еще ты спросил про отношения и потом мы про музыку заговорили..."
    masha_velvetmoon "Если честно, я сейчас немного не в себе из-за недавно закончившихся отношений..."
    "25%% [[|||||---------------] "
    masha_velvetmoon "В общем, я довольно долго встречалась с одним человеком и вот все кончилось."
    masha_velvetmoon "Он старше меня..."
    masha_velvetmoon "И был моим первым парнем с которым прямо все серьезно."
    "75%% [[|||||||||||||||-----]"
    masha_velvetmoon "Мне было тяжело, но музыка спасает, поэтому обязательно послушай."
    "100%% [[||||||||||||||||||||]"
    "( я два раза нажал на скачанный mp3 и открыл WinAmp )"
    play music "audio/bg_music_s_menu.ogg" volume 0.5
    " ( из колонок заиграла музыка ) "
    masha_velvetmoon "Слушай. Я тут подумала - а у тебя есть домашний телефон?"
    dima_desmond "Да, есть. А что?"   
    masha_velvetmoon "Это отлично. Давай я тебе наберу. А то так надоело руками печатать)"
    "( ком подступил к горлу, с одной стороны это было очень приятно, с другой - страшно )"
    dima_desmond "Хорошо, давай."    
    masha_velvetmoon "Диктуй номер!"
    dima_desmond "Вот ........."    
    masha_velvetmoon "Сейчас тебе можно позвонить? Никого не разбужу?"
    dima_desmond "Дааа.. Давай"    
    stop sound2 fadeout 1.0
    call wait(3.0) from _call_wait_100
    play sound "audio/sound_telephone_ring.ogg" volume 1 loop    
    call wait(2.0) from _call_wait_101
    dima "(громко в коридор) Это мне!!"
    "( я уселся обратно и слегка нерничая поднял трубку )"
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    call wait(2.0) from _call_wait_102
    masha "Это я."
    "( в трубке прозвучал мелодичный голос молодой девушки )"
    masha "Привет еще раз."    
    masha "Вот, так гораздо удобнее общаться будет."
    dima "Точно.. У тебя красивый голос"
    masha "Правда? Спасибо. Мне твой тоже нравится, мужественный..."
    dima "Правда? Мне всегда мой голос казался каким-то дурацким, когда я его в записи слышал."
    masha "Правда-правда, у тебя очень интересный голос..."
    masha "А ты с родителями живешь?"
    dima "Да, а ты?"
    masha "Тоже.."
    $ quick_menu = False
    call screen black_with_text(_("Время до ночи за телефонным разговром пролетело незаметно..."))    
    $ quick_menu = True
    "( я даже не помнил, чтобы когда-либо в жизни так долго говорил по телефону )"    
    dima "А у меня, кстати, завтра пар нет."
    masha "Ого. У тебя тоже? Повезло нам))"
    dima "Серьезно? И у тебя?"
    masha "Ага. Планируешь валяться-отдыхать?"
    dima "Нет.. Я подумал.. Может встретимся где-нибудь? Например, в кино сходим.. Не знаю как ты на это посмотришь.."
    masha "Я за. Мне тоже хочется познакомиться с тобой в реальности..."    
    "( во время разговров с Машей пульс у меня часто подскакивал и это был один из этих моментов... ) "
    dima "Давай тогда в \"Будущее\""
    masha "Давай.. А что там сей..."    
    $ quick_menu = False
    call screen black_with_text(_("Оставшееся время мы обсуждали время и детали..."))    
    $ quick_menu = True    
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    "( я положил трубку, в висках еще немного стучало ) "    
    scene bg_dima_flat_room_evn
    with fade
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 1 loop
    show dima_home at center, char_scale
    with dissolve
    dima "А я точно сегодня усну...?"    
    menu (screen="choice_lower"):
        "Лечь спать":
            pause 0   
    call wait(2.0) from _call_wait_103
    stop sound3 fadeout 1.0
    scene black
    with dissolve
    call wait(5.0) from _call_wait_104   
    
    if not day_three_darkside:
       jump day4  
    
#День 3 - Темная сторона
label day3_darkside:
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    play music "audio/bg_music_dark1.ogg" volume 1
    scene bg_dima_flat_corridor_dark   
    with dissolve
    call wait(2.0) from _call_wait_105
    scene black
    call wait(1.0) from _call_wait_106
    scene bg_dima_flat_corridor_dark   
    with fade    
    dima ". . ."
    call dark_voice_message1(darkside_voice_greeting) from _call_dark_voice_message1_2
    call dark_voice_message2(darkside_voice_greeting) from _call_dark_voice_message2_2    
    call wait(2.0) from _call_wait_107
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    scene bg_inside_bus_dark
    with dissolve
    call wait(2.0) from _call_wait_108
    dima "...почему мне сего▀ня так не хоч▀тся ехать в ун▒вер"
    dima "...при одной мысли пр░мо ломает"    
    scene bg_unvst_busstop_dark
    with dissolve
    dima "...мес█о знакомое, но поч▒му ночь.. сейчас же н▒ зима.. а в универе в темноте я бываю только зимой.. или"    
    dima "...зимой должен быть снег"    
    dima "...что-то здесь не то"        
    dima "надо про█ерить.."
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0       
    call wait(4.0) from _call_wait_109
    scene bg_unvst_corridor_dark
    with dissolve
    call wait(3.0) from _call_wait_110
    dima "...что-то зд▒сь не то. Ник▀го нет"        
    dima "...я пр░шел рано или пришел слишком п▀здно.."        
    dima "...а может это з░мние к░никулы и ник▀го нет.."        
    dima "...стой, но это же зн▒чит, что я не сд▒л сесси.."        
    call wait(3.0) from _call_wait_111
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    show sergey_dark at center
    with dissolve
    dima "..."        
    sergey "Ну что, Дим▒н. Теперь не удастся сб▀жать, да?"
    sergey "Давай, иди сюда, ты же х▒тел выйти, раз▀браться..."
    "( т▀лкает в грудь )"
    sergey "Что ты? Оп▀ть зассал??"
    "( толкает в гр▀дь )"
    dima "..."        
    "( во мне подн▒малась зло, сердце уч▒щенно забилось, в ушах стучало )"
    "( ни сл░ва не говоря я в▀бросил вперед кулак ц▀лясь в подбородок фиг▀ры напротив )"
    call wait(1.0) from _call_wait_112
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    show scn_university_fight_dark
    "( воздух ст▄л будто к▒сельным, а мышцы странным обр▒зом ослабли... )"
    "( я дв▒гался как в з▒медленной съемке.. )"
    "( фигура н▒против игр▄юче отклонилась в ст▒рону и перехватила мою руку )"
    sergey "Что случ▒лось, Диман?"
    sergey "Помнишь, ты спр▒шивал что я к тебе пристал?"
    "( я пытался в█рваться или уд▓рить друкой рукой )"
    "( но движения сковало ощущение к▒кой-то беспомощности )"
    "( будто у меня силы реб▓нка, а борюсь я с чем-то непр▒одолимым )"
    sergey "Я т▒бе напомню, если не п▒мнишь."
    sergey "Первый курс. Я с█дел сзади вас с Андр█хой.."
    sergey "И чел рядом со мной тебя дразнил, стучал тебе по спине и прочее.."
    sergey "И ты под█мал, что это был я"
    sergey "Помн▒шь, как ты меня тогда назвал??"
    "( я без▒спешно пыт▓лся в▒рваться из мертв▓й хватки - откуда во▓бще у него могло б▓ть столько силы?? )"
    sergey "Помнишь как??"
    sergey "ПОМНИШЬ??!"        
    call wait(5.0) from _call_wait_113       

#День 4
label day4:
    
    $ save_name = "День 4"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 4"))
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade       
    "( зевает и потягивается )"
    dima "Мммм..."
    dima "Суббота... И не просто суббота, а суббота без универа.."
    dima "Стоп. Я же на сегодня договорился с Машей.."
    "( резко садясь в кровати )"
    dima "..У \"Будущего\" в час."
    dima "..Одновременно и интересно, и слегка нервирует."
    stop sound fadeout 1.0
    "( из коридора )"
    mama "..ты там проснулся? Давай вставай и завтракать.."
    call wait(3.0) from _call_wait_114
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("Первая половина дня прошла в делах и помощи родителям"))
    call screen black_with_text(_("К середине дня я наскоро пообедал раньше обычного времени"))
    call screen black_with_text(_("И, рассказав немало удивленной маме куда иду, вышел в полуденный зной.."))   
    $ quick_menu = True
    scene bg_road_to_busstop
    with fade
    play sound3 "audio/bg_sound_street_1.ogg"
    dima "Сегодня можно было не проделывать сложных маневров в сторону конечной остановки, а просто пойти на ближашую"
    dima "Впрочем, ехать так и так приходилось на другой конец города"
    dima "Я позвал Машу в \"Будущее\" - в кинотеатр с самым большим залом из тех, что пережили 90е"
    dima "Я не так часто бывал в кино, но именно в этот кинотеатр ходил на самые громкие премьеры тех лет, которые нельзя было пропустить.."
    dima "\"Властелин Колец\" или \"Ночной дозор\", например..."
    call wait(3.0) from _call_wait_115
    scene bg_inside_bus
    with fade
    play sound3 "audio/bg_bus_ambience.ogg" volume 1 loop    
    dima "...Интересно, что из всего этого выйдет? Мы не менялись фотками и даже не говорили об этом.."
    dima "...Как она выглядит? Что она подумает о том как выгляжу я?"
    dima ". . ."
    "( последние километры до нужной останоки таяли вместе с моим самообладанием )"
    call wait(3.0) from _call_wait_116
    scene bg_cinema_future
    play sound3 "audio/bg_sound_street_3.ogg" volume 1 loop    
    with fade
    "( я перебежал травайные пути и направился к кинотеатру. )"
    "( маршрутка немного опоздала и я приехал позже, чем рассчитывал.. а еще ведь надо было купить билеты.. )"
    stop sound fadeout 1.0
    menu (screen="choice_lower"):
        "Набрать Маше по мобильнику":
            call wait(3.0) from _call_wait_117       
    play sound "audio/sound_cellphone_dial.ogg" volume 1    
    call wait(6.0) from _call_wait_118    
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    masha "Даа.. Привет, ты где?"
    dima "Я подхожу, а ты?"
    masha "Я уже приехала, жду тебя на ступеньках слева от входа.."  
    dima "Кажется, вижу.. Сейчас"  
    call wait(3.0) from _call_wait_119
    scene bg_cinema_future_entrance
    with fade    
    show dima at left, char_scale     
    call wait(3.0) from _call_wait_120
    show masha at right, char_scale    
    call wait(2.0) from _call_wait_121
    "( я уже на подходе увидел девушку в светлом, убравшую телефон в сумочку как только мы договорили, сомнений быть не могло )"
    dima "Привет. Это я"
    masha "Привет"
    "( Она улыбнулась и почему-то протянула мне руку, которую я немного смущенно пожал )"
    dima "Ты давно ждешь? Я немного опоздал"    
    masha "Неет.. Буквально только что подошла."
    dima "Отлично! Слушай, у нас уже время - пошли за билетами"        
    masha "Конечно, пойдем. А на что мы идем?"
    dima "На \"Королевство Крестоносцев\", думаю должен быть интересным"        
    call wait(2.0) from _call_wait_122
    hide masha
    with dissolve
    call wait(1.0) from _call_wait_123
    hide dima
    with dissolve
    call wait(3.0) from _call_wait_124
    scene scn_cinema_inside
    stop sound3 fadeout 1.0
    call wait(1.0) from _call_wait_125
    " . . . "    
    call wait(3.0) from _call_wait_126
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Фильм оказался неожиданно хорошим"))
    call screen black_with_text(_("Масштабным историческим полотном с красивыми сражениями и осадами"))
    call screen black_with_text(_("После титров и под впечатлением мы щурясь выбрались в жаркий почти летний день"))    
    scene bg_cinema_future_entrance
    with fade    
    $ quick_menu = True    
    show dima at left, char_scale     
    call wait(3.0) from _call_wait_127
    show masha at right, char_scale    
    call wait(2.0) from _call_wait_128
    dima "Ну.. Как тебе?"    
    masha "Мне понравилось.. Правда, местами прям так шумно.. И еще я не очень хорошо разбираюсь в истории.. А тебе?"
    dima "Мне - очень. Я люблю историческое кино. Я тебе могу все рассказать..."    
    dima "Ты ведь не спешишь? Прогуляемся?"    
    masha "Нет, я тоже очень хочу погулять."
    "( только сейчас я хорошо рассмотрел Машу )"
    "( сначала я не успел осознать, но теперь понял, что Маша - очень симпатичная девушка )"
    "( сердце стало биться чуть учащеннее )"
    "( она мне определенно уже нравилась )"
    call wait(2.0) from _call_wait_129    
    hide masha
    with dissolve
    call wait(1.0) from _call_wait_130
    hide dima
    with dissolve
    call wait(3.0) from _call_wait_131
    play music "audio/bg_music_s_menu.ogg" volume 1
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Мы бок о бок направились по зеленым улицам города к центру, стараясь выбирать теневую сторону и прячась под кронами деревьев"))
    call screen black_with_text(_("Говорили обо всем - сначала при фильм, потом про кино вообще, потом про музыку и местные рок-группы, потом обо всем, что приходило к нам в голову"))
    call screen black_with_text(_("Невозможно было запомнить какие темы мы перебрали, но разговор шел легко и непринуженно - как только он может идти между людьми испытывающими простой искренний интерес"))
    play sound "audio/bg_sound_street_3.ogg" volume 1.2 loop
    scene bg_city_street
    with fade    
    $ quick_menu = True    
    
    show dima at left, char_scale     
    show masha at right, char_scale    
    call wait(3.0) from _call_wait_132
    dima "...Вот. И они основали на святой земле королевства. Иерусалимское, в частности.."
    dima "...И они даже какое-то время существовали. А потом мы примерно видели в кино что с ними случилось. Вот такая история"
    masha "Я не знала даже насколько это интересное время.."  
    dima "Теперь ты что-нибудь расскажи..."
    masha "Конечно, я тебе сейчас расскажу как мы ездили на Юг прошлым летом и я там каталась на лошади, представляешь.."  
    call wait(2.0) from _call_wait_133
    scene scn_dima_masha_street
    with dissolve
    " ( казалось, мы можем говорить и идти так рука об руку бесконечно )"
    " ( но, наконец, мы остановились у остановки на центральной улице города..) "
    scene scn_dima_masha_street
    call wait(5.0) from _call_wait_134
    scene bg_city_street
    with fade    
    show dima at left, char_scale     
    show masha at right, char_scale    
    call wait(3.0) from _call_wait_135
    dima "Мне очень понравилось общаться.. Но тебе, наверное, уже надо домой. Тебе с этой остановки ехать, да?"
    masha "Даа.. Я живу в ........... Мне тоже очень понравилось. Обязательно надо будет повторить..."
    dima "Понятно, а мне в микрорайон.."
    masha "Давай вечером в аське спишемся?"
    dima "Конечно!"
    call wait(2.0) from _call_wait_136
    masha "А, вон моя маршрутка.."
    masha "Дима, спасибо, мне очень понравилось! Пока!"
    dima "Пока!"
    call wait(2.0) from _call_wait_137
    hide masha
    with dissolve
    "( она немного приобняла меня и вспрыгнула на подножку подъехавшей маршрутки )"
    "( пневматическая дверь захлопнулась и она помахала мне через стекло )"
    call wait(2.0) from _call_wait_138
    hide dima
    with dissolve
    "( я направился к своей остановке и поехал домой... )"
    call wait(3.0) from _call_wait_139
    scene bg_inside_bus
    with fade
    play sound "audio/bg_bus_ambience.ogg" volume 1.5 loop  
    " . . . "
    call wait(5.0) from _call_wait_140
    stop sound fadeout 1.0
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.5
    scene black
    with dissolve
    call screen black_with_text(_("Наступил вечер..."))
    $ quick_menu = True
    scene bg_dima_flat_room_evn
    with fade
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 1 loop
    call wait(2.0) from _call_wait_141
    show dima_home at center, char_scale
    with dissolve
    dima "...странные ощущения после встречи с Машей..."
    dima "С одной стороны - было как-то легко, не так как всегда.."
    dima "Будто как-то по особенному..."
    dima "С другой - она такая красивая, веселая, живая.."
    dima "Прямая противоположность меня.."
    dima "Поэтому так притягивает.."
    dima "Но нужен ли я - такой как она?"
    dima "Все мои отношения с людьми - это какой натянутый плохой театр."
    dima "Всегда все не так и не то."
    dima "И сначала винишь во всем других, жестокий мир и прочие шаблонные фразы."
    dima "А потом всегда приходишь к выводу, что во всем виноват сам..."
    dima "..."
    dima "Если я ей скажу что чувствую.. Почти уверен, что это будет провал.."
    dima "Чудес же не бывает?"
    call wait(3.0) from _call_wait_142
    scene bg_dima_flat_room_screen_evng
    with dissolve
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop
    call wait(3.0) from _call_wait_143
    " . . . "
    play sound "audio/sound_messenger_online.ogg" volume 0.3
    " . . . "
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    call wait(1.0) from _call_wait_144
    masha_velvetmoon "Привет! Ты уже тут"
    dima_desmond "Привет) Да, я тут всегда)"
    masha_velvetmoon "Прям так и всегда)) Я как-то раз заходила и тебя не было"
    dima_desmond "Нуу.. Мне правда не то, чтобы сильно есть чем заняться, кроме компа)"
    masha_velvetmoon "Ну это мы можем исправить))"
    call wait(2.0) from _call_wait_145
    scene black
    with dissolve
    call screen black_with_text(_("Как обычно, в чате с Машей время летело незаметно..."))
    $ quick_menu = True
    scene bg_dima_flat_room_screen_evng
    with fade
    call wait(2.0) from _call_wait_146
    dima_desmond "Слушай, я хотел тебя спросить"
    masha_velvetmoon "Да?"
    dima_desmond "В общем.. Я знаю, это прозвучит глупо и, скорее всего, я говорю ерунду и ничего не получится..."
    dima_desmond "Но ты мне очень понравилась.."
    stop music fadeout 2.0
    call wait(2.0) from _call_wait_147
    " . . . "
    call wait(2.0) from _call_wait_148    
    play music "audio/bg_music_s_menu.ogg" volume 1 fadein 3.0
    masha_velvetmoon "Почему ты так считаешь, Дима? Ты мне тоже очень понравился..."    
    call wait(2.0) from _call_wait_149
    masha_velvetmoon "Давай я тебе позвоню."
    call wait(2.0) from _call_wait_150
    dima_desmond "Давай.."
    stop sound2 fadeout 1.0
    call wait(2.0) from _call_wait_151
    
    scene black
    with dissolve
    play sound "audio/sound_telephone_ring.ogg" volume 1 loop    
    call wait(4.0) from _call_wait_152    
    play sound "audio/sound_telephone_pickup.ogg" volume 1.5
    call wait(2.0) from _call_wait_153
    call screen black_with_text(". . .")
    call screen black_with_text(_("Мы говорили и говорили"))
    call screen black_with_text(_("Будто как и раньше, но как-то иначе"))
    call screen black_with_text(_("И для меня это действительно было сильно иначе"))
    call screen black_with_text(_("Так, как никогда раньше не было"))
    $ quick_menu = True
    scene scn_dima_flat_telephone
    with fade
    " . . . "
    call wait(2.0) from _call_wait_154  
    scene black
    with dissolve    
    dima_desmond "Хочешь завтра встретимя? Погуляем."
    masha_velvetmoon "Да, хочу."    
    call wait(2.0) from _call_wait_155
    scene black
    with dissolve
    call screen black_with_text(_("Маме опять пришлось загонять меня спать уже сильно позже 12 ночи потому что я мешал им с отцом своими бесконечными разговорами по телефону..."))
    call screen black_with_text(_("Но, несмотря на усталость и поздний час, заснуть было тяжело..."))
    $ quick_menu = True
    scene bg_dima_flat_room_evn
    with fade
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 1 loop
    menu (screen="choice_lower"):
        "Лечь спать":
            pause 0       
    call wait(2.0) from _call_wait_156
    scene black
    stop sound3 fadeout 1.0
    call wait(3.0) from _call_wait_157

# ░ ▒ ▓ █ ▄ ▀ ■ ▚ ▞ ▒
#День 4 - Темная сторона
label day4_darkside:    
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    play music "audio/bg_music_dark1.ogg" volume 1
    scene bg_dima_flat_corridor_dark   
    with dissolve
    call wait(2.0) from _call_wait_158
    scene black
    call wait(1.0) from _call_wait_159
    scene bg_dima_flat_corridor_dark   
    with fade
    dima "...Чт...?"
    call dark_voice_message1(darkside_voice_greeting) from _call_dark_voice_message1_3
    call wait(2.0) from _call_wait_160
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0   
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    scene bg_inside_bus_dark
    with dissolve
    call dark_voice_message2(darkside_voice_greeting) from _call_dark_voice_message2_3
    call wait(2.0) from _call_wait_161    
    dima "...По░му я еду в пустой маршр▀тке? Разве так быв▒ет..?"
    
    scene bg_unvst_busstop_dark
    with dissolve    
    dima "..."    
    dima "...в▀т бы всп▒мнить какие пар▒ сегодня"    
    dima "...какие-то же должны быть, к▒гда-то я даже помнил к▒к они называются"    
    dima "...и что на н▀х говорилось"    
    dima "...но это б▒ло так давно"        
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0
    call wait(3.0) from _call_wait_162
    scene bg_unvst_corridor_dark
    with dissolve    
    call wait(4.0) from _call_wait_163
    " . . . "    
    scene bg_unvst_auditorium_dark
    with dissolve
    " . . . "    
    dima "...Ник▀го нет"
    dima "Зач▀м я так рано с▀годня или я пер░путал дни и мы не уч░мся...?"        
    dima "Или я пер░путал год.."        
    call wait(3.0) from _call_wait_164
    play sound "audio/sound_cellphone_ring.ogg" volume 1 loop
    dima "Телеф░н? Мой телефон."  
    call wait(3.0) from _call_wait_165    
    scene scn_university_andrey_call
    dima "...Андр▒ха? Серьезно?.. Мы с н▞м не гов░рили с вып░скного.. Это было.."    
    dima "...Это было.. Оч▒нь давно.. Но как тогда.."    
    "( берет трубку )"
    stop sound
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    dima "..Да?"        
    play sound "audio/sound_cellphone_busy.ogg" volume 1 loop  
    call wait(5.0) from _call_wait_166    
    dima "Странно.. Будто сбросили..."    
    dima "Но это Андрей, его номер. Перезвоню.."    
    " . . . "
    play sound "audio/sound_cellphone_dial.ogg" volume 1 loop    
    call wait(6.0) from _call_wait_167
    stop sound
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    andrey "..Да?"
    call wait(3.0) from _call_wait_168    
    scene bg_unvst_auditorium_dark
    with dissolve
    call wait(2.0) from _call_wait_169
    show andrey_dark at center
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    call wait(3.0) from _call_wait_170
    dima "Андрей, ты?.."
    andrey "..Да, прив▞т, Диман."
    dima "Пр▓вет. Ты звонил же?"
    " . . . "
    andrey "Да, Диман. Изв▓ни, ошибся номером."
    dima ". . ."
    dima "Бывает.."
    dima "Ну ты к▓к во▀бще? Ты вс▀ еще в .... жив▞шь? Сто лет не общались.."
    andrey "Да все н▀рмально, да, все т▀м же.."
    andrey "В общем ..."
    "( голос в тел▓фоне звуч▞л как гол▀с человека для кот▞рого разговор - внез▀пно возн▀кшая немного досадная помеха )"
    dima "Да. У м▀ня т▞же все нормально."
    dima "Если чт▓, ты звони.."
    andrey "Хорошо. П▞ка, Дим▀н."
    dima "П▞ка.."
    hide andrey_dark
    with dissolve
    play sound "audio/sound_cellphone_busy.ogg" volume 1 loop  
    dima ". . ."
    stop sound fadeout 10
    call wait(1.0) from _call_wait_171
    " . . ."    
    
#День 5
label day5:
    
    $ save_name = "День 5"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 5"))
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade           
    dima " . . . "
    dima "Я слышал, что во сне мы видим то, что подсознательно нас тревожит"
    dima "или оставило сильное, пускай и неосознанное впечатление в жизни..."
    dima " . . . "
    dima "Наверное, хорошо, что сегодня мне ничего не снилось."
    dima " . . . "
    stop sound fadeout 2.0
    dima "Неужели вчерашнее было правдой? Она правда сказала, что я ей нравлюсь?"
    dima "До сих пор не укладывается, что я могу понравиться такой красивой девушке как она..."
    dima "Сегодня в час в центре встреча с Машей..."
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("Все утро я был немного не в себе."))
    call screen black_with_text(_("Будто какая-то эйфория подогревала изнутри."))
    call screen black_with_text(_("Обычные напряжение и пустота последних месяцев сменились маленьким теплым солнцем, поселившимся где-то в середине груди"))
    call screen black_with_text(_("Я с трудом дотянул последний час до выхода из дома."))
    $ quick_menu = True    
    scene bg_road_to_busstop
    with fade    
    dima " . . . "
    call wait(3.0) from _call_wait_172
    scene bg_inside_bus
    with fade
    play sound3 "audio/bg_bus_ambience.ogg" volume 1.2 loop    
    dima "Мы договорились встретиться в центре и просто погулять, никуда не спеша..."
    dima "С одной стороны я волновался..."
    dima "Но ведь мне же не показалось все то, о чем мы говорили вчера.."
    dima ". . ."    
    call wait(3.0) from _call_wait_173
    play sound3 "audio/bg_sound_street_3.ogg" volume 1.2 loop
    scene bg_city_street
    with fade
    "Я ждал на остановке."
    show dima at center, char_scale
    with dissolve
    "Долго ждать не пришлось и скоро я увидел Машу."
    call wait(3.0) from _call_wait_174
    hide dima
    call wait(2.0) from _call_wait_175
    show dima at left, char_scale
    call wait(1.0) from _call_wait_176
    show masha at right, char_scale    
    dima "Привет!"
    masha "Привет!"
    dima "Пойдем?"
    masha "Да!"
    play music "audio/bg_music_s_menu.ogg" volume 0.6   
    $ quick_menu = False
    scene black
    with dissolve
    play sound3 "audio/bg_sound_street_1.ogg" volume 1.2 loop
    call screen black_with_text(_("Мы решили направиться по центральным улицам куда глаза глядят"))
    call screen black_with_text(_("Толком не выбирая маршрут, просто шли по тихим и тенистым улицам провинциального центра, на перекрестках вместе интуитивно решая куда свернуть..."))
    $ quick_menu = True        
    scene bg_spring_city_street
    with fade
    " . . . "
    "Мне нравились эти улицы. Многоэтажные старые и местами обшарпанные дома перемежались деревянными часто покосившимися домиками из совсем уж из древних времен"
    scene bg_spring_city_street
    call wait(5.0) from _call_wait_177
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("Ноги привели нас к реке и запущенному парку на ее берегу"))    
    call screen black_with_text(_("Хоть и до центра города было рукой подать - но здесь было тихо, а на другом берегу виднелись частные одноэтажные дома"))
    call screen black_with_text(_("Все это место было тихим маленьким уголком в стороне от шумной улицы"))
    $ quick_menu = True    
    play sound3 "audio/bg_forest_ambience.ogg" volume 1.2 loop    
    scene bg_river_park_2
    with fade
    "Мы шли по перекинутому через неширокую реку пешеходному подвесному мосту, нагретому полуденным весенним солнцем."
    scene scn_hand_in_hand_bridge
    with fade
    call wait(5.0) from _call_wait_178
    "Только сейчас я решился дотронуться до ее ладони, она улыбнулась и дальше мы пошли держась за руки."
    scene scn_hand_in_hand_bridge
    call wait(5.0) from _call_wait_179    
    scene bg_river_park_1
    call wait(5.0) from _call_wait_180
    with fade
    "Мы перешли реку и вступили под тень деревьев."
    "Стрекотали кузнечики, солнце пробивалось через густую листву и заливало своим светом покосившиеся разрисованные заборы, крыши домов и неряшливые запущенные лужайки."
    scene bg_river_park_1
    call wait(3.0) from _call_wait_181
    show dima at left, char_scale
    with dissolve
    show masha at right, char_scale    
    with dissolve
    masha "Давай туда, там можно идти и идти вдоль реки.. И в итоге прийти на Боярскую горку.. Смешное название, да?"
    dima "Да, забавное.."
    "Я знал это место и мне тоже хотелось идти и идти так, держась за руки, чтобы наш маршрут петлял под тенистыми кронами и никогда не кончался."
    scene bg_river_park_bench
    with fade
    call wait(2.0) from _call_wait_182
    show dima at left, char_scale
    with dissolve
    show masha at right, char_scale    
    with dissolve
    masha "Смотри, скамейка!"
    dima "Давай сядем?"
    masha "Давай."
    call wait(2.0) from _call_wait_183
    hide dima
    with dissolve
    hide masha
    with dissolve
    scene black
    "Мы распложились рядом с видом на неспешно текущую зеленоватую реку в обрамлении густых касающихся почти самой воды зарослей"
    call wait(2.0) from _call_wait_184
    scene scn_river_park_on_bench2
    with dissolve
    call wait(4.0) from _call_wait_185
    dima "Мне так хорошо сейчас с тобой..."   
    masha "Мне тоже.."
    scene scn_hand_in_hand_river_park
    with dissolve
    call wait(4.0) from _call_wait_186
    "Я машинально сорвал рукой несколько травинок и рассматривал их на своей раскрытой ладони."
    "Ее пальцы играли с этими колосками щекоча мою руку."    
    scene scn_river_park_on_bench2
    with dissolve
    call wait(4.0) from _call_wait_187
    dima "Знаешь..."
    dima "Стыдно признаться, но у меня никогда не было настоящих отношений..."
    call wait(3.0) from _call_wait_188
    dima "И смешно.. Я сейчас хочу тебя поцеловать и понимаю, что никогда этого раньше не делал."    
    call wait(3.0) from _call_wait_189
    dima "Поэтому я просто поцелую тебя в щеку."    
    scene scn_river_park_on_bench
    with dissolve  
    " . . . "
    call wait(3.0) from _call_wait_190
    masha "Ты всему научишься, не бойся.."     
#День 6
label day6:
    $ save_name = "День 6"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 6"))
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.6
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade       
    "( зевает и потягивается )"
    dima "Мммм... По-не-де-ль-ник"
    dima "Странно, почему я чувствую себя таким выспавшимся? А не как обычно по утрам, когда надо ехать на пары..."
    dima " . . . "
    dima "А может, у меня теперь броня? Может, я непобедим? Может, теперь ничто не может меня по-настоящему достать?"
    dima " . . . "
    dima "Так странно. Будто что бы плохое теперь не произошло - это теперь не важно."
    dima " . . . "    
    call wait(3.0) from _call_wait_191
    scene black
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(3.0) from _call_wait_192    
    scene bg_inside_bus
    with fade
    play sound3 "audio/bg_bus_ambience.ogg" volume 1.5 loop
    dima "...Даже не верится."   
    dima "Неужели, у меня теперь есть девушка, которая мне по-настоящему нравится..."   
    dima "С которой мне по-настоящему хорошо..."   
    dima "Я даже не думал насколько это может менять отношение ко всему.."   
    dima "А, может, я просто как наркоман сейчас на гормонах, которые производит собственный организм?.."   
    dima "Как бы то ни было..."   
    stop sound fadeout 1.0        
    $ quick_menu = False
    scene black
    with dissolve
    call screen black_with_text(_("Время летело быстро..."))
    $ quick_menu = True        
    call wait(3.0) from _call_wait_193
    scene bg_unvst_corridor
    with fade    
    play sound3 "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    call wait(3.0) from _call_wait_194
    scene bg_unvst_auditorium
    with fade
    call wait(2.0) from _call_wait_195
    show dima at left, char_scale
    call wait(2.0) from _call_wait_196
    show andrey at right, char_scale
    andrey "..Ты какой-то.. О чем думаешь вообще?"
    dima "Да? А что, заметно?"
    andrey "Ага. Молчишь, смотришь куда-то в точку.."
    dima "...."
    dima "Ну да, наверное, есть такое."
    andrey "?"
    dima "Я с девушкой познакомился."
    andrey "Да ладно, вот от тебя я такого не ожидал."
    dima "Хе. Ну да, спасибо за доверие."
    andrey "И где ты нашел себе девушку?"
    dima "Угадай. В аське."
    andrey "Логично."
    andrey "Но, я смотрю, ты серьезен по поводу этого."
    dima "Да. Давай потом расскажу."
    andrey "Как скажешь."
    scene black
    $ quick_menu = False
    play sound3 "audio/bg_bus_ambience.ogg" volume 1.5 loop
    call screen black_with_text(". . .")    
    call screen black_with_text(_("Все происходящее казалось каким-то далеким..."))    
    call screen black_with_text(_("Как будто потерявшим важность и значение."))
    call screen black_with_text(_("А может, наоборот, из незначащих вещей исчез излишний надуманный смысл? И не о чем было больше волноваться."))
    stop sound3 fadeout 1.0
    scene bg_dima_flat_room_evn
    with fade    
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 0.2 loop
    $ quick_menu = True
    scene bg_dima_flat_room_evn    
    with fade
    call wait(2.0) from _call_wait_197
    show dima_home at center, char_scale
    with dissolve
    dima "Интересно, сегодня вечером мы созвонимся с Машей..?"
    call wait(3.0) from _call_wait_198
    play sound "audio/sound_messenger_sound.ogg" volume 0.3
    call wait(2.0) from _call_wait_199
    dima "Ого, интересно, это она?"
    scene bg_dima_flat_room_screen_evng
    with dissolve
    play sound "audio/bg_keyboard.ogg" volume 1.5 loop
    masha_velvetmoon "Привет!"
    dima_desmond "Привет)"
    masha_velvetmoon "Наберу?"
    dima_desmond "Давай"
    play sound "audio/sound_telephone_ring.ogg" volume 1 loop    
    call wait(3.0) from _call_wait_200    
    play sound "audio/sound_telephone_pickup.ogg" volume 1
    call wait(1.0) from _call_wait_201
    scene bg_dima_flat_room_phone
    call wait(2.0) from _call_wait_202
    masha "Привет"
    dima "Ну как ты..?"
    scene black
    with dissolve
    $ quick_menu = False    
    call screen black_with_text(_("Мы поболтали о том как прошел день и обо всяких студенческих делах..."))        
    $ quick_menu = True
    scene bg_dima_flat_room_phone    
    with dissolve
    call wait(2.0) from _call_wait_203        
    dima "...Значит, ты теперь официально моя девушка, а я твой парень?" 
    dima "Забавно звучит..." 
    masha "Даа.. Официально так и есть. Ты так это смешно говоришь."
    dima "Я стараюсь!"    
    masha "Хи-хи"
    dima "Ты просто извини, у меня такое время в жизни..."
    play music2 "audio/bg_music_mech_horizon_1.ogg" volume 0.4
    stop music fadeout 5.0
    stop sound3 fadeout 5.0
    masha "?"
    dima "Я себя немного неполноценным чувствую.."
    call wait(1.0) from _call_wait_204
    dima "У тебя вот были отношения, есть подруги, друзья..."
    call wait(1.0) from _call_wait_205
    dima "А я.. У меня всегда были с этим проблемы"
    call wait(1.0) from _call_wait_206
    dima "Я еще когда в школе в другой класс перешел - все пошло как-то наперекосяк."
    call wait(1.0) from _call_wait_207
    dima "Не знаю.. Может со мной что-то не так.."
    call wait(1.0) from _call_wait_208
    masha "Дим.. Мне кажется, ты преувеличиваешь.."
    call wait(1.0) from _call_wait_209
    masha "Ты очень симпатичный и интересный в общении и, я думаю, это все временные проблемы.."
    dima "Спасибо. Просто эти временные проблемы затянулись уже на много лет.."
    call wait(1.0) from _call_wait_210
    dima "Я даже в универе общаюсь с парнями, но ощущаю себя каким-то чужим.."
    call wait(3.0) from _call_wait_211
    dima "Никчемным.."
    call wait(2.0) from _call_wait_212
    masha "Дим, слушай..."
    call wait(2.0) from _call_wait_213
    masha "Слуууушай."
    stop music2 fadeout 20.0
    play sound2 "audio/sound_ocean_waves.ogg" volume 1 fadein 10.0 loop
    call wait(3.0) from _call_wait_214
    masha "Мы с родителями ездили в Индию.."
    call wait(2.0) from _call_wait_215
    masha "И я сейчас вспомнила.. Послушай"
    call wait(3.0) from _call_wait_216
    masha "Шшшшшш....."
    call wait(3.0) from _call_wait_217
    dima "?"    
    call wait(2.0) from _call_wait_218
    masha "Слушай. Шшшшшшш..."
    masha "Это океан."        
    masha "Представь."
    masha "Шшшшшш....."
    masha "Это волны набегают на берег.. А потом катятся обратно.."
    masha "Пена щекочет ноги... Закрой глаза и слушай.. Шшшшш...."
    call wait(2.0) from _call_wait_219
    scene black
    $ quick_menu = False    
    $ renpy.sound.set_volume(5.0, delay=5.0, channel='sound2')
    call wait(5.0) from _call_wait_220
    call screen black_with_text(_("- ...А потом..."))        
    call screen black_with_text(_("- Я попрошу у папы надувную лодку..."))
    call screen black_with_text(_("- И мы с тобой отправимся в плавание по реке.. Хочешь?"))
    call screen black_with_text(_("- Да. Правда я даже плавать на лодке не умею.."))
    call screen black_with_text(_("- Это ничего, возьмем еды, зонтик от солнца, я так уже делала - будет классно, вот увидишь.."))
    $ quick_menu = True     

# ░ ▒ ▓ █ ▄ ▀ ■ ▚ ▞ ▒
#Последняя ночь
label fnight:
    $ save_name = "Ночь"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 7"))
    stop sound2 fadeout 3.0
    call screen black_with_text(_("День 8"))
    call screen black_with_text(_("Ночь"))
    $ quick_menu = True 
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    play music "audio/bg_music_dark1.ogg" volume 1
    scene bg_dima_flat_corridor_dark   
    with dissolve
    call wait(2.0) from _call_wait_221
    scene black
    call wait(1.0) from _call_wait_222
    scene bg_dima_flat_corridor_dark   
    with fade
    dima "...Чт...?"
    call dark_voice_message1(darkside_voice_greeting) from _call_dark_voice_message1_4
    call wait(2.0) from _call_wait_223
    menu (screen="choice_lower"):
        "Идти вперед":
            pause 0   
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    scene bg_inside_bus_dark
    with dissolve
    call dark_voice_message2(darkside_voice_greeting) from _call_dark_voice_message2_4
    call wait(2.0) from _call_wait_224
    dima "...Дост▒точно в▚йти через двери этой м▒ршрутки и сразу ок▚жешься в том м▒сте, которое иск▒л.."
    dima "...Поч▒му нел▚зя всегда так?.."
    call wait(3.0) from _call_wait_225
    scene black
    with fade
    call wait(3.0) from _call_wait_226
    scene bg_river_park_1_dark
    with fade
    call wait(3.0) from _call_wait_227
    dima "Нет.."
    call wait(3.0) from _call_wait_228
    play sound "audio/sound_surprise_fx_dark.ogg" volume 1
    show masha_dark1 at center
    with dissolve
    call wait(2.0) from _call_wait_229 
    masha "...Дима, ты м▒ня обманул..."
    dima "..."
    masha "...Мне б▒ло тяжело.. Меня бр▚сили.. Я дум▒ла с тобой мне станет легче.."
    masha "...Ты был так▒й интересный, умный, ст▒лько рассказывал. Мне не было так инт▒ресно с другими парнями как с тобой.."    
    dima "..."
    call wait(3.0) from _call_wait_230
    hide masha_dark1
    with dissolve
    call wait(2.0) from _call_wait_231
    dima "Ты к▒да? Подожди.."
    call wait(3.0) from _call_wait_232    
    scene bg_river_park_bench_dark
    with fade
    dima "То самое место..."
    call wait(3.0) from _call_wait_233
    show masha_dark1 at center
    with dissolve
    masha "...Но ты все исп▒ртил."
    masha "...Теп▒рь все не так."
    masha "Я в тебе ош▚блась. Теп▒рь мне хуже с тоб▒й, чем без тебя.."
    masha "Я д▒лжна быть сильн▒й, а с тобой я сл▒бею.."    
    masha "Зач▒м ты все так исп▒ртил?.."
    masha "Я ошибл▒сь в тебе.."
    masha "Я правд▒ пыталась пом▒чь тебе, но я нич▒го не м▒гу сделать.."
    masha "Ты с▚м должен разобр▚ться в себе б▚з меня.."
    call wait(3.0) from _call_wait_234
    show masha_dark2 at center
    with dissolve
    call wait(2.0) from _call_wait_235
    dima "Под▚жди.."
    dima "Я.. Я все испр▒влю.. Я не знал"
    dima "Я не..."
    call wait(3.0) from _call_wait_236
    hide masha_dark1
    with dissolve
    hide masha_dark2
    with dissolve
    call wait(3.0) from _call_wait_237 
    
#День 9
label day9:
    $ save_name = "День 9"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("День 9"))
    play sound3 "audio/bg_sound_street_1.ogg" volume 0.6 loop
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.4
    play sound "audio/sound_alarm_clock_1.ogg" volume 0.6
    scene bg_dima_flat_room
    with fade    
    $ quick_menu = True
    show dima_home at center, char_scale
    with fade       
    "( зевает и потягивается )"    
    call wait(4.0) from _call_wait_238
    
    $ quick_menu = False        
    call wait(5.0) from _call_wait_239
    scene black        
    play sound "audio/sound_morning_preparations_1.ogg" volume 1
    call wait(4.0) from _call_wait_240
    call screen black_with_text(". . .")
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(3.0) from _call_wait_241
    call screen black_with_text(" . . .")
    play sound "audio/bg_sound_street_1.ogg"
    call wait(5.0) from _call_wait_242
    call screen black_with_text(". . .")
    play sound "audio/bg_sound_street_2.ogg" volume 1.5 loop
    call wait(5.0) from _call_wait_243
    call screen black_with_text(". . .")
    play sound "audio/bg_bus_ambience.ogg" volume 1.5 loop
    call wait(5.0) from _call_wait_244
    call screen black_with_text(". . .")
    play sound "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    call wait(5.0) from _call_wait_245
    call screen black_with_text(". . .")
    play sound "audio/bg_bus_ambience.ogg" volume 1.5 loop
    call wait(5.0) from _call_wait_246
    call screen black_with_text(". . .")
    play sound "audio/sound_flat_door_slam_1.ogg" volume 0.8
    call wait(5.0) from _call_wait_247   
    $ quick_menu = True 
    
    scene bg_dima_flat_room_screen_evng
    play sound3 "audio/sound_evening_grasshoppers.ogg" volume 0.2 loop
    with fade    
    call wait(3.0) from _call_wait_248
    play sound "audio/sound_messenger_online.ogg" volume 0.3
    call wait(2.0) from _call_wait_249
    " . . . "
    play music "audio/bg_music_mech_horizon_2_1.ogg" volume 0.6
    call wait(4.0) from _call_wait_250
    " . . . "
    play sound2 "audio/bg_keyboard.ogg" volume 1.2 loop    
    dima_desmond "Привет)"
    call wait(4.0) from _call_wait_251
    masha_velvetmoon "Привет"
    call wait(2.0) from _call_wait_252
    dima_desmond "А у меня тоже трек есть, который неплохо ко мне подходит сейчас. Хочешь послушать?"
    call wait(2.0) from _call_wait_253
    masha_velvetmoon "Нет."
    stop music fadeout 5.0
    play music2 "audio/bg_music_mech_horizon_2_2.ogg" volume 0.6 fadein 5.0 loop
    masha_velvetmoon "Дима. Я думаю нам не стоит больше общаться.."
    call wait(5.0) from _call_wait_254
    dima_desmond "Я не понимаю.. Можно я тебе позвоню?"
    stop sound fadeout 3.0
    masha_velvetmoon "Звони."
    stop sound2 fadeout 5.0
    call wait(2.0) from _call_wait_255
    scene bg_dima_flat_room_phone
    with fade
    call wait(2.0) from _call_wait_256
    play sound "audio/sound_cellphone_dial.ogg" volume 1    
    call wait(7.0) from _call_wait_257
    play sound "audio/sound_telephone_pickup.ogg" volume 2
    call wait(2.0) from _call_wait_258
    masha "Да?"
    dima "Что случилось..?"
    masha "...."    
    masha "Я не могу с тобой больше общаться."
    call wait(2.0) from _call_wait_259
    masha "Каждый диалог в таком духе. Я просто умираю от всего этого, мне физически плохо."
    call wait(2.0) from _call_wait_260
    masha "Дима. Ты постоянно ноешь. Я не могу это больше слушать.."
    call wait(3.0) from _call_wait_261
    dima "..."
    call wait(3.0) from _call_wait_262
    masha "Понимаешь. Ты эмоциональный вампир. Ты высасываешь из меня силы.."
    call wait(1.0) from _call_wait_263
    play sound "audio/sound_telephone_pickup.ogg" volume 4
    scene black
    dima "..."
    call wait(3.0) from _call_wait_264
    dima "Я положил трубку. Это был последний раз, когда я слышал ее голос."
    stop sound3 fadeout 1.0
    stop music2 fadeout 2.0
    play music "audio/bg_music_mech_horizon_2_3.ogg" volume 1 fadein 2.0 loop
    call wait(5.0) from _call_wait_265    
    scene black
    call wait(3.0) from _call_wait_266    
    show scn_dima_bed at slow_rotation    
    call wait(5.0) from _call_wait_267    
    show scn_hand_in_hand_bridge at truecenter:
        matrixcolor SaturationMatrix(0.0) # 0.0 — полностью ЧБ, 1.0 — цветное
    call wait(5.0) from _call_wait_268
    hide scn_hand_in_hand_bridge
    call wait(5.0) from _call_wait_269
    show scn_cinema_inside at truecenter:
        matrixcolor SaturationMatrix(0.0) # 0.0 — полностью ЧБ, 1.0 — цветное
    call wait(5.0) from _call_wait_270
    hide scn_cinema_inside
    call wait(5.0) from _call_wait_271    
    show scn_hand_in_hand_river_park at truecenter:
        matrixcolor SaturationMatrix(0.0) # 0.0 — полностью ЧБ, 1.0 — цветное
    call wait(5.0) from _call_wait_272
    hide scn_hand_in_hand_river_park
    call wait(5.0) from _call_wait_273    
    show scn_river_park_on_bench at truecenter:
        matrixcolor SaturationMatrix(0.0) # 0.0 — полностью ЧБ, 1.0 — цветное
    call wait(5.0) from _call_wait_274
    hide scn_river_park_on_bench
    call wait(5.0) from _call_wait_275
    show scn_dima_masha_street at truecenter:
        matrixcolor SaturationMatrix(0.0) # 0.0 — полностью ЧБ, 1.0 — цветное
    call wait(10.0) from _call_wait_276
    scene black
    with dissolve
    call wait(3.0) from _call_wait_277
    dima "Я пару раз пытался написать.. И что-то поменять.."
    dima "Потом пришло понимание, что ошибки сделаны уже ничего не вернуть."
    dima "Еще позже я понял, что ошибки все равно были бы сделаны в любом случае и не было никакой возможности их избежать"    
    ". . ."    
#Эпилог
label epilogue:
    $ save_name = "Эпилог"
    scene black
    $ quick_menu = False
    call screen black_with_text(_("Эпилог"))
    call screen black_with_text(_("..спустя время.."))
    play music "audio/bg_music_s_gameplay1.ogg" volume 0.4        
    play sound "audio/bg_crowd_ambience_1.ogg" volume 1.2 loop
    $ quick_menu = True
    scene bg_unvst_corridor
    with fade    
    call wait(2.0) from _call_wait_278
    show dima at right, char_scale
    with dissolve
    call wait(3.0) from _call_wait_279
    show masha at left, char_scale
    with dissolve
    call wait(3.0) from _call_wait_280
    dima "..."
    call wait(3.0) from _call_wait_281
    masha "..."
    call wait(3.0) from _call_wait_282
    hide masha
    with dissolve
    call wait(3.0) from _call_wait_283
    show andrey at left, char_scale
    with dissolve
    call wait(2.0) from _call_wait_284
    andrey "Ты чего встал? Кто это..?"
    call wait(2.0) from _call_wait_285
    dima "Ничего. Пошли."
    call wait(3.0) from _call_wait_286
    hide dima
    with dissolve
    call wait(2.0) from _call_wait_287
    hide andrey
    with dissolve
    call wait(2.0) from _call_wait_288
    scene black
    stop sound fadeout 1.0
    $ quick_menu = False
    play music "audio/bg_music_mech_horizon.ogg" volume 0.5
    call screen black_with_text(_("Прошли годы"))
    $ quick_menu = True
    call wait(3.0) from _call_wait_289    
    scene bg_epilogue
    with fade    
    call wait(5.0) from _call_wait_290
    show dima_epilogue at center, char_scale
    with dissolve
    call wait(3.0) from _call_wait_291
    dima "С того времени через мою жизнь прошли насквозь и исчезли десятки людей и мест.."
    call wait(2.0) from _call_wait_292
    dima "Некотороые из них безвовзратно стерлись из памяти."
    call wait(2.0) from _call_wait_293
    dima "Но мне кажется..."
    call wait(2.0) from _call_wait_294
    dima "Где-то там, глубоко."
    call wait(2.0) from _call_wait_295
    dima "За правильным поворотом в закоулках памяти."
    call wait(2.0) from _call_wait_296
    dima "Все еще есть этот залитый ярким весенним солнцем город."
    call wait(3.0) from _call_wait_297
    dima "И мы бесконечно идем взявшись за руки по его улицам..."
    call wait(3.0) from _call_wait_298
    hide dima_epilogue
    with dissolve
    scene bg_epilogue
    call wait(5.0) from _call_wait_299    
    scene black
    $ quick_menu = False
    $ renpy.music.set_volume(1.0, delay=5.0, channel='music')
    call screen black_with_text(_("КОНЕЦ"))    
    
#Конец и титры
label ending:

    #call screen credits(True)        
    #$ renpy.call_screen("credits", from_game_end=True, _tag="menu")
    
    #$ renpy.call_in_new_context("_credits_from_end")    
    #$ renpy.full_restart()
    
    $ renpy.show_screen("credits", from_game_end=True)
    $ renpy.pause(hard=True)
    
    return

label wait(t):
    $ is_waiting = True
    pause t
    $ is_waiting = False
    return    

label splashscreen:

    $ set_first_launch_language()

    return