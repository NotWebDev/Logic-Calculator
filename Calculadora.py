import math

#Figuras 2D
def cuadrado(lado = 0, diagonal = 0, area = 0, r = 3):
    if lado != 0: 
        diagonal = (lado ** 2 * 2) ** 0.5
        area = lado ** 2
    elif diagonal != 0:
        lado = diagonal ** 2 / 2 ** 0.5
        area = lado ** 2 * 2
    elif area != 0:
        lado = area / 2 ** 0.5
        diagonal = (lado ** 2 * 2) ** 0.5
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Lado: ' + str(round(lado, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))

def rectangulo(altura = 0, base = 0, diagonal = 0, area = 0, r = 3):
    if altura != 0 and base != 0:
        diagonal = (altura ** 2 + base ** 2) ** 0.5
        area = altura * base
    elif diagonal != 0 and altura != 0:
        base = (diagonal ** 2 - altura ** 2) ** 0.5
        area = altura * base
    elif diagonal != 0 and base != 0:
        altura = (diagonal ** 2 - base ** 2) ** 0.5
        area = altura * base
    else: 
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Base: ' + str(round(base, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))

def triangulo(altura = 0, base = 0, area = 0, r = 3):
    if altura != 0 and base != 0:
        area = base * altura / 2
    elif altura != 0 and area != 0:
        base = altura / area * 2
    elif base != 0 and area != 0:
        altura = base / area * 2
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))

def paralel(altura = 0, base = 0, area = 0, r = 3):
    if altura != 0 and base != 0:
        area = base * altura / 2
    elif altura != 0 and area != 0:
        base = altura / area * 2
    elif base != 0 and area != 0:
        altura = base / area * 2
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))

def trap(altura = 0, lado1 = 0, lado2 = 0, area = 0, r = 3):
    if altura != 0 and lado1 != 0 and lado2 != 0:
        area = (lado1 + lado2) / 2 * altura 
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Lado 1: ' + str(round(lado1, r)))
    print('Lado 2: ' + str(round(lado2, r)))
    print('Area: ' + str(round(area, r)))

def circulo(radio = 0, diametro = 0, circunsferencia = 0, area = 0, r = 3):
    if radio != 0:
        diametro = radio * 2
        circunsferencia = 2 * math.pi * radio
        area = math.pi * (radio ** 2)
    elif diametro != 0:
        radio = diametro * 2
        circunsferencia = 2 * math.pi * radio
        area = math.pi * (radio ** 2)
    elif circunsferencia != 0:
        radio = circunsferencia / 2 / math.pi
        diametro = radio * 2
        area = math.pi * (radio ** 2)
    elif area != 0:
        radio = (area / math.pi) ** 0.5
        diametro = radio * 2
        circunsferencia = 2 * math.pi * radio
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Radio: ' + str(round(radio, r)))
    print('Diametro: ' + str(round(diametro, r)))
    print('Circunsferencia: ' + str(round(circunsferencia, r)))
    print('Area: ' + str(round(area, r)))

#Figuras 3D
def cubo(lado = 0, diagonal = 0, area = 0, volumen = 0, r = 3):
    if lado != 0:
        diagonal = (lado ** 2 * 3) ** 0.5
        area = lado ** 2 * 6
        volumen = lado ** 3
    if diagonal != 0:
        lado = diagonal ** 2 / 3 ** 0.5
        area = lado ** 2 * 6
        volumen = lado ** 3
    if area != 0:
        lado = area / 6 ** 0.5
        diagonal = (lado ** 2 * 3) ** 0.5
        volumen = lado ** 3
    if volumen != 0:
        lado = volumen ** (1/3)
        diagonal = (lado ** 2 * 3) ** 0.5
        area = lado ** 2 * 6
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Lado: ' + str(round(lado, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

