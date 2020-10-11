from fractions import Fraction

class fracHandle:
    def __init__(self):
        self
    #分数变为字符串
    def fracToStr(self,fraction):
        numer = fraction.numerator
        denom = fraction.denominator
        if denom == 0:
            return False
        INT = int(numer / denom)
        LEFT = numer % denom
        if LEFT==0 or denom >= numer:
            return str(Fraction(numer, denom))
        else:
            return str(INT) + '\'' + str(Fraction(LEFT, denom))
    #字符串变为分数
    def strToFrac(self,string):
        #如果是带分数
        if '\'' in string:
            fullFrac = string.split('\'')
            INT = int(fullFrac[0])
            NUMERATOR = int((fullFrac[1].split('/'))[0])
            DENOMINATOR =int((fullFrac[1].split('/'))[1])
            return Fraction((INT*DENOMINATOR+NUMERATOR),DENOMINATOR)
        elif '/' in string:
            NUMERATOR = int((string.split('/'))[0])
            DENOMINATOR = int((string.split('/'))[1])
            return Fraction(NUMERATOR,DENOMINATOR)
        else :
            return Fraction(int(string),1)
    #分数的计算
    def fracAccount(self,frac1,frac2,sign):
        if(sign == '+'):
            return frac1+frac2
        elif(sign == '-'):
            if frac1<frac2:
                return False
            else:
                return frac1-frac2
        elif(sign == '*'):
            return frac1*frac2
        else:
            if frac2 == 0:
                return False
            else:
                return frac1/frac2