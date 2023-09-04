#include <stdio.h>
int main(void) {
    int key=0,i=0,n=0;
    scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++){
	    scanf("%d",&arr[i]);
	  }
	 scanf("%d",&key);
	 for(i=0;i<n;i++){
	     if(arr[i]==key){
	           printf("yes");
	           return;
	        } 
	    }
	 printf("NO");
	 return 0;
}
