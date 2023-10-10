import re
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup as BS
import hashlib
from scrapy.linkextractors import LinkExtractor
from ..items import Kennesaw_spiderItem

class KennesawSpider(CrawlSpider):
    name="kennesaw_spider"
    allowed_domains = ["kennesaw.edu"]
    start_urls = ["https://www.kennesaw.edu/", "https://www.kennesaw.edu/student-life/", "https://www.kennesaw.edu/athletics/"]

    rules = (
        Rule(LinkExtractor(allow_domains=allowed_domains), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        html_doc = response.text
        soup = BS(html_doc, 'html.parser')
        html_text = soup.get_text().lower()
        html_text = list(filter(None, re.split(r"\s+", html_text)))
        item = Kennesaw_spiderItem()

        item["pageid"] = hashlib.md5(bytes(response.url, "utf-8")).hexdigest()
        item["url"] = response.url
        item["title"] = None if response.xpath("count(head/title)") == 0 else response.xpath("head/title/text()").get()
        item["body"] = html_text
        item["emails"] = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_doc)

        yield item