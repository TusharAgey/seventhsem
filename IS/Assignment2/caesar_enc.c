#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]){
	int flag = 0, a, b, c, p, k;
	if(argc != 4){
		printf("Usage: program input_filename output_filename k\n");
		return 1;
	}
	k = atoi(argv[3]);
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	if(ip){
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
			c = (p + k) % 26;
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
