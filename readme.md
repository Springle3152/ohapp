# Oral History App
Ohapp is an application for collecting oral histories. An interviewer is asked to create an account for each interview they will upload, giving this account an interviewee name, an email address and a password. An account is then created with a unique avatar. The interviewer, interviewee and anyone else who has the password can read and/or add an abstract and the transcript of an interview, which Ohapp stores in a database. The abstract and transcript are retrievable from the Find page and the database is searchable from the command line. In the future, Ohapp will also be able to house audio files and images associated with the interviews.

## Instructions
Ohapp is fairly easy to use. Once an interview has been transcribed, an interviewer can create or log in to an interview account and add a transcript by pasting or typing it into a form. The transcript is then stored in Ohapp's database.

This page will show you how to

 - Install Ohapp on your local server
 - Create a new interview account and an interviewee profile with a brief abstract of the interview
 - Add transcripts of interviews to interviewee accounts
 - Read interviews and abstracts
 - Consult the database to get a list of all interviewees, abstracts and transcripts attributed to these 
 - Change the name of and descriptive text on the app so as to make different versions of this app for different projects.

## Getting Started
Ohapp is coded with Python using the Flask framework. You will need to install Python and then, with Python, install Flask on your computer. You will also need to have Git installed so that you can clone Ohapp and download Ohapp onto your computer. 

## Install Python and Git

