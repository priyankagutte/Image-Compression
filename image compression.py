#converting image into matrix format

from PIL import Image
from numpy import array
import math
from numpy import *

img = Image.open("j.jpg")
arr = array(img)
print(arr)
s = shape(arr)
print(s)
m = s[0]
n = s[1]
a = m % 4
b = n % 4
print(a, b)

"""if (a != 0) and (b != 0):
    arr1 = zeros(((4-a), (4-b)), int)
elif (a != 0)and(b == 0):
    arr1 = zeros(((4 - a),), int)
elif (a == 0)and(b != 0):
 arr1 =  zeros(((4-b)), int)
print(arr1)"""

c = 0
m1 = matrix('1 2 3 4; 4 5 6 7 ; 7 8 9 1; 1 2 3 4')
sh = shape(m1)
m = sh[0]
n = sh[1]
print("the size of m1", sh)
print(m1)
#Calculating mean and standard deviation
mean = mean(m1)
std = m1.std()
print("mean =  ", mean)
s = m1.std()
print("Std deviation = ", std)
print("the value :", m, n)
a = m//4
b = n//4
m1 = zeros(m1, (a, b))

# converting image into bitplan

if (m % 4) == 0 and (n % 4) == 0:
    for i in range(4):
        for j in range(4):
            if m1[i, j] > m:
                m1[i, j] = 1
                c = c+1
            else:
                m1[i, j] = 0
    print(m1)
    # no. of 1's in matrix
    print("No. of 1's = ", c)

# calculating quantization  levels
    g1 = mean+(s*math.sqrt((16-c)/c))
    g2 = mean-(s*math.sqrt(c/(16-c)))
    print("quantization values ", g1, g2)
    for i in range(4):
        for j in range(4):
            if m1[i, j] == 1:
                m1[i, j] = float(g1)

            else:
                m1[i, j] = float(g2)
    print(m1)
