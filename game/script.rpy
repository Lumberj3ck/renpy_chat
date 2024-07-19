init -1 python:
    # В будущем загружать диалоги из файла
    # import json
    # answers = json.load(open(r"C:\Users\Lumberjack\code\renpy\asd\game\d\dialogs.json"))
    # answers = json.load(open(r"../game/d/dialogs.json"))
    answers =  {
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
        "a": {"message": "I don't know what to say", "reply_message": "Okay, Bye"}, 
        "b": {"message": "You're borring", "reply_message": "Ok"},
        "c": {"message": "Oh, shoot", "reply_message": "shit fuck off"}
        }
    },
    }
    }

    current_branch_path = ""

    def move_branch_to_the_option(current_branch, option):
        current_branch = current_branch["replies"][option]
        return current_branch

    def update_current_branch_path(option):
        global current_branch_path
        current_branch_path += option


label start:
    call screen actions_screen

screen actions_screen():
    $ current_branch = answers 
    vbox:
        for option in current_branch_path:
            # $ current_branch = current_branch["replies"][option]
            $ current_branch = move_branch_to_the_option(current_branch, option)
            text current_branch["reply_message"] 
            text current_branch["message"] 

    $ replies_present = current_branch.get("replies") 
    if replies_present:
        vbox:
            for option, repl in current_branch["replies"].items():
                hbox: 
                    xpos 2.5
                    textbutton "[repl['reply_message']]":
                        action Function(update_current_branch_path, option)