Install Git. [Here](https://github.com/DHRI-Curriculum/git/blob/master/sections/gitconfig.md) are instructions on how to install Git.

[Install Python 3](https://www.anaconda.com/distribution/#download-section) using Anaconda. Anaconda is hefty so this installation will take some time. We find that installing Anaconda is the best way to install Python.

**Note: when installing Anaconda, check the advanced options box to select "Add Anaconda to my PATH environment variable."** You may not be able to do this if you are not an administrator of your computer, in which case you can set the environment variable [manually](https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444).

## Set up Flask

First, go into your command line. On a Mac, go into the command line by typing "terminal" in Spotlight Search and hitting enter. In Windows, type "CMD" in the Windows search bar. Once you are in the command line, change directory into Desktop. 
```
$ cd Desktop/
```
Create a directory called "projects" (directories are folders; we will call them directories). Change directory into projects and create a directory called "ohapp." This is where you will put your cloned app.
```
$ mkdir projects
$ cd projects
```
To see where you are, type "pwd" in MacOS. You should be in the projects directory.
```
$ pwd
User/username/Desktop/projects
```
To see where you are in Windows, type "cd"
 ```
> cd
User/username/Desktop/projects
```
Now, create a virtual envirnoment by running the venv package
```
$ python3 -m venv venv
```
If you are using Windows, You might have to use Pip to install the venv package. If so, type
```
> pip install virtualenv
> virtualenv venv
```
Activate the virtual environment. On a Mac, type
```
$ source venv\bin\activate
```
If you are using Windows, type
```
> venv\Scripts\activate
```
You will now see (venv) in front of the directory location in the command prompt. This is how you know you are in the virtual environment. 

Clone the Ohapp repository from Github by clicking on the green Clone or Download button at the top of this screen, copying the URL in the box, and typing 
```
(venv) $ git clone https://github.com/Springle3152/ohapp.git
```
You might want to see this [tutorial](https://github.com/DHRI-Curriculum/git) for more instructions on how to clone. Once you have cloned, the files will be in a new directory called ohapp, in your projects directory. Go into the ohapp directory by typing
```
(venv) $ cd ohapp
```
Now you are in the directory that contains the app you just cloned. The next thing you need to do is install Flask. To do this, type
```
(venv) $ pip install flask
```
If you want to confirm that your virtual environment now has Flask installed, you can start the python interpreter by typing "python" and then the command to import Flask
```
(venv) $ python
>>> import flask
>>>
```
If this statement does not give you any errors, Flask is installed and ready to be used. 

## Extensions

Flask uses extensions to make the app work. You need to install five extensions before you can run the app. The **first** is to remember environment variables:
```
(venv) $ pip install python-dotenv
```
The **second** extension has to do with web forms. To install, type:
```
(venv) $ pip install flask-wtf
```
Install the **third** extension to make the database work:
```
(venv) $ pip install flask-sqlalchemy
```
The **fourth** extension you need to install is a Flask wrapper for Alembic, a database migration framework for SQLAlchemy:
```
(venv) $ pip install flask-migrate
```
Install the **fifth** extension which is for retrieving password-protected interviews:
```
(venv) $ pip install flask-login
```
**Now you have everything you need.** Run the app by typing
```
(venv) $ export FLASK_APP=ohapp
(venv) $ flask run
```
You should see this:
```
 * Serving Flask app "ohapp"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
[2019-05-23 05:33:02,434] INFO in __init__: Ohapp startup
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Running on http:127.0.0.1:5000
```
This means your enviroment is running and accessible through your local host. Leave your command window open and paste the url http://127.0.0.1:5000/ in your web browser.

**Do not close the command prompt window, the app is running from there!**

To stop running the app, type **CTRL+C** on MacOS or **CTRL+Z** on Windows. **To get out of your virtual environment, type **deactivate**. 

# Adding Interviews

To add the transcript of an interview, first click on "Add New Interview" at the bottom of the landing page. You will be redirected to the Add new interview form. 

## Register the new interview

In the Add new interview form, enter the name of the interviewee, the email of the interviewee and a password, and click on submit. You will be redirected back to the Add page. Type the name of interviewee and password that you just registered to access your new interview Add transcript page.

## Add the transcript to the database

Paste or type the transcript of your interview into the rather small box and click submit. You can paste up to 10,000 characters as many times as you like. The transcript will appear below the box as you add it. At the same time, it is being automatically saved in the database.

## Add an abstract

Click on the Read option at the top of the page. You will be redirected to the interview home page where you will see a unique avatar that has been generated for your interviewee. To add an abstract, click on edit profile. You will be redirected to a web form where you can type up to 3000 characters summarizing the story of your interviewee. Click on submit. Don't be surprised if it seems like nothing happened; you will not be redirected (we are working on adding a redirect to this page) but your abstract will be added to your interview Read page. 

## Search for other interviews

To retrieve other interviews you or someone else added to Ohapp, click on New Search. You will be redirected to the Add page. Click on Find at the top of the screen or stay in the Add page (the retrieve interview form is on both pages) and type in a different interviewee name and password. You will not be able to read interviews if you don't know the passwords associated with these. This is because we have not yet received Instituional Review Board approval to make interviews public. You can, however, get a list of interviews and email addresses from the database through the command line. You can also retrieve interview transcripts in the database through the command line.

# Search the database

To query the database, go into the ohapp directory in the command line, run Python (to run Python just type Python in the command line), and type the following commands to see the list of all interviewees (note that in the database the interviewees are called users):
```
>>> from app import db
>>> from app.models import User, Post

>>> users = User.query.all()
>>> users
[<User Irma Ostroff>, <User Sal Kove>]
>>> for u in users:
...     print(u.id, u.username)
...
1 Irma Ostroff
2 Sal Kove
```
Note that indents are important in the command line. In the above query the p in print has to be right below the u in user or the program won't do what you want. 

If you want to include the interviewees email addresses in the list, type the query as so:
```
>>> for u in users:
...     print(u.id, u.username, u.email)
... 
1 Irma Ostroff ostroff147@gmail.com
2 Sal Kove salkove@salkove.com
```
If you want to see information on only one interviewee, use that interviewee's user id as returned by the User.query.all command, to write a query like this:  
```
>>> u = User.query.get(2)
>>> u
<User Sal Kove>
```
If you want to retrieve interview transcripts from the Ohapp database through the command line, this is how you can retrieve all transcripts (note that in the database transcripts are called posts):
```
>>> from app import db
>>> from app.models import User, Post
>>> p = Post.query.all()
>>> p
[<Post I was born in Lithuania in 1952.>, <Post Thank you for the coffee (sound of coffee being poured). >, <Post Yes, I am comfortable, thank you. Unless you want to sit here? OK, I will stay here then. So. You say you want to know how I got where I am. Well, it is a long story. I will start at the beginning. I was born in Mott Haven in the Bronx on May first, 1948. My father was from West Virginia, and my mother was from Pennsylvania. We were poor but we got by until my father cut his foot at work (he was a builder) and the cut got infected, and it turned into gangrene. First, they cut his foot off, but the gangrene came back. Or maybe the doctors had not removed it all. It continued to spread, so they cut his whole leg off. >, <Post I came to the United States when I was five years old. My parents brought me here. They were running away from persecution in Lithuania. These were bad times for my family. When we came to New York we lived on the Lower East Side and things were much better. I remember that there was a Polish restaurant downstairs from where we lived, and I would sometimes do my homework there when my parents had not arrived home yet from work. There was a real community in our neighborhood. In some ways, we felt safe. In other ways not, because there was a lot of crime in this neighborhood back then. And in the seventies and eighties it got worse. I worked in a hardware store on Clinton and Rivington from 1970 to 1975, and we were robbed many times. We started keeping the door locked. When I was offered a job in a hardware store on 18th Street near Union Square I was happy to go. Union Square was very different back then. 
```
We are not sure at present how to retrieve all the transcripts of one interviewee (or all posts of one user) in the command line, but this is only because we have not had enough time to figure it out. The great thing is that all of the information you provided through the front end of the web app now resides in the app's database. 

## Error handling:

If an error occurs on the production version of the application, you will want to know right away. We have configured Flask to send us an email immediately after an error, with the stack trace of the error in the email body. As the app is configured, the email will go to one of the developers of this version of Ohapp. To change this email address, open config.py and change the email address in that module. There is also an error log built into Ohapp, located in Logs/ohapp.log

## Use of this app

If you want to modify this app and use it for another project, you can change most of the language that users will see on the front end in the HTML files in ohapp/app/templates/(filename).html and also in ohapp/app/routes.py, ohapp/app/models.py, and ohapp/app/forms.py, as well as other modules. Just be careful what you change (only change words in quotation marks and not all of these can be changed) and keep track of what you change so that you can go back, as you will probably break the code a whole bunch of times. The text editor we used to develop this app is VS Code, which you can install from your Anaconda navigator. We recommend this text editor. To open a file in the text editor from the command line, type 
```
(venv) $ code <name of file>
```
## License

Ohapp is licensed under the GNU General Public License, a free, copyleft license for software and other kinds of works. 

    This file is part of Ohapp.

    Ohapp is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Ohapp is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Ohapp.  If not, see <https://www.gnu.org/licenses/>.
