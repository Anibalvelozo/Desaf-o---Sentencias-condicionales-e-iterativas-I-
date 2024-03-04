# Solicitar de datos al usuario
peso = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su altura: "))
# Calculo IMC
imc = peso/((estatura/100)**2)
# Clasificacion de imc 
if imc < 18.5:
    print(f" La clasificación OMS es {imc:.2f} - bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"La clasificación OMS es {imc:.2f} - adecuado")
elif imc >= 25 and imc <= 29.9:
    print(f" La clasificación OMS es {imc:.2f} - sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print(f"La clasificación OMS es {imc:.2f} - obesidad grado I")
elif imc >= 35 and imc <= 39.9:
    print(f"La clasificación OMS es {imc:.2f} - obesidad grado II")
else:
    print(f"La clasificación OMS es {imc:.2f} - obesidad grado III")
