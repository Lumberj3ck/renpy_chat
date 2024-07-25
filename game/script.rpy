init -1 python:
    balance = 0
    global_event = ""
    current_branch = {}
    topic = ""

    # Для того чтобы удостовериться что пополнялось один раз за одну ветку
    last_balance_top_up_branch = ""

    def move_branch_to_the_option(branch, option):
        # if current_branch
        current_branch = branch["replies"][option]
        return current_branch

    def update_current_branch_path(option):
        global current_branch_path
        current_branch_path += option

    def update_character_chat_history(character_chat_history, topic, option):
        if topic in character_chat_history:
            character_chat_history[topic] = character_chat_history[topic] + option
        else:
            character_chat_history[topic] = option

    def top_up_money_if_required(current_branch, character_chat_history, topic):
        global balance, last_balance_top_up_branch, current_branch_path

        money_amount = current_branch.get("money_top_up", 0)

        if topic in character_chat_history:
            current_branch_path = topic + character_chat_history[topic]

            if money_amount > 0 and last_balance_top_up_branch != current_branch_path:
                balance += money_amount
                last_balance_top_up_branch = current_branch_path
                return True
        return False

    def print_to_file(data):
        f = open(r"C:\Users\Lumberjack\code\renpy\asd\test.txt", "w")
        f.write(str(data))
        f.write("\n")
        f.close()

    # def get_initial_branch(character_branch, character_chat_history, about=None):
    #     global topic
    #     if about in character_branch and about not in character_chat_history:
    #         topic = about
    #         return character_branch[about]

    #     if global_event in character_branch and global_event not in character_chat_history:
    #         topic = global_event
    #         return character_branch[global_event]

        # Default case
        # topic = "start"  # or any default topic you prefer
        return {}
    def get_initial_branch(character_branch, character_chat_history, about=None):
        global topic

        def navigate_to_branch(branch, path):
            for option in path:
                if "replies" in branch and option in branch["replies"]:
                    branch = branch["replies"][option]
                else:
                    return None
            return branch

        # Check if about is provided and not finished
        if about in character_branch:
            if about not in character_chat_history:
                topic = about
                return character_branch[about]
            else:
                branch = navigate_to_branch(character_branch[about], character_chat_history[about])
                if branch and "replies" in branch:
                    topic = about
                    return branch

        # Check if global_event is available and not finished
        if global_event in character_branch:
            if global_event not in character_chat_history:
                topic = global_event
                return character_branch[global_event]
            else:
                branch = navigate_to_branch(character_branch[global_event], character_chat_history[global_event])
                if branch and "replies" in branch:
                    topic = global_event
                    return branch

        return {}


label start:
    # $ current_branch, topic = get_initial_branch(answers["Dad"], "rock_concert")
    

    show screen contacts
    ""


    # show screen actions_screen("Dad")
    # ""
    # "Rock!"

    # $ global_event = "rock_concert"
    # show screen actions_screen("Dad")
    # ""
    # $ global_event = "dinner"
    # show screen actions_screen("Dad")
    ""



screen contacts:
    vbox:
        align (0.5,0.5)
        textbutton "Dad" action Show ("actions_screen",who="Dad", about="rock_concert")
        textbutton "Sister" action Show ("actions_screen",who="Sister")


screen money_balance():
    modal True

    
    frame:
        xalign 1.0
        vbox:
            text "Balance:"
            text str(balance)
            textbutton "Close":
                action Hide("money_balance")

# 1. Call the screen with character name and about topic
# 2. Get the branch for the topic automatically
# 2. Get the character name and the topic to speak
# 3. If there is already history chat with this character load it
# 4. Save the options for dialogs

# About is not mandatory argument
screen actions_screen(who, about=None):
    use money_balance 
    modal True

    python:
        if who not in history:
            history[who] = {}
        character_branch = answers[who]
        # Достать ветки из словаря для персонажа 
        # словарь должен быть назван например вот так: Dad_dialogs
        # ну или поменять просто строчку 
        # character_branch = globals()[who+"_dialogs"]
        character_chat_history = history[who]
    # using local var instead of global which cause a problem 
    default current_branch = get_initial_branch(character_branch, character_chat_history, about)
    

    vbox:
        textbutton "close" action Hide ("actions_screen")

        for branch, options in character_chat_history.items():
            $ render_branch = character_branch[branch]
            $ character_start = render_branch.get("character_start", False)
            if character_start:
                    hbox:
                        text render_branch["message"]
            for option in options:
                $ render_branch = move_branch_to_the_option(render_branch, option)
                $ is_image = render_branch.get("is_image")

                text render_branch["reply_message"] 
                if "message" in render_branch:
                    if is_image:
                        add render_branch["message"]
                    else:
                        text render_branch["message"] 

        # Если диалог начинает персонаж то мы добавим вот это после загрузки чата
        $ character_start = current_branch.get("character_start", False)
        if character_start:
                hbox:
                    text current_branch["message"]

    $ money_toped_up = top_up_money_if_required(current_branch, character_chat_history, topic)
    if money_toped_up: 
        use money_balance

    $ replies_present = current_branch.get("replies") 
    if replies_present:
        vbox:
            
            for option, repl in current_branch["replies"].items():
                $ up = current_branch["replies"][option]
                hbox: 
                    xpos 2.5
                    textbutton "[repl['reply_message']]":
                        action (Function(update_character_chat_history, character_chat_history, topic, option), SetScreenVariable("current_branch", up))