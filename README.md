# 基于django和scrapy的信息收集程序
## 运行方式(ubuntu下):docker-compose up -d 
## django
- 版本 **2.1**
## scrapy 
- 版本 **1.7.3**
通过scrapy收集即将到来的比赛信息，然后利用orm的方式保存到mysql数据库,通过django来显示信息.其中scrapy采用定时的方式收集信息，同时在每次收集信息时利用装饰器首先清空已经收集到信息，防止信息进行累加
- - -
### 收集的网站
|名字|网址|
|:-:|:-:|
|codeforces| http://codeforces.com/contests |
|hankerank| https://www.hackerrank.com/contests |
|csacadeny| https://csacademy.com/contests/ |
