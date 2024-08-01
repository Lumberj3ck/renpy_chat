init -1 python:
    balance = 0
    # required rn!!
    global_events = {
        "Dad":"start",
        "Sister":"start"
    }

    # Для того чтобы удостовериться что пополнялось один раз за одну ветку
    characters_balance_top_up_branches = {
    }
    # last_balance_top_up_branch = ""

    def print_to_file(*args, mode="a"):
        f = open(r"C:\Users\Lumberjack\code\renpy\asd\test.txt", mode)
        for data in args:
            f.write(str(data))
            f.write("\n")
        f.close()

    def update_character_chat_history(character_chat_history, topic, option):
        character_chat_history[topic].append(option)

    def top_up_money_if_required(current_branch, character_chat_history, topic, who):
        global balance, last_balance_top_up_branch, current_branch_path

        money_amount = current_branch.get("money_top_up", 0)

        unique_stamp = "".join(character_chat_history[global_events[who]])

        if who not in characters_balance_top_up_branches:
            characters_balance_top_up_branches[who] = ""

        last_balance_top_up_branch = characters_balance_top_up_branches[who]
        if money_amount > 0 and last_balance_top_up_branch != unique_stamp:
            # print_to_file("last", last_balance_top_up_branch, "chat-history", character_chat_history[topic], mode="w")
            balance += money_amount
            characters_balance_top_up_branches[who] = unique_stamp
            return True
        return False

    def get_initial_branch(who, character_branch, character_chat_history):
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
                branch = character_branch[global_event][last_option]
                return branch, global_event


        return {}, ""


label start:

    show screen contacts
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

screen actions_screen(who):
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
    # now is not restricted with chat history so the branch could appear multiple times
    default branch_and_topic = get_initial_branch(who, character_branch, character_chat_history)
    # suppose to add the starting branch to history
    default current_branch = branch_and_topic[0]
    default topic = branch_and_topic[1]


    vbox:
        for event, options in character_chat_history.items():
            for option in options:
                hbox:
                    # if begining of the event and the event node is required to render
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


    $ money_toped_up = top_up_money_if_required(current_branch, character_chat_history, topic, who)
    if money_toped_up: 
        use money_balance

    # $ print_to_file(current_branch)
    if "options" in current_branch:
        # add "asdf.png"
        vbox:
            for option in current_branch["options"]:
                hbox:
                    textbutton character_branch[topic][option]['text']:
                        xpos 1.5
                        action (Function(update_character_chat_history, character_chat_history, topic, option), SetScreenVariable("current_branch", character_branch[topic][option])) 
