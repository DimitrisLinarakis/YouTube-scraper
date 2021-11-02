from scrapy import Spider, Request
import re
from ..items import ChannelItem

class StatsvideoSpider(Spider):

    name = 'StatsvideoSpider'
    allowed_domains = ['stats.video']
    website_url: str = 'https://stats.video/top/most-subscribed/youtube-channels/greece/of-all-time'
    visited_links = {"of-all-time"}

    def start_requests(self):
        yield Request(self.website_url,callback=self.parse)

    def parse(self,response):
        array_fields = response.xpath("//tbody//tr").extract()
        for field in array_fields:
            profile_link=re.findall(r'(?<=\<a class=\"channelLink\" href=\").*?(?=\">)', field)[0]

            pattern ="<a class=\"channelLink\" href=\""+profile_link+"\">(.*?)</a>"
            channel_name = re.findall(pattern, field)[-1]
            subscriber_count = int(re.findall(r'(?<=title=\"Subscribers\"\>\</i\>\n                ).*?(?=</button\>)', field)[0].replace(',', ''))
            if subscriber_count>5000:
                yield Request(f"https://stats.video{profile_link}",callback=self.parse_profile,meta={"channel_name":channel_name})

        page_links=response.xpath("//a[@class='btn btn-danger purple m-1']//@href").extract()
        for link in page_links:
            pattern="[^/]+$"
            page_index=re.findall(pattern,str(link))[0]
            if not page_index in self.visited_links:
                self.visited_links.add(page_index)
                yield Request(f"{self.website_url}/page/{page_index}",callback=self.parse)
            
    def parse_profile(self,response):
        channel_id=response.xpath("//div[@data-original-title=\"YouTube Channel's ID\"]/text()").extract()[0].strip()
        channel_item=ChannelItem()
        channel_item["channel_id"]=channel_id
        channel_item["channel_name"]=response.meta["channel_name"]

        print(channel_id)
        print(response.meta["channel_name"])
        yield channel_item