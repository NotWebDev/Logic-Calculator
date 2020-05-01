import math

#2D Figures
def square(side = 0, diagonal = 0, area = 0, r = 3):
    if side != 0: 
        diagonal = (side ** 2 * 2) ** 0.5
        area = side ** 2
    elif diagonal != 0:
        side = diagonal ** 2 / 2 ** 0.5
        area = side ** 2 * 2
    elif area != 0:
        side = area / 2 ** 0.5
        diagonal = (side ** 2 * 2) ** 0.5
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Lado: ' + str(round(side, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))

def rectangle(height = 0, base = 0, diagonal = 0, area = 0, r = 3):
    if height != 0 and base != 0:
        diagonal = (height ** 2 + base ** 2) ** 0.5
        area = height * base
    elif diagonal != 0 and height != 0:
        base = (diagonal ** 2 - height ** 2) ** 0.5
        area = height * base
    elif diagonal != 0 and base != 0:
        height = (diagonal ** 2 - base ** 2) ** 0.5
        area = height * base
    else: 
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Base: ' + str(round(base, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))

def triangle(height = 0, base = 0, area = 0, r = 3):
    if height != 0 and base != 0:
        area = base * height / 2
    elif height != 0 and area != 0:
        base = height / area * 2
    elif base != 0 and area != 0:
        height = base / area * 2
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))

def paralel(height = 0, base = 0, area = 0, r = 3):
    if height != 0 and base != 0:
        area = base * height / 2
    elif height != 0 and area != 0:
        base = height / area * 2
    elif base != 0 and area != 0:
        height = base / area * 2
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))

def trap(height = 0, side1 = 0, side2 = 0, area = 0, r = 3):
    if height != 0 and side1 != 0 and side2 != 0:
        area = (side1 + side2) / 2 * height 
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Side 1: ' + str(round(side1, r)))
    print('Side 2: ' + str(round(side2, r)))
    print('Area: ' + str(round(area, r)))

def circle(radius = 0, diameter = 0, circumsference = 0, area = 0, r = 3):
    if radius != 0:
        diameter = radius * 2
        circumsference = 2 * math.pi * radius
        area = math.pi * (radius ** 2)
    elif diameter != 0:
        radius = diameter * 2
        circumsference = 2 * math.pi * radius
        area = math.pi * (radius ** 2)
    elif circumsference != 0:
        radius = circumsference / 2 / math.pi
        diameter = radius * 2
        area = math.pi * (radius ** 2)
    elif area != 0:
        radius = (area / math.pi) ** 0.5
        diameter = radius * 2
        circumsference = 2 * math.pi * radius
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Radius: ' + str(round(radius, r)))
    print('Diameter: ' + str(round(diameter, r)))
    print('Circumsference: ' + str(round(circumsference, r)))
    print('Area: ' + str(round(area, r)))

#Figuras 3D
def cube(side = 0, diagonal = 0, area = 0, volume = 0, r = 3):
    if side != 0:
        diagonal = (side ** 2 * 3) ** 0.5
        area = side ** 2 * 6
        volume = side ** 3
    if diagonal != 0:
        side = diagonal ** 2 / 3 ** 0.5
        area = side ** 2 * 6
        volume = side ** 3
    if area != 0:
        side = area / 6 ** 0.5
        diagonal = (side ** 2 * 3) ** 0.5
        volume = side ** 3
    if volume != 0:
        lado = volume ** (1/3)
        diagonal = (lado ** 2 * 3) ** 0.5
        area = lado ** 2 * 6
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Side: ' + str(round(side, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))
    print('Volume: ' + str(round(volume, r)))

