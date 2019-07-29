import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://item.jd.com/100002642218.html"
num_mp = 100
low_price = 1700
high_price = 2799
num_comment = 10000
num_comment_to_crawl = 2000


def test():
    driver = webdriver.Chrome()
    driver.get(url)
    ul = driver.find_element_by_css_selector(".parameter2.p-parameter-list")
    good_name = ul.find_element_by_tag_name("li").text[5:]
    etab = driver.find_element_by_css_selector(".tab-main.large")[-1]
    etab.find_element_by_tag_name("li")[1].click()

    details = driver.find_elements_by_css_selector(".Ptable-item")
    for info in details:
        dls = info.find_elements_by_css_selector(".clearfix")
        for dl in dls:
            dt = dls.find_element_by_tag_name("dt")
            if "机身颜色" in dt.text:
                pass



if __name__ == "__main__":
    test()

