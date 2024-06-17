print("## H.265 Video Bit Rate Calculator ##\n## = Created by z4lvus = ##")
print("\n") #Salto de linea
print("#   #   #####  ####  ##### ")
print("#   #       #  #     #     ")
print("#####      #   ####  ##### ")
print("#   #    #     #  #      # ")
print("#   # o #####  ####  ##### ")
print("\n") #Salto de linea
print("Nota: La calidad va a depender del tipo de video,\npara videos con mucho movimiento siempre se recomienda elegir la calidad alta.")
print("\n")

#Factor de compresion H265
EF_baja = 0.09                              #Alta calidad, menor compresion
EF_media = 0.07                             #Promedio entre calidad y compresion
EF_alta = 0.06                              #Baja calidad, mayor compresion

mbps_conversion = 1000000

resolucion_H = int(input("Ingrese la resolucion Horizontal: "))
resolucion_V = int(input("Ingrese la resolucion Vertical: "))
FPS = int(input("Ingrese los FPS: "))
calidad = input("Ingrese la calidad deseada: ").lower()                      #Usar alta, media o baja, mientras menor calidad mayor sera la compresion


def calculadora(resolucion_H, resolucion_V, FPS, calidad, EF_baja, EF_media, EF_alta, mbps_conversion):
    if calidad == "alta":
        return resolucion_H * resolucion_V * FPS * EF_baja / mbps_conversion
    elif calidad == "media":
        return resolucion_H * resolucion_V * FPS * EF_media / mbps_conversion
    elif calidad == "baja":
        return resolucion_H * resolucion_V * FPS * EF_alta / mbps_conversion

#Verificar la calidad, resolucion y FPS ingresados

if calidad not in ("alta", "media", "baja"):
    print("La calidad ingresada no es valida")
elif int(FPS) > 300:
    print("Los FPS ingresados superan el maximo soportado por el codec")
elif int(resolucion_H) > 7680 or int(resolucion_V) > 4320:
    print("La resolucion ingresada excede el maximo soportado por el codec")
else:
    resultado = calculadora(resolucion_H, resolucion_V, FPS, calidad, EF_baja, EF_media, EF_alta, mbps_conversion)      #Llamar la funcion
    resultado_redondeado = round(resultado, 2)                                                                          #Redondear a 2 decimales
    print("El video bit rate necesario es: ", resultado_redondeado, "Mbps")                                             #Entregar resultado

input("Presione Enter para salir")