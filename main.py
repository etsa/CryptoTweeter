import tweepy, time, requests, sys
from BeautifulSoup import BeautifulSoup

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

one = 1
while True:
	page = requests.get("http://coinmarketcap.com")
	soup = BeautifulSoup(page.text)
	div = soup.find(href="/volume.html#doge") #changable to any currency on coinmarketcap.com
	usd = div["data-usd"]
	eur = div["data-eur"]
	btc = div["data-btc"]
	u = (u'\u20ac')
	euro = ('$')
	bit = (u'\u0E3F')
	bitp = ('$')
	nowauto = time.strftime("[%I:%M %p] ")
	api.update_status(nowauto + "1 #DOGE is worth: \n$" + usd + " USD \n" + bit + btc + " #BTC \n" + u + eur + " EUR #DogeCoin")
	print (nowauto + "1 #DOGE is worth: \n$" + usd + " USD \n" + bitp + btc + " #BTC \n" + euro + eur + " EUR #DogeCoin")
	time.sleep(2700)
