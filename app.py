from flask import Flask, render_template, request, url_for
from search.search import Twitter
from search import get_tweets_csv

app = Flask(__name__)

@app.route("/")
def home():
	#Twitter().get_tweet()
	tweet = get_tweets_csv.get_tweet()

	#print(tweet['url'])

	return render_template("index.html", tweet = tweet)

@app.route("/contact_us")
def contact():
	return render_template("contact_us.html")





if __name__ == "__main__":
	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes