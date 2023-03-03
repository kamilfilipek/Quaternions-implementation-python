# Quaternions basic operations implementation in Python
## Mathematical background
### Introduction
Quaternion, in algebra, is a generalization of two-dimensional complex numbers to three dimensions. 

The quaternions are the most widely known and used hypercomplex numbers, though they have been mostly replaced in practice by operations with matrices and vectors. Still, the quaternions can be regarded as a four-dimensional vector space formed by combining a real number with a three-dimensional vector, with a basis (set of generating vectors) given by the unit vectors $1, i, j$, and $k$ such that
$$i^2 = j^2 = k^2 = ijk = −1$$

Quaternions were first described by the Irish mathematician William Rowan Hamilton in 1843 and applied to mechanics in three-dimensional space. 



### Definition
A quaternion is an expression of the form
$$a + b i + c j + d k$$,
where $a, b, c, d$, are real numbers, and $i, j, k$, are symbols that can be interpreted as unit-vectors pointing along the three spatial axes. 
In practice, if one of $a, b, c, d$ is $0$, the corresponding term is omitted; 
if $a, b, c, d$ are all zero, the quaternion is the zero quaternion, denoted 0; 
if one of $b, c, d$ equals $1$, the corresponding term is written simply $i, j, or k$.  

Hamilton describes a quaternion $q = a + b i + c j + d k$, as consisting of a scalar part and a vector part. The quaternion $b i + c j + d k$ is called the vector part (sometimes imaginary part) of $q$, and a is the scalar part (sometimes real part) of $q$. A quaternion that equals its real part (that is, its vector part is zero) is called a scalar or real quaternion, and is identified with the corresponding real number. That is, the real numbers are embedded in the quaternions.



## Matrix representations
Using 4 × 4 real matrices, that same quaternion can be written as

$$\
  \begin{bmatrix}
    a & -b & -c & -d \\
    b & a & -d & c \\
    c & d & a & -b \\
    d & -c & b & a
  \end{bmatrix}
\$$

However, the representation of quaternions in $M(4, ~ \mathbb{R})$ is not unique. For example, the same quaternion can also be represented as

$$\
  \begin{bmatrix}
    a & d & -b & -c \\
    -d & a & c & -b \\
    b & -c & a & -d \\
    c & b & d & a
  \end{bmatrix}
\$$

There exist 48 distinct matrix representations of this form in which one of the matrices represents the scalar part and the other three are all skew-symmetric.


## Implementation in Python
The definition of the **Quaternion class** is as follows:
```python
class Quaternion:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.q = [float(a), float(b), float(c), float(d)]
```

You can use **__str()__** function to print the quaternion.
```python
def __str__ (self):
  output = f"{str(self.q[0])}e"                         
  output += f" - {str(-self.q[1])}i" if self.q[1] < 0 else f" + {str(self.q[1])}i"
  output += f" - {str(-self.q[2])}j" if self.q[2] < 0 else f" + {str(self.q[2])}j"
  output += f" - {str(-self.q[3])}k" if self.q[3] < 0 else f" + {str(self.q[3])}k"

  return output
```
### Adding quaternions:
$$q_1 + q_2 ~ = ~ a_1e ~ + ~ b_1i ~ + ~ c_1j ~ + ~ d_1k ~ + ~ a_2e ~ + ~ b_2i ~ + ~ c_2j ~ + ~ d_2k ~ =$$ 
$$= (a_1 + a_2)e ~ + ~ (b_1 + b_2)i ~ + ~ (c_1+c_2)j ~ + ~ (d_1+d_2)k$$

where
$$a_1, ~ a_2, ~ b_1, ~ b_2, ~ c_1,~ c_2,~ d_1,~ d_2 ~ \in ~ \mathbb{R}$$




### Subtracting quaternions:
$$q_1 - q_2 ~ = ~ a_1e ~ + ~ b_1i ~ + ~ c_1j ~ + ~ d_1k  ~ - ~ (a_2e ~ + ~ b_2i ~ + ~ c_2j ~ + ~ d_2k) ~ =
koza x = 3$$






sources: \
https://www.britannica.com/science/quaternion \
https://en.wikipedia.org/wiki/Quaternion
