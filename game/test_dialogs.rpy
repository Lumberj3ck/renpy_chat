init -2 python:
    answers =  {
        "Dad": {
            "start": {
                "message": "Hi son",
                "character_start": True,
                "replies":{
                "a": {
                    "message": "Hi man",
                    "reply_message": "Hi, dad",
                    "required_chapter": 2,
                    "replies": {
                    "a": {
                        "message": "I don't know what to say", 
                        "reply_message": "Okay, Bye",
                        "replies": {
                            "a": {"message": "You're not my son anymore, 🖕", "reply_message": "Fuck off"},
                            "b": {"message": "Love you too ❤️\nBye", "reply_message": "Love you"},
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
                    "c": {"message": "Oh, wow", "reply_message": "I want to go to the rock concert"}
                    }
                },
            }
            },
            "end":{
                "message": "Bye", 
                "replies":{
                    "a": {"reply_message": "Auf WiederHoren"},
                    "b": {"reply_message": "Okay, Bye"}
                }
            },
            "rock_concert":{
                "message": "When are you planning to go?",
                "character_start": True,
                # "reply_message": "Hi, dad, I love you!",
                "replies": {
                    "a":{
                        "message": "And it's mine",
                        "reply_message": "Such a lonely day",
                        "replies":{
                            "a":{
                                "message": "Okay",
                                "reply_message": "Not Okay"
                            }
                        }
                    },
                    "b":{
                        "message": "Okay",
                        "reply_message": "give me money",
                        "money_top_up": 100,
                        "replies":{
                            "a":{
                                "message": "Okay",
                                "reply_message": "I want more",
                                "money_top_up": 999,
                            },
                            "b":{
                                "reply_message": "Thank you", 
                            }
                        }
                    },

            }
        }
        },
    }

    history = {
        "Dad":{
            # "start": "ba"
        }
    }
