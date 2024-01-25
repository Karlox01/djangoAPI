# WatchForum API

Welcome to the WatchForum API, the backend component of the WatchForum web application. This Django-based API serves as the engine that powers discussions about watches and timepieces.

![Watches By Karl Logo](https://res.cloudinary.com/dzchfcdfl/image/upload/v1706223406/Starting_Page_gzhvqx.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Issues and Solutions](#issues-and-solutions)
- [Credits](#credits)

## Introduction

The WatchForum API is designed to facilitate meaningful discussions among watch enthusiasts. It powers the backend of the WatchForum web application, providing essential functionalities for user engagement, conversation management, and more.

## Features

- **User Authentication**: Secure user authentication system to enable personalized experiences.
- **Discussion Threads**: API endpoints to manage watch-related discussions and topics.
- **Messaging System**: Facilitates communication between users. (*Planned to be Incorporated. Late Winter 2024*)
- **User Dashboard**: Provides a dashboard for users to manage their discussions. (*To be expanded Spring 2024*)

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
  -Navigate to the project directory:
   cd watchforum-api
  -Install the required dependencies:
   pip install -r requirements.txt
  - Apply database migrations:
   python manage.py migrate
 - Run the development server:
   python manage.py runserver

## API Endpoints

Detailed documentation about the API endpoints can be found in the API Documentation file.

## Issues and Solutions

During the development process, several challenges were encountered, and some are ongoing. For detailed information, refer to the Issues and Solutions On the main React APP.

## Credits

- Code Institute's Moments Template Project: This project is inspired by the foundation laid by the Code Institute's Moments template project.
- GPT-3.5 Assistant - Alex: Special thanks for providing valuable assistance throughout the project, including testing of code for potential errors.

Happy coding!

