simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 =('V', 'D', 'L')
restas = ('CD', 'CM', 'XL', 'XC', 'IV', 'IX')

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido")
    else:
        raise ValueError(f"parámetro {simbolo} debe ser un string")

def orden_magnitud(caracter):
    valor = simbolo_a_entero(caracter)
    return len(str(valor))

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parámetro {romano} debe ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = ""
    orden_magnitud_global = 0
    orden_magnitud_letra = 0
    ha_habido_resta = False

    for letra in romano:
        orden_magnitud_letra = orden_magnitud(letra)
        if letra == valor_anterior:
            orden_magnitud_global = orden_magnitud_letra
            if letra in tipo_5:
                raise ValueError("No es romano")
            elif c_repes >= 2:
                raise ValueError("Demasiadas repeticiones")
            elif ha_habido_resta:
                raise ValueError("Demasiadas restas")
            c_repes += 1
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior + letra not in restas:
                raise ValueError("Resta no permitida")
            elif c_repes > 0:
                raise ValueError("Resta tras repeticion no permitida")
            elif ha_habido_resta:
                raise ValueError("Demasiadas restas")

            ha_habido_resta = True
            suma -= 2*simbolo_a_entero(valor_anterior)
            c_repes = 0
        else:
            if orden_magnitud_global > orden_magnitud_letra:
                ha_habido_resta = False

            if ha_habido_resta:
                raise ValueError("Demasiadas restas")

            orden_magnitud_global = orden_magnitud_letra
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra    
    return suma
