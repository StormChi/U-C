# WorkWheets
## Arithmetic Operators
1.Arithmetic Operators 

Without running the code, completed the table below by filling in the 
values that the expressions produce and the types of those values.

|Python Expression |  Result       | Type of Result |
|------------------|---------------|----------------|
|9 / 3             |   3.0         |      float     |                     
|9 // 3            |               |                |                                         
|10 / 4            |               |                |                 
|10 // 4           |               |                |                  
|10 // 3           |               |                |                 
|10 % 3            |               |                |

2.Arithmetic Operators 

For which positive integers n does n % 2 produce 0?____________

For which positive integers n does n % 2 produce 1?____________

3.Order of Precedence of Arithmetic Operators 

| Python Expression   | Python Expression Parenthesized |
|-----------------    | --------------------------------|
| -2 + 4 * 7          | ((-2) + (4 * 7))                |
|  3 + 5 * 2          |                                 |
| 4 + 8 / 2 ** 2 / -2 |                                 |

## Build-in Functions 
1.Built-in Functions 

| Python Expression        |   Result         | Type of Result|
|--------------------------| -----------------| --------------|
| min(4, 6, 2.5)           |                  |               |                                      
| max(10.1, 13, 16)        |                  |               |
| abs(-5.2)
| pow(2, 3)                |                  |               |

2.Built-in Function: `help`

| Question                                                              |   Answer   |
|-----------------------------------------------------------------------| -----------|                      
| What type of value does function `ord` return?
| How many arguments does function `oct` take?       
| What is the *minimum* number of arguments function `round` can take?  |
| What is the *maximum* number of arguments function `round` can take?  |            |

## Variable Assignment Statements

1.Changing variable values

(a) Consider this code:

k = 5

Write an assignment statement that creates a new variable j that refers to three times k’s value:
____________ 

(b) Consider this code:

```python 
x = 4
y = 5
x = 2
```
After the code above is executed, to which value does x refer?____________

After the code above is executed, to which value does y refer?____________

(c) Consider this code:

``` python 
x = 4
y = x + 2
x = y + 1
```
After the code above is executed, to which value does x refer?__________

After the code above is executed, to which value does y refer?__________ 

2.Swapping variable values An extra exercise to try at home.

Assume that variables a and b have been assigned int values. Write code to swap which values a and
b refer to: after your statements are executed, a should refer to the value that b used to refer to, and b
should refer to the value that a used to refer to. Hint: use a third variable.

____________

Once you have written the code, trace your code using the memory model to confirm that it correctly
swaps the values:
____________ 

## Function Definitions 

1.Function Definitions 

(a) Function `double` takes a number and returns twice its value.

What value does double(7) produce?__________

What value does double(5.7) produce?__________

Write a return statement to complete the function definition:

```python 
def double(num):
    return num * 2
```

(b) Function `our_maximum` takes two numbers and returns the larger of the two.

What value does our maximum(4, 3.7) produce?__________

Complete the function definition:

```python
def our_maximum(num1, num2):
    return max(num1, num2)
```

(c) Function `max_of_min` takes four numbers, `num1`, `num2`, `value1`, and `value2`, determines the minimum

    of `num1` and `num2` and the minimum of `value1` and `value2`, and returns the maximum of those two

    minimums.

What value does max of min(4, 3.7, 6, 3.5) produce?__________

What value does max of min(1, 1.7, 4.5, 3) produce?__________

Complete the function definition. If you like, you can use several statements.

```python 
def max_of_min(num1, num2, value1, value2):
    return max(min(num1, num2), min(value1, value2))
```

## Function design Recipe

1.Function Design Recipe

Following the Function Design Recipe, write a function that satisfies this description:

This function returns a string containing a given word repeated a given number of times. For example,

someone should be able to call the function to repeat "Marcia " three times and the function should

return "Marcia Marcia Marcia ", or call the function to repeat "Buffalo " eight times and have it

return "Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo ".

**Examples** 


**Type Contract**


**Header**


**Description**


**Code the Body**


**Test**