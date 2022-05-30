![image](media/mock-up-site.png)

## About CrossfitBox.48

This is a blog owns by the owner of CrossfitBox.48. 

**Contents**

1. Contents
2. UX
3. Wireframes
4. User Stories
5. Information Architecture
    -[Blog App]
6. Techonologies
7. Features
8. Testing
9. Deployment
10. Credits
11. Acknoledgements

------

## UX

**Project Goals**

The purpose of having this blog site, is to allowe the owner of CrossfitBox.48 to promote crossfit as an sports, to share the passion and knowledges of this sports. 
To promote it as a business.
To create community for people into this sports, and willing to strengthen the skills.
And to have her members and future members to see the news of the box, and the coming daily WOD arrangements.

**Site Owner Goals** 
- Provide the users with clear WOD plan;
- Connect with users by letting them add comments to the posts;
- Promote more events in order to get more business.

**Site User Goals** 
- View the daily wod plan;
- View the news of the box;
- Ability to create an account;
- Ability to interact with posts and other member's comments.

**User Story** 
- As user, I am able to access the site on computer and mobile, tablet;
- As a user, I am able to easily navigate through the website without confusions;
- As a user, I am able to read a post list from the main page;
- As a user, I am able to access to the post detail page;
- As a user, I am able to comment the post, like the post, or unlike the post;
- As a user, I am able to edit my profile page;
- As a superuser/site owner, I am able to approve or disapprove member's comments;
- As a superuser/site owner, I am able to add or delete memebers from the admin panel;
- As a superuser/site owner, I am able to post articles;
- As a superuser/site owner, I am able to put my articles as draft, to finish the editing later;
- As a superuser/site owner, I am able to delete my post from the admin panel.

##Design Choices
**Fonts**
- ```font-family: Lato, sans-serif;```

**Colors**

![image](media/E84610.png)


**Images**
- The media files are all stores in the Cloudinary
- The blog post files are from Google, and I have used Canva to edit the photo and upload to the post.

##Wireframes


##Technologies

##Languages
- HTML
- CSS
- JavaScript
- Python

**Libraries & Frameworks**
- Django
- Django Crispy Forms
- Bootstrap
- Psycopg2
- Gunicorn

**Tools**
- pip
- git
- github
- heroku
- gitpod
- cloudinary

##Features
The website is designed using our application: Blog

**Implemented Features**

**User Account**
- The users can create an account where they can store account infromation 
    such as first name, last name, emails, and edit their details.

**Super User**
- The super user can add capabilities to the users in the database.

**Future features**
- A frontend admin page for ease of access.

## Testing

## Deployment
CrossfitBox48 project was deployed using the git, github. It is hosted on the Heroku,and all media files are stored on cloudinary.

Before deploying the application, install the following:
- Python 3
- Pip
- Git
- Heroku CLI

**Local Deployment**
1. From the applications repository, clickes the code button, and opens in gitpod.
2. The requirements.txt is already existing since the project is based on code institute full template.
3. Create env.py file to hold environmental variables in the root level:
```
    os.environ["DATABASE_URL"] = "postgres://yrrygwxkpmpiil:ea496797147b0eeb571e0960e74629605c2272932896296a7e3108538fad2641@ec2-63-35-156-160.eu-west-1.compute.amazonaws.com:5432/dcsfpvvm2q0qiq"
    os.environ["SECRET_KEY"] = "randomSecretKey8348"
    os.environ["CLOUDINARY_URL"] = "cloudinary://743457893464493:56OzhZV1jmcyojn-Z0nxQyJDljQ@carriecloud8348"
```
4. When add changes to models, need to migrate the models to the database:
```python manage.py makemigrations
    python manage.py migrate
```
5. Create a superuser to access the admin panel using the following command:
```python manage.py createsuperuser
```
6. After login to the admin panel, you can add data to be displayed in app for Blog app if required. Refer to database modeling.

7. To initiate the application, type the command python manage.py runserver in terminal. The application is now available in browser at the address:
``` 
http://localhoset:8000 
```

**Deployment to Heroku**

To deploy the app to Heroku, use the following steps:

1. Ensure you have the following dependancies installed in your app, such as PostgressSQL driver for Python, WSHI HTTP Server and dj database url that connects the the app with the database:

```
pip3 install psycopg2-binary

pip3 install install gunicorn

pip3 install dj_database_url
```
2. To update requirements.txt file containing all of the dependancies:
```pip3 freeze > requirements.txt```
3. Create a Procfile that contains the following: ```web: gunicorn main.wsgi:application```
4. Push these newly created files to repository master.
5. Login to Heroku and create a new app.
6. Since the recent incapable of depolying automatically on heroku by clicking buttons, the manual deploy from terminal is required:
- In terminal type:
    ```pip3 install heroku ```
- After it's done, then type login demand:
    ```heroku login -i```
- After typing the correct user name and password, logged in successfully from terminal, type:
   ```heroku git remote -a -the app name- ```
- When it is successfully remoted, in terminal type push command:
   ```git push heroku main```
- Once it's done, the messange in terminal shows deploy successed, open heroku app page, 
    on the menu bar right side, click three dots button, and choose "Restart all dynos".
- In Heroku Resources tab, navigate to Add-Ons section and search for Heroku Postgres. 
- In settings tab, navigate to Reveal Config Vars and add the following variables:
 ```
 KEY            	     VALUE                          
 CLOUDINARY_URL        	YOUR_CLOUDINARY_URL                
 DATABASE_URL          	YOUR_DATABASE_URL                                   
 SECRET_KEY            	YOUR_DJANGO_SECRET_KEY            

  ```           
7. In settings.py in your IDE, temporarily comment out the database and use below code instead (make sure you do not commit!):
```
DATABASES = {
        'default': dj_database_url.parse('POSTGRESS URL')
    }
```
8. In terminal, migrate the models to create the Postgress database using the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

9. Create a superuser to access the admin panel using the following command:
```
python manage.py createsuperuser
```
10. Then follow the instructions to create the superuser.
11. After login to the admin panel, you can add data to be displayed in your app for GIFTS app if required.
12. Remove the temporary database from settings.py and uncomment the original code, then push the code to origin.
13. Deploy to Heroku from terminal.


##Credits
Images
- Images in the post are found on goole, they are all have free-use right, and I have re-modify the on canva.com

Code Idea
- It is based on the Code Institute "I think I therefore blog" project

##Acknowledgements

Site Creator:
Qian Yilu, under the help of mentor Ronan McClelland, and tutor from Code Institute Ger, Christine, Sean 



