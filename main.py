import random
import time

#Variables
puntaje_inicial=0
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0 
lista_intentos=[]#lista que alamcenara el puntaje de cada intento

#Lista de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Saludo inicial
print (BLUE+"\nBienvenido a mi trivia sobre la serie Dr. House"+RESET)
time.sleep(2)
print ("\nAhora sabremos que tanto sabes sobre esta serie")
time.sleep(2)
print(YELLOW+"\nComenzaras en:", puntaje_inicial, "puntos"+RESET)
time.sleep(2)

#Recopilación del nombre, apellido y edad del participante
nombre = input("\nIngresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingrese su edad: ")

while edad.isnumeric()==False:
    print(RED+"La edad ingresada no es un número"+RESET)
    edad = input("Ingrese su edad: ")


while iniciar_trivia==True:
  intentos += 1
  lista_puntaje=[]#lista que almacenara los puntajes de cada pregunta

  print(YELLOW+"\nIntento número:", intentos,""+RESET)
  input("\nPresiona Enter para continuar")
  time.sleep(2)
  
  print (BLUE+"\nHola", nombre, apellido,", responde las siguientes preguntas escribiendo la \nletra de la alternativa y presionando 'Enter' para enviar tu \nrespuesta. Empezamos en 5 segundos"+RESET)
  time.sleep(5)

  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)

  print ("\n¡Que empiece el juego!")
  time.sleep(2)
  
  # Pregunta 1
  
  print (GREEN+"\n1) ¿Qué actor representa a James Wilson?"+RESET)
  time.sleep(3)

  Pregunta1=["a) Omar Epps", "b) Hugh Laurie", "c) Robert Sean Leonard","d) Kal Peen"]

  #Alternativas de la pregunta 1
  for numero1 in range (0, len(Pregunta1)):
    print(YELLOW+"\n",Pregunta1[numero1],""+RESET)
    time.sleep(2)
      
  
  respuesta_1 = input("\nTu respuesta: ")
  time.sleep(2)

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_1 == "a":
    print (RED+"\nTotalmente incorrecto! ..."+RESET)
    lista_puntaje.append(-20)
    
  elif respuesta_1 == "b":
    print (RED+"\n..."+RESET)
    lista_puntaje.append(-5)
    
  elif respuesta_1 == "d":
    print (RED+"\nIncorrecto! ..."+RESET)
    lista_puntaje.append(-10)
    
  else:
    print (GREEN+"\nCorrecto! ..."+RESET)
    lista_puntaje.append(10)

  time.sleep(2)

  print("\nTu puntaje actual es: ", sum(lista_puntaje))
  time.sleep(3)
  print(YELLOW+"\n¿Qué te pareció la primera pregunta?, ¿fácil?")
  time.sleep(2)
  print("\nVamos a ver si puedes con la siguiente pregunta ¿listo?"+RESET)
  time.sleep(2)
  
