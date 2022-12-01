'''
from figura_class import Pelota

objPelota = Pelota(300,400)

print(objPelota.derecha)
print(objPelota.izquierda)
print(objPelota.arriba)
print(objPelota.abajo)
'''
def funcionespecial(*parametros):
    print(type(parametros))
    for params in parametros:
        print(params)

funcionespecial("jose",25,[1,2,3,4])