import math
N = float(math.ceil(float(input("How many sides does this regular polygon have? "))-0.5))
L = float(input("What is the side length of this regular polygon? "))
A = float(((N*L*L)/4)*math.tan(math.pi/2-math.pi/N))
A = (A-0.5>=math.floor(A)+0.4) and math.ceil(A) or A # Round up if <=0.1 tolerance
print(f"The area is approximately {A}")