#include<stdio.h>
#include<conio.h>
int main()
{
    int a[10],i,n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    printf("Enter %d elements:\n",n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("The elements in the array are:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    getch();
    return 0;
}