import requests
from bs4 import BeautifulSoup as bs
import re
import numpy as np
import datetime

result = np.array([0, 0])
areas = ["http://naver.me/xdVBxAsP", "http://naver.me/FzIC7hUN", "http://naver.me/GgOvqp4t", "http://naver.me/5jYFwOXs", "http://naver.me/GSgFJeLP", "http://naver.me/GnjoXcyb", "http://naver.me/GK5DYktQ", "http://naver.me/F1L1wWNy",
         "http://naver.me/5mrbqQge", "http://naver.me/Gp0jOFzO", "http://naver.me/GRfxl5sH", "http://naver.me/G4wuKRU1", "http://naver.me/5f4YhCDi", "http://naver.me/5hgbYkPJ", "http://naver.me/xuelnOoA", "http://naver.me/G4wuKPIS", "http://naver.me/xsUHyKCR"]


def getNums(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    t1 = soup.select_one("div.top_ranker span.num").get_text()
    t2 = soup.select_one("span.gap").get_text()
    t3 = soup.select_one("span.number_area").get_text()

    t2_ = int(re.sub(",", "", t2[3:]))
    t3_ = float(t3)

    estimation = round(t2_*100/t3_, 2)

    if t1 == "1":
        return [estimation, 0]
    else:
        return [0, estimation]


for area in areas:
    temp = np.array(getNums(area))
    result = result+temp

total = 44197692
half = (total - result[0] - result[1]-1546919)/2  # 군소후보가 3.5% 차지했다고 가정
lee_percent = round((half+result[0])/total*100, 2)
yoon_percent = round((half+result[1])/total*100, 2)

print("현재 시각: {0}".format(datetime.datetime.now()))
print("대통령 예상 득표율 -- 이재명: {0}%, 윤석열: {1}%".format(lee_percent, yoon_percent))
