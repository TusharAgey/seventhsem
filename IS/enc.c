#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *strrev(char *word){
	char *p;
	char *ret_word = (char *)malloc(sizeof(char) * 100);
	int i;
	for(i = 0; i < strlen(word); i++){
		ret_word[i] = word[strlen(word) - 1 - i];
	}
	return ret_word;
}
int main(int argc, char *argv[]){
	if(argc == 2){ //executable input_file
			int i;
			char *word = (char *)malloc(sizeof(char) * 100);
			FILE *fp = fopen(argv[1], "r");
			FILE *out = fopen("output.txt", "w");
			if(fp){
				while(fscanf(fp, "%s", word) != EOF){	//for each word
					word = strrev(word);	//reverse it
					for(i = 0; i < strlen(word); i++){//for each char from this word
						word[i] = ~word[i];
					}
					fprintf(out, "%s ", word);
				}
			}
			else
				printf("%s does not exist\n", argv[1]);
		}
	else
		printf("Usage: encrypt input_file_name\n");
	return 0;
}
