# Quaternions basic operations implementation in Python
## Introduction
Quaternion, in algebra, is a generalization of two-dimensional complex numbers to three dimensions. 

The quaternions are the most widely known and used hypercomplex numbers, though they have been mostly replaced in practice by operations with matrices and vectors. Still, the quaternions can be regarded as a four-dimensional vector space formed by combining a real number with a three-dimensional vector, with a basis (set of generating vectors) given by the unit vectors $1, i, j$, and $k$ such that
$$i^2 = j^2 = k^2 = ijk = −1$$

Quaternions were first described by the Irish mathematician William Rowan Hamilton in 1843 and applied to mechanics in three-dimensional space. 



## Definition
A quaternion is an expression of the form
$$a + b i + c j + d k$$,
where $a, b, c, d$, are real numbers, and $i, j, k$, are symbols that can be interpreted as unit-vectors pointing along the three spatial axes. 
In practice, if one of $a, b, c, d$ is $0$, the corresponding term is omitted; 
if $a, b, c, d$ are all zero, the quaternion is the zero quaternion, denoted 0; 
if one of $b, c, d$ equals $1$, the corresponding term is written simply $i, j, or k$.  

Hamilton describes a quaternion $q = a + b i + c j + d k$, as consisting of a scalar part and a vector part. The quaternion $b i + c j + d k$ is called the vector part (sometimes imaginary part) of $q$, and a is the scalar part (sometimes real part) of $q$. A quaternion that equals its real part (that is, its vector part is zero) is called a scalar or real quaternion, and is identified with the corresponding real number. That is, the real numbers are embedded in the quaternions.



## Matrix representations
$${\displaystyle {\begin{bmatrix}a+bi&c+di\\-c+di&a-bi\end{bmatrix}}.}$$

$$M_{2x2}(\mathbb{C})$$


$$\begin{bmatrix}
z & w \\
-\overline{\rm w} & z 
\end{bmatrix}$$


$\begin{bmatrix}
z & w \\
-\overline{\rm w} & z 
\end{bmatrix}$

$$\left[\begin{array}{cccc}
w1 & w2 & w3 & w4	\\
x1 & x2 & x3 & x4	\\
y1 & y2 & y3 & y4	\\
z1 & z2 & z3 & z4
\end{array}\right]$$

$$\[
  \begin{bmatrix}
    a_{11} & a_{12} & a_{13} & a_{14} \\
    a_{21} & a_{22} & a_{23} & a_{24} \\
    a_{31} & a_{32} & a_{33} & a_{34} \\
    a_{41} & a_{42} & a_{43} & a_{44}
  \end{bmatrix}
\]$$


$\left|x\right| = \left\{\begin{array}{cl}
    x & \textrm{if}\ x \geq 0\\
    -x & \textrm{if}\ x < 0
\end{array}\right.$

Evaluate
$$x + 1$$


$$\[
  y=
  \begin{cases}
    x & \text{if}\quad y \geq 0 \\
    -x & \text{if}\quad y < 0
  \end{cases}
\]$$

$$\frac{2}{3}$$


$$\sum_{2}^{3}2^{-n}=1$$

sources: \
https://www.britannica.com/science/quaternion \
https://en.wikipedia.org/wiki/Quaternion
