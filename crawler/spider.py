import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://list.jd.com/list.html?cat=9987,653,655&ev=exprice%5FM1700L2799&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
num_mp = 100
low_price = 1700
high_price = 2799
num_comment = 10000
num_comment_to_crawl = 2000


class Solution(object):
    def __init__(self):
        self._driver = webdriver.Chrome()

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

    def get_goods_link(self):
        """爬取商品链接"""
        self._driver.get(url)

        results = []
        nums = 0    # 已爬取的数量
        while nums < 100:
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
                    nums += 1
                    if len(title_link) >= 100:
                        break
            print("当前网址为", "============", self._driver.current_url)
            self.print_goods(title_link)
            results += title_link
            try:
                self._driver.find_element_by_class_name("pn-next").click()
            except NoSuchElementException as nsee:
                pass
            finally:
                break

        return results

    def get_details_of_goods(self, goods):
        """
        获取商品的详细参数，并爬取2000条评论
        :param goods: list
        :return: None
        """
        for good in goods:
            link = good[1]
            self._driver.get(link)
            ul = self._driver.find_element_by_css_selector(".parameter2.p-parameter-list")
            good_name = ul.find_element_by_tag_name("li").text[5:]
            etab = self._driver.find_element_by_css_selector(".tab-main.large")[-1]
            etab.find_element_by_tag_name("li")[1].click()







if __name__ == "__main__":
    crawler = Solution()
    results = crawler.get_goods_link()

