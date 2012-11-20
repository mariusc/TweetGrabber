# TweetGrabber

These scripts allow you to get the latest tweets from a twitter account. 
To do this, in python shell, run tweets.getStatuses("_user", n), where _user is the accout name from which you want to get the tweets and n is the number of pages of tweets you want to download. A page contains 15 tweets, so in the end, you will get 15*n tweets, one per line, in the "_user_tweets" file, where _user is the account which is scanned.

Please note that the twitter API is subject to changes, which may result in these functions not working properly. Also, the Twitter API is limited to 150 requests per hour