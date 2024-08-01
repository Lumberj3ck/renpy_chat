init -1 python:
    balance = 0
    global_events = {
        "Dad":"start",
        "Sister":"start"
    }
    # current_branch = {}
    # topic = ""

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
        character_chat_history[topic].append(option)

    def top_up_money_if_required(current_branch, character_chat_history, topic):
        global balance, last_balance_top_up_branch, current_branch_path

        money_amount = current_branch.get("money_top_up", 0)

        if money_amount > 0 and last_balance_top_up_branch != character_chat_history[topic]:
            balance += money_amount
            last_balance_top_up_branch = character_chat_history[topic]
            return True
        return False

    def print_to_file(data):
        f = open(r"C:\Users\Lumberjack\code\renpy\asd\test.txt", "a")
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
    def get_initial_branch(who, character_branch, character_chat_history):
        # Check if about is provided and not finished
        # if about in character_branch:
        #     # don't need to navigate to branch cause the dict is now is flat
        #     branch = character_branch[about]
        #     return branch, about

        # Check if global_event is available and not finished
        global_event = global_events.get(who, "")

        if global_event not in character_chat_history:
            branch = character_branch[global_event]
            # character_chat_history['current_event'] = global_event
            character_chat_history[global_event] = [global_event]
            return branch, global_event

        elif global_event == character_chat_history[global_event][-1]:
            branch = character_branch[global_event]
            return branch, global_event

        elif global_event in character_chat_history:
            last_option = character_chat_history[global_event][-1]
            if "options" in character_branch[global_event][last_option]:
                print_to_file(last_option)
                branch = character_branch[global_event][last_option]
                return branch, global_event


        return {}, ""


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
        textbutton "Dad" action Show ("actions_screen",who="Dad")
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
# about is prioritised, global_event is choosed after about 
# history = {
#     "Dad": {
            # "messages": ["a1", "a2"],
            # "current_event" "str"
# }
# answers = {
#     "Dad" : {
#         "start":{
#             "response": "Hey! 1519 Lincoln Blvd, it's an Asian restaurant called \"Ifuku\" 🍜",
#             "character_start": True,
#             "options": ["a1", "a2"],
#             "a1": {
#                 "text": "Can't wait for tonight",
#                 "response": "Me too 🥰",
#                 "money_top_up": 999,
#                 "options": ["a2"]
#             },
#             "a2": {
#                 "text": "Can't wait for tonight",
#                 "response": "Me too 🥰",
#                 "money_top_up": 999,
#                 "options": ["a2"]
#             },
#         }
#     }
# }

screen actions_screen(who, about=None):
    use money_balance 
    modal True

    vbox:
        textbutton "close" action Hide ("actions_screen")


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
    # now is not restricted with chat history so the branch could appear multiple times
    default branch_and_topic = get_initial_branch(who, character_branch, character_chat_history)
    # suppose to add the starting branch to history
    default current_branch = branch_and_topic[0]
    default topic = branch_and_topic[1]
    # setup this variable to add a global event to history
    # default current_topic = topic

    # a = {
    #     "start": ["start" , "a1", "a2"]
    # } 


    vbox:
        for event, options in character_chat_history.items():
            for option in options:
                hbox:
                    if event == option:
                        $ render_branch = character_branch[option]
                    else:
                        $ render_branch = character_branch[event][option]

                    $ character_start = render_branch.get("character_start", False)
                    if character_start:
                        hbox:
                            text render_branch["response"]

                    $ is_image = render_branch.get("is_image")

                    if "text" in render_branch:
                        text render_branch["text"] 
                    if "response" in render_branch and not character_start:
                        if is_image:
                            add render_branch["response"]
                        else:
                            text render_branch["response"] 

        # Если диалог начинает персонаж то мы добавим вот это после загрузки чата
        $ character_start = current_branch.get("character_start", False)
        if character_start and global_events.get(who, None) != character_chat_history[topic][-1]:
                hbox:
                    text current_branch["response"]

    $ money_toped_up = top_up_money_if_required(current_branch, character_chat_history, topic)
    if money_toped_up: 
        use money_balance

    $ print_to_file(current_branch)
    if "options" in current_branch:
        # add "asdf.png"
        vbox:
            for option in current_branch["options"]:
                hbox:
                    textbutton character_branch[topic][option]['text']:
                        xpos 1.5
                        action (Function(update_character_chat_history, character_chat_history, topic, option), SetScreenVariable("current_branch", character_branch[topic][option])) 
