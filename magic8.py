import random
name = "Loriz"
question = "Est-ce que poudrier va bien ?"
answer = ""

random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
  answer = "Oui car il dort"
elif random_number == 2:
  answer = "Oui car il a bien mangé"
elif random_number == 3:
  answer = "Oui car il a joué avec son plumeau"
elif random_number == 4:
  answer = "Oui car il a regardé les oiseaux par la fenêtre"
elif random_number == 5:
  answer = "Oui car il a espionné les voisins"
elif random_number == 6:
  answer = "Non parce que je me suis pas levée dès son premier miaou à 5h du matin"
elif random_number == 7:
  answer = "Non car il mange la même saveur de pâtée depuis hier"
elif random_number == 8:
  answer = "Non car un voisin l'a réveillé"
elif random_number == 9:
  answer = "Non car il n'a pas eu de friandise depuis 1 heure"
else:
  answer = "Error"
  
print(name + " asks: " + question)
print("Magic 8 Ball's answer: " + answer)
