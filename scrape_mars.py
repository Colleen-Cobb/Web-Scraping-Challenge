from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars news site 
    url = 'https://redplanetscience.com'
    browser.visit(url)
    mars_dict= {}

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Extract all the text elements
    # results =soup.find("div", class_="list_text")
    # print(results)

    # Get the title
    title= results.find("div", class_="content_title").text
    preview= results.find("div", class_="article_teaser_body").text
    print(title.text)

    # Get the preview
    # @TODO: YOUR CODE HERE!

    # BONUS: Find the src for the sloth image
    # @TODO: YOUR CODE HERE!

    # Store data in a dictionary
    # mars_data = {
    #     # "sloth_img": sloth_img,
    #     "min_temp": min_temp,
    #     "max_temp": max_temp
    # }

    # # Quite the browser after scraping
    # browser.quit()

    # # Return results
    # return costa_data

    mars_dict= {
        "Title": title,
        "Preview": preview
    }

    return mars_dict