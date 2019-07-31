import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from crawler.setting import *

url = "https://item.jd.com/100005948632.html"


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    while True:
        etab = driver.find_elements_by_css_selector(".tab-main.large")[-1]
        etab.find_elements_by_tag_name("li")[4].click()
        try:
            WebDriverWait(driver, wait_time).until(
                lambda driver: len(driver.find_elements_by_css_selector(".comment-item")) >= 10)
            time.sleep(2)

            comment_items = driver.find_elements_by_css_selector(".comment-item")  # 获取商品评论
            for item in comment_items:
                comment_content = item.find_element_by_css_selector(".comment-con").text
                comment_content = comment_content.replace("\n", "")
                print(len(comment_content))
                print("\n" in comment_content)
                print(comment_content)
                print("=======================================")
            break
        except TimeoutException as te:
            print("发生了超时。。。。。。")
            time.sleep(5)
            driver.refresh()
        finally:
            pass


if __name__ == "__main__":
    main()
