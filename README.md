# Udacity Full-Stack Nanodegree
## Project 3 : Item Catalog
### by Adam Hussain
## Overview

This app represents an Item Catalog that can be used record items from various different categories. For my project, I decided to create a Home Movies Catalog to catalog all the movies a person owns. This app implements CRUD functionality to create, showcase, edit, and delete movies within the database.

## Technologies used
- Vagrant
- VirtualBox
- Python 2.7

## Prerequisites
The latest vagrant build used previously for the Udacity tournament project.

## Steps to Run

Please ensure you have Python, Vagrant and VirtualBox installed. This project uses a pre-congfigured Vagrant virtual machine which has Flask server installed.

You need to change directories into the vagrant folder from the Udacity GitHub repo we've cloned before. Once in the vagrant folder, we will need to start the vagrant virtual machine and remote into it using the following commands below.

```
$ cd vagrant
$ vagrant up
$ vagrant ssh
```

Within the virtual machine change in to the shared directory where your catalog project is located and run the project py file.

```
$ cd /vagrant/catalog/DVDCatalog
$ python project.py
```

Then navigate to localhost:5000 on your favorite browser.

## API Endpoints
| Request | What you get | 
| ------------- |:-------------:|
| '/' or '/dashboard' | Get a list of recent movies stored in the catalog |
| /movies/<string:category> | Get a list of movies with in a movie genre category |
| /movies/<string:category>/<int:movie_id> | Get the information to a specific stored movie |
| /movies/create | Create a new movie entry in the catalog |
| /movies/<string:category>/<int:movie_id>/edit | Edit the information for a particular movie |
| /movies/<string:category>/<int:movie_id>/delete | Delete a particular movie in the catalog |
| /login | Login in as a user into the movie catalog app |
| /gdisconnect | Logout as a user from the movie catalog app |
| /movies/<string:category>/JSON | Get the JSON for a movie genre category |
| /movies/<string:category>/<int:movie_id>/JSON | Get the JSON for a specific stored movie |
| /dashboard/JSON | Get the JSON for a movie catalog dashboard |