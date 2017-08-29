#include <stdio.h>
#include <stdlib.h>
struct myVector{
	int missionaries;
	int cannibals;
	int boat;//1=I have boat & 0=I dont have boat
}right_bank, left_bank;
int d;//the boat capacity
void nextStep(){
	if(right_bank.boat == 1){
		if((left_bank.missionaries - (left_bank.cannibals + 1) >= 0 || left_bank.missionaries == 0) && right_bank.cannibals - 1 >= 0){ //send 1 cannibals to other side, if no side effect
			left_bank.cannibals += 1;
			right_bank.cannibals -= 1;
		}
		else if((left_bank.missionaries - (left_bank.cannibals + d) >= 0 || left_bank.missionaries == 0) && right_bank.cannibals - d >= 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals += d;
			right_bank.cannibals -= d;
		}
		else if((right_bank.missionaries - (right_bank.cannibals + d) >= 0 || left_bank.cannibals == 0) && right_bank.missionaries - d >= 0){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries -= d;
			left_bank.missionaries += d;
		}
		else if((right_bank.missionaries >= 1 && right_bank.cannibals >= 1 && right_bank.cannibals - 1 >= 0) && right_bank.missionaries - 1 >= 0){ //send a pair of missionari and cannibal to other side if available
			left_bank.missionaries += 1;
			left_bank.cannibals += 1;
			right_bank.cannibals -= 1;
			right_bank.missionaries -= 1;
		}
		else if(right_bank.missionaries - (right_bank.cannibals + 1) >= 0 && right_bank.missionaries - 1 >= 0){ //send 1 missinaries to other side, if no side effect
			right_bank.missionaries -= 1;
			left_bank.missionaries += 1;
		}
		right_bank.boat = 0;
		left_bank.boat = 1;
	}
	else if(left_bank.boat == 1){
		if((right_bank.missionaries - (right_bank.cannibals + d) >= 0 || right_bank.missionaries == 0) && left_bank.cannibals - d >= 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals -= d;
			right_bank.cannibals += d;
		}
		else if((left_bank.missionaries - (left_bank.cannibals + d) >= 0) && (right_bank.cannibals <= right_bank.missionaries + d) && left_bank.missionaries - d >= 0){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries += d;
			left_bank.missionaries -= d;
		}
		else if(left_bank.missionaries >= 1 && left_bank.cannibals >= 1 && left_bank.missionaries - (d/2) >= 0 && left_bank.cannibals - (d/2) >= 0 && (right_bank.cannibals <= right_bank.missionaries + (d/2))	){ //send a pair of missionari and cannibal to other side if available
			left_bank.missionaries -= d/2;
			left_bank.cannibals -= d/2;
			right_bank.cannibals += d/2;
			right_bank.missionaries += d/2;
		}
		else if(left_bank.missionaries >= 1 && left_bank.cannibals >= 1 && left_bank.missionaries - 1 >= 0 && left_bank.cannibals - 1 >= 0 && (right_bank.cannibals <= right_bank.missionaries + 1)	){ //send a pair of missionari and cannibal to other side if available
			left_bank.missionaries -= 1;
			left_bank.cannibals -= 1;
			right_bank.cannibals += 1;
			right_bank.missionaries += 1;
		}
		else if((right_bank.missionaries - (right_bank.cannibals + 1) >= 0 || right_bank.missionaries == 0) && left_bank.cannibals - 1 >= 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals -= 1;
			right_bank.cannibals += 1;
		}
		else if((left_bank.missionaries - (left_bank.cannibals + 1) >= 0) && (left_bank.missionaries - 1 >= 0) && (right_bank.cannibals <= right_bank.missionaries + 1)){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries += 1;
			left_bank.missionaries -= 1;
		}
		left_bank.boat = 0;
		right_bank.boat = 1;
	}
}
int possible(){
	if(d >= 4)
		return 1;
	if(d == 3 && left_bank.missionaries <= 4)
		return 1;
	if(d == 2 && left_bank.missionaries <= 3)
		return 1;
	return 0;
}
int main(int argc, char *argv[]){
	//input number of missionaries and cannibals(single number)
	if(argc != 3){
		printf("Usage: program number_of_missionaries boat_capacity\n");
		return 1;
	}
	d = atoi(argv[2]);
	left_bank.missionaries = left_bank.cannibals = atoi(argv[1]);
	left_bank.boat = 1;
	right_bank.missionaries = right_bank.cannibals = right_bank.boat = 0;
	if(!possible()){
		printf("Solution not possible\n");
		return -1;
	}
	int flag = 0;
	FILE *fp = fopen("temp.txt", "a");
	printf("Left side of river\tright side of river\n");
	printf("| M | C |\t| M | C |\n");
	printf("| %d | %d |\t| %d | %d |\n", left_bank.missionaries, left_bank.cannibals, right_bank.missionaries, right_bank.cannibals);
	fprintf(fp, "| %d | %d |\t| %d | %d |\n", left_bank.missionaries, left_bank.cannibals, right_bank.missionaries, right_bank.cannibals);
	int i = 0;
	while(i < 20){
		if((right_bank.missionaries == atoi(argv[1])) && (right_bank.cannibals == atoi(argv[1])))
			break;
		nextStep();
		printf("| %d | %d |\t| %d | %d |\n", left_bank.missionaries, left_bank.cannibals, right_bank.missionaries, right_bank.cannibals);
		fprintf(fp, "| %d | %d |\t| %d | %d |\n", left_bank.missionaries, left_bank.cannibals, right_bank.missionaries, right_bank.cannibals);
		if(d == 2 && atoi(argv[1]) == 3 && i == 4){
			flag = 1;
			break;
		}
		i++;
	}
	fclose(fp);
	if(flag == 1){
		system("./support.sh");
		system("rm temp.txt");
	}
	
	return 0;
}