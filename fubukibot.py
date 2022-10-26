import discord
import random

TOKEN = # write your discord bot token here

client = discord.Client()

@client.event
async def on_ready():
	print('{0.user} Has logged in!'.format(client))

@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {user_message} ({channel})')
	if message.author == client.user:
		return
	
	if user_message.lower() == "?help":
		await message.channel.send("Command List: [Waifu] [Timpa lirik] [?random] [?gacha] [?help]")
		return
		
	if user_message.lower() == "waifu":
		await message.channel.send('Friend! No waifu!')
		return
	elif user_message.lower() == "Waifu":
		await message.channel.send("Friend! No waifu!")
		return
	
	if user_message.lower() == "?random":
		response = f'Your random number is: {random.randrange(10000)}'
		await message.channel.send(response)
		return
	
	waifu = ["Tokino Sora","Roboco","AZKi","Sakura Miko","Hoshimachi Suisei","Yozora Mel","Aki Rosenthal","Akai Haato","Shirakami Fubuki","Natsuiro Matsuri","Minato Aqua","Murasaki Shion","Nakiri Ayame","Yuzuki Choco","Oozora Subaru","Usada Pekora","Shiranui Flare","Shirogane Noel","Houshou Marine","Amane Kanata","Tsunomaki Watame","Tokoyomi Towa","Himemori Luna","Kiryu Coco","Yukihana Lamy","Momosuzu Nene","Shishiro Botan","Omaru Polka","Laplus Darkness","Takane Lui","Hakui Koyori","Sakamata Chloe","Kazama Iroha","Ayunda Risu","Moona Hoshinova","Airani Iofifteen","Kureiji Ollie","Anya Melfissa","Pavolia Reine","Vestia Zeta","Kaela Kovalskia","Kobo Kanaeru","Mori Calliopi","Takanashi Kiara","Ninomae Ina'nis","Gawr Gura","Watson Amelia","IRyS","Tsukumo Sana","Ceres Fauna","Ouro Kronii","Nanashi Mumei","Hakos Baelz"]

	hasil = random.choice(waifu)
	
	if user_message.lower() == "?gacha":
		await message.channel.send(hasil)
		return
		
	if user_message.lower() == "timpa lirik":
		await message.channel.send("All my friend are toxic, all ambitionless so rude and always negative i need new friends, but it's not that quick and easy oh, im drowning, let me breathe")
		return
	elif user_message.lower() == "Timpa lirik":
		await message.channel.send("All my friend are toxic, all ambitionless so rude and always negative i need new friends, but it's not that quick and easy oh, im drowning, let me breathe")
		return

client.run(TOKEN)