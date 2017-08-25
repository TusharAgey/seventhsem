#include <stdio.h>
#include <stdlib.h>
struct myVector{
	int missionaries;
	int cannibals;
	int boat;//1=I have boat & 0=I dont have boat
}right_bank, left_bank;
void nextStep(){
	if(right_bank.boat == 1){
		if(left_bank.missionaries - (left_bank.cannibals + 2) >= 0 || left_bank.missionaries == 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals += 2;
			right_bank.cannibals -= 2;
		}
		else if(right_bank.missionaries - (right_bank.cannibals + 2) >= 0 || left_bank.cannibals == 0){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries -= 2;
			left_bank.missionaries += 2;
		}
		else if(right_bank.missionaries >= 1 && right_bank.cannibals >= 1){ //send a pair of missionari and cannibal to other side if available
			left_bank.missionaries++;
			left_bank.cannibals++;
			right_bank.cannibals--;
			right_bank.missionaries--;
		}
		else if(left_bank.missionaries - (left_bank.cannibals + 1) >= 0 || left_bank.missionaries == 0){ //send 1 cannibals to other side, if no side effect
			left_bank.cannibals += 1;
			right_bank.cannibals -= 1;
		}
		else if(right_bank.missionaries - (right_bank.cannibals + 1) >= 0){ //send 1 missinaries to other side, if no side effect
			right_bank.missionaries -= 1;
			left_bank.missionaries += 1;
		}
		right_bank.boat = 0;
	}
	else if(left_bank.boat == 1){
		if(right_bank.missionaries - (right_bank.cannibals + 2) >= 0 || right_bank.missionaries == 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals -= 2;
			right_bank.cannibals += 2;
		}
		else if(left_bank.missionaries - (left_bank.cannibals + 2) >= 0 || right_bank.missionaries == 0){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries += 2;
			left_bank.missionaries -= 2;
		}
		else if(left_bank.missionaries >= 1 && left_bank.cannibals >= 1){ //send a pair of missionari and cannibal to other side if available
			left_bank.missionaries--;
			left_bank.cannibals--;
			right_bank.cannibals++;
			right_bank.missionaries++;
		}
		else if(right_bank.missionaries - (right_bank.cannibals + 2) >= 0 || right_bank.missionaries == 0){ //send 2 cannibals to other side, if no side effect
			left_bank.cannibals -= 1;
			right_bank.cannibals += 1;
		}
		else if(left_bank.missionaries - (left_bank.cannibals + 2) >= 0){ //send 2 missinaries to other side, if no side effect
			right_bank.missionaries += 1;
			left_bank.missionaries -= 1;
		}
		left_bank.boat = 0;
	}
}
int main(int argc, char *argv[]){
	//input number of missionaries and cannibals(single number)
	if(argc != 2){
		printf("Usage: program number_of_missionaries\n");
		return 1;
	}
	left_bank.missionaries = left_bank.cannibals = atoi(argv[1]);
	left_bank.boat = 1;
	right_bank.missionaries = right_bank.cannibals = right_bank.boat = 0;
	printf("Left side of river\tright side of river\n");
	printf("| M | C |\t| M | C |\n");
	while((right_bank.missionaries != atoi(argv[1])) && (right_bank.cannibals != atoi(argv[1]))){
		printf("| %d | %d |\t| %d | %d |\n", left_bank.missionaries, left_bank.cannibals, right_bank.missionaries, right_bank.cannibals);
		nextStep();
	}
	return 0;
}