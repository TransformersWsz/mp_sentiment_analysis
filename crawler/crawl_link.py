from crawler.spider import CrawlGood


def main():
    with open("link.txt", "r", encoding="utf-8") as fr:
        num = 0
        for line in fr:
            if num >= 26:
                title, href = line.split(" ---> ")
                spider = CrawlGood(title, href)
                spider.run()
            else:
                num += 1



if __name__ == "__main__":
    main()
