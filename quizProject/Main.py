nombre = input("Ingrese su nombre: ")
dias = int(input("Ingrese el numero de dias: "))
salario = int(input("Ingrese el salario correspondiete a los dias: "))

prima = salario*dias/360
cesantias=salario*dias/360
interesesCesantias=cesantias*0.12/dias
vacaciones=salario*dias/720
liquidacion=prima+cesantias+interesesCesantias+vacaciones

print(f"""Señor {nombre} para los {dias} laborados y con el salario de ${salario}, su liquidacion se compone de
      la siguiente manera: 
      prima: {prima: .2f}
      Cesantia: {cesantias: .2f}
      intereses cesantias: {interesesCesantias: .2f}
      Vacaciones: {vacaciones: .2f}
      Liquidacion: {liquidacion: .2f}""")

