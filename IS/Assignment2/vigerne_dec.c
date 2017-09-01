#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]){
	int flag = 0;
	if(argc != 4){
		printf("Usage: program input_file output_file key\n");
		return 1;
	}
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	//argv[3] is the key
	char p, c, d;
	int i = 0;
	while((c = fgetc(ip)) != EOF){
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
		d = argv[3][i%strlen(argv[3])];
		if(d <= 122 && d >= 97){
			d -= 97;
		}
		else if(d <= 90 && d >= 65)
			d -= 65;
		else{
			printf("input only alphabets\n");
			return 1;
		}
		p =( c - d) % 26;
		fputc((char)(flag == 1 ? p + 97 : p + 65 ), op);
		flag = 0;
	}
	return 0;
}
