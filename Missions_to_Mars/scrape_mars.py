#creating dependencies 
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

#defyning scrape function 
def scrape():
    url = 'https://redplanetscience.com'
    data_dict = {}
    #connecting to the browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
     # Retrieve all elements that contain book information
    news = soup.select_one('div.list_text')
    news= news.find('div', class_='content_title').get_text()
    paragraph= soup.select_one('div.list_text')
    paragraph= paragraph.find('div', class_='article_teaser_body').get_text()
    #printing the results
    print(f"News Title: {news}")
    print(f"News Paragraph: {paragraph}")  
    #closing the browser 
    browser.quit()   
    #JPL Mars space images
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

        

return data_dict