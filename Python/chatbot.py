#Chat Bot
'''features:
    *simple interaction getting input and giving it back
    *stores certain user input for later use - see goodbye message when choosing not to continue talking after wikipedia bit
    *random questions from list so isn't same each time
    *using functions to trim down on repeated code
    *even passing a function into a function incase i wanted to re-use parent function but do something different if conditionds within are met
    *evaluates positive or negative responses and responds appropriately - including not bad/not good complications
    *Plays a simple game with user - including checkign if user wants to play or play again etc
    *If input is invalid resets to a previous step using booleans - was a bit messy but works... mostly
    *on wiki ambiguous search errors - switches to another index - for some words this will throw up an html.parse warning... but still works.
    *program terminates after final line of dialogue
'''

#Import libraries 
import random, wikipedia, time, webbrowser, sys

####LOAD STUFF
#Access stopwords.txt file and read it as stopDoc variable
with open("stopwords.txt", "r") as stopDoc:
    #Get all words from stopDoc, seperated by new lines and append to stop_words list
    stop_words = stopDoc.read().split("\n")
    stop_words.append("name")
    stopDoc.close()

#Access external resource image links
with open("cuteness.txt", "r") as cutestuff:
    cuteness = cutestuff.read().split("\n")
    cutestuff.close()

####ASSET CREATION - LISTS FOR ANSWERS/STORING
#create list of possible greetings or responses
greetings = ["hello", "hey", "sup", "greetings"]
#create list of possible questions to follow greetings or responses
questions = ["how are you doing?", "having a good day?", "how's it going?", "how're you feeling?"]
#list of games
games = ["rock paper scissors", " other game"]
gameString = ','.join(games)
#every loop put a new random choice from greetings list into random_greeting variable to be used later
generic_responses = ["Ah yes, I too enjoy that", "I've always loved that", "Oh :/ i'm not really a fan of that", "eurgh boring"]
pos_responses = ["good", "great", "fantastic", "brilliant", "ok", "amazing", "yes", "yep", "yeah", "well"]
neg_responses = ["bad", "shit", "awful", "abysmal", "sick", "unwell", "bored", "poop", "nope", "no", "nah"]
pos_answer = ["that's good", "i'm glad", "I'm glad to hear it", "awesome! :D"]
neg_answer = ["i'm sorry to hear that", "oh no :(", "oh no :( hope you feel better soon", "HAHAHAHAA", "that's awful"]
rps_answers = ["rock", "paper", "scissors"]
random_cuteness = random.choice(cuteness)#gets choice from list created in load stuff section - cuteness.txt
random_pos_answer = random.choice(pos_answer)
random_neg_answer = random.choice(neg_answer)
random_response = random.choice(generic_responses)

####DEFINE VARIABLES 
random_greeting = random.choice(greetings)
random_question = random.choice(questions)
bot = "STUPIDBOT: "
global flip
flip = False
global user_feels
global get_last
global response
global greeting_response
global parse
parse = None
global wiki_index
wiki_index = 1
global rps_tie
rps_tie = False
global skip_game
skip_game = False
global neitherYesNo
user_hobbies = []


####MAKE FUNCTIONS TO HANDLE CONVERSATION ELEMENTS
def botLine(string, greeting):
    global response, greeting_response
    print(bot + string)
    response = raw_input(" ")
    
    if greeting == True:
        greeting_response = response
    

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
            
def moreWiki():
    cont_subject = wikipedia.summary(userSearch, sentences=4)
    print(bot + "here's more about that")
    print(cont_subject)

def contOrStop(checkInput, pos, neg):
    response = checkInput.split(" ")
    for word in response:
        if word.lower() in pos:
            return
        elif word.lower() in neg:
            print('Ok, I enjoyed speaking to you. Goodbye and enjoy your ' +random_hobby + ' :)')
            time.sleep(3)
            quit()

#Check respons to if subject is correct - could be used for something else
def checkYesNo(checkInput, pos, neg, chosenFunction, game):
    global wiki_index, skip_game, neitherYesNo
    response = checkInput.split(" ")
    for word in response:
        if word.lower() in pos:
            chosenFunction()
            return
        elif word.lower() in neg:
            #if this is being called within a game
            if game == True:
                skip_game = True
            print("Ok then")
        elif word.lower() not in neg and word.lower() not in pos:
            print("invalid response, please try again")
            neitherYesNo = True

#Function that does nothing
def nofunction():
    return

###Games ---------

