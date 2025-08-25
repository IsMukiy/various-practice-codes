#不知道用啥就点这个




r'''
README
语言/Language:
Simplified Chinese(only)


介绍
这是一个随机选择软件和方法的Python脚本。
它可以随机选择一个软件和对应的方法，或者添加新的软件和方法。


变量解释
softwares: 包含所有软件名称的列表。

modes: 一个字典，键为软件名称，值为该软件对应的方法列表。

keys: 一个字典，包含各种功能的关键词，用于识别用户输入。

i: 用户输入的字符串，用于选择功能。

i2: 用户输入的字符串。

s和m: 分别表示随机选择的软件名称和方法名称。

software_name: 软件名称。

modes_name: 方法名称列表。

其他变量请参考注释,注释未解释的则可以直接按照名称理解。（局部变量不做解释）


函数解释
add_software(software_name, modes_name): 
software_name为软件名称(str),modes_name为方法名称列表(list)。
正常情况下，其会添加软件和方法。(增加方法由add_mode()函数完成)
当软件已存在时,会尝试添加方法。(增加方法由add_mode()函数完成)
当方法为空时，会提示错误。

add_mode(software_name, modes_name):
software_name为软件名称(str),modes_name为方法名称列表(list)。
正常情况下，其为已有的软件会添加方法。
当软件不存在时，会提示错误。
当方法为空时，会提示错误。
当方法全部存在时，不会有任何作用。

choice_software():
随机选择一个软件和对应的方法，并返回一个列表，包含软件名称和方法名称。

check_key(i, word_list):
检查用户输入的字符串i中是否包含word_list中的任意一个关键词。

save_data():
将当前的softwares和modes数据保存到本地的json文件中。

error(reason,advice,annotation):
reason为原因(str,输入错误信息字符串即可),advice为推荐解决方案(str,默认为None),info为信息及退出原因(str,默认为None,填写此项可更好的定位问题)。
仅在问题导致无法正常运行时使用。


代码逻辑
请参考注释。


文件储存路径
Windows:C:\Users\用户名\AppData\Local\choise_software\data.json
Linux&MacOS:暂时不支持


其他信息
最低Python版本:3.6.0(因需要使用f字符串、类型注解等功能)

推荐Python版本:3.10.0及以上

依赖库:random(用于随机数),json(用于json文件保存),os(用于文件操作)
'''




#导入库
import random,json,os




#数据
softwares = ['Godot','抖音','Code software','网易发烧游戏','Steam','360安全卫士','PCL','网易云音乐','笔']
modes = {
    'Godot':['开发"房车模拟器"','开发"Forever loading"'],
    '抖音':['刷视频'],
    'Code software':['开发Python','开发"秘密行动"'],
    '网易发烧游戏':['玩Minecraft'],
    'Steam':['随便乱逛','玩Eraser','玩Stick It to the Stickman Demo','玩Is This Seat Taken Demo'],
    '360安全卫士':['把所有扫描全都干一遍','在"我的电脑"页面扫描','在"木马查杀"页面扫描','在"垃圾清理"页面扫描','在"系统修复”页面扫描','在"优化加速"页面扫描'],
    'PCL':['玩Minecraft'],
    '网易云音乐':['听《Delta Force》相关歌曲','听Liella的歌',"听μ's的歌",'听《LoveLive》相关歌曲'],
    '笔':['写暑假作业'],
    }
keys = {
    '随机选择软件':['随机','选择软件'],
    '添加软件或方法':['添加','加'],
    '添加软件':['添加软件','添加新软件'],
    '添加方法':['添加方法', '添加新方法'],
    '退出':['q','e','退','离'],
    '再来一次':['again','再','重'],
    '完成':['完成','返回','结束'],
    '查看所有软件和方法':['查看'],
    '保存数据到本地':['保存','存'],
    '删除软件或方法':['删','删除'],
    '删除软件':['删除软件','删软件'],
    '删除方法':['删除方法','删方法'],
}




