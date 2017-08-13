#include <stdio.h>
#include <stdlib.h>
int gcd(int no1, int no2){
	 if (no2 == 0)
       return no1;
    return gcd(no2, no1 % no2);
}
int main(int argc, char *argv[]){
	int flag = 0, a, b, c, p;
	if(argc != 5){
		printf("Usage: program input_filename output_filename a b\n");
		return 1;
	}
	a = atoi(argv[3]);
	b = atoi(argv[4]);
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	if(ip && gcd(a, b) == 1){
		while((p = fgetc(ip)) != EOF && (p != '\n')){
			if(p <= 122 && p >= 97){
				p -= 97;
				flag = 1;
			}
			else if(p <= 90 && p >= 65)
				p -= 65;
			else{
				printf("input only alphabets\n");
				return 1;
			}
			c = ((a * p) + b) % 26;
			fputc((char)(flag == 1 ? c + 97 : c + 65 ), op);
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
