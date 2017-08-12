from myKeys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as tweep
import random


def setAuthorization():
    # Setting the authorization tokens for twitter using tweepy from the already
    # included file containing keys of the TwitterBot
    authorization = tweep.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authorization.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweep.API(authorization)
    return api

def likeTweetOfUser(api,boltuser,user) :
    #  to find out the most recent tweet by the user
    tweet = api.user_timeline(boltuser, count=1)
    tweetID=tweet[0].id
    try:
        #  if the tweet is not already liked, then it is liked
        likedTweet=api.create_favorite(tweetID)
        api.update_status("Liked tweet by @boltiot user! #{}".format(random.randint(0, 1000)))

    # if the tweet is already liked
    except tweep.TweepError as e :
        print("Error: {}".format(e))

def searchTweetForHashtag(api, searchTerm):
    # The Cursor method is used to crawl through the search results for tweets having the required expression
    searchResults = [status for status in tweep.
                     Cursor(api.search, q=searchTerm).items(1)]
    searchTweetID = searchResults[0].id
    likedStatus = api.create_favorite(searchTweetID)
    api.update_status("Liked tweet with #IOT! #{}".format(random.randint(0, 10000)))



if __name__ == "__main__":
    # setting up authorization with twitter via tweepy
    api = setAuthorization()
    user = api.me()
    #  if the twitter bot account is successfully connected
    print("Connection established with {}".format(user.screen_name))

    #  finding the number of followers of the user
    api.update_status("Number of followers: {} #{}"
                      .format(user.followers_count,
                              random.randint(0, 10000)))

    #  finding the number of accounts followed by the user
    api.update_status("Number of following accounts: {} #{}".format(user.friends_count, random.randint(0, 1000)))

    #  to like any recent message posted by the user @boltiot
    likeTweetOfUser(api, "@boltiot", user)

    #  to like any recent tweet containing the expression #IOT
    searchTweetForHashtag(api, "IOT")