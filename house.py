import requests
from bs4 import BeautifulSoup


class Spider(object):
    """
    爬虫类，定义爬虫行为
    """
    def __init__(self, url):
        """
        初始化爬虫
        :param url:爬虫入口url
        """
        self.url = url

    def craw(self, url):
        """
        爬虫的爬取行为
        :param url:要爬取的地址
        :return:返回BeautifulSoup对象
        """
        r = requests.get(url, timeout=10)
        r.encoding = 'gbk'
        response = r.text
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def parse_info_list(self, soup):
        """
        解释页面上的每个房源信息的URL
        :param soup:页面的BeautifulSoup对象
        :return:房源具体信息的url列表
        """
        info_list = []
        infos = soup.find_all(class_='esfylist')
        for i in infos:
            info = i.find(class_='info').find(class_='fz14 fwb').get('href')

            if info not in info_list:
                info_list.append(info)

        return info_list

    def parse_info(self, soup):
        """
        解释房源的具体信息
        :param soup: 页面的BeautifulSoup对象
        :return: 房源具体信息的字典{总价：，单价：。。。}
        """
        a = {}
        info = soup.body.find(class_='house-info-bd clearfix').find_all(class_='fcg')
        value = soup.body.find(class_='house-info-bd clearfix').\
            find_all(class_='fco arial')
        house_clearfix = soup.body.find_all(class_='house-info-bd clearfix')[1]
        for i in range(len(info)-1):
            a[info[i].get_text().replace('：','')] = value[i].get_text()

        for i in house_clearfix.get_text().split('\n'):
            if i != '':
                a[i.split('：')[0]] = i.split('：')[1]
        print(a)
        return a


    def parse_next_url(self, soup):
        """
        获取下一页的URL
        :param soup:页面的BeautifulSoup对象
        :return:下一页的URL
        """
        next_url = soup.find(class_='p_redirect').get('href')
        return next_url

    def run(self):
        """
        爬虫运行，重复爬取
        :return: None
        """
        run_url = self.url
        while run_url:
            soup = self.craw(run_url)
            lis = self.parse_info_list(soup)

            soup_info = self.craw(lis[0])
            result = self.parse_info(soup_info)
            #for li in lis:
            #    soup_info = self.craw(li)
            #    result = self.parse_info(soup_info)

            run_url = self.parse_next_url(soup)


if __name__ == "__main__":
    a = Spider("http://www.gaoming.com.cn/fangyuan/house/")
    a.run()
