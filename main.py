#!/usr/bin/python3

import socket
import sys

# Global Variables
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server to join on StartUp
channel = "##BulletBan" # Channel
botnick = "BulletBan" # Your bots nick
adminname = "bulletsquid"
command_prefix = "?" # Character required at beginning of line for bot to parse command
exitcode = "Justice never sleeps."
data_max = 2048 # Can receive up to 'data_max' bytes of data from the socket
adminList = ["bulletsquid", "noone"]

def main():
	IRCconnect()
	joinchan(channel)
	while 1:
		ircmsg = ircsock.recv(data_max).decode("UTF-8")
		ircmsg = ircmsg.strip('\n\r')
		print(ircmsg)
		if ircmsg[0] == command_prefix:
			print("Parsing command")
		if ircmsg.find(channel + " :") != -1: # ChannelName : MSGS Go Here
			name = ircmsg.split('!',1)[0][1:]
			if name in adminList and ircmsg.find("?exit") != -1:
				print(name + " used command '" + command_name + "'")
				print("Shuting down...")
				sys.exit()
		if ircmsg.find("PING :") != -1:
			pong()

def IRCconnect():
	print("Atempting to join '" + server + "'")
	ircsock.connect((server, 6667))
	ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) # POSTing the required information
	ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # Give the bot (user) a Nick
	
def joinchan(chan):
	print("Atempting to join '" + chan + "'")
	ircsock.send(bytes("JOIN "+ channel +"\n", "UTF-8")) 
	ircmsg = "" # Prints msg/info to terminal
	while ircmsg.find("End of /NAMES list.") == -1:  # To determine if the bot has finished connecting
		ircmsg = ircsock.recv(data_max).decode("UTF-8")
		ircmsg = ircmsg.strip('\n\r')
		print(ircmsg)
	
def pong(): # Pongs the ping from the server (To prevent forced disconnects)
	ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
	
#def pm():
	# sends pm to someone

#def say():
	# send msg to chan
main()
# Ban commands
# Check for roles to see who can run commands (Check the proper flagged users)
# Restart/Shutdown commands
# Add a ban limit per OP (Prevents abuse or someone having unwanted access)
 
 