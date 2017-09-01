#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int gcd(int no1, int no2){
	 if (no2 == 0)
       return no1;
    return gcd(no2, no1 % no2);
}
int modInverse(int a, int m){
    a = a%m;
    for (int x=1; x<m; x++)
       if ((a*x) % m == 1)
          return x;
    return -1;
}
int fix(int val){//if c-b is negative, return a fixed number
	if(val >= 0)
		return val;
	int temp = 26, i = 1;
	while(temp < abs(val)){
		temp = 26 * i;
		i++;
	}
	return (temp - abs(val));
}
int main(int argc, char *argv[]){
	int flag = 0, a, b, c, p, x;
	if(argc != 5){
		printf("Usage: program input_filename output_filename a b\n");
		return 1;
	}
	a = atoi(argv[3]);
	b = atoi(argv[4]);
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	a = modInverse(a, 26);//find x such that ax~=1%26
	if(ip && gcd(a, b) == 1){
		while((c = fgetc(ip)) != EOF && (c != '\n')){
			if(c <= 122 && c >= 97){
                                c -= 97;
                                flag = 1;
                        }
                        else if(c <= 90 && c >= 65)
                                c -= 65;
                        else{
				printf("input only alphabets\n");
                                return 1;
                        }
            x = fix(c - b);
			p = (a * x);
			p = p % 26;
			if(p < 0)
				p += 26;
			fputc((char)(flag == 1 ? p + 97: p + 65), op);
			flag = 0;
		}
		fclose(ip);
	}
	else{
		printf("Please check if the input file is available and a and b are co-prime\n");
	}
	fclose(op);
	return 0;
}
