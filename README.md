# Tailchat Bot Interactor

Send messages as the Notify Bot on your Tailchat guild.
This program is very basic and can only send text, but it can be modifed for use with automated scripts.

## Download

Make sure you have the requests module installed.
Download the bot-interactor.py and env.py file and place them in the same directory.

## Variables

Edit the env.py file to fill out the reqired `key` and `instance_url` variables. `guild_name` and `channel_name` are optional and are only used as visual indicators. The bot key is enough to specify where the messages go.

## Usage

Once the env.py file is properly filled out, start the bot-interactor.py script.
It will output the instance URL you entered as well as the last four digits of the set bot key.
All messages sent into the program are sent through the bot into the channel specified in the guild settings.

Once you are done, press enter with a blank message to exit.
