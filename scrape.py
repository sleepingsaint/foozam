# python script to scrape google images for given search
from selenium import webdriver
import requests
import uuid
import time
import os
import argparse
import base64
import re

BASE_URL = "https://www.google.com/search?tbm=isch&q="

def download_image(image, storage_path):
    image_url = image.get_attribute('src')

    if image_url is not None and "https" not in image_url:
        image_data = re.sub('^data:image/.+;base64,', '', image_url)
        image_content = base64.b64decode(image_data)
        extension = re.sub('^data:image/', '', image_url).split(';')[0]
        filename = storage_path + "/" + str(uuid.uuid1()) + "." + extension
        with open(filename, "wb") as f:
            f.write(image_content)
        print(filename)

        return
    
    image_url = image.get_attribute("data-src")
    
    if image_url is None:
        return

    req = requests.get(image_url)
    extension = req.headers["Content-Type"].split('/')[-1]
    filename = storage_path + "/" + str(uuid.uuid1()) + "." + extension
    with open(filename, "wb") as f:
        f.write(req.content)     
    print(filename)
    
def scrape(search_input, iter = 0):
    query = "+".join(search_input.split(" "))
    driver.get(BASE_URL + query)

    page_scroll_sleep = 2

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(page_scroll_sleep)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            if iter > 0:
                try:
                    element = driver.find_elements_by_class_name('mye4qd')
                    element[0].click()
                    time.sleep(page_scroll_sleep)
                    new_height = driver.execute_script("return document.body.scrollHeight")
                except:
                    break
            else:
                break

        last_height = new_height

    images = driver.find_elements_by_class_name('rg_i.Q4LuWd')

    storage_path = "images/" + "_".join(search_input.split(" "))
    
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    for img in images:
        download_image(img, storage_path)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="command line python script to scrape google images")
    arg_parser.add_argument("-s", "--search", type=str, nargs="*", help="python3 scrape.py -s coke 'hot dog'")
    arg_parser.add_argument("-i", "--iter", type=int, help="Number of time load more results to be clicked", default=2)
    args = arg_parser.parse_args()

    if len(args.search) == 0:
        quit()

    driver = webdriver.Firefox()
    for s in args.search:
        scrape(s, args.iter)