respl = input ("O programa funciona?")
if resp1 == "SIM":
    resp2 = input("Você entende o que fez?")
    if resp2 == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        resp6 = input("Já foi na tutoria?")
    if resp6 == "SIM":
        print("Choremos !")
    else:
        print("Temos um time a disposição!")
else:
    resp3 = input("Você sabe onde está o erro?")
    if resp3 == "SIM":
        resp4 = input("Acha que pode solucionar sozinho?")
        if resp4 == "SIM":
            print ("Então mão na massa!")
        else:
            resp5 = input("Já pesquisou no Google?")
            if resp5 == "SIM":
                resp6 = input("Já foi na tutoria?")
                if resp6 == "SIM":
                    print("Choremos !")
                else:
                    print("Temos um time a disposição!")
            else: 
                print("Corre lá então!")
else: 
resp6 = input("Já foi na tutoria?")
    if resp6 == "SIM":
        print("Choremos !")
    else: 
        print("Temos um time a disposição!")
