from twitter import * #Import twitter library

#Twitter OAuth
t = Twitter (
auth = OAuth(
    consumer_key='YOUR CONSUMER KEY',
    consumer_secret='YOUR CONSUMER SECRET',
    token='YOUR TOKEN',
    token_secret='YOUR TOKEN SECRET'))



print("Successfully collected last Direct Message")

LastTweet="default"

while True:
	DM = t.direct_messages(count=200)
	
	for tweet in DM:
		print(tweet["text"])
		if tweet != LastTweet:
			if  len(tweet["text"]<140:
				t.statuses.update(status=tweet["text"])
				LastTweet = tweet
	print('Successfully tweeted:'+tweet["text"])
	sleep(randint(1800,3600))
	



	
