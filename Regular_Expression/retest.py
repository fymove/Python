import re
import requests

data = requests.get("http://www.baidu.com")
data.encoding = "utf-8"
print(data.text)

# re_str = "hello20190117haha"
#
# if re.match("^h.", re_str):
#     print("1. 以h开头")