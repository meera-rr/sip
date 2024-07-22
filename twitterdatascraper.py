import tweepy
import csv

# Your API keys and tokens
api_key = "MYH3alWpLLNjW23l43XJFMNqA"
api_key_secret = "WjTybd5udtuPCrx3CodAPBeprRqgDP4k5yXny89s2TxVh0uVvR"
access_token = "1810717170323836930-U3s8TQwaBUue29KworP0hqOZhx2DLe"
access_token_secret = "CrQ00kMQNmLyAHOUmSOcCWP9a9Trmix0D8v6sLNLaEjXK"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIiCuwEAAAAA7px3dIQTTCsBIwX60dHWEcNP%2Fzw%3DbPYWKLtRzcKcN4dUy2CPoIuLPJ1DnQh7JxkvulyYEJXBuQDXSd"

# Authenticate to Twitter
client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token, access_token_secret=access_token_secret)

tweets_data = [["Date", "Username", "Link"], ]
search_words = "#ActuallyAustic AND #BIPOC"

try:
    response = client.search_recent_tweets(query=search_words, tweet_fields=['created_at', 'id', 'author_id'], max_results=100)
    tweets = response.data

    if not tweets:
        print("No tweets found.")
    else:
        for tweet in tweets:
            user_response = client.get_user(id=tweet.author_id, user_fields=['username'])
            username = user_response.data.username
            tweet_link = f"https://twitter.com/{username}/status/{tweet.id}"
            data_list = [tweet.created_at, username, tweet_link]
            tweets_data.append(data_list)

    print("Authentication OK")
except tweepy.TweepyException as e:
    print(f"Error during authentication or fetching tweets: {e}")

# Write data to CSV
with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(tweets_data)

print(tweets_data)
