## Python Course : Crawler 

## Table of Contents
1. [課程資訊](#課程資訊)
2. [課程大綱](#課程大綱)
3. [Course Slides](#course-slides)
4. [Reference](#reference)

## 課程資訊
- 開課單位：
- 時間：2021/07/22 - 2021/09/23 (每週四 1400-1700)
- 上課時數：3小時/週, 共 30 小時
- 講師：Jason Hsu
- 授課方式：線上授課 - Google Meet (固定連結)
- 課程目標：協助學員了解基礎爬蟲技術, 透過實作進而...
- 其他事項：學員需自行準備電腦、Gmail 帳號

## 課程大綱
| Week | Topic | Time | Note |
| ---- | ---- | ---- | ---- |
| W1 | Python Variables | 1 | |
| W1 | Python Environment & Library | 1 | virtualenv, pipenv, requests, BeautifulSoup4 |
| W1 | Python Flow Control | 1 |
| ---- |
| W2 | Network Basic | 1 |
| W2 | Web Server | 1 |
| W2 | Basic Crawler | 1 | requests, status code |
| ---- |
| W3 | HTTP Methods | 1 | GET, POST, ... |
| W3 | URL Encode / Decode | 1 |
| W3 | HTTP Exercise | 1 |
| ---- |
| W4 | Query Output : JSON Format | 1 | [1], [2] |
| W4 | Query Output : HTML Format | 2 | BeautifulSoup4 ([4]) <br> Element Selecting : CSS Selector, XPath [14] |
| ---- |
| W5 | Headers, Cookie Spoofing | 2 | UA , [3] |
| W5 | Anti-Cralwer | 1 | robots.txt |
| ---- |
| W6 | 蝦皮網站練習 | 2 | [7] |
| W6 | PTT 練習 | 1 | [5], [6] |
| ---- |
| W7 | 多工 | 1 | Multi-thread | [12] |
| W7 | 多工爬蟲 | 2 | [9], [8], [13] |
| ---- |
| W8 | 反反爬蟲 : 代理IP | 1 | headless |
| W8 | Selenium 入門 | 2 | Instagram Post | [11] |
| ---- |
| W9 | Data Visualization | 2 | Matplotlib, Plotly |
| W9 | Practice | 1 |
| ---- |
| W10 | 爬蟲實戰 Demo | 2.5 |
| ---- |


## Course Slides
- W1 :
- ...

## Reference
- Virtual Environment
    - venv
        - https://docs.python.org/zh-tw/3/tutorial/venv.html
    - virtualenv
        - https://medium.com/python4u/python-virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D-9d6be2d45db9
- 爬蟲
    - https://codertw.com/程式語言/745000/
    - Scrapy 實作 PTT : https://www.maxlist.xyz/2018/08/25/python_scrapy_ptt/
    - 進階 Selenium 多線池: https://www.maxlist.xyz/2019/04/28/python-selenium-driver-threading/
- 反爬蟲
    - https://codertw.com/程式語言/745003/#outline__1
- 反反爬蟲
    - 常見機制介紹 : https://kknews.cc/zh-tw/code/q5vk3oy.
    - Proxy Pool 建構代理IP的清單 : https://tlyu0419.github.io/2020/02/07/WebCrawler-ProxyPool/
        - Code : https://colab.research.google.com/drive/1PgALsr6iArpUE4NHt4GJw2TkiGH7we-m
    - Scrapy 爬免費代理(Proxy) : https://ithelp.ithome.com.tw/articles/10208575

[1]: https://ithelp.ithome.com.tw/articles/10203382
[2]: http://json.parser.online.fr/
[3]: https://ithelp.ithome.com.tw/articles/10203744
[4]: https://ithelp.ithome.com.tw/articles/10204390
[5]: https://ithelp.ithome.com.tw/articles/10204709
[6]: https://ithelp.ithome.com.tw/articles/10205022
[7]: https://colab.research.google.com/drive/1HmmUWlQNDG8xl9iaaB8npHIyBxGXu2Z5?usp=sharing
[8]: https://medium.com/analytics-vidhya/multi-threaded-python-web-crawler-for-https-pages-e103f0839b71
[9]: https://www.maxlist.xyz/2020/03/15/python-threading/
[10]: https://www.maxlist.xyz/2020/04/05/async-python-crawler-snippets/
[11]: https://www.maxlist.xyz/2018/05/04/python/
[12]: https://www.796t.com/article.php?id=163375
[13]: https://iter01.com/523685.html
[14]: https://lufor129.medium.com/%E6%89%8B%E6%8A%8A%E6%89%8B%E5%AF%AB%E5%80%8B%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-%E4%B8%80-xpath-518553fd676d