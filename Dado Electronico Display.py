import pyfirmata
from pyfirmata import util
import time
import random
import mysql.connector


if __name__ == '__main__':
    # Inicializando comunicacion con arduino
    board = pyfirmata.Arduino('COM3')
    print("Comunicacion con Arduino iniciada")
    mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dado"
) 
    
    # crear variables del boton y los segmentos del display
    button = board.digital[11]
    g = board.get_pin("d:5:o")
    f = board.get_pin("d:4:o")
    a = board.get_pin("d:3:o")
    b = board.get_pin("d:2:o")
    e = board.get_pin("d:6:o")
    d = board.get_pin("d:9:o")
    c = board.get_pin("d:7:o")
    dp = board.get_pin("d:8:o")
    last_status = False
    counter = 0
    previous_button_state = 0
    
# Iniciar iterador para recibir datos de entrada
    it = pyfirmata.util.Iterator(board)
    it.start()
# configuracion del boton
    button.mode = pyfirmata.INPUT
    
# Funcion que alamcena los datos en la base de datos    
def insertarDato(valor):
    mycursor= mydb.cursor()
    sql= "INSERT INTO registro(valores) VALUES ("+str(valor)+")"
    mycursor.execute(sql)
    mydb.commit()
    print("Registro Exitoso")

    
 # Funciones de encedido y apagado del display depediendo del numero aleatorio entre(1-6)   
def digi1():
    b.write(1)                                             
    c.write(1)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)

def digi2():
    a.write(1)
    b.write(1)
    g.write(1)
    e.write(1)
    d.write(1)
    c.write(0)
    f.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)
    
def digi3():
    a.write(1)
    b.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    e.write(0)
    f.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)

def digi4():
    f.write(1)
    g.write(1)
    b.write(1)
    c.write(1)
    a.write(0)
    d.write(0)
    e.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)
    
def digi5():
    a.write(1)
    f.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    b.write(0)
    e.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)
    
def digi6():
    a.write(1)
    f.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    e.write(1)
    b.write(0)
    dp.write(1)
    time.sleep(2)
    b.write(0)                                             
    c.write(0)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
    dp.write(0)
    
#variables a utilizar para insertar datos a la base de datos   
aux_a=0
aux_b=0
    
while True:
                    
    #lectura del boton
    button_state = button.read()
    #decimos que si button_state es diferente al valor de previous_button_state 
    if button_state != previous_button_state:
        #button_state es igual a verdadero
            if button_state is True:
                #decimos que si button_state es diferente a last_status
                if button_state != last_status:
                    #contador va ser igual a  un numero aleatorios entre 1 y 6
                    counter = random.randint(1,6)
                    print(counter)
                    time.sleep(1)
                    #aux_a es igual a contador pero contador se convierte en un entero
                    aux_a=int(counter)
                    #esta condicion nos sirve para que si un valor ya obtenido se repite de igual forma lo ingrese a la tabla de la base de datos
                    if aux_a==aux_b:
                        insertarDato(aux_a)
                    else:
                        insertarDato(aux_a)
                    aux_b=aux_a
                    #condiciones de encedido del display dependiendo del valor que arroje el push botton
                    if counter ==1:
                        
                        digi1()
                            
                    if counter ==2:
                        
                        digi2()
                    
                    if counter ==3:
                        
                        digi3()
                        
                    if counter ==4:
                        
                        digi4()
                        
                    if counter ==5:
                        
                        digi5()
                        
                    if counter ==6:
                        
                        digi6()
    
    # Guardar el estado actual del botón como anterior para la siguente iteracion del boton
    previous_button_state = button_state
    
    