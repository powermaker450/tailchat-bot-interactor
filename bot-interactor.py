#!/usr/bin/env python3
try:
	import requests
except:
	print("Error: The requests module is not installed.")
	exit()
try:
	import env
except:
	print("Error: The env.py file appears to be missing. It needs to be in the same directory as the program.")
	exit()

#don't set the values here. edit the env.py file.
key=env.key
instance_url=env.instance_url
guild_name=env.guild_name
channel_name=env.channel_name

in_use=True
blockedtext="*"*20

#functions
def post_message(instance,apikey,msg):
	requests.post("{}/api/plugin:com.msgbyte.simplenotify/webhook/callback?subscribeId={}&text={}".format(instance,apikey,msg))

#check for required fields
if key=="":
	print("Error: You need to input the bot key by editing the env.py file.")
	exit()
if len(key)!=24:
	print("Error: Bot key appears to be invalid. Try checking if it is inputted correctly.")
	exit()
if instance_url=="":
	print("Error: You need to input the server URL by editing the env.py file.")
	exit()

#if both guild_name and channel_name are filled out in the env.py file, the program will print the guild name and channel name respectively.
#otherwise, it will just print the instance name.
if not(channel_name=="") and not(guild_name==""):
	print("\nTailchat Notify Bot Interactor 1.0")
	print("Instance: {}".format(instance_url))
	print("Guild: {} | Channel: #{}".format(guild_name,channel_name))
	print("Key: {}{}\n".format(blockedtext,key[len(key)-5:len(key)-1]))
	print("You are now interacting with the bot. All input will be sent to {} in channel #{}. (markdown is supported):".format(guild_name,channel_name))
	print("To exit, press enter.\n")
else:
	print("\nTailchat Notify Bot Interactor 1.0")
	print("Instance: {}".format(instance_url))
	print("Key: {}{}\n".format(blockedtext,key[len(key)-5:len(key)-1]))
	print("You are now interacting with the bot. All input will be sent to the guild and channel set in the guild settings. (markdown is supported):")
	print("To exit, press enter.\n")

while in_use:
	message=input()
	if not(message==""):
		post_message(instance_url,key,message)
		message=""
	else:
		in_use=False

exit()
