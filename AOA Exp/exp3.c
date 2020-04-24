#include<stdio.h>
#define max 10



int arr[max][max];

int findSort(int x,int w)
{
    int ShortVal;
    int min=100000;
    if(x=w)
        return 0;
    else
    {
        int flag=-1;
        for (int i = 0; i <= w ; i++)
        {
            if(arr[x][i] !=0)
            {
                flag = 0 ;
                ShortVal = arr[x][i]+ findSort(i,w);
            }
        }

        if(min>ShortVal)
            min = ShortVal;
        
    }
    return min;
    
}

void main()
{
    int n ,shortdist=0;
    printf("enter no of nodes :");
    scanf("%d",&n);
    for (int i = 0; i < n; ++i)
    {
        arr[i][i]=0;
        for (int j = i+1; j < n; ++j)
        {
            printf("enter the weight from %c to %c :");
            scanf("%d",&arr[i][j])
        }



    }
}
