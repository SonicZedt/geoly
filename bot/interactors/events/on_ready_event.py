import config
from discord import Client
from discord.app_commands import CommandTree
from dependency import DiscordContainer, Provide, inject

@inject
def register(client: Client = Provide[DiscordContainer.client],
			 tree: CommandTree = Provide[DiscordContainer.tree],
			 *, ready_callback = None):

	@client.event
	async def on_ready():
		await tree.sync()

		if ready_callback:
			ready_callback()