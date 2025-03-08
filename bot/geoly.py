import interactors.command
import interactors.commands
import interactors.event
import interactors.events
import interactors.task
import interactors.tasks
import config
from dependency import (
	DiscordContainer,
	ServiceContainer
)

def init_tldr():
	discord_container = DiscordContainer()
	discord_container.wire(packages=[
		interactors.commands,
		interactors.events,
		interactors.tasks
	])

	service_container = ServiceContainer()
	service_container.wire(packages=[
		interactors.commands,
		interactors.tasks
	])

	interactors.event.init(on_ready=interactors.task.init)
	interactors.command.init()

	client = discord_container.client()
	client.run(config.token)

if __name__ == '__main__':
	init_tldr()