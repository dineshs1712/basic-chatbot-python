import random

import json



class Bot:

    def __init__(self, data_dict):

        self.chatbot_data = data_dict



    def bot_engine(self, user_input):

        user_input = user_input.lower()



        if user_input in self.chatbot_data:

            bot_output = random.choice(self.chatbot_data[user_input])

            print("BOT:", bot_output)

        else:

            print("BOT: Sorry, I didn't understand that.")



def read_setup(file_name):

    with open(file_name, "r") as file:

        return json.load(file)



def main():

    data = read_setup("datas.json")

    user = Bot(data)



    while True:

        user_input = input("YOU: ")



        if user_input.lower() == "exit":

            print("BOT: Bye!")

            break



        user.bot_engine(user_input)



if __name__ == '__main__':

    main()
