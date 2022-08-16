def walkOnAxis(T, N):
    #T is starting point and N is the total number of lights
    distance = 0
    distance += (N-T)
    distance += N 
    for i in range(N):
        distance += i 

    return distance 

print(walkOnAxis(0, 2))

def yourName(name1, name2):
    #checks if name1 subsequence of name2
    name1List = [i for i in name1]
    name2List = [i for i in name2]

    
    for i in range(len(name1List)):
        try:
            for x in name2List[i:]:
                if name1List[i] == x:
                    if name1List == name2List[:len(name1List)]:
                        return 'YES'
                    break 
                else:
                    name2List.remove(x)
        except:
            break

    #checks if name2 subsequence of name1
    name1List = [i for i in name1]
    name2List = [i for i in name2]

    for i in range(len(name2List)):
        try:
            for x in name1List[i:]:
                if name2List[i] == x:
                    if name2List == name1List[:len(name2List)]:
                        return 'YES'
                    break 
                else:
                    name1List.remove(x)
        except:
            break
    return 'NO'

print(yourName('john', 'johanna'))
print(yourName('johanna', 'john'))
print(yourName('ira', 'ira'))
print(yourName('kayla', 'jayla'))

