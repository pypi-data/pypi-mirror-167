
# 例外処理を簡単に書けるツール [erf]
# 【動作確認 / 使用例】

import sys
import math
from ezpip import load_develop
# 例外処理を簡単に書けるツール [erf]
erf = load_develop("erf", "../", develop_flag = True)

# 「KeyError」が含まれる例外時に「"no_data"」を返却するようにする
@erf({"KeyError": "no_data"})
def getter(dic, key):
	return dic[key]

dic = {"fuga": 23}
print(getter(dic, "hoge"))	# -> "no_data"

# 同様のコードの略記法
@erf(KeyError = "no_data")
def getter2(dic, key):
	return dic[key]

dic = {"fuga": 23}
print(getter2(dic, "hoge"))	# -> "no_data"

# 例外オブジェクトを文字列化する方法を指定
@erf({"division by zero": math.inf}, error_str_func = "str")
def inf_div(a, b):
	return a / b

print(inf_div(3, 0))	# -> inf

# 無名関数の例外処理
print(erf({"division by zero": math.inf})(lambda a, b: a/b)(3, 0))

# 無名関数の例外処理 その2
func = lambda a, b: a/b
catcher_dic = {"division by zero": math.inf}
print(erf(catcher_dic)(func)(3, 0))

# 無名関数の例外処理 その3
func = lambda a, b: a/b
print(erf(div = math.inf)(func)(3, 0))

# 無名関数の例外処理 その4
func = lambda a, b: a/b
safe_div = erf(div = math.inf)(func)
print(safe_div(3, 0))

# 再帰の例: 再帰の場合は1重ラップする必要がある
def rec_func(arg):
	if type(arg) == type(23):
		return str(arg)
	elif type(arg) == type([]):
		return [rec_func(e) for e in arg]
	else:
		raise Exception("invalid type.")

@erf(recur = ...)
def wrapper(arg):
	return rec_func(arg)

print(wrapper([1,[2,3]]))
obj = [1,2]
obj[1] = obj
print(wrapper(obj))
