import numpy as np
from decimal import Decimal
# 第一題
print(20*np.log10(20000/20))
# 第二題
a=Decimal(np.power(10,(50/20))*20)
b=Decimal(np.power(10,(30/20))*20)
print(np.trunc(Decimal(a/b)))
