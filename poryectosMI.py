def organizar_objeto():
    # print("Colores disponibles")
    colores = ["Azul","Rojo","Verde"]
    print(colores)
    color = int(input("de que color es la tapa"))

    if color == "Azul":
        mover_servomotor("canasta_azul")
        activar_segundo_servomotor()
        return
    if color == "Rojo":
        mover_servomotor("canasta_roja")
        activar_segundo_servomotor()
        return
    if color == "Verde":
        mover_servomotor("canasta_verde")
        activar_segundo_servomotor()
        return
    
    print("No hay objeto o color no identificado")

def mover_servomotor(destino):
    print(f"Moviendo servomotor a {destino}")

def activar_segundo_servomotor():
    print("Activando segundo servomotor, empujando objeto")

# Ejemplo de uso:
organizar_objeto()