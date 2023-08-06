# 执行语言编号
class l:
    LANGS = {
        'zh' : 0,
        'en' : 1,
    }
    n = 1  # 当前使用的语言编号

import locale
if 'zh_CN' in locale.getdefaultlocale():
    l.n = l.LANGS['zh']
else :
    l.n = l.LANGS['en']

class Settings:
    auto_open_report = True