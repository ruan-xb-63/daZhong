# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import re
from itemadapter import is_item, ItemAdapter


class DazhongSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DazhongDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        pattern = re.compile("https://www.dianping.com/search/keyword/1/0_%E5%86%AC%E8%99%AB%E5%A4%8F%E8%8D%89")
        result = pattern.match(request.url)
        if result:
            request.headers['Referer'] = 'https://www.dianping.com/shanghai'
            request.headers["cookie"] = 'fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=175341d8405c8-014aa709cfa3f6-c781f38-144000-175341d8406c8; _lxsdk=175341d8405c8-014aa709cfa3f6-c781f38-144000-175341d8406c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1602897152; _hc.v=3f5ce10f-652c-6fd0-4e14-453b05d98b44.1602897152; s_ViewType=10; cy=1; cye=shanghai; dplet=aa6a6a8e0516745d172a982b99a45ba2; dper=d557e9d6b18eb101ec3037c04776371caf3d9e5a7c3be77cf5ef3b084f80aa9ffade57bb9cc5da027201492884db4d14a9be88593fa3435b74e7e2e111980ddc3e82bd697b61f752e53d04b8c8b968ada80da8fae03c8ba1cc7810b4d607b845; ll=7fd06e815b796be3df069dec7836c3df; ua=18779343660; ctu=74ce666787acc02145469f8dfe25145c70f7b3285dfc3eea39b05a484008e189; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1602901870; _lxsdk_s=175346512b5-b1c-bb2-250%7C%7C29'
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
