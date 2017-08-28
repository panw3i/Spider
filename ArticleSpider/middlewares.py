# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
from scrapy.http import HtmlResponse
import time

from .tools import IPManager


class ArticlespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware(object):
    """
    随机更换User_Agent
    """

    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()

        # 实例化一个fakeUserAgent对象
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    # 通过静态方法生成实例对象
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    # 闭包
    def process_request(self, request, spider):
        # 相当于访问 ua.random的属性
        def get_ua():
            return getattr(self.ua, self.ua_type)

        random_ua = get_ua()
        request.headers.setdefault('User-Agent', get_ua())


# class RandomProcyMiddleware(object):
#     """
#     动态设置IP代理
#     """
#
#     def process_request(self, request, spider):
#         random_ip = IPManager.IPManager.get_random_ip()
#         request.meta['proxy'] = random_ip

#
class JSPageMiddleware(object):
    """
    scrapy本身是异步的框架，但是这里chrome是同步的请求，性能会下降，所以要重写downloader
    """

    def process_request(self, request, spider):
        """
        具体哪些网站，哪些url需要使用动态加载，可以自己指定，这里只是做个示范
        """
        if spider.name == 'jobbole':
            self.browser = spider.browser
            self.browser.get(request.url)
            time.sleep(5)
            print(request.url)

            # 直接将 Response 返回 不交给下载器
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source)
