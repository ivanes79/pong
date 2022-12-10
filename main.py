
import pygame as pg
from pantallas import Partida,Menu,Resultado,Records
from scene_controller import SceneController

inicio = SceneController()
inicio.start()
'''
menu = Menu()
menu.bucle_pantalla()
records = Records()
records.bucle_pantalla()
#juego = Partida()#creamos el objeto de clase partida

#juego.bucle_fotograma()# llamamos al bucle de fotograma


juego = Partida()
valor_resultado = juego.bucle_fotograma()
print("El resultado final:",valor_resultado)
resultado = Resultado(valor_resultado)
resultado.bucle_pantalla()


menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == 'jugar':
    juego = Partida() # creamos objeto clase partida
    juego.bucle_fotograma() #llamamos al bucle fotograma
final = Resultado()
#crear otra ventana para decir quien es el ganador
'''
