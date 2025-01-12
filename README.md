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


## Validation

### PEP8 Validation
[PEP8](http://pep8online.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.

## Testing

Comprehensive testing was conducted to ensure the robustness and reliability of FitShare's functionality. The testing process included both manual and automated approaches to validate the application’s features and user stories.

---

### Manual Testing of User Stories

The manual testing focused on verifying key functionalities of the application against the defined user stories. Each feature was rigorously tested for expected outcomes and edge cases.

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User Management | Create, update, and delete users | Admin can manage user accounts seamlessly | Works as expected
User Permissions | Modify user permissions | Admin can update user roles and permissions | Works as expected
Profile Management | Create, update, and delete profiles | Users can manage their profiles | Works as expected
Post Management | Create, update, and delete posts | Users can manage posts | Works as expected
Comment Management | Create, update, and delete comments | Users can manage comments on posts | Works as expected
Likes | Add and remove likes | Users can like or unlike posts | Works as expected
Followers | Follow and unfollow users | Users can follow or unfollow other users | Works as expected

- **Authentication:** Only logged-in users can create, update, or delete posts, comments, likes, or follow/unfollow users.  
- **Authorization:** Users can only modify or delete their own content, maintaining user privacy and data security.

---

<details><summary><strong>Screenshots: User Management</strong></summary>
    <details><summary>Create User</summary>
    <img src="docs/testing/user-create-test.png" alt="Create user test screenshot">
    </details>
    <details><summary>New Test User</summary>
    <img src="docs/testing/test-user.png" alt="New Test User">
    </details>
    <details><summary>New Test User Profile</summary>
    <img src="docs/testing/test-user-profile.png" alt="New Test User Profile">
    </details>
    <details><summary>Change User Permissions</summary>
    <img src="docs/testing/user-change-permissions-test.png" alt="Change user permissions screenshot">
    </details>
</details>

<details><summary><strong>Screenshots: Profile Management</strong></summary>
    <details><summary>Update Profile</summary>
    <img src="docs/testing/profile-update-test.png" alt="Update profile screenshot">
    </details>
    <details><summary>Delete Profile 1.1</summary>
    <img src="docs/testing/profile-delete-test1.1.png" alt="Delete profile screenshot">
    </details>
        <details><summary>Delete Profile 1.2</summary>
    <img src="docs/testing/profile-delete-test1.2.png" alt="Delete profile screenshot">
    </details>
</details>

<details><summary><strong>Screenshots: Post Management</strong></summary>
    <details><summary>Create Post</summary>
    <img src="docs/testing/post-create-test.png" alt="Create post screenshot">
    </details>
    <details><summary>Update Post</summary>
    <img src="docs/testing/post-update-test.png" alt="Update post screenshot">
    </details>
    <details><summary>Delete Post 1.1</summary>
    <img src="docs/testing/post-delete-test1.1.png" alt="Delete post screenshot">
    </details>
        <details><summary>Delete Post 1.2</summary>
    <img src="docs/testing/post-delete-test1.2.png" alt="Delete post screenshot">
    </details>
</details>

<details><summary><strong>Screenshots: Comment Management</strong></summary>
    <details><summary>Create Comment</summary>
    <img src="docs/testing/comment-create-test.png" alt="Create comment screenshot">
    </details>
    <details><summary>Update Comment</summary>
    <img src="docs/testing/comment-update-test.png" alt="Update comment screenshot">
    </details>
    <details><summary>Delete Comment 1.1</summary>
    <img src="docs/testing/comment-delete-test1.1.png" alt="Delete comment screenshot">
    </details>
    <details><summary>Delete Comment 1.2</summary>
    <img src="docs/testing/comment-delete-test1.2.png" alt="Delete comment screenshot">
    </details>
</details>

<details><summary><strong>Screenshots: Likes</strong></summary>
    <details><summary>Add Like</summary>
    <img src="docs/testing/like-create-test.png" alt="Add like screenshot">
    </details>
    <details><summary>Remove Like 1.1</summary>
    <img src="docs/testing/like-delete-test1.1.png" alt="Remove like screenshot">
    </details>
    <details><summary>Remove Like 1.2</summary>
    <img src="docs/testing/like-delete-test1.2.png" alt="Remove like screenshot">
    </details>
</details>

<details><summary><strong>Screenshots: Followers</strong></summary>
    <details><summary>Follow User</summary>
    <img src="docs/testing/follower-create-test.png" alt="Follow user screenshot">
    </details>
    <details><summary>Unfollow User 1.1</summary>
    <img src="docs/testing/follower-delete-test1.1.png" alt="Unfollow user screenshot">
    </details>
    <details><summary>Unfollow User 1.2</summary>
    <img src="docs/testing/follower-delete-test1.2.png" alt="Unfollow user screenshot">
    </details>
</details>

---

### Summary

The testing phase confirmed that the FitShare application meets all functional requirements and performs reliably across different scenarios. Both manual and automated tests have validated the robustness of the backend API, ensuring a secure and seamless user experience.

##### Back to [top](#table-of-contents)


## Credits

### Code

This project was heavily inspired by the Code Institute's Django REST API walkthrough project, ['Moments'](https://github.com/Code-Institute-Solutions/drf-api).

##### Back to [top](#table-of-contents)
