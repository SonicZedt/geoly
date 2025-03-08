from interactors.events import on_ready_event

def init(*, on_ready = None):
	# register all events here
	on_ready_event.register(ready_callback = on_ready)