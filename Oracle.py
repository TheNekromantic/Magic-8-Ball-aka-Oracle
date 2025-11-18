import random
print("Welcome stranger tell me your name.\n")
name = input("Enter your name ")
print("Well then " + name +" what question can I answer for you?\n")
def oracle():
    while True:
        question = input("Ask me your question. (Enter 'q' to quit) ")
        if question.lower() == "q":
            print("\nGoodbye for now " + name + "...")
            break
        else:
            answers = ["Yes", "No", "Chances are good", "Doesn't seem likely", "Maybe", "I am tired now, ask again later"]
            response = random.choice(answers)
            print("\n"+ response)
oracle()