## I/ Objectives:
Approximate solutions of differential equations using the Runge-Kutta method

## II/ Introduction:

> dt = delta t

  - We consider a general differential equation of order 1 which is written: y' = f(t, y) where f is a function of two variables.
  - A solution of this equation is a function y(t) such that for all t we have:  y'(t) = f( (t, y(t) ).
  - For a general function f, we don't have a formula to express the solutions of the equations, but we can draw approximate solutions.

## III/ Runge-Khuta method of order 4 – RK1

  - The method consists in approaching the solutions point by point.
    We therefore set an initial value t_0 and a step dt, we set t_i = t_0 + i \* dt.
    We also fix an initial value y_0 we suppose that we have a solution y(t) such that y(t_0) = y_0.

  - We first give an approximate value of y(t_i) for t_i = t_0 + dt.
    The derivative y'(t_0) is given by the relation y'(t_0) = f(t_0, y_0).
    The expansion limited to order 1 of y(t) and t = t_0 thus gives y_1 = y(t_1) = y(t_0 + dt) approximatively equal to y_0 + dt \* f(t_0, y_0).

  - We then proceed step by step to calculate $y_{i+1}$ by setting:
    - k_1 = f(t_i, y_i),
    - y_{i+1} = y_i + dt \* k_1.

## IV/ Runge-Khuta method of order 2 – RK2

- According to the mean value theorem, we know that there exists  'c' belongs to the interval \] t_i, t_{i+1} \[ such that $\displaystyle y'(c) = ( y_{y +1} - y_i ) / dt.
  We therefore have an exact equality y_{i+1} = y_i + dt \* y'(c). Unfortunately, we can't find $c$...
  In method RK1 we took the approximate value c = t_i.
  In the RK2 method we take c = (t_i + t_{i+1} / 2 = t_i + dt/2)

- We must therefore consider the derivative $\displaystyle y'(c) = y'(t_i + dt/2) = f(t_i + dt/2, y(t_i + dt/2)

- As we do not know the exact value of $\displaystyle y(t_i + dt/2) we replace it with the approximate value: y_i + dt/2 \* f(t_i, y_i)

- In other words, we ask:

    - k_1 = f(t_i, y_i),
    - k_2 = f(t_i + dt/2, y_i dt/2 \* k_1),
    - y_{i+1} approximatively equal to y_i + dt \* k_2.

## V/ Runge-Khuta method of order 4 – RK4

Further analysis - *not detailed here* - leads to the following formulas:

  - k_1 = f(t_i, y_i)
  - k_2 = f( (t_i + dt/2), (y_i + dt/2) \* k_1 )
  - k_3 = f( (t_i + dt/2), (y_i+ dt/2) \* k_2 )
  - k_4 = f(t_i + dt, y_i + dt \* k_3)
  - y_{i+1} approx equal to y_i + (dt/6) \* (k_1 + 2k_2 + 2k_3 + k_4)