def paralelepipedo(base = 0, altura = 0, profundidad = 0, diagonal = 0, area = 0, volumen = 0, r = 3):
    dimensiones = [base, altura, profundidad]
    valores = 0
    valor1 = 0
    valor2 = 0
    for dimension in dimensiones:
        if dimension != 0:
            if valor1 == 0:
                valores += 1
                valor1 = dimension
            else:
                if valores != 2:
                    valor2 = dimension
                    valores += 1
                else:
                    valor3 = dimension

    if valores == 3:
        diagonal = (valor1 ** 2 + valor2 ** 2 + valor3 ** 2) ** 0.5
        area = base * altura * 2 + profundidad * altura * 2 + base * profundidad * 2
        volumen = base * altura * profundidad
    elif valores == 2 and diagonal != 0:
        valor3 = (diagonal ** 2 - valor1 ** 2 + valor2 ** 2) ** 0.5
        area = valor1 * valor2 * 2 + valor3 * valor2 * 2 + valor1 * valor3 * 2
        volumen = valor1 * valor2 * valor3
    elif valores == 2 and volumen != 0:
        valor3 = volumen / valor1 / valor2 
        diagonal = (valor1 ** 2 + valor2 ** 2 + valor3 ** 2)
        area = valor1 * valor2 * 2 + valor3 * valor2 * 2 + valor1 * valor3 * 2
    else:
        print('No se puede realizar la operacion con los datos aportados')
    
    if valor1 == base:
        va1 = base 
        if valor2 == altura:
            va2 = altura
            va3 = valor3
        elif valor2 == profundidad:
            va3 = profundidad
            va2 = valor3 
    elif valor1 == altura:
        va2 = altura 
        if valor2 == profundidad:
            va3 = profundidad
            va1 = valor3
    print('Base: ' + str(round(va1, r)))
    print('Altura: ' + str(round(va2, r)))
    print('Profundidad: ' + str(round(va3, r)))
    print('Diagonal: ' + str(round(diagonal, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

def piramide(altura = 0, arista1 = 0, arista2 = 0, base = 0, area = 0, volumen = 0, r = 3):
    if altura != 0 and arista1 != 0 and arista2 != 0:
        base = arista1 ** 2
        diagonalext = (altura ** 2 + arista1 ** 2) ** 0.5
        area = base + arista1 * diagonalext * 2
        volumen = base * altura / 3
    elif altura != 0 and arista2 != 0 and base != 0:
        arista1 = base ** 0.5
        diagonalext = (altura ** 2 + arista1 ** 2) ** 0.5
        area = base + arista1 * diagonalext * 2
        volumen = base * altura / 3
    elif volumen != 0 and arista1 != 0 and arista2 != 0:
        altura = volumen * 3 / (arista1 ** 2)
        base = arista1 ** 2
        diagonalext = (altura ** 2 + arista1 ** 2) ** 0.5
        area = base + arista1 * diagonalext * 2
    elif volumen != 0 and altura != 0 and arista2 != 0:
        arista1 = (volumen * 3 / altura) ** 0.5
        base = arista1 ** 2
        diagonalext = (altura ** 2 + arista1 ** 2) ** 0.5
        area = base + arista1 * diagonalext * 2
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Arista de base: ' + str(round(arista1, r)))
    print('Arista de altura: ' + str(round(arista2, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

def cilindro(altura = 0, radio = 0, diametro = 0, circunsferencia = 0, base = 0, area = 0, volumen = 0, r = 3):
    if altura != 0 and radio != 0:
        diametro = radio * 2
        circunsferencia = diametro * math.pi
        base = (radio ** 2) * math.pi
        area = circunsferencia * (radio + altura)
        volumen = math.pi * (radio ** 2) * altura
    elif altura != 0 and diametro != 0:
        radio = diametro / 2
        circunsferencia = diametro * math.pi
        base = (radio ** 2) * math.pi
        area = circunsferencia * (radio + altura)
        volumen = math.pi * (radio ** 2) * altura
    elif altura != 0 and circunsferencia != 0:
        radio = circunsferencia / 2 / math.pi
        diametro = radio * 2
        base = (radio ** 2) * math.pi
        area = circunsferencia * (radio + altura)
        volumen = math.pi * (radio ** 2) * altura
    elif altura != 0 and base != 0:
        radio = (base / math.pi) ** 0.5
        diametro = radio * 2
        circunsferencia = diametro * math.pi
        base = (radio ** 2) * math.pi
        area = circunsferencia * (radio + altura)
        volumen = math.pi * (radio ** 2) * altura
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print("Altura: " + str(round(altura, r)))
    print('Radio: ' + str(round(radio, r)))
    print('Diametro: ' + str(round(diametro, r)))
    print('Circunsferencia: ' + str(round(circunsferencia, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

def esfera(radio = 0, diametro = 0, circunsferencia = 0, area = 0, volumen = 0, r = 3):
    if radio != 0:
        diametro = radio * 2
        circunsferencia = radio * 2 * math.pi
        area = 4 * (radio ** 2) * math.pi
        volumen = (4/3) * math.pi * (radio ** 3)
    elif diametro != 0:
        radio = diametro / 2
        circunsferencia = radio * 2 * math.pi
        area = 4 * (radio ** 2) * math.pi
        volumen = (4/3) * math.pi * (radio ** 3)
    elif circunsferencia != 0:
        radio = circunsferencia / 2 / math.pi
        diametro = radio * 2
        area = 4 * (radio ** 2) * math.pi
        volumen = (4/3) * math.pi * (radio ** 3)
    elif area != 0:
        radio = (area / 4 / math.pi) ** 0.5
        diametro = radio * 2
        circunsferencia = radio * 2 * math.pi
        volumen = (4/3) * math.pi * (radio ** 3)
    elif volumen != 0:
        radio = (volumen / (4/3) / math.pi) ** (1/3)
        diametro = radio * 2
        circunsferencia = radio * 2 * math.pi
        area = 4 * (radio ** 2) * math.pi
    else:
        print('No se puede realizar la operacion con los datos aportados')
    print('Radio: ' + str(round(radio, r)))
    print('Diametro: ' + str(round(diametro, r)))
    print('Circunsferencia: ' + str(round(circunsferencia, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

def cono(altura = 0, radio = 0, diametro = 0, circunsferencia = 0, base = 0, area = 0, volumen = 0, r = 3):
    if altura != 0:
        if radio != 0:
            diametro = radio * 2
            circunsferencia = 2 * math.pi * radio
            base = math.pi * (radio ** 2)
            s = (altura ** 2 + radio ** 2) ** 0.5
            area = math.pi * (radio ** 2) + (math.pi * radio * s)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
            print(s)
        elif diametro != 0:
            radio = diametro / 2
            circunsferencia = 2 * math.pi * radio
            base = math.pi * (radio ** 2)
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
        elif circunsferencia != 0:
            radio = circunsferencia / 2 / math.pi
            diametro = radio * 2
            base = math.pi * (radio ** 2)
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
        elif base != 0:
            radio = (base / math.pi) ** 0.5
            diametro = radio * 2
            circunsferencia = 2 * math.pi * radio
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
        elif volumen != 0:
            radio = (volumen / (1/3) / math.pi / altura) ** 0.5
            diametro = radio * 2
            circunsferencia = 2 * math.pi * radio
            base = math.pi * (radio ** 2)
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
    elif radio != 0:
        if area != 0:
            diametro = radio * 2
            circunsferencia = 2 * math.pi * radio
            base = math.pi * (radio ** 2)
            altura = ((area - base / math.pi / radio) ** 2 - (radio ** 2)) ** 0.5
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
            volumen = (1/3) * math.pi * (radio ** 2) * altura
        elif volumen != 0:
            diametro = radio * 2
            circunsferencia = 2 * math.pi * radio
            base = math.pi * (radio ** 2)
            altura = volumen - base / (1/3) / math.pi / (radio ** 2)
            area = base + math.pi * radio * ((altura ** 2 + radio ** 2) ** 0.5)
    else: 
        print('No se puede realizar la operacion con los datos aportados')
    print('Altura: ' + str(round(altura, r)))
    print('Radio: ' + str(round(radio, r)))
    print('Diametro: ' + str(round(diametro, r)))
    print('Circunsferencia: ' + str(round(circunsferencia, r)))
    print('Base: ' + str(round(base, r)))
    print('Area: ' + str(round(area, r)))
    print('Volumen: ' + str(round(volumen, r)))

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
        print('No se puede realizar la operacion con los datos aportados')
    print(' ')
    print('Lado a: ' + str(round(a, 3)))
    print('Lado b: ' + str(round(b, 3)))
    print('Lado c: ' + str(round(c, 3)))
    print('Angulo de a: ' + str(round(aa, 3)))
    print('Angulo de b: ' + str(round(ab, 3)))

#Transformacion de valores
def transf1(valor, unidad1, unidad2, r = 3):
    valor1 = valor
    if unidad1 == 'mm' or unidad1 == 'milimetros':
        valor1 = valor1 / 1000
    elif unidad1 == 'cm' or unidad1 == 'centimetros':
        valor1 = valor1 / 100
    elif unidad1 == 'dm' or unidad1 == 'decimetros':
        valor1 = valor1 / 10
    elif unidad1 == 'm' or unidad1 == 'metros':
        valor1 *= 1
    elif unidad1 == 'dam' or unidad1 == 'decametro':
        valor1 *= 10
    elif unidad1 == 'km' or unidad1 == 'kilometro':
        valor1 *= 1000

    elif unidad1 == 'mil':
        valor1 *= 39370
    elif unidad1 == 'in' or unidad1 == 'pulgada':
        valor1 *= 39.37
    elif unidad1 == 'ft' or unidad1 == 'pie':
        valor1 *= 3.281
    elif unidad1 == 'yd' or unidad1 == 'yarda':
        valor1 *= 1.094
    elif unidad1 == 'ch' or unidad1 == 'chain':
        valor1 *= 0.04971
    elif unidad1 == 'fur' or unidad1 == 'furlong':
        valor1 *= 0.004971
    elif unidad1 == 'mi' or unidad1 == 'milla':
        valor1 *= 0.0006214
    elif unidad1 == 'legua' or unidad1 == 'legua':
        valor1 *= 0.0002071

    valor2 = 0

    if unidad2 == 'mm' or unidad2 == 'milimetros':
        valor2 = valor1 * 1000
    elif unidad2 == 'cm' or unidad2 == 'centimetros':
        valor2 = valor1 * 100
    elif unidad2 == 'dm' or unidad2 == 'decimetros':
        valor2 = valor1 * 10
    elif unidad2 == 'm' or unidad2 == 'metros':
        valor2 = valor1 
    elif unidad2 == 'dam' or unidad2 == 'decametro':
        valor2 = valor1 / 10
    elif unidad2 == 'km' or unidad2 == 'kilometros':
        valor2 = valor1 / 1000

    elif unidad2 == 'mil':
        valor2 = valor1 * 39370.0787
    elif unidad2 == 'in' or unidad2 == 'pulgada':
        valor2 = valor1 * 39.3700787
    elif unidad2 == 'ft' or unidad2 == 'pie':
        valor2 = valor1 * 3.2808399
    elif unidad2 == 'yd' or unidad2 == 'yarda':
        valor2 = valor1 * 1.0936133
    elif unidad2 == 'ch' or unidad2 == 'chain':
        valor2 = valor1 * 0.0497096954
    elif unidad2 == 'fur' or unidad2 == 'furlong':
        valor2 = valor1 * 0.00497096954
    elif unidad2 == 'mi' or unidad2 == 'milla':
        valor2 = valor1 * 0.000621371192
    elif unidad2 == 'legua' or unidad2 == 'legua':
        valor2 = valor1 * 0.0002071
    print(str(round(valor, r)) + ' ' + unidad1 + ' = ' + str(round(valor2, r)) + ' ' + unidad2)

def transf2():
    pass

r = input('Redondear Decimales: ')
if r != '':
    r = int(r)

print('''Tipo de operacion:
a) Areas y Volumen
b) Trigonometría
c) Variables y Gleichungen
e) Transformacion de valores''')
input1 = input()

if input1 == 'a':
    print('''Figura:
    2D
a) Cuadrado
b) Rectangulo
c) Triangulo
d) Paralelogramo
e) Trapecio
f) Circulo
    3D
g) Cubo
h) Paralelepipedo
i) Piramide
j) Cilindro
k) Esfera
l) Cono''')
    input2 = input()

    if input2 == 'a':
        ci11 = input('Lado: ')
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
            cuadrado(float(ci1), float(ci2), float(ci3))
        else:
            cuadrado(float(ci1), float(ci2), float(ci3), r)

    elif input2 == 'b':
        ri11 = input('Altura: ')
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
            rectangulo(float(ri1), float(ri2), float(ri3), float(ri4))
        else:
            rectangulo(float(ri1), float(ri2), float(ri3), float(ri4), r)

    elif input2 == 'c':
        ti11 = input('Altura: ')
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
            triangulo(float(ti1), float(ti2), float(ti3))
        else:
            triangulo(float(ti1), float(ti2), float(ti3), r)

    elif input2 == 'd':
        pi11 = input('Altura: ')
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
        ti11 = input('Altura: ')
        if ti11 == '':
            ti1 = 0
        else:
            ti1 = ti11
        ti12 = input('Lado 1: ')
        if ti12 == '':
            ti2 = 0
        else:
            ti2 = ti12
        ti13 = input('Lado 2: ')
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
        ci11 = input('Radio: ')
        if ci11 == '':
            ci1 = 0
        else:
            ci1 = ci11
        ci12 = input('Diametro: ')
        if ci12 == '':
            ci2 = 0
        else:
            ci2 = ci12
        ci13 = input('Circunsferencia: ')
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
            circulo(float(ci1), float(ci2), float(ci3), float(ci4))
        else:
            circulo(float(ci1), float(ci2), float(ci3), float(ci4), r)

    elif input2 == 'g':
        cubi1 = input('Arista: ')
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
        cubi4 = input('Volumen: ')
        if cubi4 == '':
            cub4 = 0
        else:
            cub4 = cubi4
        if r == '':
            cubo(float(cub1), float(cub2), float(cub3), float(cub4))
        else:
            cubo(float(cub1), float(cub2), float(cub3), float(cub4), r)

    elif input2 == 'h':
        parai1 = input('Base: ')
        if parai1 == '':
            para1 = 0
        else:
            para1 = parai1
        parai2 = input('Altura: ')
        if parai2 == '':
            para2 = 0
        else:
            para2 = parai2
        parai3 = input('Profundidad: ')
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
        parai6 = input('Volumen: ')
        if parai6 == '':
            para6 = 0
        else:
            para6 = parai6
        if r == '':
            paralelepipedo(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6))
        else:
            paralelepipedo(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6), r)

    elif input2 == 'i':
        parai1 = input('Altura: ')
        if parai1 == '':
            para1 = 0
        else:
            para1 = parai1
        parai2 = input('Arista de base: ')
        if parai2 == '':
            para2 = 0
        else:
            para2 = parai2
        parai3 = input('Arista de altura: ')
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
        parai6 = input('Volumen: ')
        if parai6 == '':
            para6 = 0
        else:
            para6 = parai6
        if r == '':
            piramide(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6))
        else:
            paralelepipedo(float(para1), float(para2), float(para3), float(para4), float(para5), float(para6), r)

    elif input2 == 'j':
        cili1 = input('Altura: ')
        if cili1 == '':
            cil1 = 0
        else:
            cil1 = cili1
        cili2 = input('Radio: ')
        if cili2 == '':
            cil2 = 0
        else:
            cil2 = cili2
        cili3 = input('Diametro: ')
        if cili3 == '':
            cil3 = 0
        else:
            cil3 = cili3
        cili4 = input('Circunsferencia: ')
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
        cili7 = input('Volumen: ')
        if cili7 == '':
            cil7 = 0
        else:
            cil7 = cili7
        if r == '':
            cilindro(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7))
        else:
            cilindro(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7), r)
    
    elif input2 == 'k':
        esfi1 = input('Radio: ')
        if esfi1 == '':
            esf1 = 0
        else:
            esf1 = esfi1
        esfi2 = input('Diametro: ')
        if esfi2 == '':
            esf2 = 0
        else:
            esf2 = esfi2
        esfi3 = input('Circunsferencia: ')
        if esfi3 == '':
            esf3 = 0
        else:
            esf3 = esfi3
        esfi4 = input('Area: ')
        if esfi4 == '':
            esf4 = 0
        else:
            esf4 = esfi4
        esfi5 = input('Volumen: ')
        if esfi5 == '':
            esf5 = 0
        else:
            esf5 = esfi5
        if r == '':
            esfera(float(esf1), float(esf2), float(esf3), float(esf4), float(esf5))
        else:
            esfera(float(esf1), float(esf2), float(esf3), float(esf4), float(esf5), r)

    elif input2 == 'l':
        cili1 = input('Altura: ')
        if cili1 == '':
            cil1 = 0
        else:
            cil1 = cili1
        cili2 = input('Radio: ')
        if cili2 == '':
            cil2 = 0
        else:
            cil2 = cili2
        cili3 = input('Diametro: ')
        if cili3 == '':
            cil3 = 0
        else:
            cil3 = cili3
        cili4 = input('Circunsferencia: ')
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
        cili7 = input('Volumen: ')
        if cili7 == '':
            cil7 = 0
        if r == '':
            cono(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7))
        else:
            cono(float(cil1), float(cil2), float(cil3), float(cil4), float(cil5), float(cil6), float(cil7), r)

elif input1 == 'b':
    print('a) Operaciones Trigonometricas')
    inputb = input()
    tri1 = input('Lado A: ')
    if tri1 == '':
        tr1 = 0
    else:
        tr1 = tri1
    tri2 = input('Lado B: ')
    if tri2 == '':
        tr2 = 0
    else:
        tr2 = tri2
    tri3 = input('Hipotenusa: ')
    if tri3 == '':
        tr3 = 0
    else:
        tr3 = tri3
    tri4 = input('Angulo opuesto a Lado A: ')
    if tri4 == '':
        tr4 = 0
    else:
        tr4 = tri4
    tri5 = input('Angulo opuesto a Lado B: ')
    if tri5 == '':
        tr5 = 0
    else:
        tr5 = tri5
    if r == '':
        trigonom(float(tr1), float(tr2), float(tr3), float(tr4), float(tr5))
    else:
        trigonom(float(tr1), float(tr2), float(tr3), float(tr4), float(tr5), r)

elif input1 == 'e':
    print(''' Tipo de valores:
a) Longitud
b) Area
c) Volumen
d) Peso
    ''')
    input2 = input()
    if input2 == 'a':
        vai1 = input('Valor: ')
        vail2 = input('Unidad: ')
        vail3 = input('Unidad 2: ')
        if vai1 != '':
            if vail2 != '':
                if vail3 != '':
                    if r == '':
                        transf1(float(vai1), vail2, vail3)
                    else:
                        transf1(float(vai1), vail2, vail3, r)
                else:
                    print('No se puede realizar la operacion con los datos aportados')
            else:
                print('No se puede realizar la operacion con los datos aportados')
        else:
            print('No se puede realizar la operacion con los datos aportados')

    elif input2 == 'b':
        pass