##Rock Paper Scissors
def rpsCompare(userChoice, bot_choice):
    global rps_tie
    print(bot + bot_choice)
    time.sleep(1)
    print("you chose " +userChoice)
    #For invalid input
    if userChoice.lower() not in rps_answers:
        print("Sorry your choice was invalid")
        rps_tie = True
    #For a tied result
    if userChoice == bot_choice:
        print(bot +"It's a tie, please try again")
        rps_tie = True
        return
    
    elif userChoice.lower() == "rock":
        if bot_choice == "scissors":
            print(bot +"You won! well done :)")
            rps_tie = False
            neitherYesNo = False
            return
        else:
            print(bot +"Sorry :( you lost!")
            rps_tie = False
            neitherYesNo = False
            return

    elif userChoice.lower() == "paper":
        if bot_choice == "rock":
            print(bot +"You won! well done :)")
            rps_tie = False
            neitherYesNo = False
            return
        else:
            print(bot +"Sorry :( you lost!")
            rps_tie = False
            neitherYesNo = False
            return

    elif userChoice.lower() == "scissors":
        if bot_choice == "rock":
            print(bot +"Sorry :( you lost!!")
            rps_tie = False
            neitherYesNo = False
            return
        else:
            print(bot +"You won! well done :)")
            rps_tie = False
            neitherYesNo = False
            return

    

def rockPaperScissors(userChoice):
    
    bot_choice = random.randint(1,3)
    if bot_choice == 1: bot_choice = "rock"
    elif bot_choice == 2: bot_choice = "paper"
    else: bot_choice = "scissors"
    if rps_tie == False:
        botLine("Good choice! :) I love Rock Paper Scissors. Ready when you are!", False)
        userChoice = response
    rpsCompare(userChoice, bot_choice)

def isTie():
    while rps_tie == True:
        botLine("Choose again 3... 2... 1...", False)
        userChoice = response
        if rps_tie == True:
            rockPaperScissors(userChoice)
        if rps_tie == False:
            return

##Handle game choice
def otherGame():
    while True:
        print("Sorry my creator got lazy and or ran out of time and didn't make any other games")

def chooseGame(userChoice):
    userChoiceWords = userChoice.split(" ")
    for word in userChoiceWords:
        if word.lower() in games[0]:
            rockPaperScissors(userChoice)
        elif word.lower() in games[1]:
            otherGame()
        elif word.lower() not in games:
            print("invalid response, please try again")
            neitherYesNo = True


#----------------------------------------------------------------------------
####BEGIN PROGRAM/CHATBOT CONVERSATION
#Ask users name and respond greeting them
botLine("Hello I am STUPIDBOT, what is your name? ", False)
processInput(response, random_greeting, True)

#Ask user a random question i.e how they are
botLine(random_question, True)
posOrNeg(greeting_response, pos_responses, neg_responses)

#Ask about Hobbies
botLine("do you have any hobbies? what are they ? ", False)
user_hobbies.append(response)
random_hobby = random.choice(user_hobbies)
processInput(response, random_response, False)
print(bot + "I love playing games...")
time.sleep(1)

#Play game with user
while skip_game == False:
    neitherYesNo = False
    botLine("Would you Like to play a game?", False)
    checkYesNo(response, pos_responses, neg_responses, nofunction, True)
    if skip_game == True: break
    if neitherYesNo == False:
        botLine("What would you like to play? I know: " +gameString, False)
        chooseGame(response)
        isTie()
        botLine("Would you like to play another game?", False)
        checkYesNo(response, pos_responses, neg_responses, nofunction, True)
        if skip_game == True: break 
        botLine("What would you like to play? remember I know: " +gameString, False)
        chooseGame(response)

#last step of conversation - endless wikipedia nonsense
while True:
    #Ask user for subject
    botLine("What would you like to talk about now? ", False)
    #get Last word from user input
    response_last = response.split(' ', -1)[-1]

        
    #Set parse to none by default -as only want to use html.parser for certain queries
    userSearch = wikipedia.search(response_last, parse)
        
    #Below fixes issue with ambiguous query's
    #Might get occasional warning... still works. Please ignore warning
        
    try:
        userSubject = wikipedia.summary(userSearch[wiki_index], sentences=1)
    except:
        parse = "html.parser"
        userSubject = wikipedia.summary(userSearch[0], sentences=1)

    botLine("do you mean? : \n" + userSubject, False)
    checkYesNo(response, pos_responses, neg_responses, moreWiki, False)
        
    botLine("Would you like to talk about anything else ?", False)
    contOrStop(response, pos_responses, neg_responses)









