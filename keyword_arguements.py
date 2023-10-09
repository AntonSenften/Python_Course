# keyword arguments = arguments prefixed with the names of parameters
#                                        order of the arguments doesn’t matter
#                                        helps with readability

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")       # sätter man parametern = argumentet så spelar ordning ingen roll.