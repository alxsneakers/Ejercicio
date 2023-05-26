def ejercicio1():

    # Indicar cuál es el menor de tres enteros solicitados al usuario

    n1 = int(input("Introduce numero: "))
    n2 = int(input("Introduce numero: "))
    n3 = int(input("Introduce numero: "))

    if n1 <= n2 and n1 <= n3:
        menor = n1
    else:
        if n2 < n1 and n2 <= n3:
            menor = n2
        else:
            menor = n3

    print("el numero: " + str(menor) + " es el menor")

def ejercicio2():
    #Dispones de frase y una letra, solicitados al usuario y debes mostrar la cantidad de veces que aparece la letra en la frase.

    frase = input("Introduce una frase: ")
    LETRA = input("Introduce una letra: ")
    cont = 0
    for letra in frase:
        if LETRA == letra:
            cont +=1

    print("La frase tiene " + str(cont) + " Letras " + LETRA)

def ejercicio3():
    #Suma o resta dos números reales solicita la información al usuario

    n1 = float(input("Introduce numero decimal: "))
    n2 = float(input("Introduce numero decimal: "))
    operacion = input("Que operacion desea realizar sumar | restar ")

    if operacion == "sumar":
        print("El resultado de la suma es: " + str(n1 + n2))
    elif operacion == "restar":
        print("El resultado de la resta es: " + str(n1 - n2))
    else:
        print("Operador incorrecto")

def ejercicio4():
    #Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos constantes predefinidas.

    USER = "Admin"
    PASSWRD = "Admin"
    intento = 0
    login = False
    while intento < 3 and login == False:
        user = input("Usuario: ")
        passwrd = input("Password: ")
        if (user == USER and passwrd == PASSWRD):
            print("Acceso correcto")
            login = True
        else:
            print("Incorrecto")
            intento += 1

def ejercicio5():
    """
    Crea una variable que sea una letra, si es una a muestra el número 7, si es una b,
    el 9, si es una c el 101 y si no es ninguno de los tres, indica que se han equivocado de letra

    """

    letra = input("Introduzca una letra ")

    if letra == "a":
        print(7)
    elif letra == "b":
        print(9)
    elif letra == "c":
        print(101)
    else:
        print("Letra incorrecta")

def ejercicio6():
    """
    Dispones de tres números enteros H, M, S correspondientes a hora,
    minutos y segundos respectivamente,
    debes comprobar si se trata de una hora válida.

    """
    h = int(input("Introduce Hora: "))
    m = int(input("Introduce Minutos: "))
    s = int(input("Introduce Segundos: "))

    if h >= 0 and h <= 23 and m >= 0 and m <= 60 and s >= 0 and s <= 60:
        print("Hora Correcta " + str(h) + ":" + str(m) + ":" + str(s))
    else:
        print("Hora incorrecta")

def ejercicio7():
    """
    Solicita al usuario dos fechas del mismo año e indica la cantidad de días que hay entre ellas.

    """
    ENERO = 31
    FEBRERO = 28
    MARZO = 31
    ABRIL = 30
    MAYO = 31
    JUNIO = 30
    JULIO = 31
    AGOSTO = 31
    SEPTIEMBRE = 30
    OCTUBRE = 31
    NOVIEMBRE = 30
    DICIEMBRE = 31

    print("Fecha A: Introduce una fecha")
    A_dia = int(input("Introduce dia: "))
    A_mes = int(input("Introduce mes(numero): "))
    #A_anio = int(input("Introduce anio: "))

    print("Fecha B: Introduce una fecha")
    B_dia = int(input("Introduce dia: "))
    B_mes = int(input("Introduce mes(numero): "))
    #B_anio = int(input("Introduce anio: "))



ejercicio7()

