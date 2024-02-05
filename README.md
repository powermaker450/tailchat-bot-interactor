# Tailchat Bot Interactor

Simple program to send messages as the Notify Bot on your Tailchat guild.
This program is very basic and can only send text, but it can be modifed for use with automated scripts.

## Download

Make sure you have the requests module installed.
Download the `bot-interactor.py` and `env.py` file and place them in the same directory.

## Variables

Edit the `env.py` file to fill out the reqired `key` and `instance_url` variables like so:
```python
key="1a2b3c4d5e6f7g8h9i0j"
instance_url="https://tailchat.example.com" #also supports http. do not use the "/" at the end of the URL
guild_name=""
channel_name=""
```
`guild_name` and `channel_name` are optional and are only used as visual indicators. The bot key is enough to specify where the messages go.

## Usage

Once the env.py file is properly filled out, start the bot-interactor.py script.
It will output the instance URL you entered as well as the last four digits of the set bot key.
```
❯ python bot-interator.py     

Tailchat Notify Bot Interactor 1.0
Instance: https://tailchat.example.com
Guild: Test | Channel: #Lobby
Key: ********************9i0j

You are now interacting with the bot. All input will be sent to Test in channel #Lobby. (markdown is supported):
To exit, press enter.

```
All messages sent into the program are sent through the bot into the channel specified in the guild settings.
You can verify the settings are correct by checking if the messages succesfully sent in your set channel.
Sending formatted text is supported. See https://tailchat.msgbyte.com/docs/advanced-usage/richtext for text formatting options.

Once you are done, press enter with a blank message to exit.
