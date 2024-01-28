def coinChange(coin, n): 
    solSet=[]

    for i in coin:
        while sum(solSet)<=n:
            solSet.append(i)
        
        if sum(solSet) > n:
            solSet.pop(-1)

    return solSet

print(coinChange([5,2,1],19))