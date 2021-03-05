import requests
from parsel import Selector
import pandas as pd
import time
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
}
# pages是不同页码的网址列表
pages=['https://jn.lianjia.com/ershoufang/pg{}/'.format(x) for x in range(1,1000)]
lj_shanghai= pd.DataFrame(columns=['hou_code','title','infotitle','alt',
                                   'positionIcon_region','positionIcon_new',
                                   'positionInfo_new','position_xiaoqu','starIcon','price_total_new','unitPrice'])
count=0

def l_par_html(url):
    wr=requests.get(url,headers=headers,stream=True)
    sel=Selector(wr.text)
    # hou_code用来获取房源的编号
    hou_code=sel.xpath('//div[@class="title"]/a/@data-housecode').extract()
    #获取标题
    title=sel.xpath('//div[@class="title"]//text()').extract()
    infotitle=sel.xpath('//div[@class="title"]/a/text()').extract()
# =============================================================================
#     #图片
# #    src=sel.xpath('//img[@class="lj-lazy"]//@src').extract()
# #    print('src:%s'%src)
# =============================================================================
    #图片地址
    alt=sel.xpath('//img[@class="lj-lazy"]//@alt').extract()
    positionIcon_region=sel.xpath('//div[@class="houseInfo"]/a/text()').extract()
    #获取房屋信息
    positionIcon = sel.xpath('//div[@class="houseInfo"]//text()').extract()
    positionIcon_new=([x for x in positionIcon if x not in positionIcon_region ])
    positionInfo = sel.xpath('//div[@class="positionInfo"]//text()').extract()
    position_xiaoqu = sel.xpath('//div[@class="positionInfo"]/a/text()').extract()
    positionInfo_new = ([x for x in positionInfo if x not in position_xiaoqu])
    starIcon =sel.xpath('//div[@class="followInfo"]//text()').extract()
    price_total = sel.xpath('//div[@class="totalPrice"]//text()').extract()
    price_total_new =([x for x in price_total if x != '万' ])
    unitPrice =sel.xpath('//div[@class="unitPrice"]//text()').extract()
    wr=requests.get(url,headers=headers,stream=True)
    sel=Selector(wr.text)
    tag = sel.xpath('//div[@class="tag"]//text()').extract()
#    print("tag:%s"%tag)
    pages_info=pd.DataFrame(list(zip(hou_code,title,infotitle,alt,
                                   positionIcon_region,positionIcon_new,
                                   positionInfo_new,position_xiaoqu,starIcon,price_total_new,unitPrice)),
    columns=['hou_code','title','infotitle','alt',
                                   'positionIcon_region','positionIcon_new',
                                   'positionInfo_new','position_xiaoqu','starIcon','price_total_new','unitPrice'])
 #    print(pages_info)
 #由于抓取下来的信息是存储在列表中的，出现了一对多的情况，故将tag,title,infotitle单独取出分析![在这里插入图片描述](https://img-blog.csdnimg.cn/20190627170938390.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpZmlfd3V4aWFu,size_16,color_FFFFFF,t_70)
    return pages_info,tag,title,infotitle

for page in pages:
    a=l_par_html(page)[0]
    b=l_par_html(page)[1:]
    print('advantage:{}'.format(b))
    count=count+1
    print ('the '+str(count)+' page is sucessful')
    #每隔20s翻页一次
    time.sleep(20)
    lj_shanghai=pd.concat([lj_shanghai,a],ignore_index=True)
    print(lj_shanghai)
 #将数据存储到excel表格中
lj_shanghai.to_excel(r'\\lianjia_ershou_shanghai.xlsx')