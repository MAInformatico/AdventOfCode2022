
def getCommonValue(first,second,third):    
    result = ''
    for i in range(len(first)):
        for j in range(len(second)):
            for k in range(len(third)):
                if first[i] == second[j] == third[k]:
                    result = first[i]
                    break
    return result

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        values = [i.strip() for i in lines]
    
    commonLetters = []
    lettersValues = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = 0

    for i in range(0,len(values),3):        
        firstPart = values[i-2]
        secondPart = values[i-1]
        thirdPart = values[i]
        commonLetters.append(getCommonValue(firstPart,secondPart,thirdPart))


    for i in range(len(commonLetters)):
        result += lettersValues.index(commonLetters[i])        

print(result)