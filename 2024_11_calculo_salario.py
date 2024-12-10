salario_neto=1850
prestamo_1=175
prestamo_2=220
olp=25
arriendo=600
remitly=450
total=(salario_neto-prestamo_1-prestamo_2-olp-arriendo-remitly)
print(f"Te quedan {total}")
with open("resultado.txt", "w") as archivo:
    archivo.write(f"El total de la operación es: {total}\n")
