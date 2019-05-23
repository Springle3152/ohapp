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

## Installation

Install Git. [Here](https://github.com/DHRI-Curriculum/git) are some instructions on how to install and use Git

Install Python 3. [Here](https://www.python.org/downloads/) to download and install Python

## Procedure

First, go into your command line and change directory into Desktop. 
```
$ cd Desktop/
```
Create a folder called "projects." Change directory into projects and create a folder called "Ohapp." This is where you will put your cloned app.
```
$ mkdir projects
$ cd projects
$ mkdir ohapp
$ cd ohapp
```
Type "pwd" (which stands for print working directory) to make sure you are in the ohapp folder.
```
$ pwd
User/username/Desktop/projects/ohapp
```
Create a virtual envirnoment by running the venv package
```
$ python3 -m venv venv
```
If you are using Windows, You might have to use Pip to install the venv package. If so, type
```
$ pip install virtualenv
$ virtualenv venv
```
Activate the virtual environment. If you are using Windows, type
```
$ source venv\Scripts\activate
```
On a Mac, type
```
$ source venv\bin\activate
```
You will now see (venv) in front of the directory location in the command prompt. This is how you know you are in the virtual environment. 

Clone the Ohapp repository from Github. Look again at this [tutorial](https://github.com/DHRI-Curriculum/git) for instructions on how to clone. Once you have cloned, the files will be in the ohapp folder on your Desktop. 

Run the app by typing
```
(venv) $ python ohapp.py
```
Running on http:127.0.0.1:5000

This means your enviroment is running and accessible through your local host. Leave your command prompt open and then go to this link in a web browser: http://127.0.0.1:5000/

Do not close the command prompt window, it is running from there!

To stop running the app, type ctr+c. To get out of your virtual environment, type deactivate. 

# Adding Interviews

To add the transcript of an interview to Ohapp, first click on "Add New Interview" at the bottom of the landing page. You will be redirected to the Add new interview form. 

## Register the new interview

In the Add new interview form, enter the name of the interviewee, the email of the interviewee and a password, and click on submit. You will be redirected back to the Add page. Type the name of interviewee and password that you just registered to access your new interview Add transcript page.

## Add the transcript to the database

Paste or type the transcript of your interview into the rather small box and click submit. You can paste up to 10,000 characters as many times as you like. The transcript will appear below the box as you add it. At the same time, it is being automatically saved in the app SQLite database.

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

If you want to modify this app and use it for another project, you can change most of the language that users will see on the front end in the HTML files in app/templates/ and also in app/routes.py, app/models.py, and app.forms.py, as well as other modules. Just be careful what you change (only change words in quotation marks and not all of these can be changed) and keep track of what you change so that you can go back, as you will probably break the code a whole bunch of times. 

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
