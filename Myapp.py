# -*- coding:utf-8 -*-
from sys import argv

import random
import time
from demo_random import randomMake
from fracHandle import fracHandle
from isRepeat import testRepeat
from fractions import Fraction



class exercise:
    def __init__(self,account = 100,range = 10):
        self.account = account
        self.range = range
    #生成题目
    def makeExe(self):
        localtime = time.asctime(time.localtime(time.time()))   #生成题目时间，以便核对所创建题目是否为之前重复
        #清理文件内容
        with open("Exercise.txt", 'w') as exercise_file:
            exercise_file.write("题目数量 ： "+ str(self.account)+ "\t时间 ：" + localtime+ "\n")
            exercise_file.close()
        with open("Answer.txt", 'w') as Answer_file:
            Answer_file.close()

        que_order = 0
        repeat = testRepeat()
        makeQue = randomMake(repeat,self.range)
        #生成account道题
        while que_order < self.account:
            choose2_4 = 2+random.randint(0,2)
            #两个数的运算题生成计数
            if choose2_4 == 2:
                makeQue.question_2bits(que_order+1)
                que_order = que_order + 1
            #三个数的运算题生成计数
            elif choose2_4 == 3:
                makeQue.question_3bits(que_order+1)
                que_order = que_order + 1
            else:
                makeQue.question_4bits(que_order + 1)
                que_order = que_order + 1
    #核对答案
    def confirmExe(self,exeFile,userFile):
        corrctQue = []  #记录用户的错题和对题
        wrongQue = []
        try:
            with open(exeFile) as exeFile:  #读取题目文件
                with open(userFile) as userFile:    #读取用户文件
                    orderLine = 1   #记录核对的第几道题
                    lineExe = exeFile.__next__()
                    fracAcc = fracHandle()
                    for lineExe in exeFile: #遍历题目
                        lineExe = lineExe.strip()
                        div = lineExe.split(" ")
                        # 两个数的题目
                        if len(div) == 5:
                            frac1 = fracAcc.strToFrac(div[1])
                            frac2 = fracAcc.strToFrac(div[3])
                            rightAnswer = fracAcc.fracAccount(frac1, frac2, div[2])
                            rightAnswer = fracAcc.fracToStr(rightAnswer)
                        # 三个数
                        elif len(div) == 7:
                            #如果式子中有括号
                            if '(' in lineExe:
                                for locate in range(7):
                                    #如果式子中有括号
                                    if '(' in div[locate]:
                                        #如果括号在左边
                                        if locate==1:
                                            leftFrac = fracAcc.strToFrac(div[1].replace("(",""))
                                            rightFrac = fracAcc.strToFrac(div[3].replace(")",""))
                                            thirdFrac = fracAcc.strToFrac(div[5])
                                            firstSum = fracAcc.fracAccount(leftFrac,rightFrac,div[2])
                                            rightAnswer = fracAcc.fracToStr(fracAcc.fracAccount(firstSum,thirdFrac,div[4]))
                                        else:
                                            leftFrac = fracAcc.strToFrac(div[3].replace("(", ""))
                                            rightFrac = fracAcc.strToFrac(div[5].replace(")", ""))
                                            thirdFrac = fracAcc.strToFrac(div[1])
                                            firstSum = fracAcc.fracAccount(leftFrac, rightFrac, div[4])
                                            rightAnswer = fracAcc.fracToStr(
                                                fracAcc.fracAccount(thirdFrac, firstSum, div[2]))
                            #如果式子没括号
                            else:
                                leftFrac = fracAcc.strToFrac(div[1])
                                rightFrac = fracAcc.strToFrac(div[3])
                                thirdFrac = fracAcc.strToFrac(div[5])
                                if(div[2]=='+' or div[2]=='-') and (div[4]=='*' or div[4]=="÷"):
                                    firstSum = fracAcc.fracAccount(rightFrac,thirdFrac,div[4])
                                    rightAnswer = fracAcc.fracToStr(fracAcc.fracAccount(leftFrac,firstSum,div[2]))
                                else:
                                    firstSum = fracAcc.fracAccount(leftFrac,rightFrac,div[2])
                                    rightAnswer = fracAcc.fracToStr(fracAcc.fracAccount(firstSum,thirdFrac,div[4]))
                        else:
                            print("题目出错了！")
                        try :
                            userAnswer = userFile.__next__().split(' ', 2)
                            #如果用户答案还存在的话
                            if userAnswer[0] != '\n':
                                if (userAnswer[1].strip() == rightAnswer.strip()):
                                    corrctQue.append(orderLine)
                                else:
                                     wrongQue.append(orderLine)
                            #用户答案已空
                            else:
                                print("同学，你第" + str(orderLine) + "题未完成哦！")
                                wrongQue.append(orderLine)
                            orderLine = orderLine + 1
                        except StopIteration :
                            print("同学，你第"+str(orderLine)+"题未完成哦！")
                            wrongQue.append(orderLine)
                            orderLine = orderLine + 1

                    print()
                    print("批卷完毕！答题情况如下：")
                    print("Corrct: " + str(len(corrctQue)))
                    print(str(corrctQue))
                    print("Wrong: " + str(len(wrongQue)))
                    print(str(wrongQue))

                    #答题情况写入Grade.txt
                    with open("Grade.txt", 'w') as grade_file:
                        grade_file.write("Corrct: " + str(len(corrctQue)))
                        grade_file.write(str(corrctQue) + '\n')
                        grade_file.write("Wrong: " + str(len(wrongQue)))
                        grade_file.write(str(wrongQue) + '\n')
        except FileNotFoundError:
            print("找不到文件！请重新输入！")

    def confirm_4bit(self):
        self


#输入要求题目模块
#
#



inputLen = len(argv)
if (inputLen==5) and ('-r' in argv) and ('-n' in argv):
    #通过输入文件名以及设定的数目来获取题目的数量和范围
    for i in range(inputLen):
        if argv[i] == '-r':
            userRange = int(argv[i+1])
        elif argv[i] == '-n':
            userAccount = int(argv[i+1])
        else:
            continue
    mathExercise = exercise(userAccount,userRange)
    mathExercise.makeExe()
    print("要求的小学计算题已生成完成！请在文件user.txt中查看完成！")

#核对答案的功能设定
elif (inputLen==5) and (argv[1] == '-e') and (argv[3] == '-a'):
    mathExercise = exercise()
    exerciseFile = argv[2]  #获取题目文件
    answerFile = argv[4]    #获取用户需要核对的文件
    mathExercise.confirmExe(exerciseFile,answerFile)
    print("同学，您的答题情况已存入Grade.txt中")
else:
    print("输入错误！正确的输入格式：Myapp.exe -n *** -r ***(n代表题目数量、r代表数字范围）")