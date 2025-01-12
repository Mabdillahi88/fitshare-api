# FitShare API in DRF

**Developer: Mohamed Abdillahi**

💻 [Live link](https://fitshareapi-b9588b2c11b9.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the FitShare front-end application ([repository here](https://github.com/yourgithub/fitshare) and [live website here](https://fitshare-d428ae7f1a9f.herokuapp.com/))

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories

The back-end section of the FitShare project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit, and delete users, posts, comments, and likes, so that I can have control over the content of the application and remove any inappropriate content.

#### User Model

- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field.
- ForeignKey relation with the Follower model owner and followed fields.
- ForeignKey relation with the Post model owner field.
- ForeignKey relation with the Comment model owner field.
- ForeignKey relation with the Like model owner field.

#### Profile Model

- The Profile model contains the following fields: `owner`, `name`, `content`, `created_at`, `updated_at`, and `image`.
- One-to-one relation between the `owner` field and the User model `id` field.
- Default profile image is used if no image is uploaded.

#### Post Model

- The Post model contains the following fields: `owner`, `created_at`, `updated_at`, `title`, `content`, `image`, and `image_filter`.
- ForeignKey relation with the Comment model `post` field.
- ForeignKey relation with the Like model `post` field.
- Includes options for image filters like `Hudson`, `Earlybird`, `Nashville`, and more.

#### Follower Model

- The Follower model contains the following fields: `owner`, `followed`, and `created_at`.
- ForeignKey relation between the `owner` field and the User model `id` field.
- ForeignKey relation between the `followed` field and the User model `id` field.
- Unique constraint ensures a user cannot follow the same user multiple times.

#### Comment Model

- The Comment model contains the following fields: `owner`, `post`, `created_at`, `updated_at`, and `content`.
- ForeignKey relation between the `owner` field and the User model `id` field.
- ForeignKey relation between the `post` field and the Post model `id` field.

#### Like Model

- The Like model contains the following fields: `owner`, `post`, and `created_at`.
- ForeignKey relation between the `owner` field and the User model `id` field.
- ForeignKey relation between the `post` field and the Post model `id` field.
- Unique constraint ensures a user cannot like the same post multiple times.

##### Back to [top](#table-of-contents)


## Database

The following models were created to represent the database model structure of the application:
<img src="docs/readme/fitshare-database-diagram.png">


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing.
- [Cloudinary](https://cloudinary.com/) to store static files.
- [Coverage](https://coverage.readthedocs.io/en/6.4.4/) used to produce automated testing reports.
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram.
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub.
- [GitHub](https://github.com/) was used as a remote repository to store project code.
- [Gitpod](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site.
- [Render Platform](https://render.com) was used to deploy the project into a live environment.
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication.
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation.
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python.
- [PostgreSQL](https://www.postgresql.org/) – deployed project on Render uses a PostgreSQL database.

##### Back to [top](#table-of-contents)
