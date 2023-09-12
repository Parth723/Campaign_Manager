Project Name is a Django web application for Campaign manager which sends out blog posts to the subsribers for the campaign: Save the Soil initiative.

Table of Contents: 
Prerequisites
Installation
Usage
Features
Contributing
Connect

Prerequisites: Python (>= 3.6), Django: 4.25, Database system: SQLite

Installation: 
Clone the repository: Project folder -> Try_8

Install project dependencies: Provided in requirements.txt

Apply database migrations: python manage.py migrate

Create a superuser (admin) account: ->python manage.py createsuperuser

Run the development server: ->python manage.py runserver

You can now access the project at http://localhost:8000/ 

Usage:
The system can be utilized as a Campaign Manager, the "Join Us" page accepts the following values: 1) Name 2) E-mail address (in proper format) 3) Subscription to the blog (To be sent via email) 
You can add multiple campaigns, the users wishing to subscribe for the blogs will have the status(is_active) set to True and receive the blogs. The next page then asks for confirmation regarding subscription. Once accepted the system redirects to "Email_sent" page. There also exits a popup alert for successful registration.

Features:
Home page with slides
Join Us page: Along with formatting, option to opt-in for the blogs
Confirmation page and post submission page.
A "email_base" page which formats as per the details of the user.
Add multiple campaigns as per need.

Contributions are welcome! If you'd like to contribute to this projects.

Connect: Connect with me on LinkedIn via: www.linkedin.com/in/parth-belwate723

Please make sure to follow the code of conduct and the contribution guidelines.
