'''
	We are going to create a simple 
	Intagram bot 
	using instabot
	to download the module 
	copy the code in your terminal
	and run
	--> pip install instabot <--
'''

# Import the module
from instabot import Bot

# Define the instabot
bot = Bot()

# Login using username and password
bot.login(username="<--insert-username-->", password="<--insert--pas")

# To upload a photo / image
bot.upload_photo("<--insert-picture-name-->", caption="<--insert-caption-->")

# To follow some-one
bot.follow("<--user-name-of-person-to-follow-->")

# To send message to some-one
bot.send_message("<--message-->", ['<--user-name-to-send-->])

# To get follower information
my_followers = bot.get_user_followers("<--insert-user-name-->")
for follower in my_followers:
    print(follower)

# To unfollow everyone
bot.unfollow_everyone()
