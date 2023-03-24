# MeloFile 

Music is an art form that has the power to move us in many ways. It can make us feel happy, sad, energized, or relaxed. One of the most important elements of a song is its lyrics. They tell a story, express emotions, and convey messages that can resonate with us on a personal level. MeloFile is a platform that offers a collection of song lyrics that music lovers can access and enjoy.

**To see the full live application, visit:<br/>
https://melofile.up.railway.app/**

## Features

* <b>Authentication</b> - This web application is using the build-in Django authentication system to authenticate users. This process includes filling Register form and then logging in to your account by providing your user name and password.

* <b>Profile</b> - Registered users will have a profile they can view which contains information about their contributions and their followers/following.

* <b>Edit Profile</b> - Registered users can edit their profile picture name and email at anytime through settings and profile page.

* <b>Contribute Lyrics</b> - This application allows users to add song lyrics to the platform. Users are able to add Artists and select genres for the song as well.

* <b>Song Page</b> - Users can view the song page which contains the song name, artist name, ratings, lyrics, genres, contributors and the comments.

* <b>Top Lyrics / Latest Lyrics</b> - Users can view the top rated songs as well as the most recently added songs on the home page.

* <b>Artists Index / Artist page</b> - Users can view the artist index and page, which contains all songs by the artist on the platform.

* <b>Search and Filter</b> - The platform allows for anyone to be able to search for either song name or artist, and view song pages, as well as filter songs through various genres.

* <b>Favorite</b> - Registered Users are able to add their favorite songs to their favorites list for future viewing.

* <b>Ratings</b> - Registered Users are able to rate songs out of 5 star ratings.

* <b>Comment</b> - Registered Users are able to comment on songs.

* <b>Following Feed</b> - Registered Users are able to follow other profiles and view their contributions and activities on the feed page.

* <b>Edit Request / Approval</b> - Registered Users are able to Request and edit of a song to which the original poster can then choose to confirm or deny the changes request. If changes approved the song lyrics will be updated and the requester will be add to the contributors of the song.

* <b>Responsive Web Design</b> - This application is fully responsive and because of that it can work on all platforms and devices.

* <b>REST API</b> - Using the django rest framework I implemented an api to recieve songs, individual song, artists and individal artist data at the following endpoints: 

```
    "GET /api",
    "GET /api/songs",
    "GET /api/songs/:id"
    "GET /api/artists",
    "GET /api/artist/:id",
```

## Install and Run.

If you'd like to clone this app and use it locally, then you need to do the following steps.<br/><br/>
First, you need to provide your Spotify, YouTube and Genius tokens and IDs to make fetching data from external APIs possible.<br/>
Do it in the development settings file:

```
SPOTIFY_CLIENT_ID = 'your Spotify client ID'
SPOTIFY_CLIENT_SECRET = 'your Spotify client secret'
```

Here is a guide which explain how to get IDs and tokens:
https://developer.spotify.com/documentation/general/guides/app-settings/ <br/>

1. Install all necessary dependencies
    ```python
        pip install -r requirements.txt
    ```
2. Make Migrations
    ```python
        python3 manage.py makemigrations
    ```
    ```python
        python3 manage.py migrate
    ```
    ```python
        python3 manage.py runserver
    ```
> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

## Distinctiveness and Complexity.

In my application I implemented some new distinct feaures such as :
-  `rating` - using javascript users can select their rate of a song out of 5 stars and the average rate for a song is calculated by model class aggregate function
-  `Search and filter` - I added the ability to search songs by their title and search for songs by artist name. I also added the ability to filter songs on the home feed by genre; this can be done by selecting a genre under genres heading
-  `Edit Request` - I implemented this feature where if a user would like to request and edit to another users song page they can press the 'edit request' button which using javascript opens a text field where the requestor can change the current song lyrics and press 'request', which then sends the request to the original poster. The original poster can then view the request and choose to accept or deny the request. If accepted the song obj will be updated and the requestor will be added to the song contributors. The requestor will be notified if they go on their requests tab and see either APPROVED or DENIED. If no decision has been made yet it will read PENDING.
-  `Use of external library` - My application is using an external open source library called 'diff.js' which allowed users to see the edits made to lyrics within an edit request view. the library shows deletions and insertions of characters made to text.
- `Spotify api` - using the spotipy library which is a lightweight Python Library for the Spotify Web Api I retrieved data for the various Album artworks and artist images.
-  `Mobile Responsive` - The application is completely mobile responsive

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img width="1439" alt="Screen Shot 2023-03-24 at 5 54 10 PM" src="https://user-images.githubusercontent.com/67938718/227649484-e9e250da-7061-484b-952e-cb1fd440dec7.png">
</td> 
<td width="50%">
<br>
<p align="center">
  Song Page Preview
</p>
<img width="1439" alt="Screen Shot 2023-03-24 at 5 54 37 PM" src="https://user-images.githubusercontent.com/67938718/227649116-5bf187c7-190f-41a6-95c6-6993626c5c0d.png">
</td>
</table>

 #### 🛠️ Built with

####  Front-End  
<div align="left">  
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="30" />  
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/css3-original-wordmark.svg" alt="CSS3" height="30" />  
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/javascript-original.svg" alt="JavaScript" height="30" />
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/bootstrap-plain.svg" alt="Bootstrap" height="30" /> 

</div>
</td><td valign="top">

####  Back-end  
<div align="left">  
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="40" />  
<img style="margin: 20px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="40" />  
</div>
<br/>
</td></tr></table> 
