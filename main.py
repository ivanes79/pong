from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

#definir la tasa de refresco (fps) de nuestro bucle de foto
#cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(15,300)
raqueta2 = Raqueta(782,300)


game_over = False

while not game_over:
    #imprimir los milisegundos que tarda cada fotograma (ejemplo 60 1000msg/60)
    #vt=cronometro.tick(280)#variable para controlar la velocidad entre fotogramas
    #print(vt)


    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True



        """    
        #mover raqueta
        if evento.type == pg.KEYDOWN:
            if evento.key ==pg.K_UP:
                print("ARRIBA")
                raqueta1.pos_y -= 3
            elif evento.key == pg.K_DOWN:    
                print("ABAJO")   
                raqueta1.pos_y +=3
        
    estado_teclas = pg.key.get_pressed()

    if estado_teclas[pg.K_UP] == True:
        raqueta2.pos_y -= 1
    if estado_teclas[pg.K_DOWN] == True:
        raqueta2.pos_y += 1     
    if estado_teclas[pg.K_e] == True:
        raqueta1.pos_y -= 1
    if estado_teclas[pg.K_x] == True:
        raqueta1.pos_y += 1   
    """
      

    pantalla_principal.fill((0,128,94))
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)


    pelota.dibujar(pantalla_principal)
    pelota.Mover(800,600)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    pg.display.flip()