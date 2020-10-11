#检测是否重复的类
class testRepeat:
    def __init__(self):
        self.oldNumber = {}     #已有的数字组合
        self.signDic = {}       #已有的符号组合
    #检测是否式子重复
    def isRepeat(self,numberList,signList):
        numberList.sort()
        signList.sort()
        if self.oldNumber:
            for key,value in self.oldNumber.items():
                if value==numberList and self.signDic[key]==signList:
                    return False
            self.oldNumber[key+1] = numberList
            self.signDic[key+1] = signList
        else:
            self.oldNumber[0]  = numberList
            self.signDic[0] = signList
        return True