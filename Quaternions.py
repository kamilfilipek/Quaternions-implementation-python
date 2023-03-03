import math

class Quaternion:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.q = [float(a), float(b), float(c), float(d)]

    def __str__ (self):
        output = f"{str(self.q[0])}e"                         
        output += f" - {str(-self.q[1])}i" if self.q[1] < 0 else f" + {str(self.q[1])}i"
        output += f" - {str(-self.q[2])}j" if self.q[2] < 0 else f" + {str(self.q[2])}j"
        output += f" - {str(-self.q[3])}k" if self.q[3] < 0 else f" + {str(self.q[3])}k"

        return output


    def __add__(self, other_quaternion):
        return Quaternion(a=self.q[0] + other_quaternion.q[0], b=self.q[1] + other_quaternion.q[1], c=self.q[2] + other_quaternion.q[2], d=self.q[3] + other_quaternion.q[3])

    def __sub__(self, other_quaternion):
        return Quaternion(a=self.q[0] - other_quaternion.q[0], b=self.q[1] - other_quaternion.q[1], c=self.q[2] - other_quaternion.q[2], d=self.q[3] - other_quaternion.q[3])

    def __mul__(self, other_quaternion):
        a1 = self.q[0] * other_quaternion.q[0] - self.q[1] * other_quaternion.q[1] - self.q[2] * other_quaternion.q[2] - self.q[3] * other_quaternion.q[3]
        b1 = self.q[0] * other_quaternion.q[1] + self.q[1] * other_quaternion.q[0] + self.q[2] * other_quaternion.q[3] - self.q[3] * other_quaternion.q[2]
        c1 = self.q[0] * other_quaternion.q[2] - self.q[1] * other_quaternion.q[3] + self.q[2] * other_quaternion.q[0] + self.q[3] * other_quaternion.q[1]
        d1 = self.q[0] * other_quaternion.q[3] + self.q[1] * other_quaternion.q[2] - self.q[2] * other_quaternion.q[1] + self.q[3] * other_quaternion.q[0]
        return Quaternion(a=a1, b=b1, c=c1, d=d1)

    def __truediv__(self, other_quaternion):
        return self * other_quaternion.reciprocal()


    def __invert__(self):
        return self

    def __abs__(self):
        return math.sqrt(self.determinant())


    def conjugate(self):
        return Quaternion(a=self.q[0], b=-self.q[1], c=-self.q[2], d=-self.q[3])

    def determinant(self):
        return self.q[0]*self.q[0] + self.q[1]*self.q[1] + self.q[2]*self.q[2] + self.q[3]*self.q[3]

    def magnitude(self):
        return math.sqrt(self.q[0]*self.q[0] + self.q[1]*self.q[1] + self.q[2]*self.q[2] + self.q[3]*self.q[3])

    def reciprocal(self):
        denominator = self.determinant()
        a1 = self.q[0] / denominator
        b1 = -self.q[1] / denominator
        c1 = -self.q[2] / denominator
        d1 = -self.q[3] / denominator

        return Quaternion(a=a1, b=b1, c=c1, d=d1)


    def print_as_matrix(self):
        print(f"\033[1mQuaternion '{self}' as a real matrix:\033[0m")
        print(f"{self.q[0]}  {self.q[1]}  {-self.q[3]}  {-self.q[2]}")
        print(f"{-self.q[1]}  {self.q[0]}  {-self.q[2]}  {self.q[3]}")
        print(f"{self.q[3]}  {self.q[2]}  {self.q[0]}  {self.q[1]}")
        print(f"{self.q[2]}  {-self.q[3]}  {-self.q[1]}  {self.q[0]}")
  
