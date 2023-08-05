
# 例外処理を簡単に書けるツール [erf]

import os
import sys

class Erf:
	# 初期化処理
	def __init__(self):
		pass

# 返却値指定辞書の引き当て
def pick_catcher_dic(catcher_dic, err_str):
	for key in catcher_dic:
		if key in err_str: return catcher_dic[key]
	return None

# 例外処理付き実行 (未知の例外は外側にraiseされる)
def excepted_call(
	org_func,	# 対象の関数
	args, kw_args,	# 関数実行時の引数
	catcher_dic, error_str_func	# エラー関係引数
):
	try:
		# 元関数の実行
		return org_func(*args, **kw_args)
	except Exception as e:
		err_str = error_str_func(e)
		# 返却値指定辞書の引き当て
		value = pick_catcher_dic(catcher_dic, err_str)
		if value is not None: return value
		# 処理できないエラーの場合
		raise e

# 引数付きデコレーターとしての用法
def erf_call(
	self,
	catcher_dic = {},	# 返却値指定辞書 (keyで指定された文字列が含まれたエラーの際の返却値を指定)
	error_str_func = "repr",	# 例外オブジェクトを文字列化する際の関数
	**kw_catcher_dic	# キーワード引数指定の「返却値指定辞書」
):
	# 2種類の「返却値指定辞書」を結合
	bind_catcher_dic = {**catcher_dic, **kw_catcher_dic}
	# 例外オブジェクトを文字列化する際の関数
	if error_str_func == "repr": error_str_func = repr
	if error_str_func == "str": error_str_func = str
	# 返すべき引数なしデコレータ
	def decorator_core(org_func):
		def ret_func(*args, **kw_args):
			# 例外処理付き実行 (未知の例外は外側にraiseされる)
			return excepted_call(
				org_func,	# 対象の関数
				args, kw_args,	# 関数実行時の引数
				bind_catcher_dic, error_str_func	# エラー関係引数
			)
		return ret_func
	return decorator_core

# erf_callをErfクラスの引数付きデコレーター用法に束縛
Erf.__call__ = erf_call

# 呼び出しの準備
erf = Erf()	# Erf型のオブジェクトを予め実体化
sys.modules[__name__] = erf	# モジュールオブジェクトと「erf」オブジェクトを同一視
