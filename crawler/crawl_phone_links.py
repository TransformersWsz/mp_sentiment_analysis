#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 21:24
# @Author  : Swift
# @File    : crawl_phone_links.py
# @Brief   : 爬取手机链接

import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from crawler.util import get_logger
from crawler.setting import chrome_drive_path
from crawler.setting import url
from crawler.setting import num_mp
from crawler.setting import num_comment
from crawler.setting import exceed_time


class CrawlPhoneLinks(object):

    def __init__(self, url):
        self._url = url
        self._driver = webdriver.Chrome(chrome_drive_path)
        self._logger = get_logger()

    def judge_num_comment(self, comment):
        """
        对评论数量进行判断
        :param comment: element
        :return: True | False
        """
        num = comment.text
        if "+" in num:
            num = num[0:-1]
            if "万" in num:
                num = int(float(num[0:-1])*10000)
            else:
                num = int(num)
        else:
            num = int(num)
        return True if num >= num_comment else False

    def print_goods(self, title_link):
        for row in title_link:
            print(row[0], "--->", row[1])

    def save_results(self, results):
        with open("link.txt", "a", encoding="utf-8") as fw:
            for title, href in results:
                fw.write("{} ---> {}\n".format(title, href))

    def get_phone_links(self):
        self._driver.maximize_window()
        self._driver.get(self._url)
        results = []
        num = 0    # 已爬取的手机数量

        while num < num_mp:
            time.sleep(random.uniform(exceed_time[0], exceed_time[1]))
            mps = self._driver.find_elements_by_class_name("gl-item")
            title_link = []
            for phone in mps:
                comment = phone.find_element_by_class_name("comment")
                if self.judge_num_comment(comment):    # 评论数达到要求
                    p_img = phone.find_element_by_class_name("p-img")
                    href = p_img.find_element_by_tag_name("a").get_attribute("href")

                    p_name = phone.find_element_by_class_name("p-name")
                    title = p_name.find_element_by_tag_name("em").text

                    title_link.append((title, href))
                    num += 1

            print("当前网址为", "============", self._driver.current_url)
            self.print_goods(title_link)
            results += title_link
            try:
                self._driver.find_element_by_class_name("pn-next").click()
            except NoSuchElementException as nsee:
                self._logger.error("{} click next break".format(self._driver.current_url))
                break

        return results


if __name__ == "__main__":
    solution = CrawlPhoneLinks(url)
    solution.get_phone_links()
