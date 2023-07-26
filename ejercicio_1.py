def main():
    puntos = float(input("Ingrese puntuación: "))

    if puntos == 0.0:
        dinero = puntos * 2400
        print("Nivel Inaceptable, Beneficio: ",dinero,"€")
    elif puntos == 0.4:
        dinero = puntos * 2400
        print("Nivel Aceptable, Beneficio: ",dinero,"€")
    elif puntos >= 0.6:
        dinero = puntos * 2400
        print("Nivel Meritorio, Beneficio: ",dinero,"€")
    else:
        print("ERROR: Los puntos ingresados no son validos, Intente de nuevo")

if __name__ == '__main__':
    main()