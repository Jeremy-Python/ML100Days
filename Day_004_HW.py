import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
#第一題
print(np.sum(english_score>math_score))
#第二題
a=(np.all(math_score<chinese_score))
b=(np.all(english_score<chinese_score))
if a==b:
	print(a)
elif a!=b:
	print("False")

