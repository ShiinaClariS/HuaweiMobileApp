from com.huaweiapp.main.spider import spider
from com.huaweiapp.main.mysql import mysql
import pandas as pd
import pymysql


class HuaweiappData:
    search_list = []
    all_app_list = []

    def __init__(self):
        pass

    def get_data(self):
        ms = mysql.mysql()

        data = pd.read_excel(r'W:\workspace\HuaweiApp\com\huaweiapp\搜索词0923.xlsx')
        search_data = data['搜索词']
        for search in search_data[0:50]:
            hs = spider.HuaweiappSpider()
            hs.set_url_searchword(search)
            hs.spider()
            # self.all_app_list = hs.all_app_list
            self.save_to_mysql(search, hs.all_app_list, hs.app_num, ms)
            del hs

        ms.close_()

    def save_to_mysql(self, search, all_app_list, app_num, ms):
        try:
            ms.execute_('insert into record (`name`,num) values("' + search + '","' + str(app_num) + '")')
        except Exception as e:
            print(e)

        print(search)

        for app_list in all_app_list:
            # if ms.select_(self.select_sql(app_list[0])) == ():
            print(app_list)
            sql = self.insert_sql(name=app_list[1],
                                  searchWord=search,
                                  package=app_list[2],
                                  memo=app_list[3],
                                  kindName=app_list[4],
                                  tagName=app_list[5],
                                  sha256=app_list[0])
            print(sql)
            try:
                ms.execute_(sql)
            except Exception as e:
                print(e)

    def insert_sql(self, name, searchWord, package, memo, kindName, tagName, sha256):
        memo = memo.replace('"', '“')
        sql = 'insert into app_list (`name`,searchWord,package,memo,kindName,tagName,sha256) ' \
              'values("' + name + '","' + searchWord + '","' + package + '","' + memo + '","' + kindName + '","' + tagName + '","' + sha256 + '")'

        return sql

    def select_sql(self, sha256):
        sql = 'select * from app_list where sha256 ="' + sha256 + '"'

        return sql

    def get_detial_data(self):
        for app in self.all_app_list:
            print(app)
