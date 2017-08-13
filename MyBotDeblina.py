from myKeys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as tweep
import random

class MyBotDeblina:

    def likeTweetOfUser(self,api,boltuser,user) :
        #  to find out the most recent tweet by the user
        tweet = api.user_timeline(boltuser, count=1)

        # obtaining unique tweet id
        tweetID=tweet[0].id
        try:
            #  if the tweet is not already liked, then it is liked
            likedTweet=api.create_favorite(tweetID)
            api.update_status("Tweet #{} : Liked tweet by @boltiot user!".format(random.randint(0, 1000)))

        # if the tweet is already liked exception is displayed on the console
        except tweep.TweepError as e :
            print("Error: {}".format(e))

    def searchTweetForHashtag(self,api, searchTerm):
        # The Cursor method is used to crawl through the search results for tweets having the required expression
        searchResults = [status for status in tweep.Cursor(api.search, q=searchTerm).items(1)]
        searchTweetID = searchResults[0].id

        # once the expression is found in the tweet, the tweet is liked
        likedStatus = api.create_favorite(searchTweetID)
        api.update_status("Tweet #{} : Liked tweet with #IOT!".format(random.randint(0, 10000)))

    def set_user_authorization(self):
        # Setting the authorization tokens for twitter using tweepy from the already
        # included file containing keys of the TwitterBot
        user_auth = tweep.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        user_auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweep.API(user_auth)
        return api
# creating object of the class to access different functions and variables
ob = MyBotDeblina()

# setting up authorization with twitter via tweepy
api = ob.set_user_authorization()
user = api.me()

#  if the twitter bot account is successfully connected
print("Connection established with {}".format(user.screen_name))
#  finding the number of followers of the user
api.update_status("Tweet #{} : Number of followers: {}".format(random.randint(0, 10000), user.followers_count))

#  finding the number of accounts followed by the user
api.update_status("Tweet #{} : Number of following accounts: {}".format(random.randint(0, 1000), user.friends_count))

#  to like any recent message posted by the user @boltiot
userID = "@boltiot"
ob.likeTweetOfUser(api, userID, user)

#  to like any recent tweet containing the expression #IOT
searchText = "#IOT"
ob.searchTweetForHashtag(api, searchText)