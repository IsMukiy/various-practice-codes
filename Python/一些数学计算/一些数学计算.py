#一些数学计算




'''
MIT License

Copyright (c) 2025 IsMukiy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''




#变量定义
__all__ = ['plus','minus','multiply','divide','remainder','power','xor','triangle']




#函数定义
def plus(n1:int|float,n2:int|float) -> int|float:#加法
    try:
        return n1 + n2

    except ValueError:
        raise ValueError

    except Exception as e:
        raise e


def minus(minuend:int|float,subtrahend:int|float) -> int|float:#减法
    try:
        return minuend - subtrahend

    except ValueError:
        raise ValueError

    except Exception as e:
        raise e


def multiply(n1:int|float,n2:int|float) -> int|float:#乘法
    try:
        return n1 * n2

    except ValueError:
        raise ValueError

    except Exception as e:
        raise e


def divide(dividend:int|float,divisor:int|float,exact:bool=False) -> int|float:#除法
    try:
        if exact:
            return dividend // divisor
        
        else:
            return dividend / divisor

    except ValueError:
        raise ValueError
    
    except ZeroDivisionError:
        raise ZeroDivisionError

    except Exception as e:
        raise e


def remainder(dividend:int|float,divisor:int|float) -> int|float:#取余
    try:
        return dividend % divisor

    except ValueError:
        raise ValueError

    except ZeroDivisionError:
        raise ZeroDivisionError

    except Exception as e:
        raise e


def power(base:int|float,exponent:int|float) -> int|float:#次方
    try:
        return base ** exponent

    except ValueError:
        raise ValueError

    except Exception as e:
        raise e


def xor(n1:int|bool,n2:int|bool) -> int:#异或
    try:
        return n1 ^ n2

    except ValueError:
        raise ValueError

    except TypeError:
        raise TypeError

    except Exception as e:
        raise e


def _check_type(value:list,tp:int|float|tuple) -> bool:
    try:
        for i in value:#检查参数类型
            if not isinstance(i,tp):
                return False
        
        return True
    
    except Exception:
        return False




#定义类
class triangle:#三角形
    class istri:#三角形分辨
        def angle(angles:list) -> bool:#角度判断
            if (len(angles) < 2) or (not _check_type(angles[0:3],(int,float))):
                return ValueError
        
            if len(angles) >= 3:
                if (angles[0] + angles[1] + angles[2]) == 180:#如果角度总和超过了180°
                    return True#可以组成

                else:
                    return False#不能组成

            else:
                if angles[0] + angles[1] > 180:#如果角度总和超过了180°
                    return False#不能组成

                else:
                    return True#可以组成
        

        def length(lengths:list) -> bool:#长度判断
            if ((len(lengths) < 3) or (len(lengths) > 3)) or ((not isinstance(lengths,list)) or (not _check_type(lengths[0:3],(int,float)))):#判断
                return ValueError

            #找到最小的两个值
            n1 = min(lengths)
            lengths.remove(n1)
            n2 = min(lengths)

            if n1 + n2 >= lengths[0]:#如果长度大于第三边
                return True#可以组成

            else:
                return False#不能组成


    class find_No3:
        def find_angle(angle1:int|float,angle2:int|float):#找第三个角的角度
            if (not _check_type([angle1,angle2],(int,float))) or (angle1 + angle2) > 180:#检查
                raise ValueError

            return 180 - angle1 - angle2 # 直接用180°减去两个角度


        def find_length(side_length1:int|float,side_length2:int|float):#找第三条边的长度
            if not _check_type([side_length1side_length2],(int,float)):#检查
                raise ValueError
            
            side_length1,side_length2 = abs(side_length1),abs(side_length2)#转换为正数
            numbers = []#候选列表

            if side_length1 > side_length2: # 如果第一条边大于第二条边
                r = side_length1 - side_length2 + 1 # 用第一条边减去第二条边

            else:
                r = side_length2 - side_length1 + 1 # 用第二条边减去第一条边

            for i in range(r,side_length1 + side_length2): # 逻辑：从最小可能的边长到最大可能的边长
                numbers.append(i)
            
            return numbers
