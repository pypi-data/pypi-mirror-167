# Matrix

> This is a Module which can perform Matrix Functions.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Functions-Methods](#functions-methods)
- [Author Info](#author-info)

---

## Description

Matrix can be Created using 2D Arrays (Lists in Python), but Complex Functions like Determinant(N X N), Inverse, Matrix Arithmetic Operations ... is Required. I hope this Module can save your time and effort as well as provide you with some consistency across your Matrix Journey.

[Back To The Top](#matrix)

---

## Functions-Methods

### Methods List

#### __init__(self,r,c)
> This method of the Class will initialize the class by creating a matrix A(r,c). And will create the matrix. All elements will be 0.

> obj=Matrix(3,3)

#### inputAdd(self)
> This Method of the Class will change the elements of the Matrix by User Input.

> obj.inputAdd()

#### listTomatrix(self, lst:list)
> This method of the Class converts the List Parameter to Matrix (self.matrix).

> obj.listTomatrix([1,2,3,4,5,6,7,8,9])

#### printMatrix(self)
> This Method prints the Matrix using Tabulate Module.

> obj.printMatrix()

#### transpose(self)
> This Method Returns a Transpose of the Matrix (self.matrix).

> Return Type -> Matrix

> obj2 = obj.transpose()

#### sizeMatrix(self)
> This Method returns the Dimensions of the Matrix.

> Return Type -> Tuple

> tuple1 = obj.sizeMatrix()

#### matrixMultiplication(self, m2:Matrix)
> This method returns the Result of the Multiplication of 2 Matrices. One Matrix is the Parameter and other is the Matrix created while initializing the Class.

> Return Type -> Matrix

> C = A x B

> obj3 = obj.matrixMultiplication(obj2)

#### matrixAddition(self, m2:Matrix)
> This Method returns the Result of the Addition of 2 Matrices. One Matrix is the Parameter and other is the Matrix created while initializing the Class.
Return Type -> Matrix

> C = A + B

> obj4 = obj.matrixAddition(obj2)

#### matrixSubtraction(self, m2:Matrix)
> This Method returns the Result of the Subtraction of 2 Matrices. One Matrix is the Parameter and other is the Matrix created while initializing the Class.

> Return Type -> Matrix

> C = A - B

> obj4 = obj.matrixSubtraction(obj2)

#### matrixMultiplicationConstant(self, int1 : int OR float)
> This Method multiplies the Original Matrix with the Constant (int1).

> A = A * c

> obj.matrixMultiplicationConstant(5)

#### adj(self)
> This Method returns the Adjoint of the Original Matrix.

> Return Type - Matrix

> obj5 = obj.adj()

#### inverse(self)
> This Method returns the Inverse of the Original Matrix.

> Return Type -> Matrix

> obj6 = obj.inverse()

#### mean(self)
> This Method returns the mean of the Original Matrix.

> Return Type -> Float

> float1 = obj.mean()

#### rowMeans(self)
> This Method returns the mean of all rows of the Original Matrix.

> Return Type -> Matrix

> obj7 = obj.rowMeans()

#### colMeans(self)
> This Method returns the mean of all columns of the Original Matrix.

> Return Type -> Matrix

> obj8 = obj.colMeans()

#### rowSum(self)
> This Method returns the sum of all rows of the Original Matrix.

> Return Type -> Matrix

> obj9 = obj.colMeans()

#### colSum(self)
> This Method returns the sum of all columns of the Original Matrix.

> Return Type -> Matrix

> obj10 = obj.colSum()

#### sum(self)
> This Method returns the sum of all elements of the Matrix.

> Return Type -> Float/Int

> var = obj.sum()

#### matrixDivision(self)
> This Method returns the Result of the Multiplication of 2 Matrices. One Matrix is the inverse of the Parameter and other is the Matrix created while initializing the Class.

> Return Type -> Matrix

> C = A * B^-1

> obj11 = obj.matrixDivision(obj2)

### Functions List

#### diag(m1 : Matrix OR List)
> This Function returns the Diagonal Matrix if the parameter is a List, And Returns the List of all the Diagonal Elements of the Matrix if the parameter is a Matrix.

> Return Type -> Matrix/List

> list1 = diag(obj)  OR   obj12 = diag([1,2,3,4,5,6])

#### identity(m1:Matrix)
> This Function returns an Identity Matrix.

> obj13 = identity(obj)

#### determinant(m1:Matrix)
> This Function returns the Deteminant of a Matrix (N x N).

> Return Type -> Float/Int

> det12 = determinant(obj)

[Back To The Top](#matrix)

---

## Author Info

- Instagram - [prak_entech983](https://www.instagram.com/prak_entech983/)
- Youtube - [Prak EnTech](https://www.youtube.com/c/PrakEnTech)

[Back To The Top](#matrix)