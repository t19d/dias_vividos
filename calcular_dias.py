# encoding: utf-8
import time

# DÍAS DE CADA MES
dias_anho = (31,28,31,30,31,30,31,31,30,31,30,31)

# FECHA ACTUAL
fecha_actual = time.strftime("%d/%m/%Y")
dia_today = fecha_actual[0]+fecha_actual[1]
mes_today = fecha_actual[3]+fecha_actual[4]
anho_today = fecha_actual[6]+fecha_actual[7]+fecha_actual[8]+fecha_actual[9]
dia_hoy = int(dia_today)
mes_hoy = int(mes_today)
anho_hoy = int(anho_today)

# NACIMIENTO
dia = input ("Día de nacimiento: ")
mes = input ("Mes de nacimiento: ")
anho = input ("Año de nacimiento: ")



# RESTAR (DÍAS QUE SOBRAN DEL AÑO DE NACIMIENTO)
# DÍAS
restar_dias = dia
# MESES
for i in range (0, (mes-1)):
    restar_dias += dias_anho[i]


# SUMAMOS (EN EL AÑO DE NACIMIENTO SUMAMOS LOS DÍAS DEL AÑO Y DEPUÉS LE RESTAMOS LOS DÍAS EN LOS QUE NO ESTABA VIVO)
# DÍAS
dias_tot=dia_hoy
# MESES
for i in range (0, (mes_hoy-1)):
    dias_tot += dias_anho[i]
# AÑOS
for i in range (anho, anho_hoy):
    if (i%400==0):
        dias_tot += 366
    elif (i%100==0):
        dias_tot += 366
    elif (i%4==0):
        dias_tot += 366
    else:
        dias_tot += 365

print dias_tot-restar_dias
