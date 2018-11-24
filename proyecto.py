from tabulate import tabulate

print("Venta de garrafones".center(120, "="))
print("PRIMER VIAJE: ")

g1 = int(input("Garrafones vendidos de $8.00: "))
g2 = int(input("Garrafones vendidos de $10.00: "))
g3 = int(input("Garrafones vendidos de $11.00: "))
g4 = int(input("Garrafones vendidos de $12.00: "))
g5 = int(input("Garrafones vendidos de $15.00: "))

sub1 = int(f" {g1 * 8}")
sub2 = int(f" {g2 * 8}")
sub3 = int(f" {g3 * 8}")
sub4 = int(f" {g4 * 8}")
sub5 = int(f" {g5 * 8}")

total =(sub1 + sub2 + sub3 + sub4 + sub5)

Venta_garrafones = [['$8.00', 'Subtotal', '$10.00', 'Subtotal', '$11.00', 'Subtotal', '$12.00', 'Subtotal', '$15.00', 'Subtotal'], [g1, sub1, g2, sub2, g3, sub3, g4, sub4, g5, sub5]] 
                                                                                                                                       
print(tabulate(Venta_garrafones, headers='firstrow', tablefmt='fancy_grid'))

print(f"Tu venta de este viaje fue de: $ {total}")


print("SEGUNDO VIAJE: ")

f1 = int(input("Garrafones vendidos de $8.00: "))
f2 = int(input("Garrafones vendidos de $10.00: "))
f3 = int(input("Garrafones vendidos de $11.00: "))
f4 = int(input("Garrafones vendidos de $12.00: "))
f5 = int(input("Garrafones vendidos de $15.00: "))

subf1 = int(f" {f1 * 8}")
subf2 = int(f" {f2 * 8}")
subf3 = int(f" {f3 * 8}")
subf4 = int(f" {f4 * 8}")
subf5 = int(f" {f5 * 8}")

total2 =(subf1 + subf2 + subf3 + subf4 + subf5)

Venta_garrafones2 = [['$8.00', 'Subtotal', '$10.00', 'Subtotal', '$11.00', 'Subtotal', '$12.00', 'Subtotal', '$15.00', 'Subtotal'], [f1, subf1, f2, subf2, f3, subf3, f4, subf4, f5, subf5]] 
                                                                                                                                       
print(tabulate(Venta_garrafones2, headers='firstrow', tablefmt='fancy_grid'))

print(f"Tu venta de este viaje fue de:$ {total2} ")


print("TERCER VIAJE: ")

h1 = int(input("Garrafones vendidos de $8.00: "))
h2 = int(input("Garrafones vendidos de $10.00: "))
h3 = int(input("Garrafones vendidos de $11.00: "))
h4 = int(input("Garrafones vendidos de $12.00: "))
h5 = int(input("Garrafones vendidos de $15.00: "))

subh1 = int(f" {h1 * 8}")
subh2 = int(f" {h2 * 8}")
subh3 = int(f" {h3 * 8}")
subh4 = int(f" {h4 * 8}")
subh5 = int(f" {h5 * 8}")

total3 =(subh1 + subh2 + subh3 + subh4 + subh5)

Venta_garrafones3 = [['$8.00', 'Subtotal', '$10.00', 'Subtotal', '$11.00', 'Subtotal', '$12.00', 'Subtotal', '$15.00', 'Subtotal'], [h1, subh1, h2, subh2, h3, subh3, h4, subh4, h5, subh5]] 
                                                                                                                                       
print(tabulate(Venta_garrafones3, headers='firstrow', tablefmt='fancy_grid'))

print(f"Tu venta de este viaje fue de: ${total3}")


print("CUARTO VIAJE: ")

i1 = int(input("Garrafones vendidos de $8.00: "))
i2 = int(input("Garrafones vendidos de $10.00: "))
i3 = int(input("Garrafones vendidos de $11.00: "))
i4 = int(input("Garrafones vendidos de $12.00: "))
i5 = int(input("Garrafones vendidos de $15.00: "))

subi1 = int(f" {i1 * 8}")
subi2 = int(f" {i2 * 8}")
subi3 = int(f" {i3 * 8}")
subi4 = int(f" {i4 * 8}")
subi5 = int(f" {i5 * 8}")

total4 =(subi1 + subi2 + subi3 + subi4 + subi5)

Venta_garrafones4 = [['$8.00', 'Subtotal', '$10.00', 'Subtotal', '$11.00', 'Subtotal', '$12.00', 'Subtotal', '$15.00', 'Subtotal'], [i1, subi1, i2, subi2, i3, subi3, i4, subi4, i5, subi5]] 
                                                                                                                                       
print(tabulate(Venta_garrafones4, headers='firstrow', tablefmt='fancy_grid'))

print(f"Tu venta de este viaje fue de: ${total4}")


print("QUINTO VIAJE: ")

j1 = int(input("Garrafones vendidos de $8.00: "))
j2 = int(input("Garrafones vendidos de $10.00: "))
j3 = int(input("Garrafones vendidos de $11.00: "))
j4 = int(input("Garrafones vendidos de $12.00: "))
j5 = int(input("Garrafones vendidos de $15.00: "))

subj1 = int(f" {j1 * 8}")
subj2 = int(f" {j2 * 8}")
subj3 = int(f" {j3 * 8}")
subj4 = int(f" {j4 * 8}")
subj5 = int(f" {j5 * 8}")

total5 =(subj1 + subj2 + subj3 + subj4 + subj5)

Venta_garrafones5 = [['$8.00', 'Subtotal', '$10.00', 'Subtotal', '$11.00', 'Subtotal', '$12.00', 'Subtotal', '$15.00', 'Subtotal'], [j1, subj1, j2, subj2, j3, subj3, j4, subj4, j5, subj5]] 
                                                                                                                                       
print(tabulate(Venta_garrafones5, headers='firstrow', tablefmt='fancy_grid'))

print(f"Tu venta de este vaije fue de: ${total5}")

total_dia = (f" Tu venta del dia es de: ${total + total2 + total3 + total4 + total5}")
total_dia
             
      
