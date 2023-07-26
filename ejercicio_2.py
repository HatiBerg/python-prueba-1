def area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

def volumen_cilindro(radio, altura):
    volumen = area_circulo(radio) * altura
    return volumen

def main():
    radio_circulo = int(input("Ingrese el radio del circulo: "))
    altura_cilindro = int(input("Ingrese la altura del cilindro: "))
    resultado_area = area_circulo(radio_circulo)
    resultado_volumen = volumen_cilindro(radio_circulo, altura_cilindro)
    print("Area del circulo: ", resultado_area)
    print("Volumen del cilindro: ", resultado_volumen)

if __name__ == '__main__':
    main()