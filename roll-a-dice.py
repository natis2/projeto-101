import random



response= "y"

while response == "y":
    no = random.randint(1,6)
    if no == 1:
     print("[-----]")
     print("[     ]")
     print("[  0  ]")
     print("[     ]")
     print("[-----]")

    if no == 2:
     print("[-----]")
     print("[     ]")
     print("[  0  ]")
     print("[  0  ]")
     print("[-----]")

    if no == 3:
     print("[-----]")
     print("[  0  ]")
     print("[  0  ]")
     print("[  0  ]")
     print("[-----]")

    if no == 4:
     print("[-----]")
     print("[     ]")
     print("[  00 ]")
     print("[  00 ]")
     print("[-----]")

    if no == 5:
     print("[-----]")
     print("[  0  ]")
     print("[ 000 ]")
     print("[  0  ]")
     print("[-----]")

    if no == 6:
     print("[-----]")
     print("[  00 ]")
     print("[  00 ]")
     print("[  00 ]")
     print("[-----]")

    print(no)
    response=input("Pressione y se quiser jogar o dado :")

