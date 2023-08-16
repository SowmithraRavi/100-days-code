# Decimal to binary
void toBinary(int N)
{
    int biarr[32];
    int i=0,j;
    while(N>0)
    {
        biarr[i]=N%2;
        N=N/2;
        i++;
    }
    for(j=i-1;j>=0;j--)
    {
        printf("%d",biarr[j]);
    }
}
