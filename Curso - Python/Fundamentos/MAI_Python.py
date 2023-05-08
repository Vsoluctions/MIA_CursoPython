

def  nuevo_tema(tema):
    print("\n ----------------",tema,"---------------------");

if __name__ == "__main__":

    print("1==2", 1==2)
    print("1>2", 1>2)
    print("1<2", 1<2)
    print("1!=2", 1!=2)
    print("1<=2", 1<=2)
    print("1>=2", 1>=2)

    print("--------------funciones en python------")

    nuevo_tema("Operadores")
    _variable1=10
    _variable2=6.2547
    _variable3="peje"
    nombrevariable =8
    nombre_variable=31.2
    print(_variable1,_variable2,_variable3,nombrevariable,nombre_variable)

    a,b,c=5,10.0,"hola"
    print(a)
    print(b)
    print(c)

    w=105
    x=1234567898745
    y=-58
    z=0b00110011
    h=0xff
    print(w,type(w))
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(h,type(h))

    nuevo_tema("Flotantes")
    x=1234.56
    print(x,type(x))
    y=-9874.56
    print(y,type(y))

    nuevo_tema("Numeros complejos")
    x=-46j
    y=12+45j
    z=2j
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))

    nuevo_tema("Booleanos")
    lis =[5]
    print(lis,bool(lis))
    nuevo_tema("Listas")
    a=[10,20.5,"Python List"]
    print(a)
    print(a[1])
    a[1] ="Hola"
    print(a)
    nuevo_tema("Tuplas")
    t=(25,"Tupla",1+10j)
    print(t)
    print(t[1])

    nuevo_tema("Cadenas")
    cadena1="Esto es una cadena"
    cadena2='Esto tambien es una cadena'
    print(cadena1,type(cadena1))
    print(cadena2,type(cadena2))
    print(cadena1[5])
    cadenaMultilinea =''' Esto es una cadena
    de varias lineas con tabuladores y
    saldp
    de 
    linea'''
    print(cadenaMultilinea,type(cadenaMultilinea))

    nuevo_tema("Conjuntos")
    a={20,30,40,50}
    print(a)

    nuevo_tema("Dicionarios")






