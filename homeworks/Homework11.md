# Homework 11

1. To do this question, copy the following code-snippet into a new file on IDLE.
The goal is to write two functions. The first function, `is_negative`, returns
`True` if the number given to it (`x`) is negative and `False` otherwise. The
second function, `triangular_number`, returns the `n`th triangular number (see
<https://en.wikipedia.org/wiki/Triangular_number>). I provided the start of the
functions and some code to test your solutions so you know when you get it
right. Only change code where the comments say to. If you run the code without
any changes, you will see that the tests fail because the functions don't work
yet! Good luck!

    ```python
    def is_negative(x):
        # TODO: put your code here (only here) and delete the following line
        pass

    def triangular_number(n):
        # TODO: put your code here (only here) and delete the following line
        pass

    def test(f, x, y):
        passed = f(x) == y
        status = "PASSED" if passed else "FAILED"
        print(f"{status}: {f.__name__}({x}) == {y}")


    test(is_negative, 4, False)
    test(is_negative, -3, True)
    test(is_negative, 0, False)
    test(is_negative, -2, True)
    test(is_negative, 9, False)

    test(triangular_number, 0, 0)
    test(triangular_number, 1, 1)
    test(triangular_number, 2, 3)
    test(triangular_number, 3, 6)
    test(triangular_number, 4, 10)
    test(triangular_number, 5, 15)
    test(triangular_number, 100, 5050)
    ```
