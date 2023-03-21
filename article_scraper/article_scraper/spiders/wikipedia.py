import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import linkExtractor
from article_scraper.items import Article



class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Kevin_Bacon']
    rules= [Rule(linkExtractor(allow=r'wiki/((?!:).)*$'), callback = 'parse_info', follow=True)]

    def parse(self, response):
        article = Article()
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        article['url'] = response.url
        article['lastupdated'] =  response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        
        # return {
        # 'title': response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get(),

        # 'url': response.url,
        # 'last_edited': response.xpath('//li[@id="footer-info-lastmod"]/text()').get() }