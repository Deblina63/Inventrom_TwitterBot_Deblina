from myKeys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as tweep
import random

class My_bot_deblina:



    def like_tweet_of_boltiot(self,api,boltuser,user) :
        """ Function to extract the most recent tweet of the user @boltiot, obtain it's unique id and like the tweet. If the
        tweet is already liked, then an error message is displayed on the console. """

        #  to find out the most recent tweet by the user. Value of count indicates the number of tweets to be extracted.
        tweet = api.user_timeline(boltuser, count=1)

        # obtaining unique tweet id
        tweet_id = tweet[0].id
        try:
            #  if the tweet is not already liked, then it is liked
            tweet_liked=api.create_favorite(tweet_id)
            api.update_status("Tweet #{} : Liked tweet by @boltiot user!".format(random.randint(0, 1000)))

        except tweep.TweepError as e :
            # if the tweet is already liked exception is displayed on the console
            print("Error: {}".format(e))

    def search_tweet_having_hashtag(self,api, search_item):
        """ Funtion to search the most recent tweet from all the tweets on twitter containing the expression '#IOT'
        and like the tweet. If the tweet is already liked, then an error message is displayed on the console."""

        # The Cursor method is used to crawl through the search results for tweets having the required expression
        searched_tweet = [status for status in tweep.Cursor(api.search, q=search_item).items(1)]

        # Obtaining the unique tweet id
        tweet_id = searched_tweet[0].id

        try:
            # once the expression is found in the tweet, the tweet is liked if not already liked.
            tweet_liked = api.create_favorite(tweet_id)
            api.update_status("Tweet #{} : Liked tweet containing '#IOT'!".format(random.randint(0, 10000)))

        except tweep.TweepError as e:
            # if the tweet is already liked then an error message is displayed on the console
            print("Error: {}".format(e))

    def set_user_authorization(self):
        """ Function to set the authorization tokens for the bot to perform the required functions"""

        # Setting the authorization tokens for twitter using tweepy from the already
        # included file containing keys of the TwitterBot
        user_auth = tweep.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        user_auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweep.API(user_auth)
        return api

    def getFollowers(self, username):
        """ Function to obtain the followers of the user and display them in the console"""

        # Extracting each follower of the user using the Cursor, converting it into string and
        # displaying it on the console
        print("List of followers: ")
        for userObj in tweep.Cursor(api.followers, screen_name=username).items(200):
            name_of_follower = str(userObj.screen_name)
            print(name_of_follower + '\n')

    def getFollowingAccounts(self, username):
        """ Function to obtain the user names followed by the user and display them in the console"""

        # Extracting each twitter handle followed by the user using the Cursor, converting it into string and
        # displaying it on the console
        print("List of following accounts: ")
        for userObj in tweep.Cursor(api.friends, screen_name=username).items(200):
            name_of_following_account = str(userObj.screen_name)
            print(name_of_following_account + '\n')


""" Creating object to access the different methods. If the processes are successful, different tweets are posted by 
the bot to imply the successful completion of the task"""
# creating object of the class to access different functions and variables
ob = My_bot_deblina()

# setting up authorization with twitter via tweepy
api = ob.set_user_authorization()
user = api.me()

#  if the twitter bot account is successfully connected
print("Connection established with {}".format(user.screen_name))
#  finding the number of followers of the user
api.update_status("Tweet #{} : Number of followers: {}".format(random.randint(0, 10000), user.followers_count))
#  displaying the number of followers in the console
ob.getFollowers(user)

#  finding the number of accounts followed by the user
api.update_status("Tweet #{} : Number of following accounts: {}".format(random.randint(0, 1000), user.friends_count))
#  displaying the number of accounts followed by the user
ob.getFollowingAccounts(user)

#  to like any recent message posted by the user @boltiot
twitter_handle_id = "@boltiot"
ob.like_tweet_of_boltiot(api, twitter_handle_id, user)

#  to like any recent tweet containing the expression #IOT
text_to_be_searched = "#IOT"
ob.search_tweet_having_hashtag(api, text_to_be_searched)