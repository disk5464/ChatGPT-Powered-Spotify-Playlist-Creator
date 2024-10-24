# ChatGPT Powered Spotify Playlists 
This python program will create a playlist in your Spotify with songs suggested from chat GPT based on a given song.

## **How does this work?**

When you run the GUI python script a GUI will spawn that will ask you for the name of a song and its artist. 

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
