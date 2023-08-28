segundos_Str = input("Entre com o nr de segundos que deseja converter: ")
totalSegundos = int(segundos_Str)

dias = totalSegundos // (86400)
RestoOperacao = totalSegundos % 86400

horas = RestoOperacao// (3600)
segundosRestantes = RestoOperacao % 3600 

minutos = segundosRestantes // 60
segRestantes_final = segundosRestantes % 60


print(dias, "dias,", horas, "horas,", minutos, "minutos e", segRestantes_final, "segundos.")
#print(horas, "horas", minutos, "minutos e", segRestantes_final, "segundos")