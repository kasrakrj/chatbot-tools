from chatterbot import ChatBot

chatbot = ChatBot("First Bot")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
inp = ""
while(inp != "exit"):
    inp =  input("input: ")
    response = chatbot.get_response(inp)
    print(response)

print(response)

