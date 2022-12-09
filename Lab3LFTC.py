if __name__ == '__main__':
    states=[]
    tranzitii=[]
    init=[]
    alfabet=[]
    fn=[]
    i=open("inputlab3.txt", "r")
    
    inpt = i.read().split("\n") 
    for line in inpt:
        linii=line.split("->")
        left=linii[0]
        right=linii[1]  
        state=left.split(",")[0][1:]
        caracter=left.split(",")[1][0:-1]
        if state not in states:
            if state[0] == "{":
                state=state.replace("{", "").replace("}", "") 
                if state not in init:
                    init.append(state)
            states.append(state)
        if caracter not in alfabet:
            alfabet.append(caracter)
        if right[0] == "(":
            elem=right.replace("(", "").replace(")", "")
            if elem not in fn:
                fn.append(elem)
            if elem not in states:
                states.append(elem)
            tranzitii.append([state, elem])
        if right[0] == "[":
            elem = right.replace("[", "").replace("]", "")
            if elem not in states:
                states.append(elem)
            tranzitii.append([state, elem])
    print("Alfabetul este-> \n", alfabet, "\n")
    print("Starea initiala este-> \n", init, "\n")
    print("Starea finala este-> \n", fn, "\n")
    print("Starile sunt-> \n", states, "\n")
    print("Tranzitiile sunt-> \n", tranzitii, "\n")
