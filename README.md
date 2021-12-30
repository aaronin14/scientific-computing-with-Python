# Scientific Computing with Python
> Aaron Nguyen | Completed on September 27th, 2021
---
[Link to the Course](https://www.freecodecamp.org/learn/scientific-computing-with-python/#scientific-computing-with-python-projects)

## List of Projects
### 1. Arithmetic Arranger
**Arithmetic Arranger** receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
### 2. Time Calculator
**Time Calculator** takes in `start_time`, `duration_time` and `day`(optional). It returns the exact time after adding `duration_time` to `start_time`. It also tells how many days have passed.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```
### 3. Budget App
**Budget App** creates categories like food, clothing, and entertainment. It has basic features like deposit, withdraw, and transfer funds between categories.
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
It also return a bar chart represent percentage spent by category:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g
```

### 4. Polygon Area Calculator
**Polygon Area Calculator** creates and calculates area, perimeter and draws rectangle or square shape with our choice of width and height.
It also returns the amount of shapes with the same size that will fit in another shape.
### 5. Probability Calculator
**Probability Calculator** calculate the probability of drawing an expected set of ball out of a hat by reapeting the same process by many times.
```py
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
```
Output:
```
Probability: 0.17066666666666666
```
