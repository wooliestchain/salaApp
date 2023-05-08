import datetime

start_time = datetime.time(9, 0, 0)  # heure de début : 9h00
end_time = datetime.time(17, 0, 0)  # heure de fin : 17h00



current_time = datetime.datetime.now().time()  # heure actuelle

if start_time <= current_time <= end_time:
    print("L'heure actuelle est comprise dans la plage horaire.")
else:
    print("L'heure actuelle est en dehors de la plage horaire.")

plage = (start_time,end_time)

print(plage)