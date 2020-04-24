


def lcs(A,B,a,b):
    if a==0 or b==0:# end of the string
        return 0
    elif A[a-1]==B[b-1]:# when char is same then we have to increase the lcs value by 1
        return 1 + lcs(A,B,a-1,b-1)
    else:# move to lefr and right and pick max from theme
        return max(lcs(A,B,a,b-1),lcs(A,B,a-1,b))
    


s1=input('enter first string :')
s2=input('enter second string :')
print(lcs(s1,s2,len(s1),len(s2)))