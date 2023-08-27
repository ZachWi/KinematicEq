import math

print ("Kinematic Eq 1.3")

print ("Displacement = dx, Velocity inital = Vo, Velocity final  = Vf, Acceleration = A, Gravity = G, Time = T")
Dx, Vo, Vf, Ac, Ti = input(). split()
print ("Entered Displacement: ", Dx)
print ("Entered Velocity Initial: ", Vo)
print ("Entered Velocity Final: ", Vf)
print ("Entered Acceleration: ", Ac)
print ("Entered Time: ", Ti)

if Dx != ("x"):
    Dx1 = float(Dx)
if Vo != ("x"):
    Vo1 = float(Vo)
if Vf != ("x"):
    Vf1 = float(Vf)
if Ac == ("G"):
    Ac1 = -9.8
else:
    if Ac != ("x"):
        Ac1 = float(Ac)
if Ti != ("x"):
    Ti1 = float(Ti)

try:
    Dxp = Vo1 * Ti1 + 0.5 * Ac1 * Ti1 * Ti1
    print ("Dx =")
    print (Dxp)
except NameError: 
    print ("1st form error")

try:
    Vf2 = Vo1 * Vo1 + 2 * Ac1 * Dx1
    Vfp = math.sqrt(Vf2)
    print ("Vf =")
    print (Vfp)
except NameError:
    print ("2nd form error")
except ValueError:
    print ("2nd form error")

try:
    Vop = Vf1 - Ac1 * Ti1
    print ("Vo =")
    print (Vop)
except NameError:
    print ("3rd form error")

try:
    Acp = (Vf1 - Vo1) / Ti1
    print ("Ac =")
    print (Acp)
except NameError:
    print ("4th form error")

try:
    Tip = (Vf1 - Vo1) / Ac1
    print ("Ti =")
    print (Tip)
except NameError:
    print ("5th form error")

try: 
    Vfp2 = Vo1 + (Ac1 * Ti1)
    print ("Vf w/out dx=")
    print (Vfp2)
except NameError:
    print ("6th form error")
