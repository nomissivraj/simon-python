#Chat Bot

#Import library for random selections 
import random

bot = "shitBot: "

#Access stopwords.txt file and read it as stopDoc variable
with open("stopwords.txt", "r") as stopDoc:
    #Get all words from stopDoc, stripping out the new lines? store in stop_words variable... now is a list
    stop_words = stopDoc.read().split("\n")
    stop_words.append("name")
    stopDoc.close()
    
#create list of possible greetings or responses
greetings = ["hello", "hey", "sup", "greetings"]
#create list of possible questions to follow greetings or responses
questions = ["how are you doing?", "having a good day?", "how's it going?", "how're you feeling?"]
#every loop put a new random choice from greetings list into random_greeting variable to be used later
random_greeting = random.choice(greetings)
random_question = random.choice(questions)

#get user first input and respond
response = raw_input("What is your name? ")

def processInput(input, output, useName):
    response = input.split(" ")
    #loop through user response words
    for word in response:
        #Check if words are not in stop words
        if word.lower() not in stop_words:
            #use words, not in stop_words and continue
            if useName: print(bot + output + " " + word)
            else: print(bot + output +" ")


processInput(response, random_greeting, True)




#second step of conversation

pos_responses = ["good", "great", "fantastic", "brilliant", "ok", "amazing",]
neg_responses = ["bad", "shit", "awful", "abysmal", "sick", "unwell", "bored", "poop"]
pos_answer = ["that's good", "i'm glad", "I'm glad to hear it", "awesome! :D"]
neg_answer = ["i'm sorry to hear that", "oh no :(", "oh no :( hope you feel better soon", "HAHAHAHAA", "that's awful"]
random_pos_answer = random.choice(pos_answer)
random_neg_answer = random.choice(neg_answer)

def posOrNeg(checkInput, posList, negList):
    response = checkInput.split(" ")
    for word in response:
        if word.lower() in posList:
            print(bot +random_pos_answer +" ")
        if word.lower() in negList:
            print(bot +random_neg_answer +" ")
        elif word.lower() not in posList and negList:
            print(bot +"i don't understand your response, please try again")
            
greeting_response = raw_input(random_question +" ")
posOrNeg(greeting_response, pos_responses, neg_responses)

