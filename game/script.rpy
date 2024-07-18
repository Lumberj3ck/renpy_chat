# Пока на оформление я не обращаю внимание, его сделать несложно. 
# Единственное что нужно помнить - это сообщения отправленне и полученные должны выводится по-разному.

# Я не могу понять как лучше делать. Через словари или списки. Поэтому два варианта.



    # menu:
    #     "Option 1":
            # call screen actions_screen
        # "Option 2":
        #     call screen actions_screen_2



#Вариант 1. Через списки.
# Идея - один список выводим на экран, во втором все сообщения. 
# По нажатию кнопки, в первый список добавялем, из второго удаляем. То же самое с ответами на сообщения.
# Надо будет добавить переменные, чтобы функция понимала какой именно элемент списка добавлять или удалять. 

# Проблема текущего варианта, что сообщения и реплаи выводятся не друг за другом, а вначале все сообщения, потом все реплаи.
# Можно их все помещать в один список, а не в два разных и выводить вместе. 
# Но тогда вопрос как сделать чтобы они визально выводились по разному. 



# default messages_1 = []
# default messages_2 = [ "message 1", "message 2", "message 3", "message 4","" ]

# default reply_1 = []
# default reply_2 = [ "reply 1", "reply 2", "reply 3", "reply 4","" ]



# init -1 python:

#     def fun1():

#         messages_1.append(messages_2[0])
#         messages_2.pop(0)
#         messages_2.pop(0)

#         reply_1.append(reply_2[0])
#         reply_2.pop(0)
#         reply_2.pop(0)

#         return



# screen actions_screen():
    
#     vbox:


#         # for i in messages_1:
#         #     text "[i]"

#         # for i in reply_1:
#         #     text "[i]" 
#         # messages_1 = ["Hi, Dad"]
#         # reply_1 = ["Hi, son"]
#         for idx, elem in enumerate(messages_1):
#             text "[elem]" 
#             text "[reply_1[idx]]" 


#         # for idx, elem in enumerate(messages_1[:1]):
#         textbutton "[messages_2[0]]":
#             action Function(fun1)

#         textbutton "[messages_2[1]]":
#             action Function(fun1)




####################

# Вариант 2. Через словари.
# Идея примерно та же, что и выше. Проблема что вместо этой кнопки "Add" должен быть текст сообщения. 
# Т.е. первый элемент списка в словаре. А у меня не получается его вывести.

# Ну и когда начинаю добавлять переменные, чтобы происходил сдвиг на словарь со следующими сообщениями и реплаями, возникают проблемы.


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
        "message": "Good day, son",
        "reply_message": "Hi, day",
        "replies": {
        "a": {"message": "I don't know what to say", "reply_message": "Okay, Bye"}, 
        "b": {"message": "I don't know", "reply_message": "Ok"},
        "c": {"message": "fuck off", "reply_message": "Oh, shoot"}
        }
    },
    }
    }

    current_branch = "a"

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
    
    # def render_replies(branch):
    #     cb = ans
    #     for i branch:
    #         cv = cb[i]
        
    #     for i in cb["replies"]:
    #         print(cb["replies"][i][reply_message])


define e = Character("asfd")
label start:
    # call screen actions_screen
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
    $ curr = answers 
    vbox:

        for option in current_branch:
            $ curr = curr["replies"][option]
            text curr["message"] 
            text curr["reply_message"] 

    vbox:
        for repl in curr["replies"].values():
            hbox: 
                xpos 0.5
                text repl["message"]


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