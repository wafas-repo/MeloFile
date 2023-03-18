# MeloFile 

Music is an art form that has the power to move us in many ways. It can make us feel happy, sad, energized, or relaxed. One of the most important elements of a song is its lyrics. They tell a story, express emotions, and convey messages that can resonate with us on a personal level. MeloFile is a platform that offers a collection of song lyrics that music lovers can access and enjoy.

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

## Install and Run.

1. Install all necessary dependencies
    ```python
        pip install -r requirements.txt
    ```
2. Make Migrations
    ```python
        python manage.py makemigrations
    ```
    ```python
        python manage.py migrate
    ```

## Files and Directories.

- `Main Directory`

    - `templates` - Contains main template for layout structure of application

        - `main.html` - main layout of application
        - `navbar.html` - navbar of application containing searchbar, logo/app name, and links to different pages.
        - `footer.html` - footer of application contains artist index and links to socials

    - `base` - main app directory
        - `static` - Holds all static files.
            - `static/images` - Holds all profile images and svg files.
            - `static/js` - Holds js file for app
            - `static/styles` - holds all css files used for styling
        - `templates/base` - all templates for pages of app.  
            - `home.html` - contains genres_component  feed_component and top lyrics div as well as latest lyrics div
            - `login.html` - contains form for login
            - `register.html` - contains form for user registration
            - `genres_component.html` - displays all genres from database in div
            - `feed_component.html` - displays all song objects from database in div
            - `top_lyrics.html` - displays top 5 highest rated lyrics when in mobile responsive mode
            - `song_form.html` - form for adding a song to platform
            - `song.html` - displays song page with artist name, song title, like button, rating form, contributors and comments
            - `delete.html` - a confirmation page when delete song is selected
            - `profile.html` - user profile displaying contributions followers and following. Also contains follow unfollow and edit profile button.
            - `update-user.html` - displays form for updating user avatar username and email
            - `following.html`- displays a feed of contributions and comments made by a profiles followers
            - `favorite_songs.html` - where user can view their favorited songs
            - `edit_requests.html` - displays all edit requests made by user of for user songs.
            - `request_view.html` - displays the edit request made to lyrics and also form for approval or denial
            - `artist_index.html` - list of artist names under letter
            - `artist_page.html` - lists all songs on app by artist
        - `models.py` - contains various models to hold information for User, Song, Artist, Genre, Comments, Rating and Edit Requests.
        - `urls.py` - contains paths for all routes of the application.
        - `views.py` - contains all view functions for template rendering.
         - `forms.py` - contains form metadata for add song and update_user


## Distinctiveness and Complexity.

In my application I implemented some new distinct feaures such as :
-  `rating` - using javascript users can select their rate of a song out of 5 stars and the average rate for a song is calculated by model class aggregate function
-  `Search and filter` - I added the ability to search songs by their title and search for songs by artist name. I also added the ability to filter songs on the home feed by genre; this can be done by selecting a genre under genres heading
-  `Edit Request` - I implemented this feature where if a user would like to request and edit to another users song page they can press the 'edit request' button which using javascript opens a text field where the requestor can change the current song lyrics and press 'request', which then sends the request to the original poster. The original poster can then view the request and choose to accept or deny the request. If accepted the song obj will be updated and the requestor will be added to the song contributors. The requestor will be notified if they go on their requests tab and see either APPROVED or DENIED. If no decision has been made yet it will read PENDING.
-  `Use of external library` - My application is using an external open source library called 'diff.js' which allowed users to see the edits made to lyrics within an edit request view. the library shows deletions and insertions of characters made to text.
-  `Mobile Responsive` - The application is completely mobile responsive