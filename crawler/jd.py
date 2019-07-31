from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from crawler.setting import *
from crawler.spider import CrawlGood


class Solution(object):
    """爬取京东网站上的一系列手机商品链接"""
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
        self._driver.maximize_window()
        self._driver.get(url)
        results = []
        nums = 0    # 已爬取的数量
        while nums < num_mp:
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
                    if len(title_link) >= num_mp:
                        break
            print("当前网址为", "============", self._driver.current_url)
            self.print_goods(title_link)
            results += title_link
            try:
                self._driver.find_element_by_class_name("pn-next").click()
            except NoSuchElementException as nsee:
                break
            finally:
                pass
        return results

    def save_results(self, results):
        with open("link.txt", "w", encoding="utf-8") as fw:
            for title, href in results:
                fw.write("{} ---> {}\n".format(title, href))

    def crawl_single_good(self, title, href):
        spider = CrawlGood(title, href)
        spider.run()


if __name__ == "__main__":
    solution = Solution()
    results = solution.get_goods_link()
    solution.save_results(results)
    for (title, href) in results:
        solution.crawl_single_good(title, href)
