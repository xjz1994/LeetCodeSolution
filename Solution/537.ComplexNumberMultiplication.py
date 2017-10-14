
a+biabthe output should be also in this form
# =C9=E8z1=a+bi=A3=ACz2=c+di(a=A1=A2b=A1=A2c=A1=A2d=A1=CAR)=CA=C7=C8=CE=D2=E2=C1=BD=B8=F6=B8=B4=CA=FD
# =C4=C7=C3=B4=CB=FC=C3=C7=B5=C4=BB=FD(a+bi)(c+di)=(ac-bd)+(bc+ad)i.
class Solution(object):
    def complexNumberMultiply(self, a, b):
        import re
        pattern = re.compile("-*\d+")
        numA = int(pattern.findall(a)[0])
        numB = int(pattern.findall(a)[1])
        numC = int(pattern.findall(b)[0])
        numD = int(pattern.findall(b)[1])
        real = numA * numC - numB * numD
        imaginary = numB * numC + numA * numD
        return str(real) + "+" + str(imaginary) + "i"
