init -1 python:
    balance = 0
    global_event = "start"
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
        f = open(r"C:\Users\Lumberjack\code\renpy\asd\test.txt", "a")
        f.write(str(data))
        f.write("\n")
        f.close()

    def get_initial_branch(character_branch, character_chat_history, about=None):
        # Пока что пусть определяет исходя из времени на устройстве
        global current_branch, topic
        # global_event это например концерт
        if about in character_branch and about not in character_chat_history:
            current_branch, topic = character_branch[about], about
            return

        if global_event in character_branch and global_event not in character_chat_history:
            current_branch, topic = character_branch[global_event], global_event
            return


label start:
    # $ current_branch, topic = get_initial_branch(answers["Dad"], "rock_concert")
    call screen actions_screen("Dad")


screen money_balance():
    modal True

    frame:
        vbox:
            text "Your account balance has been topped up"
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
    python:
        if who not in history:
            history[who] = {}
        character_branch = answers[who]
        character_chat_history = history[who]
        get_initial_branch(character_branch, character_chat_history, about)

    vbox:
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
                        action (Function(update_character_chat_history, character_chat_history, topic, option), SetVariable("current_branch", up))
