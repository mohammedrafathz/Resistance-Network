# Resistance-Network

1. Clone the git-hub repo:- git clone https://github.com/risky-boy/Resistance-Network.git

2. Setting up MySQL DB
	-> Install MySQL server:- $ sudo apt-get install mysql-server

	-> Secure server installation:- $ sudo mysql_secure_installation

	-> Install MySQL client:- $ sudo apt-get install libmysqlclient-dev

	-> Create a new mysql user with username= djangouser & password = Django@123

3. Setting up python environment
	-> Install python virtual environment(I user python 2.7):- $ sudo apt-get install python-virtualenv
								   $ sudo pip install virtualenv

	-> Create a new virtual environment:- cd Resistance-Network
					      virtualenv venv

	-> Activate virtual environment:- source vene/bin/activate

	-> Install django, rest framework, cors headers, Mysql for python & mysqlclient:- pip install django djangorestframework 		    django-cors-headers MySQL-python mysqlclient

	-> Make database migrations:- python manage.py makemigrations
				      python manage.py migrate

	   NOTE:- "django.db.utils.OperationalError: (1049, "Unknown database 'ResistanceNetwork'")" Incase you see this error, Create the 			   database manually using mysql work bench or using terminal

	-> Run the server:- cd server
			    python manage.py runserver

4. Running client
	-> I used visual studio code's live server extension to work on client on port 5500 you can directly access the app by running 
	   (your local path)/Resistance-Network/client/signup.html file.
