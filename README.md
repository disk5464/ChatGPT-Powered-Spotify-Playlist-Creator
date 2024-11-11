# ChatGPT Powered Spotify Playlists 
This python program will create a playlist in your Spotify account with songs suggested from Chat GPT based on a given song and artist.





## How do I get it running?
**Step 1:** Install Python 3. If you don't have it installed check out this guide https://www.howtogeek.com/197947/how-to-install-python-on-windows/

**Step 2:** Open API_Keys.json and replace each instance of <API_KEY_HERE> with your API keys. The first one is for the ChatGPT API Key and the rest are for Spotify. For help creating these keys check out the Q&A at the bottom of the page.

<p align="center"><img src="https://github.com/user-attachments/assets/9731740f-3bc4-4690-a89a-c2cf099e0b9b"/> </p>





## **How do I use this?**

After installing Python and setting your API keys, see above, double-click the ChatGPT_Spotify_Launcher.bat file. This will launch a GUI that will ask you for the name of a song and its artist. 
<p align="center"><img src="https://github.com/user-attachments/assets/724a9a35-f470-40fc-ac78-581e15607f00"/> </p>
<p align="center"><img src="https://github.com/user-attachments/assets/d5a4a872-9d29-47b0-aea6-f707356665f7"/> </p>

Once you click the "Click me to create the new playlist" button, python will check that you have set your API keys in the API_Keys.json file along with importing the required libraries.

<p align="center"><img src="https://github.com/user-attachments/assets/83b0fd73-5435-4d31-9130-afa2895ec2d6"/> </p>

After this python will send the song to ChatGPT-3.5-turbo where it will respond with 5 songs.

<p align="center"><img src="https://github.com/user-attachments/assets/3312cdd2-bb4d-47ce-ae43-fe0e3aaeb4c4"/> </p>

Next, it will log into your Spotify account and create a new playlist called "My AI Playlist"

<p align="center"><img src="https://github.com/user-attachments/assets/d88b169b-557e-457d-96fe-36294bced6a2"/> </p>

Finally it will add the songs to the new playlist.

<p align="center"><img src="https://github.com/user-attachments/assets/58be30c7-c442-489b-9bb9-5da182f81eba"/> </p>

You can now go to Spotify and listen to your new playlist!

<p align="center"><img src="https://github.com/user-attachments/assets/dc7b582f-1a35-412f-9d4f-9e5ffe878c8c"/> </p>





## Q&A

### Ok, cool, but WHY?


In short, because I can. 
In long, I was thinking about how I love the soundtrack for the movie _Whiplash_ and would love to hear more jazz songs like it, but I know nothing about Jazz. So I thought well I could ask chatGPT for recomendations. But I realized that I'd have to then copy paste them into Spotify and build it by hand. Considering how lazy I am my first thought was "Why not automate it"


### Isn't this a built-in function of Spotify?


Yep. Just right-click on a song, artist, album, etc, and click "Go to song radio". From there hit "Save to Libary". 


### So why not just use that?


Because this is more fun, plus it allowed me to learn more about Python, APIs, and how ChatGPT works.


### Does this cost money?

Sort of. When you create a new ChatGPT dev account it will set you up with some free credits, however if you have exaushted this you will need to pay 5 bucks to add some credits. As for Spotify, the dev account is free however this program may only work for paid Spotify premium accounts, which I haven't tested with free spotify accounts.


### How does this log into my Spotify account?

The script uses the SSO provided by Spotify's API to log into your account. When the script hits the login section it will launch your default browser and go to http://localhost:4202 to either grab your cached credentials or to have you log in. This is all done by spotify's API, no credentials are handled by the script. 


### How do I get a chat GPT API key?


**Step 1:** Go to the ChatGPT API website and create an account. https://platform.openai.com/docs/overview

**Step 2:** Create a new project. https://platform.openai.com/settings/organization/projects

**Step 3:** Go to the API keys page. https://platform.openai.com/api-keys

**Step 4:** Click "Create New Secret Key".  

**Step 5:** Once the key is created you will get the "Save your key" prompt. The key in this popup is what you will need to save and put into the API_keys.json file


### How do I get the Spotify API keys?


**Step 1:** Create a Spotify developer account. https://developer.spotify.com

**Step 2:** Once logged in, click "Create an app"

**Step 3:** Give the app a name and description. 

**Step 4:** Skip the website

**Step 5:** Add in _http://localhost:4202_ as the redirect URI. This is used for the login section, if you don't add this Python won't be able to connect to your Spotify account!

**Step 6:** Click the checkbox for Web API.

**Step 7:** Agree to the terms and conditions and press save.

**Step 8:** Once the page refreshes you can go into the app, click on settings and the page will display your Client ID. Click "View Client Secret" to get your client secret.

**Step 9:** Add the client ID, Client secret, and Redirect URI to the API_keys.json file

If you want a more detailed version of this check out steps 1 to 8 in this guide from @barraider. https://docs.barraider.com/faqs/spotify/getting-started/
