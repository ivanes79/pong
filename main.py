
import pygame as pg
from pantallas import Partida,Menu


juego = Partida()#creamos el objeto de clase partida

juego.bucle_fotograma()# llamamos al bucle de fotograma


menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == 'jugar':
    juego = Partida() # creamos objeto clase partida
    juego.bucle_fotograma() #llamamos al bucle fotograma

#crear otra ventana para decir quien es el ganador

