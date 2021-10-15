from Listener import register
from event import provider

data: str = 'BLABLA'
register()

provider('log', data)
