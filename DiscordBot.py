import discord
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# getting environment variables loaded into the program
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# variables for spotipy
redirect_url = 'http://localhost/'
scope = "playlist-modify-public"

#initializing spotipy and Discord
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=redirect_url, scope=scope)
)

client = discord.Client()


# alert to know
@client.event
async def on_ready():
    print('Ready!')


# function to parse through incoming messages and if they are a spotify link to save the song id
@client.event
async def on_message(message):
    # taking spotify song link and excavating the song id
    if "https://open.spotify.com/" in message.content:
        messageContent = message.content
        # todo make these next two lines more concise (re for two delimiters)
        str_list = messageContent.split('track/')
        str_list = str_list[1].split('?')
        song_id = [str_list[0]]  # song ids must be in an array for spotipy

        if message.channel.id == '999020947141046423:  # 'Olive Garden' server song recs
            playlist_id = '79v7GklSr4IHgkpunO3PJX'
            sp.playlist_add_items(playlist_id, song_id)

        elif message.channel.id == '999849942023675994':  # 'Pizza Hut' server song recs
            playlist_id = '0wCWdOhSHgQazopQDonV6L'
            sp.playlist_add_items(playlist_id, song_id)

        else:
            print('Bark?')

client.run(TOKEN)
