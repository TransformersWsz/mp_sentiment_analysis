"""将文件数据存储到数据库中"""


import pymysql
import os

HOST = "106.15.231.105"
PORT = 3306
USER = "root"
PASSWORD = "206209"
DATABASE = "mp"


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as fr:
        num = 0
        for line in fr:
            line = line.strip().split("\t")
            for item in line:
                num += 1
                if item == None:
                    item = "None"
                if item == "":
                    item = "space"
                print("{} ---> {}".format(num, item))
            print(len(line))
            break


def list_files(dirname):
    files = os.listdir(dirname)
    for item in files:
        print(os.path.join(dirname, item))


def preprocess(line, pic):
    line = [item if item != "" else "unknown" for item in line]
    pic_url = "http://106.15.231.105:8000/static/phone/{}".format(pic)
    line.insert(1, pic_url)
    return tuple(line)


def insert(datapath):
    db = pymysql.connect(HOST, USER, PASSWORD, DATABASE, PORT)
    cursor = db.cursor()

    files = os.listdir(datapath)
    num = 0
    for filename in files:
        if filename.find(".txt") != -1:
            filepath = os.path.join(datapath, filename)
            with open(filepath, "r", encoding="utf-8-sig") as fr:
                for line in fr:
                    line = line.strip().split("\t")

                    pic = "{}.png".format(line[0])
                    row_data = preprocess(line, pic)
                    print(row_data)
                    sql = "insert into specification(name, pic, color, length, width, thickness, weight, cards, sim, rom, ram, size, resolution, front, cameras, back, power, earphone, thunderport) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                    try:
                        cursor.execute(sql, row_data)
                        db.commit()
                        print("{} insert success".format(line[0]))
                        num += 1
                    except Exception as e:
                        print(e)
                        db.rollback()
                        print("{} insert error".format(line[0]))
                    finally:
                        break
    db.close()


def update_pic():
    db = pymysql.connect(HOST, USER, PASSWORD, DATABASE, PORT)
    cursor = db.cursor()

    for i in range(93, 137):
        sql = "update specification set pic = %s where p_id = %s"

        try:
            cursor.execute(sql, ("https://transformerswsz.github.io/2019/09/19/picture%20bed/{}.png".format(i), i))
            db.commit()
        except:
            print("{} update failure".format(i))
            db.rollback()
            break




def batch_rename(dirpath):
    db = pymysql.connect(HOST, USER, PASSWORD, DATABASE, PORT)
    cursor = db.cursor()

    sql = "select p_id, name from specification"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        os.rename(os.path.join(dirpath, "{}.png".format(row[1])), os.path.join(dirpath, "{}.png".format(row[0])))



if __name__ == "__main__":
    update_pic()