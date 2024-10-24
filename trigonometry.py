import math 
import fishgics as f
x0 = int(input())
y0 = int(input())
v0 = int(input())
x = x0 + v0*f.t
y = y0 + v0*f.t - (f.g*f.t**2/(2))
print (x,y)