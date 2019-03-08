import  requests

def  get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except:
        print(r.status_code)
        return "异常！！ ---   返回状态码为:"
    r.encoding = r.apparent_encoding
    return r.text


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(get_html_text(url))
