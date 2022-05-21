#Variables
import string

#Definir variables
mes = "Enero 2022"
dias_lab = int(input("Ingresa los días laborales :"))
pago_dia = int(input("Ingresa el pago por día :"))

#Proceso
pago_bruto = dias_lab * pago_dia
iva_tras = pago_bruto * 16
sub_total = iva_tras + pago_bruto
iva_reten = 2/3*iva_tras
isr_reten = pago_bruto*0.1
pago_neto = sub_total-iva_reten-isr_reten

#Salida de datos
print("Mes :", mes)
print("La cantidad de pago base es de:", round(pago_bruto, 2))
print("La cantidad de IVA trasladado es de :", round(iva_tras, 2))
print("La cantidad de subtotal es de : ", sub_total)
print("La cantidad de IVA retenido es de :", iva_reten)
print("La cantidad de ISR retenido es de : ", isr_reten)
print("La cantidad de pago neto es de :", pago_neto)
