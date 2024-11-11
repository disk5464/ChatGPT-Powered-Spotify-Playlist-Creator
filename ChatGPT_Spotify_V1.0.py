#This script will ask a user for a song title and aritst then ask ChatGPT for a list of similar songs. It will then pass that info to Spotify where it will create a playlist with thoes songs for the user. 
#Created By: Disk5464
#Last Modified: 10/22/24
#Version 1.0: Inital Commit. All previous versions have been re numbered to 0.X since they are unpblished.
######################################################################
#Check that the libaries are installed if not install them. Once installed import them.
import json, subprocess, sys, os

def install_and_import(packages):
    for package in packages:
        try:
            __import__(package)
            print(f"'{package}' is already installed. Importing...")
        except ModuleNotFoundError:
            print(f"'{package}' is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"'{package}' installed successfully.")
            __import__(package)

#Import the libaries
install_and_import(['openai', 'spotipy'])
import openai,spotipy
from spotipy.oauth2 import SpotifyOAuth

#Retrieve arguments passed from the calling script, check that they are not empty.
incomingTitle = sys.argv[1]
incomingArtist = sys.argv[2]

if "" in (incomingArtist, incomingArtist):
    print("\n" + "Either your song title or artist is missing!!")
    exit()

######################################################################
#Load the Json file with the API keys, check that they have been changed from the dummy values, then add them to the variables we will use.

#Get the working directory path and pair it with the json file name. Then open the json. Finally load it into a dictonary variable.
json_file_Location = os.path.dirname(os.path.abspath(sys.argv[0])) + "\API_Keys.json"
rawJson = open(json_file_Location)
API_Keys_Json = json.load(rawJson)

#Take the data from json and add it into local variables that will be used for the rest of the script.
chatGPT_Key = API_Keys_Json['chatGPT_Key']
spotify_client_id = API_Keys_Json['spotify_client_id']
spotify_client_secret  = API_Keys_Json['spotify_client_secret']
spotify_redirect_uri = API_Keys_Json['spotify_redirect_uri']

#Check that all of the API keys are now changed from the default values.
if "<API_KEY_HERE>" in (chatGPT_Key, spotify_client_id, spotify_client_secret, spotify_redirect_uri):
    print("One or more of your API keys are not set. Add them in the API_Keys.json file.")
    exit()
else:
    print("\n" +"All API keys have been set.")

######################################################################
#Set the local variables for the title & artist from the global ones from the GUI. Then print them to the screen to verify that they made it over.
usersongtitle = incomingTitle
usersongArtist = incomingArtist

print("\n" + "Recieved Song Title: " + usersongtitle)
print("Recieved Artist: " + usersongArtist)

######################################################################
#This section will take the request, pair it with the ChatGPT API key and send the request then store the response in a variable.
#Set your API key
openai.api_key = chatGPT_Key

#Build the prompt. This will make sure the returned format is the one python will be expecting: - Title - Artist.
chat_prompt = f"""
Based on the song "{usersongtitle}" by {usersongArtist}, suggest 5 similar songs. Ensure the response strictly follows this format:
- "Song Title" - Artist Name

Do not include numbering or any other text. Just provide the songs in this exact format.
"""

#Build the full ChatGPT API request and send it.
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # or gpt-4 if you have access
    messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": chat_prompt} ]
)

#Save the response into a variable. This has a lot of junk in it that we will clear out in the next step.
raw_response = response.choices[0].message.content
print("\n" + raw_response)

######################################################################
#This section takes the chat GPT response and cleans it up. First create an empty array for the songs / artist
songs_array = []

for line in raw_response.split('\n'):
    #Remove the - at the beginning of the item
    noDash = line.replace("- ", "", 1)

    #Split the artist and song title into their own vairables using the middle dash as a delimiter
    song, artist = noDash.split(' - ')

    #Add the item to the array
    songs_array.append((song, artist))

######################################################################
#This section will connect to spotify and log the user in. It then will create a blank playlist

#Connect to spotify, grant the read/write premission, specify the caching filename.
print("\n" + "Loging into spotify, check with your browser." )
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri=spotify_redirect_uri, scope='playlist-modify-private', cache_path='cache.txt')) 

#Create a variable with the person's username then set a variable with the playlist name.
username = sp.current_user()
playlist_name = "My AI Playlist"

#Create the playlist and get it's ID
playlist = sp.user_playlist_create(user=username['id'], name=playlist_name, public=False)
playlistID = playlist['uri']
print("Created the playlist" + "\n")

######################################################################
#Get the track info for each song and add it via ID to the playlist
for song, artist in songs_array:
    #This builds the query to search spotify for the given track
    query = f"{song} - {artist}"
    print("Adding: " + query)

    #This executes the search and only saves the first result
    search = sp.search(q=query, limit=1)

    #This grabs the unique track ID
    trackID = search['tracks']['items'][0]['uri']

    #This adds the track to the playlist
    sp.playlist_add_items(playlistID, [trackID])

#Let the user know the playlist is done building and clear the cache file so that the spotify token isn't stored
print("\n" + "Playlist has been built! Check your spotify!")
os.remove("cache.txt")

