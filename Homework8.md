# Homework 8

1. What is the output (i.e. what is printed to the console) of the following
code snippet:

    ```python
    def someFunction1(x, y):
        return x * x + y * y
    
    print(someFunction(3, 4))
    ```

2. What is the difference between `float` and `int`?

3. Describe what the function below does when given numbers for the parameters
`a` and `b`. The numbers can be `float` or `int`; it doesn't matter.

    ```python
    def someFunction2(a, b):
        if a <= b:
            return a
        else:
            return b
    ```

4. Describe what the function below does when given a list of numbers for the
parameter `someList`.

    ```python
    def someFunction3(someList):
        if len(someList) > 0:
            result = someList[0]
            for i in range(1, len(someList)):
                if result > someList[i]:
                    result = someList[i]
            return result
        else:
            return None
    ```
