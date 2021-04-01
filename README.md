# foozam
shazam for food

## Setting Up

install all the required dependencies

```bash
pip3 install -r requirements.txt
```

## Scraping food images from google

run the __scrape.py__ along with keywords of images with __-s__ or __--search__ flag

```bash
python3 scrape.py -s burger 'hot dog'
```

after scraping all the images will be stored in images/<keyword> folder
* All the images scraped will be having a unique name

image/ <br />
|__ burger/ <br /> 
|__ hot_dog/
