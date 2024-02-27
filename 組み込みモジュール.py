#組み込みモジュール

#mathモジュール
import math

#randomモジュール
import random

#statisticsモジュール
import statistics

math.pow(2,3)


random.randint(0,100)


#mean(平均値)
nums = [1,5,33,12,46,33,2]
statistics.mean(nums)

#median(中央値)
statistics.median(nums)

#mode(最頻値)
statistics.mode(nums)

#文字列がpythonのキーワードか調べるには

import keyword

keyword.iskeyword("for")
keyword.iskeyword("football")
