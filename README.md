# Web Scraping with Python
# [*Course Certificate*]()

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

### [3] Advanced Techniques:
### [4] Acting Human:
### [5] Conclusion: