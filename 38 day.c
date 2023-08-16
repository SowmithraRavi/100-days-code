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
#binary to decimal
int binary_to_decimal(char str[]) {
    int decimal = 0;
    int base = 1;  
    int length = strlen(str);

    for (int i = length - 1; i >= 0; i--) {
        if (str[i] == '1') {
            decimal += base;
        }
        base *= 2;  
    }

    return decimal;
}
