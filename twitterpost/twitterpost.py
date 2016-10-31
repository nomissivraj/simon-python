#twitter poster
#First import the required libraries
import twitter
import urllib2
import sqlite3
import time

userID = 791950937006800896 #not needed for twitterpost - is for getting stuff from my account, if i wanted to

####GET BROWSER HISTORY
###SQL ATTEMPT

#put in while loop so that this can be repeated at intervals
while True:
    #locate and enter History file
    console = sqlite3.connect("/Users/sjarvis5/Library/Application Support/Google/Chrome/Default/History")
    #Start search in history database
    getTableInfo = console.cursor()
    #USE SQL query to search for titles within the urls visited table
    getTableInfo.execute("SELECT urls.title FROM urls")
    #Get all titles from all urls - store in rows variable
    rows = getTableInfo.fetchall()

    #set up list to store all titles for easy access
    allHistory = []

    #make a 'current' variable to iterate through all rows in database and append them to history list
    for row in rows:
        allHistory.append(row)
    #get the last (most recent page viewed) item from list as a string rather than list item
    getLast = str(allHistory[-1])
    #trim the (u' ',) ugliness from said string
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

    #set program to sleep for 1 hour in seconds - interval to repeat at
    time.sleep(3600)


''' Example to Get stuff from twitter
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
