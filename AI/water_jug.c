#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct jugs{
	int jug_capacity;
	int jug_water;
}jug;
jug m, n;
void solve(int d){ //d is the required ltr of water in either of the jugs
	int x, s1 = 0, s2 = 0;
	FILE *fp1 = fopen("output1.txt", "w");
	FILE *fp2 = fopen("output2.txt", "w");
	fprintf(fp1, "%dltr %dltr\n", m.jug_capacity, n.jug_capacity);
	while(m.jug_water != d && n.jug_water != d){
		if(m.jug_water == m.jug_capacity){
			m.jug_water = 0;
			fprintf(fp1, "small jug is full, empty it:\n");
		}
		if(n.jug_water == 0){
			n.jug_water = n.jug_capacity;
			fprintf(fp1, "larger jug is empty, fill it:\n");
		}
		fprintf(fp1, "| %d | %d |\n", m.jug_water, n.jug_water);
		x = m.jug_capacity - m.jug_water;//free space in smaller jug
		if(n.jug_water >= x){
			m.jug_water += x; //pour it to smaller jug
			n.jug_water -= x; //hence removed from larger jug
		}
		else{
			m.jug_water += n.jug_water; //pour everything remaining
			n.jug_water -= n.jug_water;//hence removed
		}
		fprintf(fp1, "pour from larger jug to smaller one:\n");
		fprintf(fp1, "| %d | %d |\n", m.jug_water, n.jug_water);
		s1++;
	}
	m.jug_water = n.jug_water = 0;
	fprintf(fp2, "%dltr %dltr\n", m.jug_capacity, n.jug_capacity);
	while(m.jug_water != d && n.jug_water != d){
		if(n.jug_water == n.jug_capacity){
			n.jug_water = 0;
			fprintf(fp2, "larger jug is full, so empty it:\n");
			}
		if(m.jug_water == 0){
			m.jug_water = m.jug_capacity;
			fprintf(fp2, "smaller jug is empty, so fill it:\n");
		}
		fprintf(fp2, "| %d | %d |\n", m.jug_water, n.jug_water);
		x = n.jug_capacity - n.jug_water;//free space in larger jug
		if(m.jug_water >= x){
			n.jug_water += x; //pour it to larger jug
			m.jug_water -= x; //hence removed from smaller jug
			
		}
		else{
			n.jug_water += m.jug_water; //pour everything remaining
			m.jug_water -= m.jug_water; //hence removed
		}
		fprintf(fp2, "pour from smaller jug to larger one:\n");
		fprintf(fp2, "| %d | %d |\n", m.jug_water, n.jug_water);
		s2++;
	}
	fclose(fp1);
	fclose(fp2);
	if(s1 < s2)//print optimised production rules followed
		system("cat output1.txt");
	else
		system("cat output2.txt");
	system("rm output1.txt output2.txt");//comment this statement to see output of both ways if followed
	printf("\nyay! got the final state.\n");
}
int main(){
	int x, d;
	m.jug_water = n.jug_water = 0;
	printf("Enter the capacity of 1st mug, 2nd mug and required ltr of water\n");
	scanf("%d %d %d", &m.jug_capacity, &n.jug_capacity, &d);
	if(m.jug_capacity > n.jug_capacity){ //ensure that m is always smaller
		x = m.jug_capacity;
		m.jug_capacity = n.jug_capacity;
		n.jug_capacity = x;
	}
	if(n.jug_capacity < d){
		printf("Solution is not possible\n");
		return 1;
	}
	solve(d);
	return 0;
}
