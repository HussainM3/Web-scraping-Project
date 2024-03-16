# Web-scraping-Project

- Hussain Muhammed [hussainmohd2003@outlook.com]

## Description

- Phone plan and computer web scraping project
- Uses Python and Selenium web scraping tool to scrape websites and capture info on phone plans and computers
- Displays info first in separate text file then uses HTML and CSS files to publish on website
- View website at https://hussainm3.github.io/Web-scraping-Project/ [Web-scraping-Project](https://hussainm3.github.io/Web-scraping-Project/)

## How to Run 

- Install Selenium using pip install selenium
- Run the PlansWebScraper.py file to scrape phone plans and computers from websites
    - This will create a text file with the scraped info
- Open a server and run the index.html file to view the website

## Bugs

- Deals with the website not loading properly as text file not uploaded on server 
    - resolved! parseData function was being called twice, erasing data from first call
- Constantly need to check and re-update scraper as websites change their layout

## Roadmap of future improvements

- Add more websites to scrape from
- Add more info to scrape from websites
- Add more HTML, CSS and JavaScript to make website look better
- Configure scraper python file so data paths are updated automatically or don't need to be regularly updated
