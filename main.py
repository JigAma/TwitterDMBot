from twitter import * #Import twitter library
from time import sleep 
#Twitter OAuth
t = Twitter (
auth = OAuth(
    consumer_key='YOUR CONSUMER KEY',
    consumer_secret='YOUR CONSUMER SECRET',
    token='YOUR TOKEN',
    token_secret='YOUR TOKEN SECRET'))



print("Successfully collected last Direct Message")

LastTweet="default"

while True: #Infinite loop
	DM = t.direct_messages(count=200) #Recover last 200 DM received
	
	for tweet in DM:
		print(tweet["text"]) #print last DM in console
		if tweet != LastTweet:
			if  len(tweet["text"]<140: #check if the tweet if the lenght of the DM is inferior to 140 characters
				t.statuses.update(status=tweet["text"]) #tweet the last DM
				LastTweet = tweet
	print('Successfully tweeted:'+tweet["text"])
	sleep(randint(1800,3600)) # wait between 1800 to 3600s
	



	