#函数
def add_software(software_name:str,modes_name:list):
    #software_name为软件名称(str),modes_name为方法名称列表(list)
    global softwares, modes

    if software_name == '':#检测软件名称
        print('软件名称不能为空')
        return

    elif software_name in softwares:#检测软件是否已存在
        print(f'软件"{software_name}"已存在，将尝试添加方法...')
        add_mode(software_name, modes_name)
        return

    else:
        softwares.append(software_name)#添加软件到软件列表
        add_mode(software_name, modes_name)#添加方法
        print(f'软件"{software_name}"已添加，所有方法已添加。')#提示


def add_mode(software_name:str,modes_name:list):
    #software_name为软件名称(str),modes_name为方法名称列表(list)
    global softwares, modes

    if software_name not in softwares:#检测软件是否存在
        print('不存在的软件，请先添加软件后再添加方法！')
        return

    for m in modes_name:#m为方法名称
        if m == '':#检测方法名称
            print('方法不能为空')

        elif m in modes[software_name]:#检测方法是否已存在
            print(f'方法"{m}"已存在，将尝试添加其他方法...')

        else:
            modes[software_name].append(m)#添加方法
            print(f'方法"{m}"已添加到软件"{software_name}"中')


def choice_software():
    #s为软件名, m为方法名
    s = random.choice(softwares)#随机选择软件
    m = random.choice(modes[s])#随机选择软件的方法
    return [s,m]


def check_key(i:str,word_list:list):
    #i为用户输入的字符串(str)，word_list为关键词列表(list)
    for word in word_list:#遍历关键词列表
        if word in i:#如果用户输入的字符串中包含关键词
            return True#成立
    return False#不成立


def error(reason:str,advice:str=None,info:str=None):
    print(f'错误:{reason}')#提示错误

    if advice is not None:
        print(f'建议解决方案:{advice}')#提示解决方案（如果已填写）

    if info is not None:
        print(f'相关信息:{info}')#提示信息（如果已填写）
    
    input('回车来退出\n')#提示
    print('--------退出-----------')
    exit(info)#退出



def save_data():
    #保存数据到本地
    global softwares, modes
    try:
        with open(rf'{os.getenv("LOCALAPPDATA")}\choise_software\data.json', 'w', encoding='utf-8') as f:
            json.dump({'softwares': softwares, 'modes': modes}, f, ensure_ascii=False, indent=4)  # 写入数据
        print('数据已保存到本地')#提示数据已保存

    except Exception as e:
        input(f'保存数据失败: {e}')




#储存
if not os.path.exists(rf'{os.getenv("LOCALAPPDATA")}\choise_software'):#如果目录不存在
    try:
        os.makedirs(rf'{os.getenv("LOCALAPPDATA")}\choise_software',exist_ok=True)#创建目录

    except PermissionError as e:
        error(e,'以管理员身份运行此程序(请放心,此程序不会攻击您的电脑)','Create directory fail.')

    except Exception as e:
        error(e,info='Create directory fail.')#提示错误

if not os.path.exists(rf'{os.getenv("LOCALAPPDATA")}\choise_software\data.json'):#如果数据文件不存在
    save_data()#保存默认数据到本地

else:#如果数据文件存在
    try:
        with open(rf'{os.getenv("LOCALAPPDATA")}\choise_software\data.json', 'r', encoding='utf-8') as f:#读取数据文件
            data = json.load(f)#读取数据
            softwares = data['softwares']#读取软件列表
            modes = data['modes']#读取方法列表
        
    except PermissionError as e:
        error(e,'以管理员身份运行此程序(请放心,此程序不会攻击您的电脑)','Load data file fail.')

    except Exception as e:
        error(e,info='Load data file fail.')#提示错误




