from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd 
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
  # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape_info():
    # # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars news site 
    browser= init_browser()
    mars_dict={}
    url = 'https://redplanetscience.com'
    browser.visit(url)
    mars_dict= {}

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the title and preview
    title= soup.find("div", class_="content_title")[0].text
    preview= soup.find("div", class_="article_teaser_body")[0].text
    # print(title.text)
    # print(preview.text)

    # Mars temperature data to be scraped
    temp_url= 'https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html'
    browser.visit(temp_url)
    tables=pd.read_html(temp_url)
    mars_temp_df=tables[7]
    mars_temp_df.columns=["id", "terrestrial_date", "sol", "ls", "month", "min_temp", "pressure"]
    mars_html_table=mars_temp_df.to_html()
    mars_html_table.replace('\n', '')

    # Store data in a dictionary
    mars_data = {
        "title": title,
        "preview": preview,
        "temp_table": mars_html_table
    }

    # # Quite the browser after scraping
    browser.quit()



    return mars_data