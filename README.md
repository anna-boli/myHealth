# myHealth

### Introduction
This is a website application to make a closer relationship among doctors and patients.


************************************************************************************************************************************
### Pythonanywhere Deployment
https://myhealth.pythonanywhere.com/

************************************************************************************************************************************

### Local Deployment
This guide is for user to install related environment and application on local machine to run the “MyHealth” application. 
#### Python version: 3.7.5
#### Django version: 2.2.2
************************************************************************************************************************************
#### Steps:
1.	Downloading Anaconda for Windows, macOS or Linux from:
https://www.anaconda.com/download/ 

2.	Click the “🔎” symbol (magnifying glass) at the bottom left-hand corner of your screen and type "anaconda" into the search box; then click on “Anaconda Prompt”. 
This will start up the Anaconda command prompt with the “base” environment.

3.	Clone the `ella-boli/myHealth` repository into your working directory.

4.	Initialize a python 3.7.5 (virtual) environment:
    `$ conda create -n myhealth python=3.7.5`
    
5.	Activate this environment:
   `$ conda activate myhealth`

6.	Install packages:
    `$ pip install -r requirements.txt`
    
7.	Go to the project directory /myhealth_project/
    `$ cd ./myhealth_project/`
    
8.	Initialize the database by `$ python manage.py makemigrations` 
    and then `$ python manage.py migrate`
    
9.	Populate data for users by `$ python manage.py loaddata fixtures.json`

10.	Run the server by `$ python manage.py runserver` 

11.	Now you can go to `http://127.0.0.1:8000/.`

### Account Inforamtion

- User Role: **Patient**
   -  Email: patient@myhealth.com
   -  Password: bo2435638
   
- User Role: **Doctor**
   -  Email: doctor@myhealth.com
   -  Password: bo2435638
  
- User Role: **Administrator**
   -  Email: admin@myhealth.com
   -  Password: bo2435638
