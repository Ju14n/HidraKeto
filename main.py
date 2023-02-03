def calculo_agua_necesaria(peso):
    # Cálculo de la cantidad de agua necesaria por día en función del peso corporal
    cantidad_agua = peso * 0.035
    return cantidad_agua

def registro_agua_consumida(cantidad_agua, agua_consumida):
    # Actualiza la cantidad de agua consumida y devuelve el total actual
    agua_consumida += cantidad_agua
    return agua_consumida

def main():
    peso = float(input("Ingrese su peso corporal (en kilogramos): "))
    agua_necesaria = calculo_agua_necesaria(peso)
    print("Necesita consumir al menos", agua_necesaria, "litros de agua por día.")

    agua_consumida = 0
    while True:
        cantidad_agua = float(input("Ingrese la cantidad de agua consumida (en litros) [0 para salir]: "))
        if cantidad_agua == 0:
            break
        agua_consumida = registro_agua_consumida(cantidad_agua, agua_consumida)
        print("Has consumido un total de", agua_consumida, "litros de agua hasta ahora.")

if __name__ == '__main__':
    main()
