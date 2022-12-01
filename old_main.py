from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")




#definir la tasa de refresco (fps) de nuestro bucle de foto
cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(15,300)
raqueta2 = Raqueta(782,300)
pelota.vx = 1
raqueta1.vy = 3
raqueta1.vy = 3
inicial =0
final=50
game_over = False

while not game_over:

    #imprimir los milisegundos que tarda cada fotograma (ejemplo 60 1000msg/60)
    vt=cronometro.tick(600)#variable para controlar la velocidad entre fotogramas
    #print(vt)


    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
  

    pantalla_principal.fill((0,128,94))
    pg.draw.line(pantalla_principal, (255,255,255), (400,inicial), (400,final), width=8)
    
    #pg.draw.line(pantalla_principal, (0,128,94), (400,inicial), (400,final), width=8)


    inicial += 5
    final += 10

    #logica de choque
  

    #pelota.comprobar_choque(raqueta1,raqueta2)
    pelota.comprobar_choque2(raqueta1,raqueta2)#da igual el orden de las raquetas en main 
    pelota.Mover(800,600)  
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    pelota.dibujar(pantalla_principal)
    
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    
    pelota.marcador(pantalla_principal)

    pg.display.flip()