# Pregunta 2
  
  print (GREEN+"\n2) ¿En qué temporada renuncian Cameron, Chase y Foreman?"+RESET)
  time.sleep(3)
  
  #Alternativas de la pregunta 2
  Pregunta2=["a) Temporada 3", "b) Temporada 4", "c) Temporada 2","d) Temporada 5"]

  for numero2 in range (0, len(Pregunta2)):
    print(YELLOW+"\n",Pregunta2[numero2],""+RESET)
    time.sleep(2)

  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d", "h"):
    respuesta_2 = input(RED+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_2 == "b":
    lista_puntaje.append(-5)
    print(RED+"\nIncorrecto!", nombre, apellido, "Cameron, Chase y Foreman no renuncian en la \ntemporada 4"+RESET)
  
  elif respuesta_2 == "c":
    lista_puntaje.append(-10)
    print(RED+"\nIncorrecto!", nombre, apellido,"Cameron, Chase y Foreman no renuncian en la \ntemporada 2"+RESET)
  
  elif respuesta_2 == "d":
    lista_puntaje.append(-20)
    print(RED+"\nIncorrecto!", nombre, apellido, "Cameron, Chase y Foreman no renuncian en la \ntemporada 5"+RESET)

  #Puntaje secreto si se escribe la lera h
    
  elif respuesta_2 == "h":
    lista_puntaje.append(int(edad))
    print(RED+"\nUna verdad básica de la condición humana, es que todo el mundo \nmiente, lo único que varía es acerca de que mienten. Por haber \napretado la tecla h se añadió tu edad a tu puntaje, es decir,", edad, "\npuntos"+RESET)
    
  else:
    lista_puntaje.append(15)
    print(GREEN+"\n¡Muy bien", nombre, apellido,"!"+RESET)

  time.sleep(2)

  print("\nTu puntaje actual es: ", sum(lista_puntaje))
  time.sleep(3)
  print(YELLOW+"\n¿Y como te fue con esta pregunta?, ¿difícil?")
  time.sleep(2)
  print("\nVamos a ver si puedes con la última pregunta ¿listo?"+RESET)
  time.sleep(2)

# Pregunta 3
  
  print (GREEN+"\n3) ¿Qué enfermedad padece la trece?"+RESET)
  time.sleep(2)

   #Alternativas de la pregunta 3
  Pregunta3=["a) Huntington", "b) Parkinson", "c) Síndrome de Edward","d) Síndrome de Patau"]

  for numero3 in range (0, len(Pregunta3)):
    print(YELLOW+"\n",Pregunta3[numero3],""+RESET)
    time.sleep(2)

  
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)


  if respuesta_3 == "c":
    print (RED+"\nMuy frío! ..."+RESET)
    lista_puntaje.append(-30)
    
  elif respuesta_3 == "b":
    print (RED+"\Tibio"+RESET)
    lista_puntaje.append(-10)
    
  elif respuesta_3 == "d":
    print (RED+"\nFrío ..."+RESET)
    lista_puntaje.append(-25)
  else:
    print (GREEN+"\nCaliente! ..."+RESET)
    lista_puntaje.append(40)

  time.sleep(2)
  
#Ruleta alealtoria de puntaje extra para el puntaje final
  print("\nAhora se le sumará el número que resulte al final de la siguiente \nruleta de 10 números aleatorios entre 0 y 100 a tu puntaje final:")
  time.sleep(3)
  print("\n")
  
  for x in range(0,10,1):
    y=random.randint(0,100)
    if x==9:
      print(RED+"",y,""+RESET)
      time.sleep(1)
    else:
      print(y)
      time.sleep(1)

  print("\n¡Felicidades se le sumará", y,"puntos a tu puntaje final!")
  lista_puntaje.append(y)
  
  lista_intentos.append(sum(lista_puntaje))#se agrega el puntaje al intento respectivo

  time.sleep(3)
  #Se muestra el puntaje final
  print (YELLOW+"\nGracias", nombre, apellido, "por jugar mi trivia, alcanzaste", sum(lista_puntaje), " puntos"+RESET)

  #Pregunta si lo intenta de nuevo
  print(GREEN+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  time.sleep(2)
  
  repetir_trivia = input("\nIngresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  time.sleep(2)

  if repetir_trivia != "si":  
    print(YELLOW+"\nEspero", nombre, apellido, "que lo hayas pasado bien"+RESET)
    time.sleep(2)

    print(GREEN+"\nEsta es la lista de los puntajes de todos tus intentos"+RESET)
    time.sleep(2)

  #Se muestra los puntajes de todos los intentos
    for i in range(0,len(lista_intentos),1):
      print("\nTu puntaje final del intento",i+1,"es: ",lista_intentos[i])
  
    iniciar_trivia = False 
    time.sleep(3)
    
#Frase del Dr. House
    print(BLUE+"\nY recuerda lo que una vez dijo el Dr. house:"+RESET)
    time.sleep(2)
    print(GREEN+"\nEl tiempo lo cambia todo, eso es lo que la gente dice, pero no \nes verdad. ")
    print("Hacer cosas cambia las cosas.")
    print("No hacer nada, deja las cosas exactamente como están."+RESET)
    time.sleep(5)
    
#Despedida
    print(BLUE+"\n¡Adiós!"+RESET)
  