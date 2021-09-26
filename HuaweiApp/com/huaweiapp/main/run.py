from com.huaweiapp.main.data import data
from com.huaweiapp.main.mysql import mysql
from com.huaweiapp.main.spider import spider
import time

if __name__ == '__main__':
    # search_list = ['王者荣耀']
    # hs = spider.HuaweiappSpider()
    # hs.set_url_list(search_list)
    # hs.spider()
    # print(hs.all_app_list)

    start = time.time()
    hd = data.HuaweiappData()
    hd.get_data()
    end = time.time()
    print('跑完了,用了', end-start)
