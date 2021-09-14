/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
int i,firstD,secondD,thirdD,fourthD;
printf("numbers\n");
for(i=100;i<=5000;i++)
{
    firstD  =  i % 10;
     secondD = (i/10) % 10;
     thirdD  = (i/100) % 10;
     
     if(firstD == 0 || secondD == 0 || thirdD == 0)
		{
	   printf("%d adds up to 8, but has digit 0. So this need to be excluded\n",i);
		}
		else 
		printf("%d adds up to 8\n",i);
}
    return 0;
}
