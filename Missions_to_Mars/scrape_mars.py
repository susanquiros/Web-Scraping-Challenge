#creating dependencies 
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
# import pymongo
# from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
from pprint import pprint as pp 

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
    news_dict = {'title': news, 'paragraph': paragraph} 
    data_dict['news']= news_dict
    #closing the browser 
    # browser.quit()   

    #JPL Mars space images
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #creating the path for the image
    image = browser.links.find_by_partial_text('FULL IMAGE').click()

    # to keep connection with the website
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    featured_image_url = url + soup.find('img',class_='fancybox-image')['src']
    print(f"Featured Image URL: {featured_image_url}")
    data_dict['images']= featured_image_url
    #closing the browser 
    # browser.quit()  

    #Mars facts
    #inserting the url
    url= 'https://galaxyfacts-mars.com/'
    browser.visit(url)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    mars_table= soup.find('table', class_="table table-striped")
    mars_table= pd.read_html(str(mars_table))[0]
    #mars_table   
    mars_df = mars_table.rename(columns={ 0: "Characteristics", 1: "Facts"})
    mars_df = mars_df.set_index('Characteristics') 
    #converting df to html
    mars_df_html= mars_df.to_html()
    data_dict['table'] = mars_df_html
    
    #Mars Hemispheres
    url= 'https://marshemispheres.com/'
    browser.visit(url)
    #looping to get the information 
    information = []

    #creating the loop to get the information for all of the pages
    for i in range (4):
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        links = browser.find_by_css('.description h3')
        links[i].click()
        title = browser.find_by_css('h2.title').text
        img_url = browser.find_link_by_text('Sample').first
        img_url = img_url['href']
        information.append({'title': title, 'img_url':img_url})
        print(title)
        print(img_url)
        browser.back()
    #data table 
    data_dict['hemispheres']= information
    print(data_dict)   

    return data_dict