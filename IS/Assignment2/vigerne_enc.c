#include <stdio.h>
int main(int argc, char *argv[]){
	if(argc != 4){
		printf("Usage: program input_file output_file key\n");
		return 1;
	}
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	//argv[3] is the key
	char p, c;
	int i = 0;
	while((p = fgetc(ip)) != EOF){
		c =( p + argv[3][i%strlen(argv[3])] ) % 26;
	}
	return 0;
}
