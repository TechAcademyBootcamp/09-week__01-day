# Triangles

This assignment focuses on the implementation and testing of a Python class to manipulate triangles, as well as an application program which uses that class.

## Assignment Specifications

The instructors have designed “class Triangle” and have supplied an outline of that class in the file named ***Unsolved.py***.

You will complete the development of “class Triangle” by implementing each function which currently appears in ***Unsolved.py*** as a stub (incomplete function definition).  You will demonstrate that your implementation of the class is correct by developing a program which serves as a test bed for that class.

When you have implemented and tested “class Triangle”, you will develop an application program which uses that class to read a series of user-supplied triangles and then displays information about those triangles (see below).

## Specifications for Class Triangle

1.  Your implementation of “class Triangle” must be based on the class outlined in ***Unsolved.py*** on the course website.  That file contains a stub for each method (member function); each stub contains the following line:

	pass # REPLACE

    For each method, you will delete that line and replace it with one or more lines of Python source code to complete the method.

2.  You may not alter “class Triangle” in any other way:  you may not alter any line of the file except those lines which contain “pass” statements.  This implies that you may not add new methods to the class, nor may you delete existing methods from the class.

3.  The constructor (method “__init__”) will accept three lengths as parameters.  If those three lengths are all numeric values, the constructor will save them as the lengths of the three sides of the triangle.  Otherwise, the lengths of the three sides of the triangle will all be set to be zero.

4.  The constructor will validate the three sides.  A triangle is defined to be valid when the lengths of all three sides are greater than zero and the sum of the lengths of the shortest two sides is greater than the length of the third side.

5.  The representation of an object of type “Triangle” will be a string containing the length of each side.  That string will be in the form “( xx.x, xx.x, xx.x )”, where the parentheses and spaces are required.  Each “xx.x” represents the length of one side; each length will be displayed with exactly one digit to the right of the decimal point.  For example:  ( 17.2, 3.8, 15.0 ).

6.  The method “sides” will return a tuple containing the lengths of the three sides.

7.  The method “angles” will return a tuple containing the degree measure of the three interior angles, if the triangle is valid.  Otherwise, it will return a tuple containing three instances of None.

8.  The method “perimeter” will return the perimeter, if the triangle is valid.  Otherwise, it will return zero.

9.  The method “area” will return the area, if the triangle is valid.  Otherwise, it will return zero.

10.  The method “scale” will multiply each of the sides by the given factor, if the triangle is valid and the factor is greater than zero.  Otherwise, it will not alter the three sides.

11.  None of the methods in “class Triangle” will use function “print”.  That is, they will not display messages to the user, even if an error is detected.

Please note that you may wish to use function “print” to display various items as you are developing your implementation of the class.  However, all invocations of function “print” must be removed from the final version of your class (or at least turned into comments).

## Specifications for the Test Program

1.  You will develop a program to serve as a test bed for “class Triangle”.  That is, the only purpose of the program is to demonstrate that each method of “class Triangle” is implemented correctly.

The source code for your test bed will be contained in the file named ***tests.py***.  That file will import ***Unsolved.py***.

2.  Your test bed will not perform any input operations.  Instead, all test cases will be embedded in the program itself.

3.  The output produced by your test bed will be appropriately labeled so that the reader can understand the purpose and result of each test case without examining the source code.


## Specifications for the Application Program

1.  You will develop an application program which uses “class Triangle” to solve the problem described below.

The source code for your application program will be contained in the file named ***main.py***.  That file will import ***Unsolved.py***.

2.  The program will attempt to access the file named ***input.txt***.  If that input file cannot be opened, the program will display an appropriate message and halt.

3.  The input file will contain zero or more lines, where each line contains at most one triangle.

    A triangle will appear as a string in the form “ ( xx, xx, xx ) ”, where “xx” represents the length of a side.  The double quotes will not be present, the parentheses are required, and the whitespace is optional. 

4.  The program will read each line of the input file and display it.  The display will be on one line, will begin with “Line NN:” (where NN is the current line number) and will contain the exact contents of the line.  Line numbers will begin with 1.

5.  If a line contains a valid triangle, the program will display the triangle as a string, and then display its perimeter and area.  If a line does not contain a valid triangle, the program will display an appropriate message.

6.  When the program has processed all of the lines in the input file, it will display the following:

    - The total number of lines processed.
    - The total number of valid triangles processed.
    - The average perimeter for all valid triangles processed.
    - The average area for all valid triangles processed.
    - The valid triangle with the largest perimeter (the triangle itself, its perimeter and area).
    - The valid triangle with the largest area (the triangle itself, its perimeter and area).


## Assignment Notes

1.  As noted under “Specifications for Class Triangle”, the only lines in ***Unsolved.py*** which you may alter are the lines containing “pass # REPLACE”.  Each of those lines should be deleted, and you should substitute one or more lines to complete the functionality of the class.

2.  Please note that method “angles” returns a tuple containing the three interior angles, where the angles are measured in degrees.

3.  The following definitions may be useful:

    - A scalene triangle has no sides whose lengths are equal.
    - An isosceles triangle has at least two sides whose lengths are equal.
    - An equilateral triangle has three sides whose lengths are equal.



4.  Heron’s formula can be used to compute the area of a triangle:

    Let A, B and C be the lengths of the three sides of a triangle, and let S be one-half the perimeter of the triangle.  Compute:

    ```
	T = S (S-A) (S-B) (S-C)
    ```

    Then, the area of the triangle is equal to the square root of T.

5.  You would be wise to develop your implementation of “class Triangle” and your test program incrementally and in parallel.  That is, implement one class method at a time and then test that method by adding statements to your test program.

Clearly, the first class method which must be implemented and tested is the constructor (“__init__”).  However, you might choose to first implement the constructor without worrying about erroneous parameters (error handling could be added later).

Perhaps the second class method to implement and test is “__str__” so that you have a way to display the value of an object of type “Triangle” using function “print”.

Then, you might be wise to implement and test a relatively simple method, such as “perimeter”.

After implementing and testing those three methods, you would continue to implement and test one method at a time until you have completed the class.

Be sure to insert and test any necessary error handling at the appropriate time.  For example, it makes no sense to add error handling to method “perimeter” until the constructor detects invalid parameters.