def parallelepiped(base = 0, height = 0, depth = 0, diagonal = 0, area = 0, volume = 0, r = 3):
    dimensions = [base, height, depth]
    values = 0
    value1 = 0
    value2 = 0
    for dimension in dimensions:
        if dimension != 0:
            if value1 == 0:
                values += 1
                value1 = dimension
            else:
                if valuees != 2:
                    value2 = dimension
                    valuees += 1
                else:
                    value3 = dimension

    if values == 3:
        diagonal = (value1 ** 2 + value2 ** 2 + value3 ** 2) ** 0.5
        area = base * height * 2 + depth * height * 2 + base * depth * 2
        volume = base * height * depth
    elif values == 2 and diagonal != 0:
        value3 = (diagonal ** 2 - value1 ** 2 + value2 ** 2) ** 0.5
        area = value1 * value2 * 2 + value3 * value2 * 2 + value1 * value3 * 2
        volume = value1 * value2 * value3
    elif values == 2 and volume != 0:
        value3 = volume / value1 / value2 
        diagonal = (value1 ** 2 + value2 ** 2 + value3 ** 2)
        area = value1 * value2 * 2 + value3 * value2 * 2 + value1 * value3 * 2
    else:
        print('Unable to realize operation with given data')
    
    if value1 == base:
        va1 = base 
        if value2 == height:
            va2 = height
            va3 = value3
        elif value2 == depth:
            va3 = depth
            va2 = value3 
    elif value1 == height:
        va2 = height 
        if value2 == depth:
            va3 = depth
            va1 = value3
    print(' ')
    print('Base: ' + str(round(va1, r)))
    print('Height: ' + str(round(va2, r)))
    print('Depth: ' + str(round(va3, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))
    print('Volume: ' + str(round(volume, r)))

def pyramid(height = 0, edge1 = 0, edge2 = 0, base = 0, area = 0, volume = 0, r = 3):
    if height != 0 and edge1 != 0 and edge2 != 0:
        base = edge1 ** 2
        diagonalext = (height ** 2 + edge1 ** 2) ** 0.5
        area = base + edge1 * diagonalext * 2
        volume = base * height / 3
    elif height != 0 and edge2 != 0 and base != 0:
        edge1 = base ** 0.5
        diagonalext = (height ** 2 + edge1 ** 2) ** 0.5
        area = base + edge1 * diagonalext * 2
        volume = base * height / 3
    elif volume != 0 and edge1 != 0 and edge2 != 0:
        height = volume * 3 / (edge1 ** 2)
        base = edge1 ** 2
        diagonalext = (height ** 2 + edge1 ** 2) ** 0.5
        area = base + edge1 * diagonalext * 2
    elif volume != 0 and height != 0 and edge2 != 0:
        edge1 = (volume * 3 / height) ** 0.5
        base = edge1 ** 2
        diagonalext = (height ** 2 + edge1 ** 2) ** 0.5
        area = base + edge1 * diagonalext * 2
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Base edge: ' + str(round(edge1, r)))
    print('Height edge: ' + str(round(edge2, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('Volume: ' + str(round(volume, r)))

def cilinder(height = 0, radius = 0, diameter = 0, circumsference = 0, base = 0, area = 0, volume = 0, r = 3):
    if height != 0 and radius != 0:
        diameter = radius * 2
        circumsference = diameter * math.pi
        base = (radius ** 2) * math.pi
        area = circumsference * (radius + height)
        volume = math.pi * (radius ** 2) * height
    elif height != 0 and diameter != 0:
        radius = diameter / 2
        circumsference = diameter * math.pi
        base = (radius ** 2) * math.pi
        area = circumsference * (radius + height)
        volume = math.pi * (radius ** 2) * height
    elif height != 0 and circumsference != 0:
        radius = circumsference / 2 / math.pi
        diameter = radius * 2
        base = (radius ** 2) * math.pi
        area = circumsference * (radius + height)
        volume = math.pi * (radius ** 2) * height
    elif height != 0 and base != 0:
        radius = (base / math.pi) ** 0.5
        diameter = radius * 2
        circumsference = diameter * math.pi
        base = (radius ** 2) * math.pi
        area = circumsference * (radius + height)
        volume = math.pi * (radius ** 2) * height
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print("Height: " + str(round(height, r)))
    print('Radius: ' + str(round(radius, r)))
    print('Diameter: ' + str(round(diameter, r)))
    print('Circumsference: ' + str(round(circumsference, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('volume: ' + str(round(volume, r)))

def sphere(radius = 0, diameter = 0, circumsference = 0, area = 0, volume = 0, r = 3):
    if radius != 0:
        diameter = radius * 2
        circumsference = radius * 2 * math.pi
        area = 4 * (radius ** 2) * math.pi
        volume = (4/3) * math.pi * (radius ** 3)
    elif diameter != 0:
        radius = diameter / 2
        circumsference = radius * 2 * math.pi
        area = 4 * (radius ** 2) * math.pi
        volume = (4/3) * math.pi * (radius ** 3)
    elif circumsference != 0:
        radius = circumsference / 2 / math.pi
        diameter = radius * 2
        area = 4 * (radius ** 2) * math.pi
        volume = (4/3) * math.pi * (radius ** 3)
    elif area != 0:
        radius = (area / 4 / math.pi) ** 0.5
        diameter = radius * 2
        circumsference = radius * 2 * math.pi
        volume = (4/3) * math.pi * (radius ** 3)
    elif volume != 0:
        radius = (volume / (4/3) / math.pi) ** (1/3)
        diameter = radius * 2
        circumsference = radius * 2 * math.pi
        area = 4 * (radius ** 2) * math.pi
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Radius: ' + str(round(radius, r)))
    print('Diameter: ' + str(round(diameter, r)))
    print('Circumsference: ' + str(round(circumsference, r)))
    print('Area: ' + str(round(area, r)))
    print('Volume: ' + str(round(volume, r)))

def cone(height = 0, radius = 0, diameter = 0, circumsference = 0, base = 0, area = 0, volume = 0, r = 3):
    if height != 0:
        if radius != 0:
            diameter = radius * 2
            circumsference = 2 * math.pi * radius
            base = math.pi * (radius ** 2)
            s = (height ** 2 + radius ** 2) ** 0.5
            area = math.pi * (radius ** 2) + (math.pi * radius * s)
            volume = (1/3) * math.pi * (radius ** 2) * height
            print(s)
        elif diameter != 0:
            radius = diameter / 2
            circumsference = 2 * math.pi * radius
            base = math.pi * (radius ** 2)
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
            volume = (1/3) * math.pi * (radius ** 2) * height
        elif circumsference != 0:
            radius = circumsference / 2 / math.pi
            diameter = radius * 2
            base = math.pi * (radius ** 2)
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
            volume = (1/3) * math.pi * (radius ** 2) * height
        elif base != 0:
            radius = (base / math.pi) ** 0.5
            diameter = radius * 2
            circumsference = 2 * math.pi * radius
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
            volume = (1/3) * math.pi * (radius ** 2) * height
        elif volume != 0:
            radius = (volume / (1/3) / math.pi / height) ** 0.5
            diameter = radius * 2
            circumsference = 2 * math.pi * radius
            base = math.pi * (radius ** 2)
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
            volume = (1/3) * math.pi * (radius ** 2) * height
    elif radius != 0:
        if area != 0:
            diameter = radius * 2
            circumsference = 2 * math.pi * radius
            base = math.pi * (radius ** 2)
            height = ((area - base / math.pi / radius) ** 2 - (radius ** 2)) ** 0.5
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
            volume = (1/3) * math.pi * (radius ** 2) * height
        elif volume != 0:
            diameter = radius * 2
            circumsference = 2 * math.pi * radius
            base = math.pi * (radius ** 2)
            height = volume - base / (1/3) / math.pi / (radius ** 2)
            area = base + math.pi * radius * ((height ** 2 + radius ** 2) ** 0.5)
    else: 
        print('Unable to realize operation with given data')
    print(' ')
    print('Height: ' + str(round(height, r)))
    print('Radius: ' + str(round(radius, r)))
    print('Diameter: ' + str(round(diameter, r)))
    print('Circumsference: ' + str(round(circumsference, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('Volume: ' + str(round(volume, r)))

#Trigonometria
def trigonom(a = 0, b = 0, c = 0, aa = 0, ab = 0, r = 3):
    if a != 0 and b != 0:
        c = (a ** 2 + b ** 2) ** 0.5
        aa = math.degrees(math.asin(a / c))
        ab = 90 - aa
    elif a != 0 and c != 0:
        b = (c ** 2 - a ** 2) ** 0.5
        aa = math.degrees(math.asin(a / c))
        ab = 90 - aa
    elif b != 0 and c != 0:
        a = (c ** 2 - b ** 2) ** 0.5
        aa = math.degrees(math.asin(a / c))
        ab = 90 - aa
    elif a != 0:
        if aa != 0:
            c = a / math.sin(math.radians(aa)) 
            b = (((c ** 2) - (a ** 2)) ** 0.5)
            ab = 90 - aa
        if ab != 0:
            c = a / math.cos(math.radians(ab))
            b = (c ** 2 - a ** 2) ** 0.5
            aa = 90 - ab
    elif b != 0:
        if aa != 0:
            c = b / math.sin(math.radians(aa))
            a = (c ** 2 - b ** 2) ** 0.5
            ab = 90 - aa
        if ab != 0:
            c = b / math.cos(math.radians(ab))
            a = (c ** 2 - b ** 2) ** 0.5
            aa = 90 - ab
    elif c != 0:
        if aa != 0:
            a = c / math.sin(math.radians(aa))
            b = (c ** 2 - a ** 2) ** 0.5
            ab = 90 - aa
        if ab != 0:
            a = c / math.cos(math.radians(ab))
            b = (c ** 2 - a ** 2) ** 0.5
            aa = 90 - ab
    else:
        print('Unable to realize operation with given data')
    print(' ')
    print('Side A: ' + str(round(a, 3)))
    print('Side B: ' + str(round(b, 3)))
    print('Hypotenuse: : ' + str(round(c, 3)))
    print('Angle opposite to side A: ' + str(round(aa, 3)))
    print('Angle opposite to side B: ' + str(round(ab, 3)))

#Transformacion de valuees
def transf1(value, unit1, unit2, r = 3):
    value1 = value
    if unit1 == 'mm' or unit1 == 'milimetros' or unit1 == 'millimeters':
        value1 = value1 / 1000
    elif unit1 == 'cm' or unit1 == 'centimetros' or unit1 == 'centimeters':
        value1 = value1 / 100
    elif unit1 == 'dm' or unit1 == 'decimetros' or unit1 == 'decimeters':
        value1 = value1 / 10
    elif unit1 == 'm' or unit1 == 'metros' or unit1 == 'meters':
        value1 *= 1
    elif unit1 == 'dam' or unit1 == 'decametros' or unit1 == 'decameters':
        value1 *= 10
    elif unit1 == 'km' or unit1 == 'kilometros' or unit1 == 'kilometers':
        value1 *= 1000

    elif unit1 == 'mil' or 'mils': 
        value1 *= 39370
    elif unit1 == 'in' or unit1 == 'pulgadas' or unit1 == 'inches':
        value1 *= 39.37
    elif unit1 == 'ft' or unit1 == 'pies' or unit1 == 'feet':
        value1 *= 3.281
    elif unit1 == 'yd' or unit1 == 'yardas' or unit1 == 'yards':
        value1 *= 1.094
    elif unit1 == 'ch' or unit1 == 'chain' or unit1 == 'chains':
        value1 *= 0.04971
    elif unit1 == 'fur' or unit1 == 'furlongs' or unit1 == 'furlongs':
        value1 *= 0.004971
    elif unit1 == 'mi' or unit1 == 'millas' or unit1 == 'miles':
        value1 *= 0.0006214
    elif unit1 == 'leguas' or unit1 == 'league' or unit1 == 'leagues':
        value1 *= 0.0002071

    value2 = 0

    if unit2 == 'mm' or unit2 == 'milimetros'  or unit2 == 'millimeters':
        value2 = value1 * 1000
    elif unit2 == 'cm' or unit2 == 'centimetros'  or unit2 == 'centimeters':
        value2 = value1 * 100
    elif unit2 == 'dm' or unit2 == 'decimetros' or unit2 == 'decimeters':
        value2 = value1 * 10
    elif unit2 == 'm' or unit2 == 'metros' or unit2 == 'meters':
        value2 = value1 
    elif unit2 == 'dam' or unit2 == 'decametros' or unit2 == 'decameters':
        value2 = value1 / 10
    elif unit2 == 'km' or unit2 == 'kilometros' or unit2 == 'kilometers':
        value2 = value1 / 1000

    elif unit2 == 'mil' or unit2 == 'mils':
        value2 = value1 * 39370.0787
    elif unit2 == 'in' or unit2 == 'pulgadas' or unit2 == 'inches':
        value2 = value1 * 39.3700787
    elif unit2 == 'ft' or unit2 == 'pies' or unit2 == 'feet':
        value2 = value1 * 3.2808399
    elif unit2 == 'yd' or unit2 == 'yardas' or unit2 == 'yards':
        value2 = value1 * 1.0936133
    elif unit2 == 'ch' or unit2 == 'chain' or unit2 == 'chains':
        value2 = value1 * 0.0497096954
    elif unit2 == 'fur' or unit2 == 'furlongs' or unit2 == 'furlong':
        value2 = value1 * 0.00497096954
    elif unit2 == 'mi' or unit2 == 'millas' or unit2 == 'miles':
        value2 = value1 * 0.000621371192
    elif unit2 == 'legua' or unit2 == 'league' or unit2 == 'leagues':
        value2 = value1 * 0.0002071
    print(' ')
    print(str(round(value, r)) + ' ' + unit1 + ' = ' + str(round(value2, r)) + ' ' + unit2)

def transf2():
    pass

r = input('Decimal Rounding: ')
if r != '':
    r = int(r)

print('''Operation:
a) Areas and Volume
b) Trigonometry
c) Value transformation''')
input1 = input()

if input1 == 'a':
    print('''Figure:
    2D
a) Square
b) Rectangle
c) Triangle
d) Parallelogram
e) Trapeze
f) Circle
    3D
g) Cube
h) Parallelepiped
i) Pyramid
j) Cilinder
k) Sphere
l) Cone''')
    input2 = input()

    if input2 == 'a':
        ci11 = input('Side: ')
        if ci11 == '':
            ci1 = 0
        else:
            ci1 = ci11
        ci12 = input('Diagonal: ')
        if ci12 == '':
            ci2 = 0
        else:
            ci2 = ci12
        ci13 = input('Area: ')
        if ci13 == '':
            ci3 = 0
        else:
            ci3 = ci13
        if r == '':
            square(float(ci1), float(ci2), float(ci3))
        else:
            square(float(ci1), float(ci2), float(ci3), r)

    elif input2 == 'b':
        ri11 = input('Height: ')
        if ri11 == '':
            ri1 = 0
        else:
            ri1 = ri11

        ri12 = input('Base: ')
        if ri12 == '':
            ri2 = 0
        else:
            ri2 = ri12

        ri13 = input('Diagonal: ')
        if ri13 == '':
            ri3 = 0
        else:
            ri3 = ri13

        ri14 = input('Area: ')
        if ri14 == '':
            ri4 = 0
        else:
            ri4 = ri14
        if r == '':
            rectangle(float(ri1), float(ri2), float(ri3), float(ri4))
        else:
            rectangle(float(ri1), float(ri2), float(ri3), float(ri4), r)

    elif input2 == 'c':
        ti11 = input('Height: ')
        if ti11 == '':
            ti1 = 0
        else:
            ti1 = ti11
        ti12 = input('Base: ')
        if ti12 == '':
            ti2 = 0
        else:
            ti2 = ti12
        ti13 = input('Area: ')
        if ti13 == '':
            ti3 = 0
        else:
            ti3 = ti13
        if r == '':
            triangle(float(ti1), float(ti2), float(ti3))
        else:
            triangle(float(ti1), float(ti2), float(ti3), r)

    elif input2 == 'd':
        pi11 = input('height: ')
        if pi11 == '':
            pi1 = 0
        else:
            pi1 = pi11
        pi12 = input('Base: ')
        if pi12 == '':
            pi2 = 0
        else:
            pi2 = pi12
        pi13 = input('Area: ')
        if pi13 == '':
            pi3 = 0
        else:
            pi3 = pi13
        if r == '':
            paralel(float(pi1), float(pi2), float(pi3))
        else:
            paralel(float(pi1), float(pi2), float(pi3), r)

    elif input2 == 'e':
        ti11 = input('Height: ')
        if ti11 == '':
            ti1 = 0
        else:
            ti1 = ti11
        ti12 = input('Side 1: ')
        if ti12 == '':
            ti2 = 0
        else:
            ti2 = ti12
        ti13 = input('Side 2: ')
        if ti13 == '':
            ti3 = 0
        else:
            ti3 = ti13
        ti14 = input('Area: ')
        if ti14 == '':
            ti4 = 0
        else:
            ti4 = ti14
        if r == '':
            trap(float(ti1), float(ti2), float(ti3), float(ti4))
        else:
            trap(float(ti1), float(ti2), float(ti3), float(ti4), r)

    elif input2 == 'f': 
        ci11 = input('Radius: ')
        if ci11 == '':
            ci1 = 0
        else:
            ci1 = ci11
        ci12 = input('Diameter: ')
        if ci12 == '':
            ci2 = 0
        else:
            ci2 = ci12
        ci13 = input('Circumsference: ')
        if ci13 == '':
            ci3 = 0
        else:
            ci3 = ci13
        ci14 = input('Area: ')
        if ci14 == '':
            ci4 = 0
        else:
            ci4 = ci14
        if r == '':
            circle(float(ci1), float(ci2), float(ci3), float(ci4))
        else:
            circle(float(ci1), float(ci2), float(ci3), float(ci4), r)

    elif input2 == 'g':
        cubi1 = input('Edge: ')
        if cubi1 == '':
            cub1 = 0
        else:
            cub1 = cubi1
        cubi2 = input('Diagonal: ')
        if cubi2 == '':
            cub2 = 0
        else:
            cub2 = cubi2
        cubi3 = input('Area: ')
        if cubi3 == '':
            cub3 = 0
        else:
            cub3 = cubi3
        cubi4 = input('Volume: ')
        if cubi4 == '':
            cub4 = 0
        else:
            cub4 = cubi4
        if r == '':
            cube(float(cub1), float(cub2), float(cub3), float(cub4))
        else:
            cube(float(cub1), float(cub2), float(cub3), float(cub4), r)

    elif input2 == 'h':
        parai1 = input('Base: ')
        if parai1 == '':
            para1 = 0
        else:
            para1 = parai1
        parai2 = input('Height: ')
        if parai2 == '':
            para2 = 0
        else:
            para2 = parai2
        parai3 = input('Depth: ')
        if parai3 == '':
            para3 = 0
        else:
            para3 = parai3
        parai4 = input('Diagonal: ')
        if parai4 == '':
            para4 = 0
        else:
            para4 = parai4
        parai5 = input('Area: ')
        if parai5 == '':
            para5 = 0
        else:
            para5 = parai5
        parai6 = input('Volume: ')
        if parai6 == '':
            para6 = 0
        else:
            para6 = parai6
        if r == '':
            parallelepiped(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6))
        else:
            parallelepiped(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6), r)

    elif input2 == 'i':
        parai1 = input('Height: ')
        if parai1 == '':
            para1 = 0
        else:
            para1 = parai1
        parai2 = input('Base edge: ')
        if parai2 == '':
            para2 = 0
        else:
            para2 = parai2
        parai3 = input('Height edge: ')
        if parai3 == '':
            para3 = 0
        else:
            para3 = parai3
        parai4 = input('Base: ')
        if parai4 == '':
            para4 = 0
        else:
            para4 = parai4
        parai5 = input('Area: ')
        if parai5 == '':
            para5 = 0
        else:
            para5 = parai5
        parai6 = input('Volume: ')
        if parai6 == '':
            para6 = 0
        else:
            para6 = parai6
        if r == '':
            pyramid(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6))
        else:
            pyramid(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6), r)

    elif input2 == 'j':
        cili1 = input('Height: ')
        if cili1 == '':
            cil1 = 0
        else:
            cil1 = cili1
        cili2 = input('Radius: ')
        if cili2 == '':
            cil2 = 0
        else:
            cil2 = cili2
        cili3 = input('Diameter: ')
        if cili3 == '':
            cil3 = 0
        else:
            cil3 = cili3
        cili4 = input('Circumsference: ')
        if cili4 == '':
            cil4 = 0
        else:
            cil4 = cili4
        cili5 = input('Base: ')
        if cili5 == '':
            cil5 = 0
        else:
            cil5 = cili5
        cili6 = input('Area: ')
        if cili6 == '':
            cil6 = 0
        else:
            cil6 = cili6
        cili7 = input('Volume: ')
        if cili7 == '':
            cil7 = 0
        else:
            cil7 = cili7
        if r == '':
            cilinder(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7))
        else:
            cilinder(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7), r)
    
    elif input2 == 'k':
        esfi1 = input('Radius: ')
        if esfi1 == '':
            esf1 = 0
        else:
            esf1 = esfi1
        esfi2 = input('Diameter: ')
        if esfi2 == '':
            esf2 = 0
        else:
            esf2 = esfi2
        esfi3 = input('Circumsference: ')
        if esfi3 == '':
            esf3 = 0
        else:
            esf3 = esfi3
        esfi4 = input('Area: ')
        if esfi4 == '':
            esf4 = 0
        else:
            esf4 = esfi4
        esfi5 = input('Volume: ')
        if esfi5 == '':
            esf5 = 0
        else:
            esf5 = esfi5
        if r == '':
            sphere(float(esf1), float(esf2), float(esf3), float(esf4), float(esf5))
        else:
            sphere(float(esf1), float(esf2), float(esf3), float(esf4), float(esf5), r)

    elif input2 == 'l':
        cili1 = input('Height: ')
        if cili1 == '':
            cil1 = 0
        else:
            cil1 = cili1
        cili2 = input('Radius: ')
        if cili2 == '':
            cil2 = 0
        else:
            cil2 = cili2
        cili3 = input('Diameter: ')
        if cili3 == '':
            cil3 = 0
        else:
            cil3 = cili3
        cili4 = input('Circumsference: ')
        if cili4 == '':
            cil4 = 0
        else:
            cil4 = cili4
        cili5 = input('Base: ')
        if cili5 == '':
            cil5 = 0
        else:
            cil5 = cili5
        cili6 = input('Area: ')
        if cili6 == '':
            cil6 = 0
        else:
            cil6 = cili6
        cili7 = input('Volume: ')
        if cili7 == '':
            cil7 = 0
        if r == '':
            cone(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7))
        else:
            cone(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7), r)

elif input1 == 'b':
    print('a) Trigonometrycal operations')
    inputb = input()
    tri1 = input('Side A: ')
    if tri1 == '':
        tr1 = 0
    else:
        tr1 = tri1
    tri2 = input('Side B: ')
    if tri2 == '':
        tr2 = 0
    else:
        tr2 = tri2
    tri3 = input('Hypotenuse: ')
    if tri3 == '':
        tr3 = 0
    else:
        tr3 = tri3
    tri4 = input('Angle opposite to side A: ')
    if tri4 == '':
        tr4 = 0
    else:
        tr4 = tri4
    tri5 = input('Angle opposite to side B: ')
    if tri5 == '':
        tr5 = 0
    else:
        tr5 = tri5
    if r == '':
        trigonom(float(tr1), float(tr2), float(tr3), float(tr4), float(tr5))
    else:
        trigonom(float(tr1), float(tr2), float(tr3), float(tr4), float(tr5), r)

elif input1 == 'c':
    print('''Value type:
a) Length
b) Area
c) Volume
d) Weight''')
    input2 = input()
    if input2 == 'a':
        vai1 = input('Value: ')
        vail2 = input('Unit: ')
        vail3 = input('Unit 2: ')
        if vai1 != '':
            if vail2 != '':
                if vail3 != '':
                    if r == '':
                        transf1(float(vai1), vail2, vail3)
                    else:
                        transf1(float(vai1), vail2, vail3, r)
                else:
                    print('Unable to realize operation with given data')
            else:
                print('Unable to realize operation with given data')
        else:
            print('Unable to realize operation with given data')

    elif input2 == 'b':
        pass
