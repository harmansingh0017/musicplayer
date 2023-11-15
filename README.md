# Music Player Web Application

This is a music player web application with admin and user features built using Python, Django, MongoDB, and Scikit-Learn.

## Project Details

The application has two main use cases:

- Admin: Can add songs, playlists, and users

- User: Can register, login, listen to music, and create playlists

A machine learning model is implemented that suggests songs to users based on their age and gender.

## MongoDB Database

The MongoDB database contains the following collections:

- Music_playlist: Stores playlist name, songs, and user info

- Music_song: Stores song metadata like artist, audio file, genre etc.

- Music_user: Stores user account information

## Key Python Methods

- index(): Fetches user info, songs, and playlists for homepage

- register(): Creates new user accounts

- playlist_detail(): Gets a single playlist by id

- playlist_view(): Saves new playlists created by users

## User Interface

The main UI components are:

- Homepage: Displays songs and playlist options

- Create Playlist: Form to create new playlists

- Register Page: Allows user registration

## Matplotlib Charts

Two sample charts are created:

- Songs per artist bar chart

- Songs per genre bar chart

## Machine Learning

A Random Forest model predicts music genres based on user age and gender. It is used to suggest songs on login.

The model is trained on custom sample data and saved to forest.pkl.

## Installation

Follow these steps to run the project:

1. Clone the repository

2. Install dependencies

3. Configure MongoDB connection

4. Run migrations

5. Start development server
