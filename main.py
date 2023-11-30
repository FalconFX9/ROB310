import math


def f(x):
    return a * x + math.cos(x)


a = 1/(2*math.pi)
l0 = 1
r0 = math.pi
round_digits = 5
tol = 1E-4

lk = l0
rk = r0
num_iterations = 0

while abs(rk - lk) > tol:
    c = (lk + rk)/2

    if f(c)*f(lk) < 0:
        rk = c
        lk = lk
    elif f(c)*f(rk) < 0:
        rk = rk
        lk = c
    num_iterations += 1


print(f"Found a root between {round(lk, round_digits)} and {round(rk, round_digits)} with accuracy "
      f"{round(abs(rk-lk), round_digits)}\n in {num_iterations} iterations.")



