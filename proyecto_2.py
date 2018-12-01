
# coding: utf-8

# In[4]:


print("Venta de garrafones". center(120, "="))

viajes={}
print("Escribe precio de garrafones y 0 para terminar")
num_viaje = int(input("Viajes realizados: "))

for nviaje in range ( num_viaje):
    print(f"---#nviaje: {nviaje +1}---")
    
    suma = 0
    viajes[nviaje] = {}
    while True:
        precio = int(input("Precio: "))
        
        if precio !=0:
            num_vendido = int(input(f"Garrafones vendidos de ${precio}: "))
            viajes[nviaje][precio] = num_vendido
            
            sub_total = num_vendido * precio
            print(f"Tu subtotal de es de: ${sub_total}")
            
            for sub_total in range():
                suma += sub_total
            print(suma) 
                        
        else:
            break
               
    

