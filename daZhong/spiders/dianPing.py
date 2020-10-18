import scrapy
import redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from daZhong.items import DazhongItem


class DianpingSpider(CrawlSpider):
    name = 'dianPing'
    conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True, charset='UTF-8', encoding='UTF-8')
    start_urls = ['https://www.dianping.com/search/keyword/1/0_冬虫夏草']

    rules = (
        Rule(LinkExtractor(allow=r'/p\d'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        a_list = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a[1]/@href')
        for a in a_list:
            url = a.extract()
            yield scrapy.Request(url=url, callback=self.get_data)

    def get_data(self, response):
        """获取店铺名"""
        item = DazhongItem()
        title = response.xpath('//*[@id="body"]/div/div[1]/span/text()').extract()
        if title:
            item['title'] = title[0]
            yield item
        else:
            print("被要求验证了")
