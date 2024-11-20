# AIML

https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/index.html

https://textbooks.math.gatech.edu/ila/index.html

https://scikit-learn.org/stable/

Matrix
======
A matrix is a system of m n numbers, arranged in a rectangular array where we have m horizontal lines and n vertical lines, here horizontal lines are called rows and vertical lines are called columns and this is called as my by n or m cross n and represented by m x n

======================================= Types of Matrix =======================================

Row Matrix
==========
A Row Matrix contains only one row and any number of colums

Column Matrix
=============
A columc matrix contains only one column and any number of rows

Square Matrix
=============
Number of rows equal to number of colums vise versa

Diagonal Matrix
==============
A Square Matrix with all non diagonal elements should be '0'. Left to right diagonal called principal diagonal or leading diagonal, the other diagonal called non   principal or non leading diagonal

Scalar Matrix
=============
A diagonal matrix with all diagonal elements should be equal to k which is a scalar value (k=2, k=5, k=-21, ..... k=any value)

Unit or Identity Matrix
=======================
A scalar Matrix where k=1

Null Matrix
===========
A matrix with all zeros

Sub Matrix
==========
A Matrixh which is obtained from a given matrix by deleting any number of rows or any number of ccolumns

Upper Traingular Matrix
=======================
For all the elements below the leading diagonal are zero

Lower Traingular Matrix
=======================
For all the elements above the leading diagonal are zero

Transpose Matrix
================
Transpose is not a matrix, it is an operation on a matrix. If we interchange rows and with the corresponding columns of a given matrix, A, the new matrix obtained is called Transpose of a matrix. It is denoted as AT or A'

Symmetric Matrix
================
It should be a square matrix and the transpose of the matrix should be the original matrix. A' = A. The other words aij = aji, for all the values of i, j

Skew Symmetric Matrix
=====================
It should be a square matrix and the transpose of the matrix should be the negative matrix of original matrix. A' = -A. aij = -aji. In Skew Symmetric Matrix all diagonal elements are zero

Inverse of a Matrix
===================
The inverse of a square matrix A, denoted as A-', is a matrix such that
                A.A-' = A-'.A = I where 'I' is the Identity matrix

                     
                     a b
For a 2x2 matrix A = c d then inverse A-' is given by:
                
                A-' = adj(A)/|A| or A-' = 1/det(A)
                
Adjoint of a Matrix
===================
The adjoint of a square matrix A, denoted as adj(A), is the transpose of the matrix of cofactors of A

Determinant
===========
The determinant of a matrix calculated by adding the product of the elements of a matrix with their cofactors. The determinant of a matrix can only be calculated for a square matrix.
            It is represented by |A|


For a 2x2 matrix A = a b
                     c d  the determinant is |A| = (a*d) - (b*c)


For a 3x3 matrix A = a b c
                     d e f
                     g h i the determinant is |A| = a(e*i - f*h) - b(d*i - f*g) + c(d*h - e*g)

Orthogonal Matrix
=================
If we have a square matrix A and A.A' = A'.A = I (Identity Matrix), then this is called Orthogonal Matrix

Singular & Non Singular Matrix
==============================
If the determinant of a square matrix is zero then it is Singular matrix, If the determinant of a square matrix is not equal to zero then it is non singular matrix. For a given square matrix A, |A| = 0 ----> Singular Matrix. For a given square matrix A, |A| != 0 ----> Non Singular Matrix
Inverse of a singular matrix cannot be found


======================================= Algebra of Matrix =======================================

Properties of Matrix Addition
=============================
A + B = B + A                  ---> Commutative Law

A + (B + C) = (A + B) + C      ---> Associate Law

k(A + B) = KA + KB             ---> Distributive Law

A + 0 = 0 + A = A              ---> Additive Identity Law

A + B = 0 = B + A              ---> B is additive inverse

A + X = 0 = X + A this equation has an unique solution when x = -A

Properties of Matrix Multiplication
===================================
A(BC) = (AB)C Associate Law

A(B + C) = AB + AC Distributive Law

AB = BA sometimes AB != BA so not necessarily commutative

Transformation Matrix
=====================
Vector: vector is row matix or column matrix. From a matrix we can define n number of vectors. A transformation matrix changes the position of a vector. If we multiply a vector with a scaler matrix then the position of the vector will change (zoom in), here the scaler matrix we call it as transformation matrix. Trandformation matrix can be any matrix which can change the position of the vector (object).

If we use a matrix which can rotate the actual image (object/vector) then this matrix we call it as rotational transformation matrix like this we have scalling matrix and others...
Any matrix we multiply with vector we call it as a transformation matrix

Linear Independence
===================
A set of vectors is linearly independent if no vectors can be represented as a liner conbination of the others.
If we have vectors {v1, v2, v3, .....vk} and C1v1+C2v2+C3v3+....Ckvk = 0 and C1 = C2 = C3 = ...Ck = 0 and if this has only one solution then these vectors are called linearly independent. Here C1, C2, C3 ...Ck are coefficients

Linear independence is used in feature selection and dimensionality reduction

Basis & Span
============
The vectors which are used to span the entire dimensionality space are called as Basis vectors. Using Basis vectors we can cover the entire space in the dimensionality. These Basis vectors are useful when we want to reduce the features and dimensionality reduction. In Principal Component Analysis (PCA) Basis vectors play vital role. Basis vectors are linearly independent.

[1], [1 0] [0 1], [1 0 0] [0 1 0] [0 0 1] these are some of the Basis vectors respectively for the 1d, 2d and 3d dimensionality, and there might be other Basis vectors.

Vector Space
============
A vector space is, a set of vectors on which we perform addition and scaler multiplication and satisfy commutative and associativity laws. A vector space is denoted by V or R power n, here n is dimensions.

v1 + v2 = v2 + v1, v1.v2 = v2.v1 ----> commutative
v1 + (v2 + v3) = (v1 + v2) + v3, v1 .(v2.v3) = (v1.v2).v3 ----> associativity

Span
====
From a given set of vectors {v1, v2, v3, v4,....vk}, all possible linear combinations called as span.
span {v1, v2, v3, v4,....vk} = {alpha symbol1v1 + as2v2 + as3v3 + as4v4.....+askvk | (such that) as1, as2, as3 as4,....askvk belongs to real numbers}

Rank of a Matrix
================

Eigen vectors & Eigen values
============================

Row Echelon Form & Reduced Row Echelon Form
===========================================

Krammers Rule
=============
