#!/usr/bin/env python

import sys,os,CardDeck

money=100
stdbet=10

deck=CardDeck.Deck(1)

def mainmenu(m):
	clear()
	print "----K3YMKR BlackJack----\n"
	if (m>0):
		print "You have $%d"%m
	else:
		print "You owe $%d"%(-1*m)

	print "\nYour standard bet is $%d"%stdbet
	print """\n1). Deal with standard bet
2). Deal with custom bet
3). Change standard bet
4). Quit

Enter your choice: """
	ans=raw_input()
	return ans



def clear():
	os.system("/usr/bin/clear")


class Hand:
	def __init__(self,player):
		self.cards=[]
		self.value=0
		self.label=player

	def getvalue(self):
		return self.value

	def isblackjack(self):
		sum=self.value
		for a in self.cards:
			if a.ishidden():
				a.flipcard()
				sum+=a.getvalue()
				a.flipcard()
		return len(self.cards)==2 and sum == 21
			

	def revealcards(self):
		for a in self.cards:
			if a.ishidden():
				a.flipcard()
				self.addvalue(a)

	def addvalue(self,card):
		if not card.ishidden():
			self.value+=card.getvalue()
		if (self.value>21):
			for a in self.cards:
				if self.value > 21 and a.getvalue() == 11:
					a.acelower()
					self.value-=10
		


	def cansplit(self):
		return (self.cards[0].getvalue() == self.cards[1].getvalue()) and len(self.cards) == 2


	def getcard(self,card):
		self.cards.append(card)
		self.addvalue(card)


	def cardcount(self):
		return  len(self.cards)

	def __str__(self):
		carddisp=""
		for a in range(0,len(self.cards)):
			carddisp="%s,%s"%(carddisp,self.cards[a].__str__())
		carddisp=carddisp[1:]
			
		return "%s has %d: %s"%(self.label,self.value,carddisp)
		



def deal(bet):
	ddoption=0
	clear()
	d=Hand("Dealer")
	d.getcard(deck.dealcard(1))
	d.getcard(deck.dealcard())
	p=Hand("Player")
	p.getcard(deck.dealcard(1))
	p.getcard(deck.dealcard(1))
	print d
	if (p.isblackjack()):
		print "\n%s\nYou won BlackJack!!!"%(p.__str__())
		return bet*1.5
	if (d.isblackjack()):
		d.revealcards()
		print d
		print "\n%s\nYou lose.  Dealer has blackjack."%(p.__str__())
		return -1*bet
	ans="1"
	while ans!="2":
		print p
		print """What would you like to do?
1). Hit
2). Stay """
	
		if (p.cardcount() == 2 and money > bet*2):
			ddoption=1
			print "3). Double Down"
		ans=raw_input()
		if (ans=="3" and ddoption==1):
			bet*=2
		if (ans=="1" or ans == "3"):
			p.getcard(deck.dealcard(1))
			if (p.getvalue()>21):
				print p
				print "You lose. Busted"
				return -1*bet
		if (ans=="3"):
			print p
			ans="2"
	d.revealcards()
	while(d.getvalue()<17):
		d.getcard(deck.dealcard(1))
		if (d.getvalue()>21):
			print d
			print "You win.  Dealer Busted"
			return bet
	print d
	print p
	if (d.getvalue()>p.getvalue()):
		print "You lose"
		return -1*bet
	elif (d.getvalue()<p.getvalue()):
		print "You win!"
		return bet
	else:
		print "Push"
		return 0


ans=1
while (ans!="4") and money >= 5:
	ans=mainmenu(money)
	if (ans=="3"):
		bet=int(raw_input("What should your standard bet be? "))
		if (bet>5):
			stdbet=bet
		else:
			print "Bets must be more than $5"
			b=raw_input("Hit Enter\n")
	elif (ans != "4"):
		bet=stdbet
		if (ans=="2"):
			bet=int(raw_input("How much would you like to bet? "))
		
		if (bet>=5) and bet <= money:
			money+=deal(bet)
		else:
			print "Bets must be more than $5 and less than or equal to how much you have."
		b=raw_input("Hit Enter\n")

