import requests

proxies = {
  "http": "http://1.85.220.39:8118"
}

res = requests.get("https://www.baidu.com", proxies=proxies)

print(res.text)




