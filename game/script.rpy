init -1 python:
    # 19:45
    # В будущем загружать диалоги из файла
    # import json
    # answers = json.load(open(r"C:\Users\Lumberjack\code\renpy\asd\game\d\dialogs.json"))
    # answers = json.load(open(r"../game/d/dialogs.json"))
    # from dialogs import answers
    # answers =  {
    # "message": "Hi son",
    # "replies":
    # {
    # "a": {
    #     "message": "Hi man",
    #     "reply_message": "Hi, dad",
    #     "replies": {
    #     "a": {
    #         "message": "I don't know what to say", 
    #         "reply_message": "Okay, Bye",
    #         "replies": {
    #             "a": {"message": "You're not my son anymore, 🖕", "reply_message": "Fuck off", },
    #             "b": {"message": "Love you too ❤️\nBye", "reply_message": "Love you"},
    #             "required_chapter": 2
    #         }
    #     }, 
    #     "b": {"message": "You're borring", "reply_message": "Ok"},
    #     "c": {"message": "Oh, shoot", "reply_message": "shit fuck off"}
    #     }
    # },
    # "b": {
    #     "message": "I love you too, son",
    #     "reply_message": "Hi, dad, I love you!",
    #     "replies": {
    #     "a": {"message": "rose.png", "reply_message": "Okay, Bye", "is_image": True}, 
    #     "b": {"message": "Okay, I sent it", "reply_message": "I need some money, please", "money_top_up": 10},
    #     "c": {"message": "Oh, shoot", "reply_message": "shit fuck off"}
    #     }
    # },
    # }
    # }

    balance = 0
    current_branch_path = ""
    current_chapter = 1
    branch_path = {
        "Dad": ""
    }
    # Для того чтобы удостовериться что пополнялось один раз за одну ветку
    last_balance_top_up_branch = ""

    def move_branch_to_the_option(current_branch, option):
        current_branch = current_branch["replies"][option]
        return current_branch

    def update_current_branch_path(option):
        global current_branch_path
        current_branch_path += option

    def top_up_money_if_required(current_branch):
        global balance, last_balance_top_up_branch, current_branch_path

        money_amount = current_branch.get("money_top_up", 0)

        if money_amount > 0 and last_balance_top_up_branch != current_branch_path:
            balance += money_amount
            last_balance_top_up_branch = current_branch_path
            return True

        return False
        # Проверял баланс
        # f = open(r"C:\Users\Lumberjack\code\renpy\asd\test.txt", "a")
        # f.write(str(balance))
        # f.write(str(current_branch) + "\n")
        # # f.write("asdf")
        # f.close()

    def get_initial_branch(character_branch, about=None):
        # Пока что пусть определяет исходя из времени на устройстве
        current_hour = datetime.now().hour
        # global_event это например концерт
        if global_event in character_branch:
            return character_branch[global_event]
        if about in character_branch:
            return character_branch[about]
        if current_hour < 12 and "morning" in character_branch:
            return character_branch["morning"]
        elif current_hour < 18 and "afternoon_chat" in character_branch:
            return character_branch["afternoon_chat"]
        elif "evening_talk" in character_branch:
            return character_branch["evening_talk"]



label start:
    # list_of_strings = ["sylvia_dialogs", "dad_dialogs", "schwester_dialogs"]
    # s = [sylvia_dialogs, dad_dialogs, schwester_dialogs]

    # name_character = "Todd"
    # key = name_character + "_dialogs" # "Todd_dialogs"
    call screen actions_screen ("Sylvia", sylvia_dialogs)

screen money_balance():
    modal True

    frame:
        vbox:
            text "Your account balance has been topped up"
            text "Balance:"
            text str(balance)
            textbutton "Close":
                action Hide("money_balance")

# in charge
# 1. Call the screen with character name and about topic
# 2. Get the branch for the topic automatically
# 2. Get the character name and the topic to speak
# 3. If there is already history chat with this character load it
# 4. Save the options for dialogs
# 5. Go through the dialogs if there is a next option change current_branch

history = {
    "Dad": {
        "event": "abacad"
    }
}

screen actions_screen(who, about=None):
    # get some specific branch by default like day time
    $ character_branch = answers[who]
    $ current_branch = get_initial_branch(character_branch, about)
    # $ current_branch = globals()[where][who]

    vbox:
        $ first_message = answers.get("message", False)
        if first_message:
                hbox:
                    text first_message
        for option in current_branch_path:
            # $ current_branch = current_branch["replies"][option]
            $ current_branch = move_branch_to_the_option(current_branch, option)
            $ is_image = current_branch.get("is_image")

            text current_branch["reply_message"] 
            if is_image:
                add current_branch["message"]
            else:
                text current_branch["message"] 

    $money_toped_up = top_up_money_if_required(current_branch)
    if money_toped_up: 
        use money_balance


    $ replies_present = current_branch.get("replies") 
    # $ req_chapter = None
    # $ if replies_present:
    # $   req_chapter = replies_present.get("required_chapter", -1) 
    if replies_present:
        vbox:
            for option, repl in current_branch["replies"].items():
                hbox: 
                    xpos 2.5
                    textbutton "[repl['reply_message']]":
                    # textbutton "1":
                        action Function(update_current_branch_path, option)