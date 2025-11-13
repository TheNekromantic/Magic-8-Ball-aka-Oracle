import random
print("Welcome to my parlor, come tell me your name... \n")
player = input("Enter a name: ")
print("\nTake a seat " + player + " have a seat and ask your question. ")
print("\nBut be mindful, you can ask only one...\n")
def Oracle():
    question = input("Ask me a question: ")
    answers = ["Yes", "No", "Maybe", "Doesn't seem likely", "Seems very likely", "Ask again later"]
    future_told = random.choice(answers)
    print("\n" + future_told)
    input("\nPress enter to exit ")
Oracle()