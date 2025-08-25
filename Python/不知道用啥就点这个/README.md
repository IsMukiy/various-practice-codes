**语言/Language:**

Simplified Chinese(only)


**介绍**

这是一个随机选择软件和方法的Python脚本。
它可以随机选择一个软件和对应的方法，或者添加新的软件和方法。


**变量解释**

*softwares*: 包含所有软件名称的列表。

*modes*: 一个字典，键为软件名称，值为该软件对应的方法列表。

*keys*: 一个字典，包含各种功能的关键词，用于识别用户输入。

*i*: 用户输入的字符串，用于选择功能。

*i2*: 用户输入的字符串。

*s和 m*: 分别表示随机选择的软件名称和方法名称。

*software_name*: 软件名称。

*modes_name*: 方法名称列表。

其他变量请参考注释,注释未解释的则可以直接按照名称理解。（局部变量不做解释）


**函数解释**

*add_software(software_name, modes_name):*
software_name为软件名称(str),modes_name为方法名称列表(list)。
正常情况下，其会添加软件和方法。(增加方法由add_mode()函数完成)
当软件已存在时,会尝试添加方法。(增加方法由add_mode()函数完成)
当方法为空时，会提示错误。

*add_mode(software_name, modes_name):*
software_name为软件名称(str),modes_name为方法名称列表(list)。
正常情况下，其为已有的软件会添加方法。
当软件不存在时，会提示错误。
当方法为空时，会提示错误。
当方法全部存在时，不会有任何作用。

*choice_software():*
随机选择一个软件和对应的方法，并返回一个列表，包含软件名称和方法名称。

*check_key(i, word_list):*
检查用户输入的字符串i中是否包含word_list中的任意一个关键词。

*save_data():*
将当前的softwares和modes数据保存到本地的json文件中。

*error(reason,advice,annotation):*
reason为原因(str,输入错误信息字符串即可),advice为推荐解决方案(str,默认为None),info为信息及退出原因(str,默认为None,填写此项可更好的定位问题)。
仅在问题导致无法正常运行时使用。


**代码逻辑**

请参考注释。


**文件储存路径**

*Windows*:C:\Users\用户名\AppData\Local\choise_software\data.json

*Linux & MacOS*:暂时不支持


**其他信息**

*最低Python版本*:3.6.0

*依赖库*:random(用于随机数),json(用于json文件保存),os(用于文件操作)

*最后更新时间*:2025.8.20
