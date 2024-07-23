init python:
    answers =  {
        "Dad": {
            "start": {
                "message": "Hi son",
                "a": {
                    "message": "Hi man",
                    "reply_message": "Hi, dad",
                    "required_chapter": 2,
                    "replies": {
                    "a": {
                        "message": "I don't know what to say", 
                        "reply_message": "Okay, Bye",
                        "replies": {
                            "a": {"message": "You're not my son anymore, 🖕", "reply_message": "Fuck off", "next": "end"},
                            "b": {"message": "Love you too ❤️\nBye", "reply_message": "Love you", "next": "end"},
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
                    "c": {"message": "Oh, wow", "reply_message": "I want to go to the rock concert", "next": "rock_concert"}
                    }
                },
            },
            "end":{
                "message": "Bye", 
                "reply_message": "Bye, father",
            },
            "rock_concert":{
                "message": "When are you planning to go?",
                # "reply_message": "Hi, dad, I love you!",
                "replies": {
                "a": {
                    "message": "Ah I don't have yet", 
                    "reply_message": "I want to go tommorow, But, I need some money for entry", 
                    "replies":{
                        "a": {"message": "That's okay", "reply_message": "Okay", "next": "end"},
                        "b": {"message": "But you owe me money!", "reply_message": "No I don't ", "next": "end"},
                    }
                },
                "b": {"message": "I wanna go with you", "reply_message": "I want to go today", "next": "end"}
            }
        }
    },
}

history = {
    "Dad": [("start", "abaabca"), ("end", "aacab"), ("rock_concert", "baaca")]
    "Sylvia": [("start", "abaabca"), ("end", "aacab"), ("rock_concert", "baaca")]
}


