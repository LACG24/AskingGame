import re

def lee_respuestas():
    #Convierte el archivo con las respuestas en una lista
    respuestas_lista=[]
    respuestas_final=[]
    archivo=open("Respuestas.txt","r",encoding="utf-8")
    renglon=archivo.readline() 
    while renglon!="":
        respuestas_lista.append(renglon.split())
        renglon=archivo.readline()
    for i in range(len(respuestas_lista)):
        espaciado = " ".join(respuestas_lista[i])
        if espaciado == "":
            continue
        else:
            respuestas_final.append(espaciado)
    archivo.close()
    return(respuestas_final)

def calificar(obtenido,correcto):
    #Identifica y almacena las respuestas correctas
    correctas=0
    mayuscula=obtenido.upper()
    if mayuscula.count(correcto)>0:
        correctas+=1
    return correctas
        
def cuestionario():
    #Lee las preguntas del documento, las imprime y pide las respuestas
    contador=0
    correctas=0
    preguntas=[]
    resultados=[]
    respuestas=lee_respuestas()
    archivo=open("Preguntas.txt","r",encoding="utf-8")
    renglon=archivo.readline() 
    while renglon!="":
        preguntas.append(renglon.split())
        renglon=archivo.readline()
    for i in range(len(preguntas)):
        texto_espaciado = " ".join(preguntas[i]) 
        if texto_espaciado == "":
            respuesta_usuario=input("R: ")
            print("")
            correctas+=calificar(respuesta_usuario,respuestas[contador])
            contador+=1
        else:
            if texto_espaciado[0]=="¯": #Reiniciar contador de resultados con cada tema
                resultados.append(correctas)
                correctas=0
            print(texto_espaciado)
    archivo.close()
    return resultados

def main():
    #Imprime el resultado final las veces indicadas
    resultados=cuestionario()
    resultado_total=sum(resultados)
    print("\nTiene",resultado_total, "resultados correctos en total")
    
main()

