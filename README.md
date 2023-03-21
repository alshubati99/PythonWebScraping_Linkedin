# Web Scraping with Python
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/4a8188238fb768e3bd903b9aed275e602a05556b8c945d26b8bcccc34d724d31)
 ---
 
### [1] Basics of Web Scraping:
- What is Web Scraping: 
- known as Screen Scraping, Web Harvesting, Web Crawling, Spiders, Bot. 
    - An automated program that requests an HTML webpage or DOM meant for humans and parses the displayed data. 
    - A program that requests and parses any data on the web, especially in an unexpected way. 
- Types of Web Scraping:
    - A crawler that scans medical patient message boards looking for experiences with drug combinations.
    - Automated UI testing of a company's app. 
    - A bot that interacts with an airline flight search app, monitoring price changes.
    - Would a program that monitors prices changes using puplic API be considered web scraping? 
- Fields in Web Scrapig: 
    - Application security.
    - Networking.
    - Data science.
    - Natural language processing.
    - Law.
    - Data architecture.
> being able to look for a website and check your database.
- How the internet works?
- Web Scraping Error Causes: 
    - You made a programming mistake.
    - Your computer's Ethernet is unplugged.
    - Your router cannot reach the web server.
    - The web server is blocking your IP address.
    - There is some programming error on the web server.
    - And more.
> Real-World Addresses have Layers: Ryan Mitchel, 123 Main street, Apt 456, Medford, MA 02155. 
- Internet Layers: 
    1. Physical layer: Actual electrons on a wire - High/Low voltage.
    2. Data Link Layer: Frames MAC addresses and physical machines on a local network.
    3. Network Layer: Router to router, Creates network IP addresses.
    4. Transport Layer: Presistent communication channels - TCP, UDP, ports.
    5. Session Layer: Open, close, manage sessions - AppleTalk, SCP.
    6. Presentation Layer: String encoding, encryption/decryption - Object serialization, files, compression.
    7. Application Layer: HTTP, POST and GET requests, REST APIs
- Think about the Internet as: 
    - Each request goes through many layers of wrapping and unwrapping to get to its destination and back.
    - These requests do not require a web browser.
    - Requests can be examined, replicated, and saved.
- Hello World With Scrapy: 
    1. Install scrapy using `pip instal scrapy`
    2. run `scrapy start project [name of the folder] `. 
    3. Navigate to `spiders`
    4. run `scrapy genspider ietf pythonscraping.com`.
    5. run `scrapy runspider ietf.py`
- Challenge:
    - CSS selectors or xpath selectors.
    - //h1
    - //div/h1
    - //span[@class = "title"]
    - /text()
    - /@id
    - @content: to get the value.
### [2] Learning to Crawl:
- Crawling a website: 
> Wikipedia crawling. 
`\PythonWebScraping_Linkedin\article_scraper\article_scraper\spiders\wikipedia.py`
- Recording Data. 
    - Go to `items.py`
    - Item is type of content you are scraping.
    - Wikipedia is a source. 
    - To run the file: `scrapy runspider wikipedia.py -o article.csv -t csv -s CLOSESPIDER_PAGECOUNT=10`
        - `-s` stands for settings. 
    - To List all `cat articles.csv`
    - > you can have the file with `.json` or `.xml`
- Scrapy Settings File: 
    - You can add any custome settings to the `settings.py`
- Structure your scrapers for resusablility: 
    - `pipeline.py`.
- Challenge: 
    - scrape different data from different websites. 

### [3] Advanced Techniques:
- Submitting a form: 
    - https requests: GET, POST
    - `from scrapy.http import FormRequest`
- Finding and Using hidden APIs. 
- Siteemaps and robots.txt:
    - A text to any scraper of what they should and should not scrape from a website and it appears with any website.
    - To be able to follow the robots.txt rules **Automatically** activate the `ROBOTSTXT_OBEY = True` in `settings.py` of the project. 
- Challenge: 
    - Use CNN's sitemap and scrape data to database. 
    - Sitemap = `index.html`
    - Quick scraping. 
### [4] Acting Human:
- Logging in: 
    - `login.html`
- Browser automation with Selenium: 
    - First install scrapy-selenium library => `pip install scrapy-selenium`.
    - Second download browser driver file: https://chromedriver.chromium.org/downloads 
    - Then move this file somewhere memorable
- Interacting with a page: 
    - Use selenium functions. 
### [5] Conclusion:
- Check out: 
    1. [Python Automation and Testing](https://www.linkedin.com/learning/python-automation-and-testing) for more information about selenium. 
    2. [MySql Essential Training](https://www.linkedin.com/learning/mysql-essential-training-2)
    3. [Python Data Analysis](https://www.linkedin.com/learning/python-data-analysis-2)
    4. Web Scraping with Python book by Ryan Mitchell. 
    4. [Web Scraping With Python](https://www.linkedin.com/learning/web-scraping-with-python)