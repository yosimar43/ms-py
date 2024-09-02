def decidir_dormir(hay_ruido, hay_mas_habitaciones, se_puede_soportar_ruido):
    if not hay_ruido:
        # Dormir sin problemas
        return "Dormir sin problemas"
    
    if hay_mas_habitaciones:
        # Dormir en otra habitación
        return "Dormir en otra habitación"
    
    if se_puede_soportar_ruido:
        # Dormir usando tapones para los oídos
        return "Dormir usando tapones para los oídos"
    
    # No se puede dormir
    return "No se puede dormir"

# Ejemplo de uso
resultado = decidir_dormir(hay_ruido=True, hay_mas_habitaciones=False, se_puede_soportar_ruido=True)
print(resultado)
