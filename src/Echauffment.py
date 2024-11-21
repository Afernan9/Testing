import datetime

class Echauffment:
    def greeting():
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning"
        elif hour < 18:
            return "Good afternoon"

    def goodbye():
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Have a nice day"
        elif hour < 18:
            return "Have a good evening"

    def process_input(input):
        output = input[::-1] 
        if output == input:
            return "It's a palindrome"
        else:
            return output
        
def main():
    print(Echauffment.greeting())
    while True:
        #capture input from user
        word = input("I'm listening (type 'quit' to exit): ")
        print(Echauffment.process_input(word))
        
        if word == "quit":
            print(Echauffment.goodbye())
            break

if __name__ == "__main__":
    main()