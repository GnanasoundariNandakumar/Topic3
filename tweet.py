from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt

consumerKey = "i2LejbniPkatL0M6m3rB3iVzH"
consumerSecret = "0Dh4lm7mmfKrkV0LsuAK1Yjv81rRlGw8qRFVgjDSO6xkOWVVIv"
accessToken = "3640015754-gdeo5vgLSyO87MA7KMwBTaNRoqgJ7dIOiXgEABO"
accessTokenSecret = "dwzflycZJto73QcVsGhrnmWa0Dvl5RWI6Elnh4syndaZj"


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def percentage(part, whole):
    return 100 * float(part) / float(whole)


keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input("Please enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search(), q=keyword).items(noOfTweet)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
        # print(analysis)

    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
        print(analysis)

    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
        # print(analysis)

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)

positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

# Creating PieCart

labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.style.use('default')
plt.legend(patches, labels, loc='best')
plt.title("Sentiment Analysis Result for keyword=  " + keyword + "")
plt.axis('equal')
plt.show()