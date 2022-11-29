import pygame as pg

class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=100,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))    
    '''
    def mover(self,tecla_arriba,tecla_abajo,ymax =600,ymin=0):
        estado_teclas = pg.key.get_pressed()
        
        if estado_teclas[tecla_arriba] == True and self.pos_y > (ymax-self.h//2):
            self.pos_y -= 1
        if estado_teclas[tecla_abajo] == True and self.pos_y > (ymin-self.h//2):
            self.pos_y += 1 
    '''
    def mover(self,tecla_arriba,tecla_abajo,y_max=600,y_min=0):
        estado_teclas = pg.key.get_pressed()
       
        if estado_teclas[tecla_arriba] == True and self.pos_y > (y_min+self.h//2):
            self.pos_y -= 1
        if estado_teclas[tecla_abajo] == True and self.pos_y < (y_max-self.h//2) :
            self.pos_y += 1  
        

class Pelota:
    def __init__(self,pos_x,pos_y,radio=20,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.contadorderecha = 0
        self.contadorizquierda = 0
        self.font= pg.font.Font(None,40)
    
    def Mover(self,xmax,ymax):
        
        self.pos_x += self.vx
        self.pos_y += self.vy     


        if  self.pos_y >= ymax-self.radio or self.pos_y <= 0 + self.radio :
            self.vy *= -1
        #objetivo que l apelota desaparezca en los limites y aparezca rebotando hacia el lado contrario

        if self.pos_x >= xmax+self.radio*10: #limite derecha
            self.contadorizquierda += 1
            self.vx *= -1
            self.vy *= -1
            

        if self.pos_x <= 0 - self.radio*10 : #limite izquierda
            self.contadorderecha += 1
            self.vx *= -1
            self.vy *= -1

    def marcador(self,pantalla_principal):
        #font= pg.font.Font(None,40) fuera del while
        # dentro del while
        marcador_derecha = self.font.render(str(self.contadorizquierda),0,(255,255,0))
        marcador_izquierda = self.font.render(str(self.contadorderecha),0,(255,255,0))
        pantalla_principal.blit(marcador_derecha,(200,50))
        pantalla_principal.blit(marcador_izquierda,(600,50))

    def posicionX(self):

        return self.pos_x + self.radio 
    
    def posicionY(self):
        return self.pos_y + self.radio 

    def izquierda(self):       
        if self.pos_x < 400 :
            return True
        return False

    def derecha(self): 
        if self.pos_x > 400 :
            return True
        return False 

    def arriba(self):
        if self.pos_y < 300 :
            return True
        return False 


    def abajo(self):
        if self.pos_y > 300 :
            return True
        return False  
 

        '''
        if  self.pos_x >= xmax-self.radio or self.pos_x <= 0 + self.radio :
            self.vx *= -1
            
        if  self.pos_y >= ymax-self.radio or self.pos_y <= 0 + self.radio :
            self.vy *= -1
        '''


    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)

  