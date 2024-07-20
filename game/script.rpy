init -1 python:
    # В будущем загружать диалоги из файла
    # import json
    # answers = json.load(open(r"C:\Users\Lumberjack\code\renpy\asd\game\d\dialogs.json"))
    # answers = json.load(open(r"../game/d/dialogs.json"))
    answers =  {
    "message": "Hi son",
    "replies":
    {
    "a": {
        "message": "Hi man",
        "reply_message": "Hi, dad",
        "replies": {
        "a": {
            "message": "I don't know what to say", 
            "reply_message": "Okay, Bye",
            "replies": {
                "a": {"message": "You're not my son anymore, 🖕", "reply_message": "Fuck off"},
                "b": {"message": "Love you too ❤️\nBye", "reply_message": "Love you"}
            }
        }, 
        "b": {"message": "You're borring", "reply_message": "Ok"},
        "c": {"message": "Oh, shoot", "reply_message": "shit fuck off"}
        }
    },
    "b": {
        "message": "I love you too, son",
        "reply_message": "Hi, dad, I love you!",
        "replies": {
        "a": {"message": "rose.png", "reply_message": "Okay, Bye", "is_image": True}, 
        "b": {"message": "Okay, I sent it", "reply_message": "I need some money, please", "money_top_up": 10},
        "c": {"message": "Oh, shoot", "reply_message": "shit fuck off"}
        }
    },
    }
    }

    balance = 0
    current_branch_path = ""
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


label start:
    call screen actions_screen

screen money_balance():
    modal True

    frame:
        vbox:
            text "Your account balance has been topped up"
            text "Balance:"
            text str(balance)
            textbutton "Close":
                action Hide("money_balance")

screen actions_screen():
    $ current_branch = answers 

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
    if replies_present:
        vbox:
            for option, repl in current_branch["replies"].items():
                hbox: 
                    xpos 2.5
                    textbutton "[repl['reply_message']]":
                        action Function(update_current_branch_path, option)