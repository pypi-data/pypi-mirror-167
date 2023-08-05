#
# Helper functions for finding root of a complex number
#
def arctan_taylor(x, terms=9):
    '''
    arctan for small x with Taylor series
    effective for |x| < 0.1. stops working when |x| -> 1.0 (convergence radius)
    '''
    getcontext().prec += 2 # for extra precision
    # use Ghorners scheme
    t = Decimal(0)
    x2 = x * x
    for n in range(2 * terms - 1, 0, -2):
        t = Decimal(1) / Decimal(n) - x2 * t
    getcontext().prec -= 2
    return +(x * t) # unar plus to apply precision

def arctan_taylor_with_reduction(real, imag, terms, threshold=0.1):
    '''
    use argument reduction to make finding arctan more effective
    complex number argument is calculated according to rules
    '''
    if real != 0:
        x = imag / real
        reductions = 0
        while abs(x) > threshold:
            x = x / (1 +  Decimal(1 + x * x).sqrt())
            reductions += 1
        
        if real > 0:
            return +arctan_taylor(x, terms=terms) * 2**reductions
        elif real < 0:
            if imag >= 0:
                return +arctan_taylor(x, terms=terms) * 2**reductions + pi()
            elif imag < 0:
                return +arctan_taylor(x, terms=terms) * 2**reductions - pi()
    else:
        if imag > 0:
            return pi() / 2
        elif imag < 0:
            return -pi() / 2

def pi():
    # calculate pi with set precision
    getcontext().prec += 2 # for extra precision
    lasts, t, s, n, na, d, da = 0, Decimal(3), 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s # unar plus to apply precision

def cos(x):
    # calculate cos with set precision
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = Decimal(0), Decimal(0), Decimal(1), Decimal(1), Decimal(1), Decimal(1)
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s # unar plus to apply precision

def sin(x):
    # calculate sin with set precision
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = Decimal(1), Decimal(0), Decimal(x), Decimal(1), Decimal(x), Decimal(1)
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s # unar plus to apply precision

#
# ComplexDecimal class provides arbitrary precision complex numbers and all math operators on them.
#
from decimal import Decimal, getcontext
getcontext().prec = 36

class ComplexDecimal:
    def __init__(self, real=0, imag=0) -> None:
        if type(real) not in [int, Decimal]:
            raise ValueError
        if type(imag) not in [int, Decimal]:
            raise ValueError
        if type(real) == Decimal:
            if real.is_zero():
                self.real = Decimal(0)
            else:
                self.real = real
        else:
            self.real = Decimal(real)
        if type(imag) == Decimal:
            if imag.is_zero():
                self.imag = Decimal(0)
            else:
                self.imag = imag
        else:
            self.imag = Decimal(imag)

    # defines + op. (ComplexDecimal + <SupportedType>)
    def __add__(self, other):
        other_type = type(other)
        if other_type in [ComplexDecimal, complex]:
            real = self.real + other.real
            imag = self.imag + other.imag
        elif other_type == Decimal:
            real = self.real + other
            imag = self.imag
        elif other_type == int:
            real = self.real + other
            imag = self.imag
        else:
            return TypeError
        return ComplexDecimal(real, imag)
    
    # defines - op. (ComplexDecimal - <SupportedType>)
    def __sub__(self, other):
        other_type = type(other)
        if other_type in [ComplexDecimal, complex]:
            real = self.real - other.real
            imag = self.imag - other.imag
        elif other_type == Decimal:
            real = self.real - other
            imag = self.imag
        elif other_type == int:
            real = self.real - other
            imag = self.imag
        else:
            return TypeError
        return ComplexDecimal(real, imag)

    # defines * op. (ComplexDecimal * <SupportedType>)
    def __mul__(self, other):
        other_type = type(other)
        if other_type == ComplexDecimal:
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
        elif other_type == Decimal:
            real = self.real * other
            imag = self.imag * other
        elif other_type == int:
            real = self.real * other
            imag = self.imag * other
        else:
            return TypeError
        return ComplexDecimal(real, imag)

    # defines / op. (ComplexDecimal / <SupportedType>)
    def __truediv__(self, other):
        other_type = type(other)
        if other_type == ComplexDecimal:
            if other.real or other.imag:
                real = (self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2)
                imag = (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2)
            else:
                return ZeroDivisionError
        elif other_type == Decimal:
            if other:
                real = self.real / other
                imag = self.imag / other
            else:
                return ZeroDivisionError
        elif other_type == int:
            if other:
                real = self.real / other
                imag = self.imag / other
            else:
                return ZeroDivisionError
        else:
            return TypeError
        return ComplexDecimal(real, imag)

    # defines ** op. (ComplexDecimal ** <SupportedType>)
    def __pow__(self, power):
        if self.real == 0 and self.imag == 0:
            return ComplexDecimal(0, 0)
        elif type(power) in [Decimal, int]: # finding root
            # use Moivre formula
            r2 = self.real**2 + self.imag**2
            r = r2.sqrt()
            theta = arctan_taylor_with_reduction(self.real, self.imag, terms=getcontext().prec)
            zn = r**power
            return ComplexDecimal(zn * cos(power * theta), zn * sin(power * theta))
        return TypeError

    # defines unar - op. (-ComplexDecimal)
    def __neg__(self):
        return ComplexDecimal(-self.real, -self.imag)

    # defines == op. (ComplexDecimal == <SupportedType>)
    def __eq__(self, other) -> bool:
        if type(other) not in [ComplexDecimal, complex]:
            return TypeError
        return self.real == other.real and self.imag == other.imag

    def __repr__(self) -> str:
        if self.imag >= 0:
            imag = f'+{self.imag.normalize()}'
        else:
            imag = f'{self.imag.normalize()}'
        return f'({self.real.normalize()}{imag}j)'