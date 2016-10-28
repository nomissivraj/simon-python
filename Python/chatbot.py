#Chat Bot
'''features:

'''

#Import libraries 
import random
import wikipedia
import time
import webbrowser

####LOAD STUFF
#Access stopwords.txt file and read it as stopDoc variable
with open("stopwords.txt", "r") as stopDoc:
    #Get all words from stopDoc, stripping out the new lines? store in stop_words variable... now is a list
    stop_words = stopDoc.read().split("\n")
    stop_words.append("name")
    stopDoc.close()

with open("cuteness.txt", "r") as cutestuff:
    cuteness = cutestuff.read().split("\n")
    cutestuff.close()

####ASSET CREATION - LISTS FOR ANSWERS/STORING
#create list of possible greetings or responses
greetings = ["hello", "hey", "sup", "greetings"]
#create list of possible questions to follow greetings or responses
questions = ["how are you doing?", "having a good day?", "how's it going?", "how're you feeling?"]
#every loop put a new random choice from greetings list into random_greeting variable to be used later
pos_responses = ["good", "great", "fantastic", "brilliant", "ok", "amazing", "yes", "yep", "yeah"]
neg_responses = ["bad", "shit", "awful", "abysmal", "sick", "unwell", "bored", "poop", "nope", "no", "nah"]
pos_answer = ["that's good", "i'm glad", "I'm glad to hear it", "awesome! :D"]
neg_answer = ["i'm sorry to hear that", "oh no :(", "oh no :( hope you feel better soon", "HAHAHAHAA", "that's awful"]
random_cuteness = random.choice(cuteness)#gets choice from list created in load stuff section - cuteness.txt
random_pos_answer = random.choice(pos_answer)
random_neg_answer = random.choice(neg_answer)




####DEFINE VARIABLES 
random_greeting = random.choice(greetings)
random_question = random.choice(questions)
bot = "STUPIDBOT: "
global flip
flip = False
global user_feels
global get_last

####MAKE FUNCTIONS TO HANDLE CONVERSATION ELEMENTS
def processInput(input, output, useName):
    response = input.split(" ")
    #loop through user response words
    for word in response:
        #Check if words are not in stop words
        if word.lower() not in stop_words:
            #use words, not in stop_words and continue
            if useName: print(bot + output + " " + word)
            else: print(bot + output +" ")
        time.sleep(0.5)

def posOrNeg(checkInput, posList, negList):
    while True:
        time.sleep(0.5)
        response = checkInput.split(" ")
        for word in response:
            global flip
            user_feels = "nothing"
            if word == "not": flip = True
            elif word.lower() in posList: user_feels = "positive"
            elif word.lower() in negList: user_feels = "negative"
            if flip and user_feels == "positive":
                print(bot +random_neg_answer +" . hopefully this will cheer you up ")
                webbrowser.open(random_cuteness, new=1)
                return
            if not flip and user_feels == "positive":
                print(bot +random_pos_answer +" ")
                return
            if flip and user_feels == "negative":
                print(bot +random_pos_answer +" ")
                return
            if not flip and user_feels == "negative":
                print(bot +random_neg_answer +" . hopefully this will cheer you up ")
                webbrowser.open(random_cuteness, new=1 )
                return
            get_last = checkInput.split(' ', -1)[-1]
            if get_last not in posList and get_last not in negList:
                print('sorry I dont understand, please try again')
                checkInput = raw_input(" ")
            time.sleep(1)
            
def checkYesNo(checkInput, pos, neg):
    response = checkInput.split(" ")
    for word in response:
        if word.lower() in pos:
            cont_subject = wikipedia.summary(userSearch, sentences=4)
            print(bot + "here's more about that")
            print(cont_subject)
        elif word.lower() in neg:
            print('whoops, try something else')

####BEGIN PROGRAM/CONVERSATION

#get user first input and respond
print(bot +"Hello I am STUPIDBOT, what is your name? ")
response = raw_input(" ")
processInput(response, random_greeting, True)



#second step of conversation

print(bot + random_question)
greeting_response = raw_input(" ")
posOrNeg(greeting_response, pos_responses, neg_responses)


# ask why then work in further respons to cheer up if negative, tell joke, show picture, offer figurative hug?
#sort out if not_something combination -- = + etc

#tell me about yourself, ask questions about appearance, then eventually hobbies - set responses + wikipedia?

#do a word game here?

#last step of conversation - endless wikipedia nonsense
while True:
    response = raw_input("What would you like to talk about now? ")
    response_last = response.split(' ', -1)[-1]
    parse = None
    userSearch = wikipedia.search(response_last, parse)
    
    #Below fixes issue with ambiguous query's
    #Might get occasional warning... still works. Please ignor warning
    try:
        userSubject = wikipedia.summary(userSearch[1], sentences=1)
    except:
        parse = "html.parser"
        userSubject = wikipedia.summary(userSearch[0], sentences=1)
    
    print("do you mean? : ")
    print(bot + userSubject)
    response = raw_input(" ")
    checkYesNo(response, pos_responses, neg_responses)
    
    #response = raw_input("Would you like to talk about something else? ")
    #if response in (neg_responses):  break









