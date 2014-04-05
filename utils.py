#!/usr/bin/python
import tweepy, time, requests, math, re
from decimal import *
from BeautifulSoup import BeautifulSoup

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def followback():
	inf = 1
	while true:
		for follower in tweepy.Cursor(api.followers).items():
			follower.follow()
	time.sleep(2700)

def stream():
	sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
	sapi.filter(track=["@DOGEUSD"])
	
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
		tweet = status.text
		id = status.id
		replyusr = status.user.screen_name
		reply = tweet.encode('ascii', 'ignore').strip()
		now = time.strftime("[%I:%M %p] ")
		api.create_favorite(id)
		try:
			page = requests.get("http://coinmarketcap.com")
			soup = BeautifulSoup(page.text)
			div = soup.find(href="/volume.html#doge")
			usd = div["data-usd"]
			splitty = reply
			samt = splitty.split(' ',1)
			amt = splitty.split(' ', 1)[1]
			amt = splitty.split(' ', 2)[1]
			info = ('info')
			error = ('error')
			current = ('current')
			commands = ('commands')
			if amt == error:
				api.update_status(now + "@" + replyusr + " Thank you for the report. It has been logged and sent to the dev.")
				print("[CMD: ERROR] " + now + "@" + replyusr + " Thank you for the report. It has been logged and sent to the dev.")
				f = open('errors.txt', 'w')
				f.write(now + "@" + replyusr + "\n")
				f.close()
				print("[ALERT] error logged")
				return stream()
			if amt == info:
				api.update_status(now + "@" + replyusr + " I am a bot, and I tweet the current price of DogeCoin every 45 minutes.")
				print("[CMD: INFO] " + now + "@" + replyusr + " I am a bot, and I tweet the current price of DogeCoin every 45 minutes.")
				return stream()
			if amt == commands:
				api.update_status(now + "@" + replyusr + " Commands: info, error, and current.")
				print("[CMD: CMDS] " + now + "@" + replyusr + " .")
				return stream()
			if amt == current:
				api.update_status(now + "@"+ replyusr + " 1 DOGE is currently worth $" + usd + " USD.")
				print("[CMD: CURRENT] " + now + "@"+ replyusr + " 1 DOGE is currently worth $" + usd + " USD.")
				return stream()
			if amt != info:
				api.update_status(now + "@" + replyusr + " I'll get back to your message ASAP. For bot info, reply with \"info\". DogeUSD.tk")
				print("[CMD: REPLY] " + now + "@" + replyusr + " I'll get back to your message ASAP. For bot info, reply with \"info\". DogeUSD.tk")
				return stream()
			amount = int(amt)
			money = Decimal(usd)
			total = amount * money
			usertotal = str(total)
			currentprice = money * 1
			api.update_status(now + "@"+ replyusr + " " + amt + " DOGE is currently worth $" + usertotal + " USD.")
			print("[CMD: DOGE]" + now + "@"+ replyusr + " " + amt + " DOGE is currently worth $" + usertotal + " USD.")
			return stream()
		except ValueError:
			return stream()

stream()
