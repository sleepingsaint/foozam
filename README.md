# foozam
shazam for food

## Setting Up

Install all the required dependencies in the requirements.txt

You can install using the below command.

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


To load more pictures by clicking __load more results__ pass the number of time using __-i__ or __--iter__ flag

```
python3 scrape.py -i 3 -s burger
```

above script will click on load more results for atmost 3 times (sometimes the results might be less and the load more results button may not be loaded like in final results page.)

* Default value for iter is 0