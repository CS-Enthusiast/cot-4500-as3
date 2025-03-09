Numerical Calculus Assignment 3a
================================

Overview
--------

This assignment covers Chapter 5, focusing on numerical methods for solving initial value problems (IVPs) for ordinary differential equations. Specifically, it implements and tests the following numerical methods:

-   **Euler's Method**
-   **Runge-Kutta Method (4th order)**

Both methods approximate the solution of the given differential equation: 


$\frac{dy}{dt} = t - y^2$

on the interval $0≤t≤2$, with initial condition $y(0)=1$


Project Structure
-----------------

```
cot-4500-as3/
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_3.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_3.py
└── README.md

```

Requirements
------------

No external libraries beyond Python's standard library are required for this assignment.

Instructions to Run
-------------------

Navigate to the project root directory and execute the following command:

```
python3 src/main/assignment_3.py
```

Instructions to Run Tests
-------------------------

To run the unit tests, navigate to the project root directory and execute:

```
python3 src/test/test_assignment_3.py
```

Expected Output
---------------

Running the main script should produce outputs approximately:

```
Euler's Method Approximation: 1.2446380979332121
Runge-Kutta Method Approximation: 1.251316587879806
```
