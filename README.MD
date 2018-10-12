# incre_std_avg
## 一个简单的增量计算海量数据均值,标准差,方差的python类
***
用于实现增量计算海量数据均值,标准差,方差的python类
***
example
<pre>
from incre_std_avg import incre_std_avg

incre_obj = incre_std_avg()
#按值增量计算
incre_obj.incre_in_value(0.05) 
#输出当前结果
print incre_obj.avg 
print incre_obj.std 
print incre_obj.n 
#按list增量计算
incre_obj.incre_in_value(0.02)
incre_obj.incre_in_list([0.5, 0.2, 0.3]) 
#输出当前结果
print incre_obj.avg 
print incre_obj.std 
print incre_obj.n 
</pre>

# 算法说明见blog
[算法实现说明](http://www.calmkart.com/?p=369 "算法实现说明")