Fitshare API in DRF
Developer: Mohamed Abdillahi

💻 Live link

This repository contains the API set up using Django REST Framework for the Fitshare front-end application, a platform for gym enthusiasts to share and explore gyms through posts, likes, and follows. (repository here and live website here)

 - Table of Contents
 - User Stories
 - Database
 - Technologies Used
 - Validation
 - Testing
 - Credits

User Stories

 - The back-end section of the project focuses on its administration side and covers one user story:

As an admin, I want to be able to create, edit, and delete users, posts, comments, and likes, so that I can maintain control over the content of the platform and remove any inappropriate material.

Database

The following models were created to represent the database model structure of the application:





User Model

The User model contains information about the user and is part of the Django allauth library.

 - One-to-one relation with the Profile model via the owner field.
 - ForeignKey relation with the Follower model via the owner and followed fields.
 - ForeignKey relation with the Post model via the owner field.
 - ForeignKey relation with the Comment model via the owner field.
 - ForeignKey relation with the Like model via the owner field.

Profile Model

The Profile model contains the following fields: owner, name, description, created_on, updated_on, and image.

 - One-to-one relation between the owner field and the User model's id field.

Post Model

The Post model contains the following fields: owner, created_on, updated_on, title, description, category, and image.

 - ForeignKey relation with the Comment model via the post field.
 - ForeignKey relation with the Like model via the post field.

Follower Model

The Follower model contains the following fields: owner, followed, and created_on.

 - ForeignKey relation between the owner field and the User model's id field.
 - ForeignKey relation between the followed field and the User model's id field.

Comment Model

The Comment model contains the following fields: owner, post, created_on, updated_on, and content.

 - ForeignKey relation between the owner field and the User model's id field.
 - ForeignKey relation between the post field and the Post model's id field.

Like Model

The Like model contains the following fields: owner, post, and created_on.

 - ForeignKey relation between the owner field and the User model's id field.
 - ForeignKey relation between the post field and the Post model's id field.