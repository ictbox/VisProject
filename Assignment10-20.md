## 任务分配

特征：
微信： 文本信息
知乎： 文本信息，回答点赞，回答评论，回答感谢，回答关注者（粉丝数）
微博：文本信息， 微博转发，微博评论，微博点赞， 粉丝数






李老师
- [ ] 完成9维度,折线图，d3

黄老师

- [ ] 微信公众平台的文章
- [ ] 知乎专栏文章 50+
- [ ] 知乎人物爬虫


方老师
- [ ] 微博爬虫入库
- [ ] 后端服务器
- [ ] 数据库清洗（函数）


高老师

- [x] 声量定义
- [x] 数据库清洗（函数）
- [x] 后端服务器

数据库清洗：
能够得到
（2017年6月18日-8月28日）
文章的9维向量。


## api接口

```
post /compute 
parameters : data {}

examples:
{
    "zhihu_vote": 3,
    "zhihu_comments": 4,
    "zhihu_thanks": 7,
    "zhihu_follow": 10,
    "weibo_retweet": 11,
    "weibo_comment": 12,
    "weibo_vote": 13,
    "weibo_follow": 20
}

return 
{
    "topic1": [],
    "tolic2": [],
    ...
}

```


