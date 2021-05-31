import random

def bad_service_chatbot():
    answers = ["We don't do that",
                "We will get back to you right away",
                "Your call is very important to us"]
    yield "Can I help you?"
    while True:
        yield random.choice(answers)

g2 = bad_service_chatbot()
print(next(g2))
print(g2.send('I want to complain'))
print(g2.send("No, really. I want to complain."))