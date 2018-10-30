# Image classifier project

## 1. Installation
I use python 3.5 to create this project and the main libraries I used are:
- Flask==1.0.2
- gunicorn==19.9.0
- numpy==1.15.0
- pandas==0.23.4
- plotly==3.3.0

The detailed list is included in requirements.txt

## 2. Project Motivation

Project code is deployed an analysis result as a web application in the internet. The web application Programming is a project in Udacity Data Scientist Nanodegree program. In this project, I first develop code for an Chinese wine marketing analysis, then use bootstrap framework to design a web page and then plot the figure with plotly chart libary and flask, finally use heroku website to deploy the web application.

## 3. File Descriptions
webapp
     - data
     - nettravelapp
     - nettravelapp.py
       - app.run must be comment out before it is deployed on the website.
     - Procfile
     - readme.md
     - requirements.txt
     - wrangling_script
webapp\data
     - wine.csv
webapp\nettravelapp
     - routes.py
     - static
     - templates
     - __init__.py
webapp\nettravelapp\static
     - img
webapp\nettravelapp\static\img
     - githublogo.png
     - linkedinlogo.png
webapp\nettravelapp\templates
     - index.html
webapp\wrangling_scripts
     - wrangle_data.py

## 4. Summary

The analysis result is deployed in the heroku website . It can be visited as the following links:
 - https://nettravel-webapp.herokuapp.com/

## 5. Licensing, Author, Acknowledgements
This work is licensed under a [Creative Commons  Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
