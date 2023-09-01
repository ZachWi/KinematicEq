import math

## WELCOME TO MY CODE
## If you're here for the kinematic equations, thanks alot!

print ("Kinematic Eq 2.0")

## I don't like how long these print functions are, but they do the job 

print ("Displacement = Dx, Velocity inital = Vo, Velocity final  = Vf, Acceleration = Ac, Time = Ti")
print ("Then, represent what you're looking for")

## Splits the inputs, but I have how this works
## May be subject to change

Dx, Vo, Vf, Ac, Ti, Eq = input().split()
print ("Entered Displacement: ", Dx)
print ("Entered Velocity Initial: ", Vo)
print ("Entered Velocity Final: ", Vf)
print ("Entered Acceleration: ", Ac)
print ("Entered Time: ", Ti)
print ("Entered Equation: ", Eq)

## Turns the input text into a floating point number
## Funnily enough stll returns floating point errors 

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

## Tests if the equation entered is valid or not

if Eq != ("Dx") or ("Vf") or ("Vo") or ("Ac") or ("Ti"):
    print("Equation error")

## Actual equations, the only part that actually does math LOL
## Also put in try functions because it would return an error if given X

if Eq == ("Dx"):
    try:
        Dxp = Vo1 * Ti1 + 0.5 * Ac1 * Ti1 * Ti1
        print ("Dx =")
        print (Dxp)
    except NameError: 
        print ("1st form error")
if Eq == ("Vf"):
    try:
        Vf2 = Vo1 * Vo1 + 2 * Ac1 * Dx1
        Vfp = math.sqrt(Vf2)
        print ("Vf =")
        print (Vfp)
    except NameError:
        print ("2nd form error")
    except ValueError:
        print ("2nd form error")
if Eq == ("Vo"):
    try:
        Vop = Vf1 - Ac1 * Ti1
        print ("Vo =")
        print (Vop)
    except NameError:
        print ("3rd form error")
if Eq == ("Ac"):
    try:
        Acp = (Vf1 - Vo1) / Ti1
        print ("Ac =")
        print (Acp)
    except NameError:
        print ("4th form error")
if Eq == ("Ti"):
    try:
        Tip = (Vf1 - Vo1) / Ac1
        print ("Ti =")
        print (Tip)
    except NameError:
        print ("5th form error")
if Eq == ("Vf"):
    try: 
        Vfp2 = Vo1 + (Ac1 * Ti1)
        print ("Vf w/out dx=")
        print (Vfp2)
    except NameError:
        print ("6th form error")
