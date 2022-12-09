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
        
        if caracter not in alfabet:
            alfabet.append(caracter)
            
        if state not in states:
            if state[0] == "{":
                state=state.replace("{", "").replace("}", "") 
                if state not in init:
                    init.append(state)
            states.append(state)
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
    print("Alfabet:\n", alfabet, "\n")
    print("Initial state:\n", init, "\n")
    print("Final states:\n", fn, "\n")
    print("Stari:\n", states, "\n")
    print("Tranzitii:\n", tranzitii, "\n")