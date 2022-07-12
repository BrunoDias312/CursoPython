"""
Converter minutos em horas, mim e seg
"""

segundos = int(input("Informe o horario: "))

hora = segundos // 3600
min = segundos // 60
seg = segundos % 60

if seg == 0:
    print(f"{hora}:{min}:{seg}0")
else:
    print(f"{hora}:{min}:{seg}")