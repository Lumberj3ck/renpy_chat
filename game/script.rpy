init -1 python:
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
                "a": {"message": "No, 👉", "reply_message": "Fuck off"}
            }
        }, 
        "b": {"message": "I don't know", "reply_message": "Ok"},
        "c": {"message": "fuck off", "reply_message": "Oh, shoot"}
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

    def render_the_branch(branch):
        curr = answers 
        for option in branch:
            curr = answers["replies"][option]
            print(curr["message"])
            print(curr["reply_message"])
            # text curr["reply_message"] pos (1.0, 0)
        return cb
    
    def move_branch(option, curr):
        curr = curr["replies"][option]
        return curr

    def update_current_branch_path(option):
        global current_branch_path
        current_branch_path += option


label start:
    menu:
        "Option 1":
            call screen actions_screen

screen actions_screen():
    # python:
    #     # a = {"asdf": 'asadf'}
    #     # say("asdf", a["asdf"])
    #     curr = answers 
    #     for option in current_branch:
    #         curr = curr["replies"][option]
    #         renpy.show("image tag", what=Text(curr["message"]))
    $ current_branch = answers 
    vbox:
        for option in current_branch_path:
            $ current_branch = current_branch["replies"][option]
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


# default dict1 = {"m1": ["Hello", "Hi"],}

# default dict2 = {"m2": ["How are you?", "Fine"],}


# init -1 python:
#     def fun2():
#         dict1.update(dict2)
#         return


# screen actions_screen_2():

#     vbox:

#         for message in dict1.values():
#             text message[0] pos (1.0, 0)
#             text message[1] pos (0.0, 0)

#         textbutton "[dict2['m2'][0]]":
#             action Function(fun2)