Award
#### Author: [Rubyroy12](https://github.com/Rubyroy12)
## Description
This is an application that will allow users to read news basically from bitcoin, apple and tesla news. 
As a user of the web application you will be able to:
1. user authentication user registration and login.
2. User creating a pitch
3. Ability to comment to the created pitch


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source venv/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py server`
* Access the live site using the local host provided
  
## Specifications
* user Authentication
* crating a pitch
* 
*  
### Prerequisites
* python3.8
* virtual environment
* pip
#### Clone the Repo and rename it to suit your needs.
bash
git clone https://github.com/Rubyroy12/1minute-pitch.git

#### Initialize git and add the remote repository
bash
git init

bash
git remote add origin https://github.com/Rubyroy12/1minute-pitch.git

#### Create and activate the virtual environment
bash
python3.8-venv venv

bash
source venv/bin/activate

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
bash
python3.8 manage.py check
python manage.py makemigrations 
python3.8 manage.py sqlmigrate 
python3.8 manage.py migrate

#### Run the app
bash
python3.8 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000)
## Testing the Application
`python3.8 manager.py test`
## Built With
* [Python3.8](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS

### Licence
This project is under the  [MIT](LICENSE.md) licence