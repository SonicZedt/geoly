from discord import Client, Intents
from discord.app_commands import CommandTree
from dependency_injector import containers, providers
from services.aws import AWS
from dependency_injector.wiring import Provide, inject

class DiscordContainer(containers.DeclarativeContainer):
	def _instantiate_client():
		intents = Intents.default()
		intents.message_content = True
		return Client(intents=intents)
	client = providers.Singleton(_instantiate_client)

	tree = providers.Singleton(CommandTree, client = client)


class ServiceContainer(containers.DeclarativeContainer):
	aws = providers.Singleton(AWS)