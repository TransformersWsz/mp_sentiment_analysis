url = "https://list.jd.com/list.html?cat=9987,653,655&ev=exprice%5FM0L499&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar"    # 起始页面

chrome_drive_path = r"C:\Users\antco\Downloads\chromedriver_win32\chromedriver.exe"    # 谷歌驱动位置

num_mp = 1000    # 带爬取的手机数量
low_price = 1700
high_price = 2799
num_comment = 10000
num_comment_to_crawl = 1000

wait_time = 20    # WebDriverWait等待时间
before_get_element_time = 2    # 获取元素前等待时间
exceed_time = [5, 10]    # 超时重刷浏览器时间

