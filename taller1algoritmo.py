# taller1 algoritmo.py

# consumo de energia en kwh

consumo = int(input("Ingrese el consumo de energia en kwh: "))

if consumo <= 100:
    categoria = "bajo"
    precio = 450
    recomendacion = "'excelente ahorro energetico' ."
elif 101 <consumo <= 200:
    categoria = "medio"
    precio = 500
    recomendacion = "'consumo normal' ."
elif 201<= consumo <= 350:
    categoria = "alto"
    precio = 650
    recomendacion = "'considere reducir el uso de electrodomesticos' ."
else:
    categoria = "critico"
    precio = 800
    recomendacion = "'alerta: consumo excesivo. revise fugas o desconecte equipos' ."

valor_a_apagar = consumo * precio
# categoria
print("Categoria de consumo:", categoria)
# valor a pagar
print("Valor a pagar: $", valor_a_apagar)
# recomendacion
print("Recomendacion:", recomendacion)  