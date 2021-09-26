import requests


class HuaweiappSpider:
    url = ''
    url1 = "https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.completeSearchWord&serviceType=20" \
           "&keyword=%s&zone=&locale=zh"
    url2 = 'https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum' \
           '=1&uri=searchApp|%s&maxResults=25&version=10.0.0&zone=&locale=zh'
    url_searchword = ''
    all_app_list = []
    app_num = 0

    def __init__(self):
        pass

    def spider(self):
        url = self.url_searchword.replace('reqPageNum=1', 'reqPageNum=%s')
        hasNextPage = 1
        page = 1

        '''若hasNextPage=1,则继续爬取下一页数据;否则爬取下一个搜索词'''
        while hasNextPage == 1:
            url_page = url % str(page)
            print('url: ', url_page)
            req = requests.get(url_page)
            json_data = req.json()

            '''url1'''
            # app_list = req.json()['appList']

            '''url2'''
            layout_app_list = json_data['layoutData']

            for layoutData in layout_app_list:
                app_detial_list = layoutData['dataList']
                for app in app_detial_list:
                    app_list = []
                    if app.__contains__('sha256'):
                        app_list.append(app['sha256'])
                    else:
                        app_list.append('null')
                    if app.__contains__('name'):
                        app_list.append(app['name'])
                    else:
                        app_list.append('null')
                    if app.__contains__('package'):
                        app_list.append(app['package'])
                    else:
                        app_list.append('null')
                    if app.__contains__('memo'):
                        app_list.append(app['memo'])
                    else:
                        app_list.append('null')
                    if app.__contains__('kindName'):
                        app_list.append(app['kindName'])
                    else:
                        app_list.append('null')
                    if app.__contains__('tagName'):
                        app_list.append(app['tagName'])
                    else:
                        app_list.append('null')
                    print(app_list)
                    self.all_app_list.append(app_list)
                    self.app_num += 1

            hasNextPage = json_data['hasNextPage']
            page += 1

    def set_url_searchword(self, search_word):
        """
        :param search_word:
        :return:
        """
        url_searchword = self.url2 % search_word
        self.url_searchword = url_searchword

    def get_url_searchword(self):
        return self.url_searchword

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url
