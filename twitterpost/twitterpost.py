#twitter poster
#First import the required libraries
import twitter
import urllib2
import sqlite3
import time

userID = 791950937006800896 #not needed - for getting stuff

####GET BROWSER HISTORY
###SQL ATTEMPT
while True:
    console = sqlite3.connect("/Users/sjarvis5/Library/Application Support/Google/Chrome/Default/History")
    getTableInfo = console.cursor()

    getTableInfo.execute("SELECT urls.title FROM urls")
    rows = getTableInfo.fetchall()

    recent = []

    for row in rows:
        recent.append(row)

    getLast = str(recent[-1])
    lastTitle = getLast[3:-3]
    console.close()

    ##post to twitter
    file = open("twitterCredentials.txt")
    creds = file.read().split('\n') 

    #Create a new API wrapper, passing in my credentials one at a time
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    #Post status update and get the response from Twitter
    response = api.PostUpdate("I last viewed: " +lastTitle )

    #Print out response text (should be the status update if everything worked)
    print("Status updated to: " + response.text)
    time.sleep(3600)


''' Get stuff from twitter
#Hardcode a user ID into a variable (Stephen Fry)
user = 15439395

#Load in my keys and secrets from the credentials file into a list (array)
file = open("twitterCredentials.txt")
creds = file.read().split('\n')

#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#Get the most recent batch of status updates from the user
statuses = api.GetUserTimeline(user)

#Just print out the most recent one
print (statuses[0].text)
'''