#主程序
try:
    while True:
        i = input('''请选择功能：
    1.随机选择软件
    2.添加软件和方法
    3.删除软件和方法
    4.查看所有软件和方法
    5.保存数据到本地(退出前务必保存)
    6.退出
    ''')#获取用户输入

        if (i == '1') or (check_key(i, keys['随机选择软件'])):#如果用户选择随机选择软件
            s, m = choice_software()#随机选择软件和方法
            print(f'使用{s}{m}!')#提示

            while True:
                i2 = input('请输入反馈\n')#获取用户反馈
                if check_key(i2, keys['退出']):#如果用户选择退出
                    exit('User exit.')

                elif check_key(i2, keys['再来一次']):#如果用户选择再来一次
                    s, m = choice_software()
                    print(f'使用{s}{m}！')

                elif check_key(i2,keys['完成']):#如果用户选择完成
                    print('会话完成')
                    break#退出循环，回到主菜单

                else:
                    print('无效输入，请重新输入')#提示无效输入
                    print('------重新输入---------')#提示重新输入
                    
                    
        
        elif (i == '2') or (check_key(i, keys['添加软件'])):#如果用户选择添加软件
            print('---二级菜单:添加软件或方法---')
            i2 = input('''请选择添加类型:
1.软件
2.方法
    ''')#获取用户输入
            if (i2 == '1') or (check_key(i2, keys['添加软件'])):
                software_name = input('请输入软件名称：')#获取软件名称
                modes_name = input('请输入方法名称（多个方法用逗号分隔）：').split(',')#获取方法名称
                add_software(software_name, modes_name)#添加软件和方法

            elif (i2 == '2') or (check_key(i2, keys['添加方法'])):
                software_name = input('请输入软件名称：')#获取软件名称
                modes_name = input('请输入方法名称（多个方法用逗号分隔）：').split(',')#获取方法名称
                add_mode(software_name, modes_name)#添加方法
            
            else:
                print('无效输入。')#提示无效输入
        
        elif (i == '3') or (check_key(i, keys['删除软件或方法'])):
            print('---二级菜单:删除软件或方法---')
            i2 = input('''请选择删除类型:
    1.软件
    2.方法
    ''')#获取用户输入
            if (i2 == '1') or (check_key(i2, keys['删除软件'])):
                software_name = input('请输入要删除的软件名称：')#获取软件名称
                if software_name in softwares:#如果软件存在
                    softwares.remove(software_name)#删除软件
                    del modes[software_name]#删除软件对应的方法
                    print(f'软件"{software_name}"及其所有方法已删除。')#提示

                else:
                    print(f'软件"{software_name}"不存在。')

            elif (i2 == '2') or (check_key(i2, keys['删除方法'])):
                software_name = input('请输入要删除方法的软件名称：')#获取软件名称
                if software_name in softwares:#如果软件存在
                    mode_name = input('请输入要删除的方法名称：')#获取方法名称
                    if mode_name in modes[software_name]:#如果方法存在
                        modes[software_name].remove(mode_name)#删除方法
                        print(f'方法"{mode_name}"已从软件"{software_name}"中删除。')#提示

                    else:
                        print(f'方法"{mode_name}"在软件"{software_name}"中不存在。')

                else:
                    print(f'软件"{software_name}"不存在。')

            else:
                print('无效输入。')

        elif (i == '4') or (check_key(i, keys['查看所有软件和方法'])):#如果用户选择查看所有软件和方法
            print('---查看所有软件和方法---')
            for sw,md in modes.items():#遍历所有软件和方法
                print(f'{sw}的方法有:{md}')
        
        elif (i == '5') or (check_key(i, keys['保存数据到本地'])):#如果用户选择保存数据到本地
            save_data()#保存数据到本地

        elif (i == '6') or (check_key(i, keys['退出'])):#如果用户选择退出
            print('--------退出-----------')
            save_data()
            exit('User exit.')#退出程序
        
        else:
            print('无效输入。')#提示无效输入
        
        print('-------新会话----------')#提示新会话开始

except Exception as e:#如果发生错误
    error(e)