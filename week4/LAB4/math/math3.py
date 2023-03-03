import math
sds = float(input("Input number of sides: "))
sd_l = float(input("Input length of one side: "))
print("The area of polygon is:", math.ceil(((sds/4) * math.pow(sd_l, 2))
      * (math.tan(math.pi/sds))))
