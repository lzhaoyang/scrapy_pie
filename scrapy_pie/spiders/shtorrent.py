# -*- coding: utf-8 -*-
import scrapy

# 对 https://www.sehuatang.org/forum-103-1.html
# 该网页的中文字幕种子下载，并将相关数据保存到数据库中
# 默认请求走了本地的shadowsocks代理
from scrapy_pie.configure import sht_headers
from scrapy_pie.items import ShtCategoryItem, ShtItemCountItem


class ShtorrentSpider(scrapy.Spider):
    name = 'shtorrent'
    allowed_domains = ['sehuatang.org']
    # 有时你填写http也可以返回正确的response
    # 但是最好写成和浏览器访问的一支
    # 要不然会报错：https://github.com/scrapy/scrapy/issues/3103
    start_urls = ['https://sehuatang.org/']

    # 是否需要爬去
    need_scrapy = True

    # 作品链接
    films_link_list = []

    def __init__(self):
        self.header = sht_headers

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.header)

    def parse(self, response):
        # 抽取出默认页的分类url
        all_tags_urls = response.xpath('//div[contains(@id,"category_")]')
        tags_urls_list = []
        for cat_url in all_tags_urls:
            # "//*[@id="category_1"]/table/tbody/tr[1]/td[1]/dl/dt/a"
            # 找到原创BT栏目
            if cat_url.xpath("@id").extract_first() == "category_1":
                tag_url = cat_url.xpath(".//*/dl/dt/a")
                for item_url in tag_url:
                    sht_category_item = ShtCategoryItem()
                    a_link_name = item_url.xpath(".//text()").extract_first()
                    a_link = self.start_urls[0] + item_url.xpath(".//@href").extract_first()
                    sht_category_item["category_name"] = a_link_name
                    sht_category_item["category_url"] = a_link

                    tags_urls_list.append([a_link_name, a_link])
                    yield sht_category_item
                    # print(a_link)
                    # print(a_link_name)
                    # print("--------------")
        # yield tags_urls_list

        # 高清中文字幕
        for item in tags_urls_list:
            if item[0] == "高清中文字幕":
                yield scrapy.Request(item[1], callback=self.parse_item_page, headers=self.header)

    def parse_item_page(self, response):
        """
        解析具体的分类url
        :param response:
        :return:
        """
        print(f"进入解析{response}")
        # 解析有多少部 决定要不要更新数据库
        '//*[@id="thread_types"]/li[2]/a'
        '//*[@id="thread_types"]/li[3]/a'
        code_item_kind = response.xpath('//*[@id="thread_types"]/li[2]/a/text()').extract_first()
        code_item_count = response.xpath('//*[@id="thread_types"]/li[2]/a/span/text()').extract_first()

        nocode_item_kind = response.xpath('//*[@id="thread_types"]/li[3]/a/text()').extract_first()
        nocode_item_count = response.xpath('//*[@id="thread_types"]/li[3]/a/span/text()').extract_first()

        shtitemcountitem = ShtItemCountItem()
        shtitemcountitem["code_kind"] = code_item_kind
        shtitemcountitem["code_count"] = code_item_count
        shtitemcountitem["nocode_kind"] = nocode_item_kind
        shtitemcountitem["nocode_count"] = nocode_item_count
        shtitemcountitem["total"] = int(code_item_count) + int(nocode_item_count)
        yield shtitemcountitem
        # print(f"{code_item_kind}:{code_item_count}/{nocode_item_kind}:{nocode_item_count}")

        page_list = response.xpath('//*[@id="fd_page_bottom"]/div/a/@href').extract()
        # 'ml'
        page_prefix = page_list[0].split(".")[0][:-2]
        page_num_max = max([int(i.split("-")[2].split(".")[0]) for i in page_list])
        page_list_url = [self.start_urls[0] + page_prefix + "-" + str(i) + ".html" for i in range(1, page_num_max + 1)]
        if not self.need_scrapy:
            print("哈哈哈哈哈，不需要爬去数据了")
        else:
            print(page_list_url)
            for page in page_list_url:
                # dont_filter=True 不要过滤重复的请求
                yield scrapy.Request(page, callback=self.parse_item_film, headers=self.header, dont_filter=True)

    def parse_item_film(self, response):
        """
        抽取每一页的film 列表url，然后依次访问
        :param response:
        :return:
        """
        # ['thread-71669-1-3.html', 'thread-71668-1-3.html', 'thread-71667-1-3.html', ]
        # '//*[@id="normalthread_74503"]/tr/th/time'
        update_date = response.xpath('//tbody[contains(@id,"normalthread_")]/tr/th/time/text()').extract()
        item_url = response.xpath('//tbody[contains(@id,"normalthread_")]/tr/th/a[2]/@href').extract()
        item_name = response.xpath('//tbody[contains(@id,"normalthread_")]/tr/th/a[2]/text()').extract()

        # ['https://sehuatang.org/thread-71669-1-3.html', ]
        per_item_urls = [self.start_urls[0] + i for i in item_url]

        # print(f"date: {update_date}")
        # print(f"title: {item_url}")
        # print(f"数量：{len(item_url)}")
        # print(f"name: {item_name}")

        # 对每一页的film url请求
        for url in per_item_urls:
            yield scrapy.Request(url, callback=self.parse_file_page, headers=self.header, dont_filter=True)

    def parse_file_page(self, response):
        """
        解析作品页面
        :param response:
        :return:
        """
        print("----->ok")
        pass
