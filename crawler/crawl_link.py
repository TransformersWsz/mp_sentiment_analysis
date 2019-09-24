import logging

from crawler.spider import CrawlGood


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("crawler.log", mode="a")    # 日志输出到文件
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()    # 日志输出到控制台
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(message)s")    # 设置输出格式
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def main():
    logger = get_logger()
    with open("link.txt", "r", encoding="utf-8") as fr:
        num = 1
        for line in fr:
            if num >= 5:
                try:
                    title, href = line.split(" ---> ")
                    spider = CrawlGood(title, href)
                    spider.run()
                except Exception as e:
                    logger.info("第{}行 {} {}爬取发生了异常".format(num, title, href))
                finally:
                    num += 1
            else:
                num += 1


if __name__ == "__main__":
    main()
