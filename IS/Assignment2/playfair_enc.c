#include <stdio.h>
#include <string.h>
int exists(char k, char matrix[]){
	int i;
	for(i = 0; i < 25; i++){
		if(matrix[i] == k)
			return 1;
	}
	return 0;
}
char matrix[25];
int indexof(char k){

}
int main(int argc, char *argv[]){
	if(argc != 3){
		printf("Usage: program input_file output_file");
		return 1;	
	}
	FILE *ip = fopen(argv[1], "r");
	FILE *op = fopen(argv[2], "w");
	if(ip){
		char key[26];
		int i, j;
		char alphabets[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
		i = 0;
		printf("Enter the key:- ");
		scanf("%s", key);
		for(i = 0; i < 25; i++){
			matrix[i] = '-';
		}
		for(i = 0, j = 0; i < strlen(key); i++, j++){
			if(exists(key[i], matrix)){
				i++;
				if(i == strlen(key))
					break;
			}
			matrix[j] = key[i];
			alphabets[key[i] - 97] = '-';//deleting already used alphabet
		}
		for(i = 0; j < 25; i++, j++){
			while(alphabets[i] == '-' || alphabets[i] == 'j')
				i++;
			matrix[j] = alphabets[i];
		}
		for(i = 0; i < 25; i++){
			printf("%c\n", matrix[i]);
		}
		char p, q, hist;
		while((p = fgetc(ip)) != EOF){
			hist = p;
			
		}
	}
	else{
		printf("Input file does not exist.\n");
		return 1;
	}
	return 0;
}
