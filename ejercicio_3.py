def main():
    fecha = input("Ingrese fecha de nacimiento en formato dd/mm/aaaa :")
    dia = fecha[:2]
    mes = fecha[3:5]
    año = fecha[-4:]
    print("Dia ",dia)
    print("Mes ",mes)
    print("Año ",año)

if __name__ == '__main__':
    main()