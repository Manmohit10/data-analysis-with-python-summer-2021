#!/usr/bin/env python3

class Rational(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __mul__(self, number):
        return Rational(self.num*number.num,self.den*number.den)
    def __truediv__(self,number):
        return Rational(self.num*number.den,self.den*number.num)
    def __add__(self,number):
        mult=self.den*number.den
        return Rational(self.num*(mult/self.den)+number.num*(mult/number.den),mult)
    def __sub__(self, number):
        mult=self.den*number.den
        return Rational(self.num*(mult/self.den)-number.num*(mult/number.den),mult)
    def __eq__(self,number):
        mult=self.den*number.den
        return self.num*(mult/self.den) == number.num*(mult/number.den)
    def __gt__(self,number):
        mult=self.den*number.den
        return self.num*(mult/self.den) > number.num*(mult/number.den)
        '''
        if num1.b == num2.b:
            return num1.b > num2.b
        else:
            return num1.a*num2.b > num2.a*num1.b
        '''
    def __lt__(self, number):
        mult=self.den*number.den
        return self.num*(mult/self.den) < number.num*(mult/number.den)
        '''
        if num1.b == num2.b:
            return num1.b < num2.b
        else:
            return num1.a*num2.b < num2.a*num1.b
        '''

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()