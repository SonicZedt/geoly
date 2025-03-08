import datetime
from discord.ext import tasks
from discord import Client
from services.aws import AWS
from config import Guild
from dependency import DiscordContainer, ServiceContainer, Provide, inject

@inject
def register(client: Client = Provide[DiscordContainer.client],
			 aws: AWS = Provide[ServiceContainer.aws]):

	@tasks.loop(seconds=1)
	async def check_ip():
		channel = client.get_guild(Guild.id).get_channel(Guild.channel_log_ip)
		if not channel:
			return
		
		ip = aws.checkip()
		if not ip:
			return

		messages = [message async for message in channel.history(limit=1)]

		# only send if ip is changed
		if(len(messages) > 0 and ip == messages[0].content):
			return 
			
		await channel.send(ip)

	@check_ip.before_loop
	async def check_ip_check():
		await client.wait_until_ready()

	check_ip.start()