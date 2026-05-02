init python:
    import locale

    def set_first_launch_language():
        if persistent.language_initialized:
            return

        system_locale = locale.getdefaultlocale()[0] or ""

        if system_locale.lower().startswith("ru"):
            renpy.change_language("russian")
        else:
            renpy.change_language("english")

        persistent.language_initialized = True
        renpy.save_persistent()