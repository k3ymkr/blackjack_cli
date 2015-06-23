#!/usr/bin/env python
import random,time

class Card:
	faces=["Hearts","Diamonds","Spades","Clubs"]
	
	def __init__(self,size=0,face=0):
		if (size >0 ) and (size < 14) and (face >= 0 ) and (face < 4):
			self.size=size
			self.face=face
		else:
			self.size=random.randint(1,13)
			self.face=random.randint(0,3)
		if (self.size == 1):
			self.value=11	
		elif (self.size <11):
			self.value=int(self.size)
		else:
			self.value=10
		self.hidden=1


	def ishidden(self):
		return self.hidden == 1

	def flipcard(self):
		self.hidden=1-self.hidden

	def getsize(self,full=0):
		if (self.hidden==1):
			if full==0:
				return "H"
			else:
				return "Face Down"

		options={1:"Ace",2:"Two",3:"Three",4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
		if (full == 0):
			options={1:"A",2:"2",3:"3",4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
		return options[self.size]

	def acelower(self):
		if (self.value==11):
			self.value=1

	def getvalue(self):
		return self.value

	def getface(self,full=0):
		if (self.hidden==1):
			if (full == 1):
				return "Face Down"
			else:
				return -1
		if (full == 1):
			return self.faces[self.face]
		return self.face
		

	def __str__(self):
		if (self.hidden == 1):
			return "Face Down"
		return "%s of %s"%(self.getsize(1),self.faces[self.face])


class Deck:
	
	def __init__(self,shuffle=0):
		self.newdeck(shuffle)


	def newdeck(self,shuffle):
		hold=[];
		for a in range(0,4):
			for b in range(1,14):
				hold.append(Card(b,a))
		self.cards=hold
		if (shuffle == 0):
			self.shuffled=0
		else:
			self.shuffle()
		


	def shuffle(self):
		random.shuffle(self.cards)
		self.shuffled=time.strftime("%Y/%m/%d %H:%M:%S")

	def printcards(self):
		for a in range(0,len(self.cards)):
			print self.cards[a]
	def getcardcount(self):
		return len(self.cards)


	def dealcard(self,faceup=0):
		if len(self.cards)==0:
			if(self.shuffle==0):
				self.newdeck(0)
			else:
				self.newdeck(1)
		a=self.cards.pop()
		if (faceup!=0):
			a.flipcard()
		return a

	def __str__(self):
		ret="%d cards."%len(self.cards)
		if (self.shuffled == 0):
			ret+="  Never Shuffled"
		else:
			ret+="  Shuffled at %s"%self.shuffled


		return ret
	
				

if __name__ == "__main__":
	bob=Deck()
	bob.shuffle()
	print bob
	a=bob.dealcard()
	print a
	print a.getvalue()

	print bob
	

