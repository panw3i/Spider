# -*- coding: utf-8 -*-
import pymysql
import requests

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="proxy", charset="utf8")
cursor = conn.cursor()


class IPManager(object):
    def delete_ip(self, ip):
        sql = """
            delete from ip_pool where ip_address='{0}'
        """.format(ip)
        cursor.execute(sql)
        conn.commit()
        return True

    def check_ip(self, ip, port, types):
        http_url = "{0}://www.baidu.com".format(types.lower())
        proxy_url = "{0}://{1}:{2}".format(types.lower(), ip, port)
        try:
            proxy_dict = {
                "{0}".format(types.lower()): proxy_url
            }

            # 设置请求的超时时间 , 单位为秒
            response = requests.get(http_url, proxies=proxy_dict, timeout=5)

            print("有效IP")

        except Exception as e:
            print(e)
            print("无效IP")
            self.delete_ip(ip)

        else:
            code = response.status_code
            if 200 <= code < 300:
                print("有效 IP")
                return True
            else:
                print("无效IP")
                self.delete_ip(ip)
                return False

    def get_random_ip(self):

        sql = """
            SELECT ip_address, port, type FROM ip_pool ORDER BY RAND() LIMIT 1
        """
        result = cursor.execute(sql)
        for ip_info in cursor.fetchall():
            ip, port, types = ip_info
            available = self.check_ip(ip, port, types)
if __name__ == '__main__':

    for  i in range(100):

        t = IPManager()
        t.get_random_ip()
