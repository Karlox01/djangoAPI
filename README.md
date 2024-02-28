# WatchForum API

Welcome to the WatchForum API, the backend component of the WatchForum web application. This Django-based API serves as the engine that powers discussions about watches and timepieces.

![Watches By Karl API](https://res.cloudinary.com/dzchfcdfl/image/upload/v1709080774/API_oudeoa.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Utilized Programs](#programs-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Issues and Solutions](#issues-and-solutions)
- [Admin Rights](#Rights-and-solutions)
- [Credits](#credits)

## Introduction

The WatchForum API is designed to facilitate meaningful discussions among watch enthusiasts. It powers the backend of the WatchForum web application, providing essential functionalities for user engagement, conversation management, and more.

## Features

- **User Authentication**: Secure user authentication system to enable personalized experiences.
- **Discussion Threads**: API endpoints to manage watch-related discussions and topics.
- **Messaging System**: Facilitates communication between users. (*Planned to be Incorporated. Late Winter 2024*)
- **User Dashboard**: Provides a dashboard for users to manage their discussions. (*To be expanded Spring 2024*)

# Utilized Programs and Libraries

The WatchForum API relies on a range of programs and libraries to achieve its functionality. Below is a list of the programs and libraries along with their versions:

1. **asgiref (3.7.2)**: ASGI framework for Python, providing a standard interface between web servers and Python web applications or frameworks.

2. **click (8.1.7)**: A Python package for creating command-line interfaces.

3. **click-log (0.4.0)**: Extension for Click to enhance the logging capabilities of command-line applications.

4. **cloudinary (1.38.0)**: A cloud service that offers a solution for managing images and videos. *(Heavy use for hosting profile images and multiple post images)*

5. **cloudinary-cli (1.10.0)**: Command-line interface for Cloudinary, allowing interaction with the Cloudinary service through the command line.

6. **dj-database-url (2.1.0)**: A Django utility for utilizing the `DATABASE_URL` environment variable to configure a Django application.

7. **dj-rest-auth (2.1.9)**: A Django package providing a set of REST API endpoints for handling authentication.

8. **Django (3.2.23)**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

9. **django-allauth (0.44.0)**: A Django-based authentication system that handles signup, login, and account management.

10. **django-cloudinary-storage (0.3.0)**: A Django storage backend for Cloudinary, allowing seamless integration of Cloudinary with Django projects.

11. **django-cors-headers (3.7.0)**: A Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

12. **django-filter (23.5)**: A Django application for allowing users to filter queryset dynamically.

13. **djangorestframework-simplejwt (5.3.0)**: A JSON Web Token (JWT) authentication plugin for the Django REST Framework.

14. **gunicorn (20.1.0)**: A Python WSGI HTTP server for UNIX, used to serve the Django application in production.

15. **docstring-parser (0.15)**: A Python library for parsing docstrings and extracting metadata.

16. **oauthlib (3.2.2)**: A generic and reusable Python library for implementing OAuth1 and OAuth2.

17. **pillow (10.2.0)**: The Python Imaging Library adds image processing capabilities to your Python interpreter.

18. **psycopg2 (2.9.9)**: PostgreSQL adapter for Python, required for Django applications using a PostgreSQL database.

19. **PyJWT (2.8.0)**: A Python library to work with JSON Web Tokens.

20. **python-dotenv (1.0.0)**: A Python module that reads key-value pairs from a .env file and can set them as environment variables.

21. **python3-openid (3.2.0)**: A set of Python packages to support use of the OpenID decentralized identity system.

22. **pytz (2023.3.post1)**: A library for working with timezone-aware datetime calculations.

23. **requests-oauthlib (1.3.1)**: OAuthlib support for Python-requests.

24. **sqlparse (0.4.4)**: A non-validating SQL parser for Python, used for formatting SQL queries.

These programs and libraries contribute to the functionality, security, and efficiency of the WatchForum API. Each plays a specific role in ensuring a robust and feature-rich backend for the WatchForum web application.


## Technology Stack

- **Django**: The web framework for perfectionists with deadlines.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **SQLite Database**: A lightweight, file-based database for ease of development.
- **Python 3.9.17**: The programming language driving the backend logic.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone [repository_url]
   cd watchforum-api
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

## API Endpoints

Detailed documentation about the API endpoints can be found in the API Documentation file.

## Likes models 

The Like model represents the likes functionality in the WatchForum API. Here's a detailed explanation:

Like is associated with two main fields: owner and post.✔️
owner is a ForeignKey pointing to the User model, representing the user who liked the post.✔️
post is a ForeignKey pointing to the Post model, establishing a relationship with the post being liked.✔️
created_at stores the timestamp of when the like was created.✔️

```

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'

```

## Post Models 

The Post model is a core component of your API, representing the watch-related discussions and topics. Let's break it down:

Post is linked to the User model through the owner field, indicating the user who created the post.✔️
created_at and updated_at track the timestamps of when the post was created and last updated.✔️
title stores the title of the discussion topic.✔️
content is a TextField allowing for a detailed description or comments related to the topic.✔️
image_filter is a CharField with predefined choices for image filtering.✔️


The PostImage model is related to the Post model and handles images associated with a post

PostImage has a ForeignKey (post) linking it to a specific Post.✔️
image is an ImageField storing the image associated with the post. ✔️

```

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.post.title + ' Image'

```

### Profiles models

The Profile model represents user profiles, providing additional information about each user:

Profile is associated with a user through a OneToOneField (owner), ensuring a one-to-one relationship with the User model.✔️
created_at and updated_at record the creation and last modification timestamps.✔️
name stores the name of the user.✔️
content is a TextField providing space for additional user information or descriptions.✔️
image is an ImageField storing the user's profile picture.✔️

```

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_wfihdl_mufv7v'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)

```

## Issues Testing and Solutions 

During the development process, several challenges were encountered, and some are ongoing. For detailed information, refer to the Issues and Solutions On the main React APP.

![Postman](https://res.cloudinary.com/dzchfcdfl/image/upload/v1709076562/Postman_numhdl.jpg)



The `PostImage` endpoint posed a unique challenge during development, specifically regarding the association of images with posts. Extensive testing was conducted using Postman to validate the functionality.

Challenges:

Association: Ensuring each uploaded image is correctly associated with the corresponding post.
Implementation Details:

Association with Post: Each uploaded image is associated with a specific post through the post field in the model. During testing, the correctness of this association was verified.

Example Response:
```
{
    "id": 1,
    "post": 3,  # ID of the associated post
    "images":[],
    "created_at": "2024-02-26T12:00:00Z"
}
```

Testing:

Postman was extensively utilized for testing various scenarios:

Single image upload.
Verification of correct association with the respective post.
Bulk image upload using the /post_images/bulk_upload/ endpoint.
Example Request (Postman):

```
POST https://apifinalproject-bcabd5b820ec.herokuapp.com/posts/
Content-Type: multipart/form-data
Authorization: Bearer [YOUR_ACCESS_TOKEN]

```

# Admin Rights Configuration

In the WatchForum API, specific changes have been made to the admin configurations to enhance the functionality and ease of management. Below are the details of the changes made to the admin configurations for the `Profile`, `Post`, and `PostImage` models.

## Profile Model Admin Configuration

```
from django.contrib import admin
from profiles.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #  existing Profile admin configurations

    def user_posts(self, obj):
        return "\n".join([str(post) for post in obj.owner.posts.all()])

    user_posts.short_description = "User Posts"


```
Post and PostImage Model Admin Configurations

In the PostAdmin class, additional functionalities are added, including the ability to search posts by owner username, title, and content. Also, a custom action delete_selected_posts is defined to allow the deletion of selected posts along with their related post images.

In the PostImageAdmin class, the ability to search post images by post title is added for improved navigation and management in the admin panel.

These changes provide administrators with enhanced tools and features to manage user profiles, posts, and post images efficiently through the Django admin interface.

```
# Import the Post and PostImage models
from .models import Post, PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'created_at', 'updated_at')
    search_fields = ['owner__username', 'title', 'content']
    list_filter = ('created_at', 'updated_at', 'owner')
    actions = ['delete_selected_posts']

    def delete_selected_posts(modeladmin, request, queryset):
        # Delete selected posts and related post images
        for post in queryset:
            post.images.all().delete()
            post.delete()

    delete_selected_posts.short_description = "Delete selected posts"

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    search_fields = ['post__title']

```

* Note: The admin panel currently lacks static CSS due to an ongoing issue with static files. Regrettably, time constraints have hindered resolving this issue. Work in progress to rectify the problem and restore the missing static files in the admin panel.

## Credits

- Code Institute's Moments Template Project: This project is inspired by the foundation laid by the Code Institute's Moments template project.
- GPT-3.5 Assistant - Alex: Special thanks for providing valuable assistance throughout the project, including testing of code for potential errors.

## THIS API IS USED ON A MAIN FORUM PROJECT , WHICH CAN BE ACCESSED HERE - [FORUM](https://watchforumkarlo-1fa8fac8032c.herokuapp.com/)
Watch forum Repo [Can be accesed here](https://github.com/Karlox01/WatchForum)

Happy coding!

