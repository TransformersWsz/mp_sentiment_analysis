import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from crawler.setting import *


class CrawlGood(object):
    """爬取单个商品的参数和评价"""

    def __init__(self, title, href):
        self._title = title
        self._href = href

    def print_list(self, result):
        print(len(result), "--->")
        for item in result:
            print(item)
        print("============================")

    def run(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self._href)


        ul = driver.find_element_by_css_selector(".parameter2.p-parameter-list")
        good_name = ul.find_element_by_tag_name("li").text[5:]
        etab = driver.find_elements_by_css_selector(".tab-main.large")[-1]
        etab.find_elements_by_tag_name("li")[1].click()
        details = driver.find_elements_by_css_selector(".Ptable-item")  # 获取商品参数

        color = "unknown"
        length = "unknown"
        width = "unknown"
        thickness = "unknown"
        weight = "unknown"
        cards = "unknown"
        sim = "unknown"
        rom = "unknown"
        ram = "unknown"
        size = "unknown"
        resolution = "unknown"
        front = "unknown"
        cameras = "unknown"
        back = "unknown"
        power = "unknown"
        earphone = "unknown"
        thunderport = "unknown"

        for info in details:
            dls = info.find_elements_by_css_selector(".clearfix")
            for dl in dls:
                dt_title = dl.find_element_by_tag_name("dt").text
                dd_content = dl.find_element_by_tag_name("dd").text.strip()
                if "机身颜色" in dt_title:
                    color = dd_content
                if "机身长度" in dt_title:
                    length = dd_content
                if "机身宽度" in dt_title:
                    width = dd_content
                if "机身重量" in dt_title:
                    thickness = dd_content
                if "双卡机类型" in dt_title:
                    cards = dd_content
                if "SIM卡类型" in dt_title:
                    sim = dd_content
                if "ROM" in dt_title or "机身存储" in dt_title:
                    rom = dd_content
                if "RAM" in dt_title or "运行内存" in dt_title:
                    ram = dd_content
                if "主屏幕尺寸" in dt_title:
                    size = dd_content
                if "分辨率" in dt_title:
                    resolution = dd_content
                if "前置摄像头的主像素" in dt_title:
                    front = dd_content
                if "摄像头数量" in dt_title:
                    cameras = dd_content
                if "后置摄像头的主像素" in dt_title:
                    back = dd_content
                if "电池容量" in dt_title:
                    power = dd_content
                if "耳机接口类型" in dt_title:
                    earphone = dd_content
                if "充电接口类型" in dt_title:
                    thunderport = dd_content

        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(good_name, color,
                                                                                                length, width,
                                                                                                thickness, weight,
                                                                                                cards, sim,
                                                                                                rom, ram, size,
                                                                                                resolution,
                                                                                                front, cameras,
                                                                                                back, power,
                                                                                                earphone,
                                                                                                thunderport))

        time.sleep(before_get_element_time)
        etab.find_elements_by_tag_name("li")[4].click()
        nums = 0  # 已爬取的评论数量
        comment_list = []
        while nums < num_comment_to_crawl:
            try:
                WebDriverWait(driver, wait_time).until(
                    lambda driver: len(driver.find_elements_by_css_selector(".comment-item")) >= 10)
                time.sleep(before_get_element_time)
                comment_items = driver.find_elements_by_css_selector(".comment-item")  # 获取商品评论
                temporary = []
                for item in comment_items:
                    comment_content = item.find_element_by_css_selector(".comment-con").text
                    comment_content = comment_content.replace("\n", "")
                    temporary.append(comment_content)
                    nums += 1

                    if nums >= num_comment_to_crawl:
                        break

                self.print_list(temporary)
                comment_list += temporary
                try:
                    time.sleep(before_get_element_time)
                    driver.find_element_by_css_selector(".ui-pager-next").click()
                except NoSuchElementException as nsee:
                    break
                finally:
                    pass
            except TimeoutException as te:
                print("发生了超时。。。。。。")
                if nums > 0:
                    break
                else:
                    driver.refresh()
                    time.sleep(before_get_element_time)
                    driver.find_elements_by_css_selector(".tab-main.large")[-1].find_elements_by_tag_name("li")[4].click()
            finally:
                pass

        print("({} {}) 爬取结束 ----------------------------------------".format(self._title, self._href))
        with open("{}.txt".format(good_name), "w", encoding="utf-8") as fw:
            fw.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(good_name, color,
                                                                                                       length, width,
                                                                                                       thickness,
                                                                                                       weight, cards,
                                                                                                       sim, rom, ram,
                                                                                                       size, resolution,
                                                                                                       front, cameras,
                                                                                                       back, power,
                                                                                                       earphone,
                                                                                                       thunderport))
            for content in comment_list:
                fw.write(content + "\n")
