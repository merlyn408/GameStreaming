import random
print("""
What shall I stream next?
 a)   Days Gone
 b)   Resident Evil 2
 c)   Fortnite
 d)   Apex Legends
 e)   Death Stranding
 f)   Surprise Us!
""")
tally={'Days Gone': 0,
  'Resident Evil 2': 0,
  'Fortnite': 0,
  'Apex Legends': 0,
  'Death Stranding': 0
}
choice=""
games=['Days Gone', 'Resident Evil 2','Fortnite','Apex Legends','Death Stranding']
while True: 
  print('\n [Type "quit" to quit. Type "menu" to view the menu] \nPlease enter your choice: \t')
  ch=input("")
  if ch=='quit':
    break
  elif ch=='menu':
    print("""
What shall I stream next?
 a)   Days Gone
 b)   Resident Evil 2
 c)   Fortnite
 d)   Apex Legends
 e)   Death Stranding
 f)   Surprise Us!
""")
  elif ch=='a':
    choice='Days Gone'
  elif ch=='b':
    choice='Resident Evil 2'
  elif ch=='c':
    choice='Fortnite'
  elif ch=='d':
    choice='Apex Legends'
  elif ch=='e':
    choice='Death Stranding'
  elif ch=='f':
    choice=random.choice(games)
    print(f"Surprise! You got {choice}")
  

  tally[choice]+=1
  print(f"You have chosen {choice}. I appreciate your time and hope to see you in the next one!")

print("\n Survey results: \n")
for game,count in tally.items():
  print(f"{game}:{count}")
