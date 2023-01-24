from scipy.stats import norm
x_l = 10
x_r = 20
x_m = (x_r + x_l ) / 2
x = x_l
n = 0
while x <= x_m:
    print(x)
    x = x + norm.pdf(x, x_m, 3) +1
    n = n + 1
print (n)

y = norm.pdf(4, 4, 1)
print(y)