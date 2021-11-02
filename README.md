# YouTube-scraper
This tool enables its users to extract public data from YouTube channels and calculate, through a strictly defined procedure, metrics that are linked to the performance of both channels and videos using YouTube Data API.

The present tool is a key part of my dissertation with the title "From digital footprints to facts: mining social data for marketing practices", through which conclusions are drawn for the Greek YouTube community in three areas:

- The behavior and preferences of the Greek Instagram & YouTube community 
- The tactics whereby businesses operate on Instagram and YouTube
- The impact of COVID-19 virus on digital behavior of the users

## Useful Tools
- Python 3.6+
- Scrapy framework
- Web browser (recommended: Chrome or Mozilla browser)
- YouTube Data API
- MongoDB

## Description
### Setting up our Scrapy spider
1. To install Scrapy simply enter the command *"pip install scrapy"* in the command line
2. Navigate to your project folder Scrapy automatically creates and run the “startproject” command along with the project name (“instascraper” in this case) and Scrapy will build a web scraping project folder for you, with everything already set up. So enter the commands in the order shown below:  
    ```
    scrapy startproject youtubescraper
    cd youtubescraper
    scrapy genspider youtube youtube.com
    ```
### Structure of project folder
Once we have entered the above commands, Scrapy spider templates are set up. It should be noted that in this case we have two additional files:
- the *"resources"* folder
  > created to store files that contain important data for the scraping mechanism, such as names of Instagram profiles
- the *"tools"* folder
  > created to store files that contain usually used functions, such as functions that carry out the communication with the database
### Important note 
The provided web scraper reads as input usernames of Instagram users from:
- a database collection
- a JSON file
  > located in the "resources" folder
### Selection criteria for Instagram accounts 
- the number of subscribers of each channe; must be greater than or equal to 5000 
- each channel need to be part of the Greek YouTube community 
- the number of videos during the year 2020 must be greater than or equal to 1
- this mechanism scrapes only the videos that were uploaded during the year 2020
- this mechanism uses multiple API keys in order to achieve a large number of daily requests within the shortest possible time
  > check below how to get a YouTube API key
### Collected fields 
Collected fields are classified into two sub-categories:
* Fields of a YouTube channel:
    * Channel title
    * Channel ID
    * Channel creation date
    * Total number of views
    * Number of subscribers
    * Number of videos
    * List of channel keywords
    * Owned by
      > It was manually populated, beacause Instagram does not provide this field
* Fields of a YouTube video:
    * Video ID
    * Video title
    * Upload date
    * Video duration
    * Number of Comments
    * Number of Views
    * Number of Likes
    * Number of Dislikes
    * Video category
    * List of video hashtags

### Important note 
In order to handle YouTube Data API's tactic that divides the videos of each channel at subsections videos, the collection of the fields mentioned above was completed via the following methods:
* parse()
    > Collects the general information of each channel and asks for the list of the uploaded videos by this channel
* parse_videos()
    > Iterates over the list and asks for the available information about each video
* parse_video_stats()
    > Collects the selected fields of each video 

As it was mentioned above, the mechanism uses multiple YouTube Data API keys that are handled with the following methods:
* get_active_API()
    > Selects an API key that has not surpassed its daily requests threshold
* handle_API_error()
    > Deactivates an API key that has surpassed its daily requests threshold and selects another that is available
## How to get a YouTube API key
1. Log in to Google Developers Console
2. Create a new project
3. On the new project dashboard, click Explore & Enable APIs.
4. In the library, navigate to YouTube Data API v3 under YouTube APIs
5. Enable the API
6. Create a credential
7. A screen will appear with the API key
8. Copy the API key 
9. Open the file *"APIkeys.json"*, located in the folder *"resources"*
10. Paste your API key
## How to use
1. Download project
2. Unzip 
3. Open the *"spiders"* folder and then open the file *"youtube_spider.py"*
4. Choose if you want to populate the list "channels_to_scrape" from file or database
5. Open the file *"pipelines.py"* and update the variables *"myclient"*, *"db"* and *"collection"*, according to the address and the name of your database
6. Go to the folder *"tools"* and open the file *"documents_finder.py"*, then update the variables *"myclient"*, *"db"* and *"collection"*, according to the address and the name of your database
7. Go to the folder *"tools"* and open the file *"documents_deleter.py"*, then update the variables *"myclient"*, *"db"* and *"collection"*, according to the address and the name of your database
8. Open the command line and go the the folder in which the project is located
9. Run the following command:
    ```
    scrapy crawl YouTubeSpider
    ```
