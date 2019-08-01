from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

url = "https://item.jd.com/100005948632.html"

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    driver.save_screenshot("test.png")

    # etab = driver.find_elements_by_css_selector(".tab-main.large")[-1]
    # etab.find_elements_by_tag_name("li")[4].click()
    # WebDriverWait(driver, 10).until(
    #     lambda driver: len(driver.find_elements_by_css_selector(".comment-item")) >= 10)
    #
    # comment = driver.find_element_by_css_selector(".comment-column.J-comment-column")
    # star = comment.find_element_by_tag_name("div")
    # print(int(star.get_attribute(name="class")[-1]))
    #
    # message = comment.find_element_by_css_selector(".order-info")
    # spans = message.find_elements_by_tag_name("span")
    # for info in spans:
    #     print(info.text)


if __name__ == "__main__":
    main()