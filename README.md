 **Project is a Django web application for "Campaign Manager" which sends out blog posts to the subsribers for the campaign: Save the Soil initiative.**

## Table of Contents: 
 - Prerequisites
 - Installation
 - Usage
 - Features
 - Contributing
 - Connect

## Prerequisites: 
 - Python (>= 3.6)
 - Django: 4.25
 - Database system: SQLite

## Installation: 
- Clone the repository: Project folder -> Try_8

- Install project dependencies: Provided in requirements.txt

- Apply database migrations: python manage.py migrate

- Create a superuser (admin) account: ->python manage.py createsuperuser

- Run the development server: ->python manage.py runserver

- You can now access the project at http://localhost:8000/ 

## Usage:
The system can be utilized as a Campaign Manager, the "Join Us" page accepts the following values: 
- Name 
- E-mail address (in proper format) 
- Subscription to the blog (To be sent via email) 
- You can add multiple campaigns, the users wishing to subscribe for the blogs will have the status(is_active) set to True and receive the blogs.
- The next page then asks for confirmation regarding subscription. Once accepted the system redirects to "Email_sent" page.
- There also exits a popup alert for successful registration.

## Features:
- Home page with slides

  ![slide_1](https://github.com/Parth723/Campaign_Manager/assets/55731159/89ff2ebd-2523-4924-9d63-912b873ca21d)

- Join Us page: Along with formatting, option to opt-in for the blogs
  
 ![Join_us_page](https://github.com/Parth723/Campaign_Manager/assets/55731159/d12d0ee0-7bd3-4abf-b0c6-bfa1c515ce36)

- Confirmation page and post submission page.

  ![confirmation](https://github.com/Parth723/Campaign_Manager/assets/55731159/4c067b65-4627-4d3a-b1b8-d2fef0d02149)

- A "email_base" page which formats as per the details of the user.
- Email sent acknowledgement page.

  ![2023-09-14 (1)](https://github.com/Parth723/Campaign_Manager/assets/55731159/4e547e8e-a9e9-401c-834b-58d5a1d3588f)

- The final email

  ![Email](https://github.com/Parth723/Campaign_Manager/assets/55731159/03c43528-f0be-4bea-9c9f-0536aa7fccc5)

  
- Add multiple campaigns as per need.

## Connect: 
- Connect with me on LinkedIn via: www.linkedin.com/in/parth-belwate723

Contributions are welcome! If you'd like to contribute to this projects.
Please make sure to follow the code of conduct and the contribution guidelines.

