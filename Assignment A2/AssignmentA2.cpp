#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int dataBit,count,m,r,arr[20],d,d1;		
	//m=no. of data bits. r= no. of redundant bits. arr[] contains individual data bit
	dataBit=count=m=r=0;
	cout<<"Enter number of Data bits you want to enter: "<<endl;
	cin>>dataBit;
	m=dataBit;
	while(m+r+1>pow(2,r))
	{
		count++;
		r=count;
	}
	cout<<"Number of Redundant bits to be added: "<<r<<"\nTotal number of bits= "<<m<<" + "<<r<<" = "<<m+r<<endl;
	cout<<"Enter the data bits one by one :"<<endl;
	for(int i=1;i<=m;i++)
		cin>>arr[i];
	cout<<"\nData Bits entered"<<endl;
	for(int i=1;i<=m;i++)
		cout<<arr[i]<<" ";
	cout<<endl;

	//below part is used for inserting parity bits to data code. parity bits need to be fit in locations
	// 2^d where d>=0.
	int data[m+r];
	d=0;				//used to enter values into 2^n'th position
	d1=1;				//used to enter data bits which have been user derived. d1 is used in the array arr.

	for(int i=1;i<=m+r;i++)
	{
		if((i)==pow(2,d))
		{
			data[i]=0;  //enters 0 as a redundant bit
			d++;		//increment to go to next position
		}
		else
		{
			data[i]=arr[d1]; //if position is not 1,2,4,8,16, then enter data bit into it's position
			d1++;			//increment to go to next position
		}
	}
	cout<<"Data bits encoded with Parity bits(X): "<<endl;
	for(int i=1;i<=m+r;i++)
	{
		cout<<data[i]<<" ";	//displays data bit+redundant bit.
	}
	d1=0;					//we'll be reusing d1 as a value to signify redundant bits
	int min,max,parity,j,s;
	min=max=0;

	//Parity bit calculation
	for(int i=1; i<m+r; i=pow(2,d1))	//i is a redundant bit.
	{
		d1++;
		parity=0;			//just initializing parity bit
		j=i;
		s=i;
		min=1;
		max=i;
		for(j;j<=m+r;)
		{
			for(s=j;max>=min && s<=m+r;min++, s++)
			{
				if(data[s]==1)
					parity++;
			}
			j=s+i;
			min=1;
		}
		if(parity%2==0)//Even Parity
		{
			data[i]=0;
		}
		else
		{
			data[i]=1;
		}
	}
	cout<<"\nHamming codewords for even parity are: "<<endl;

	for(int i=1; i<=m+r;i++)
	{
		cout<<data[i]<<" ";
	}
	cout<<endl<<endl;
}
