# myHealth
This guide is for user to install related environment and application on local machine to run the “myHealth” application. 
Python version: 3.7.5
Django version: 2.2.2

************************************************************************************************************************************
1.	Downloading Anaconda for Windows, macOS or Linux from:
https://www.anaconda.com/download/ 

2.	Click the “🔎” symbol (magnifying glass) at the bottom left-hand corner of your screen and type "anaconda" into the search box; then click on “Anaconda Prompt”. 
This will start up the Anaconda command prompt with the “base” environment.

3.	Clone the ella-boli/myHealth repository into your working directory.

4.	Initialize a python 3.7.5 (virtual) environment:
    $ conda create -n myhealth python=3.7.5
    
5.	Activate this environment:
    $ conda activate myhealth

6.	Install packages:
    $ pip install -r requirements.txt
    
7.	Go to the project directory /myhealth_project/
    $ cd ./myhealth_project/
    
8.	Initialize the database by $ python manage.py makemigrations 
    and then $ python manage.py migrate
    
9.	Populate data for users by $ python manage.py loaddata fixtures.json

10.	Run the server by $ python manage.py runserver 

11.	Now you can go to http://127.0.0.1:8000/.

Account Information:
User Role# patient	
           Email: patient@myhealth.com
           Password: bo2435638
User Role# doctor	
           Email: doctor@myhealth.com
           Password: bo2435638
User Role# administrator	
           Email: admin@myhealth.com
           Password: bo2435638           
           
Superuser for admin page:
           Email: 2435638L@student.gla.ac.uk
           Password: bo2435638 
