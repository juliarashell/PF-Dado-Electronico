import pyfirmata, time
import random # push nos de resultado aleatorios de 1 a 6
import mysql.connector# conecar la base de datos a python



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
    
    # crear variables del boton y los leds
    button = board.digital[9]
    LED1 = board.digital[2]
    LED2 = board.digital[3]
    LED3 = board.digital[4]
    LED4 = board.digital[5]
    LED5 = board.digital[6]
    LED6 = board.digital[7]
    LED7 = board.digital[8]
    LED8 = board.digital[10]
    last_status = False
    counter = 0
    previous_button_state = 0
    
   
# Iniciar iterador para recibir datos de entrada
    it = pyfirmata.util.Iterator(board)
    it.start()
# configuraciion del boton
    button.mode = pyfirmata.INPUT
    
    
    
# Funcion que alamcena los datos en la base de datos    
def insertarDato(valor):
    mycursor= mydb.cursor()
    sql= "INSERT INTO registro(valores) VALUES ("+str(valor)+")"
    mycursor.execute(sql)
    mydb.commit()
    print("Registro Exitoso")

def uno():
    LED8.write(1)
    LED4.write(1)
    time.sleep(2)
    LED8.write(0)
    LED4.write(0)
    
    
def dos():
    LED8.write(1)
    LED3.write(1)
    LED7.write(1)
    time.sleep(2)
    LED8.write(0)
    LED3.write(0)
    LED7.write(0)
    
    
def tres():
    LED8.write(1)
    LED3.write(1)
    LED4.write(1)
    LED7.write(1)
    time.sleep(2)
    LED8.write(0)
    LED3.write(0)
    LED4.write(0)
    LED7.write(0)
    
    
def cuatro():
    LED8.write(1)
    LED5.write(1)
    LED7.write(1)
    LED3.write(1)
    LED1.write(1)
    time.sleep(2)
    LED8.write(0)
    LED5.write(0)
    LED7.write(0)
    LED3.write(0)
    LED1.write(0)
    

def cinco():
    LED8.write(1)
    LED5.write(1)
    LED7.write(1)
    LED4.write(1)
    LED3.write(1)
    LED1.write(1)
    time.sleep(2)
    LED8.write(0)
    LED5.write(0)
    LED7.write(0)
    LED4.write(0)
    LED3.write(0)
    LED1.write(0)
    
    
def seis():
    LED8.write(1)
    LED5.write(1)
    LED7.write(1)
    LED6.write(1)
    LED2.write(1)
    LED3.write(1)
    LED1.write(1)
    time.sleep(2)
    LED8.write(0)
    LED5.write(0)
    LED7.write(0)
    LED6.write(0)
    LED2.write(0)
    LED3.write(0)
    LED1.write(0)
    
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
                    #condiciones de encedido de led dependiendo del valor que arroje el push botton
                    if counter ==1:
                        
                        uno()
                            
                    if counter ==2:
                        
                        dos()
                    
                    if counter ==3:
                        
                        tres()
                        
                    if counter ==4:
                        
                        cuatro()
                        
                    if counter ==5:
                        
                        cinco()
                        
                    if counter ==6:
                        
                        seis()
    
    # Guardar el estado actual del botón como anterior para la siguente iteracion del boton
    previous_button_state = button_state
    
    
    