def naiveAlgo(sentence,key):
    lenKey=len(key)
    count =0
    flag= True
    for y in sentence:
        if key == sentence[count:count+lenKey]:
            print('match found at',count)
            flag=False
        count+=1
    if flag:
        print('\t\tmatch not found!!')

s1= input('enter the string in which key is to be searched :')
s2= input('enter the key :')
naiveAlgo(s1,s2)