#声量定义和计算

##物理意义
>信息被接受的总量  
>计算方法：
>文章信息量以及阅读该文章人数的期望的乘积

>       V = I*N

>单位：bit

##具体计算   
声量的计算分为两部分   
1.文章信息量的计算:

>文章的信息量定义为所有实词的信息量的和，单个实词信息量的计算使用以下方式：
>>对于文章A中的实词W，我们假设在整件事件结束后，该词出现的概率是百分之百，那么在事件发展过程中某篇文章发表后，该词出现的概率增大了，那么这篇文章中这个词带给我们的信息量就是这篇文章出现前后信息量的差。特别的，对于第一篇文章而言，其发表之前这个词没有出现过，认为概率是0，那信息量就会无穷大，所以我们定义每个词在事件开始之前，就有一定的概率出现，这里设定该概率为1/该词总词频+1。

        I(A,W)=-log(P_beforeA(W))+log(P_afterA(W))

2.阅读该文章的人数期望的计算：

>人数的期望由该文章的一系列外部特征决定，这些特征分为两部分，一部分是作者本身的知名度带来的可能阅读的人，一部分是文章的转发和点赞等带来的可能阅读的人，最后的值为这两部分的最大值

>1)    作者本身带来的可能阅读的人数  
>>由作者的粉丝数决定，设粉丝数为FN，粉丝阅读转化率为C  

>>       N1=FN*C
>2)    文章的转发和点赞带来的阅读的数的期望

>>文章的转发和点赞带来的阅读人数的期望由下面的参数决定，下面的键值对左边表示对该文章的行为，右边表示该行为带来阅读人数的期望。最后取右边的值构成向量Y，与进行进行该行为的人数向量相乘，得到该文章的转发和点赞等行为带来的阅读人数的期望N2

>>     "zhihu_vote": 3,
    "zhihu_comments": 4,
    "zhihu_thanks": 7,
    "zhihu_follow": 10,
    "weibo_retweet": 11,
    "weibo_comment": 12,
    "weibo_vote": 13,
    "weibo_follow": 20
>
>阅读该文章A的人数的期望E(A)=N=max(N1,N2)
