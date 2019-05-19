# Oral History App
This is an application for collecting oral histories. An interviewer is asked to create an account for each interview they will upload, giving this account an interviewee name (in the code this is called the username), an email address and a password. An account is then created with a unique avatar. The interviewer, interviewee and anyone else who has the password is then able to log in and add the transcription of an interview, which the app stores in a database. The transcript is retrievable from the find interview page (coded as the login page) and the database is searchable from the command line. 

## Instructions
The app is fairly easy to use. Once an interview has been transcribed, an interviewer can create or log in to an interview account and paste the text of the transcript in order to have it stored in the database of the oral history app.

This page will show you how to

 - Install the oral history app on your local server
 - Add a new interview account to the database and create an interviewee profile with a brief abstract of the interview
 - Retrieve interview accounts on the web app
 - Consult the app database to get a list of all interviewees and posts attributed to these 
 - Remove interview accounts from the database
 - Change the name of the app and descriptive text on the app home page so that you can make different versions of this app for different projects.

## Getting Started
This app is coded with Python using the Flask framework. You will need to first install first Python and then Flask on your computer. 

## Installation
### Prerequisites

* git: https://git-scm.com/downloads
* Python 3: https://www.python.org/downloads/



>C:\> install python
>C:\> 
>```

### Procedure

* Open your command prompt and install virtualenv (a Python virtual enviroment package) using Python's pip tool:
```
$ pip install virtualenv
```
* from within a directory for projects, clone the Ohapp repository:
```
git clone https://github.com/ . . . . 
```
* change into the cloned directory, Ex. C:\Users\Username\ophapp:
```
$ cd C:\Users\Username\ohapp
```
* Create and load virtual environment in a subdirectory, for example we created one called "venv"
```
$ virtualenv venv
```
* Activate the virtual environment (it will say venv infront of the directory location on the command prompt, that is how you know you are in the virtual environment)
* If you are using Windows, type:
```
$ source venv\Scripts\activate
```
* On a Mac, type:
```
$ source venv\bin\activate
```
* Run the ohapp app:
```
(venv) $ python ohapp.py
```
Running on http:127.0.0.1:5000
```
This means your enviroment is running and accessible through your local host. Leave your command prompt open and then go to this link in a web browser:

http://127.0.0.1:5000/

!!!Do not close the command prompt window, it is running from there!!!

## Configure OAI Repository

From the Ohapp form:

- click
- click 
- click 

Error handling:

If an error occurs on the production version of the application, you will want to know right away. We have configured Flask to send us an email immediately after an error, with the stack trace of the error in the email body. As the app is configured, the email will go to one of the developers of this version of the oral history app. To change this email address, open config.py at the top level of the ohapp folder and change the email address in that module.

