from os import environ
from stormpath.client import Client

client = Client(
  id=environ['STORMPATH_CLIENT_APIKEY_ID'],
  secret=environ['STORMPATH_CLIENT_APIKEY_SECRET']
)
