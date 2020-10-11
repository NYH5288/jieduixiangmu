import random
from fractions import Fraction
from fracHandle import fracHandle
from isRepeat import testRepeat

class randomMake:
    def __init__(self,repeat,range):
        self.repeat = repeat
        self.range = range
    #生成两个数的题目
    def question_2bits(self,order):
        while True:
            frac_Handle = fracHandle()
            sign = self.random_sign()
            numberList = []
            signList = []
            firstNum = self.random_frac()
            secondNum = self.random_frac()#生成两个分数

            question = ''
            rightAnswer = ''
            numberList.append(str(firstNum)+','+str(secondNum))     #将生成的数字和符号放在字典同一个位置
            signList.append(sign)
            if(self.repeat.isRepeat(numberList,signList) == True):  #检测此组数字和运算符是否重复
                rightAnswer = frac_Handle.fracAccount(firstNum,secondNum,sign)
                if rightAnswer != False:
                    rightAnswer = fracHandle.fracToStr(self,rightAnswer)
                    question = str(order) + ". " + frac_Handle.fracToStr(firstNum) + " " + sign+" "+ frac_Handle.fracToStr(
                        secondNum) + " ="
                else:
                    continue
            else:
                continue
            #将问题写入 Exercise.txt中，将答案写入Answer.txt中
            with open("Exercise.txt",'a') as exercise_file:
                exercise_file.write(question+"\n")
                exercise_file.close()
            with open("Answer.txt",'a') as Answer_file:
                Answer_file.write(str(order)+". "+rightAnswer+"\n")
                Answer_file.close()
            break
    #生成三个数的题目
    def question_3bits(self,order):
        while True:
            frac_Handle = fracHandle()
            #生成相应的数字和符号
            sign1 = self.random_sign()
            sign2 = self.random_sign()
            numberList = []
            signList = []
            firstNum = self.random_frac()
            secondNum = self.random_frac()
            thirdNum = self.random_frac()

            question = ''
            rightAnswer = ''
            numberList.append(str(firstNum) + ',' + str(secondNum)+','+str(thirdNum))
            signList.append(sign1+','+sign2)
            if self.repeat.isRepeat(numberList,signList)== True:    #检测是否重复
                brackets = random.randint(0,2)#随机生成括号的位置
                # 不生成括号
                if(brackets == 0):
                    question = str(order) + ". " + frac_Handle.fracToStr(
                        firstNum) + " " + sign1 + " " + frac_Handle.fracToStr(
                        secondNum) +" "+ sign2 +" "+frac_Handle.fracToStr(thirdNum)+" ="
                    #如果前面是加号和减号而后面不是
                    if (sign1 == '+' or sign1 == '-') and (sign2=='*' or sign2=='÷'):
                        firstSum = frac_Handle.fracAccount(secondNum,thirdNum,sign2)
                        if firstSum != False:
                            rightAnswer = frac_Handle.fracAccount(firstNum,firstSum,sign1)
                            if rightAnswer != False:
                                rightAnswer = frac_Handle.fracToStr(rightAnswer)
                            else:
                                continue
                        else:
                            continue
                    #其他情况
                    else:
                        firstSum = frac_Handle.fracAccount(firstNum, secondNum, sign1)
                        if firstSum != False:
                            rightAnswer = frac_Handle.fracAccount(firstSum, thirdNum, sign2)
                            if rightAnswer != False:
                                rightAnswer = frac_Handle.fracToStr(rightAnswer)
                            else:
                                continue
                        else:
                            continue
                #左边加一个括号：
                elif(brackets==1):  #左边加括号
                    question = str(order) + ". (" + frac_Handle.fracToStr(
                        firstNum) + " " + sign1 + " " + frac_Handle.fracToStr(
                        secondNum) +") "+ sign2 + " " + frac_Handle.fracToStr(thirdNum) + " ="
                    firstSum = frac_Handle.fracAccount(firstNum, secondNum, sign1)
                    if firstSum != False:
                        rightAnswer = frac_Handle.fracAccount(firstSum, thirdNum, sign2)
                        if rightAnswer != False:
                            rightAnswer = frac_Handle.fracToStr(rightAnswer)
                        else:
                            continue
                    else:
                        continue
                #右边加括号
                else:
                    question = str(order) + ". " + frac_Handle.fracToStr(
                        firstNum) + " " + sign1 + " (" + frac_Handle.fracToStr(
                        secondNum) + " " + sign2 + " " + frac_Handle.fracToStr(thirdNum) + ") ="

                    firstSum = frac_Handle.fracAccount(secondNum, thirdNum, sign2)
                    if firstSum != False:
                        rightAnswer = frac_Handle.fracAccount(firstNum, firstSum, sign1)
                        if rightAnswer != False:
                            rightAnswer = frac_Handle.fracToStr(rightAnswer)
                        else:
                            continue
                    else:
                        continue

                with open("Exercise.txt",'a') as exercise_file:
                    exercise_file.write(question+"\n")
                    exercise_file.close()
                with open("Answer.txt",'a') as Answer_file:
                    Answer_file.write(str(order)+". "+rightAnswer+"\n")
                    Answer_file.close()
                break
            #运算式子重复
            else:
                continue
    #生成四个数的题目
    def question_4bits(self,order):
        signList =[]
        numberList = []
        braLen = 0
        signLenth = 0
        mustSign = 0
        frac_handle = fracHandle()

        #生成三个符号
        while(signLenth<3):
            makeBra = random.randint(0,3)
            #生成左括号
            if mustSign == 1 or (makeBra > 1):
                signList.append(self.random_sign())
                signLenth = signLenth + 1
                mustSign = 0
            elif makeBra==0:
                    signList.append('(')
                    braLen = braLen+1
                    mustSign = 1
            elif makeBra==1:
                if braLen != 0:
                    signList.append(')')
                    braLen = braLen - 1
                    mustSign = 0
                else:
                    continue
        while braLen > 0:
            signList.append(')')
            braLen = braLen - 1
        for i in range(4):
            numberList.append(frac_handle.fracToStr(self.random_frac()))
        numberNext=True
        question = str(order)+'. '
        n=0
        i=0
        while n<len(numberList) or i<len(signList):
            if n<len(numberList):
                number=numberList[n]
            if i<len(signList):
                sign=signList[i]
            if sign=='(' :
                question+=str(sign)
                i+=1
            elif numberNext==True:
                question+=str(number)
                numberNext=False
                n+=1
            elif sign==')':
                question+=str(sign)+' '
                i+=1
            else:
                question+=' '+str(sign)+' '
                numberNext=True
                i+=1

        with open("Exercise.txt", 'a') as exercise_file:
            exercise_file.write(question+'=' + "\n")
            exercise_file.close()
        with open("Answer.txt", 'a') as Answer_file:
            Answer_file.write(str(order) + ". "  + "\n")
            Answer_file.close()


    #随机生成符号
    def random_sign(self):
        randomSign = random.randint(0, 3)
        if randomSign == 0:
            sign = '+'
        elif randomSign == 1:
            sign = '-'
        elif randomSign == 2:
            sign = '*'
        else:
            sign = '÷'
        return sign
    #随机生成分数
    def random_frac(self):
        while(True):
            numer = random.randint(0, self.range)  # 分子
            dno = random.randint(1, self.range)  # 分母
            Num = Fraction(numer, dno)
            if Num:
                break
        return Num



