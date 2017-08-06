#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
typedef struct jugs{
	int jug_capacity;
	int jug_water;
}jug;
jug m, n;
void solve(int d){ //d is the required ltr of water in either of the jug
	int x;
	srand(time(NULL));
	int choice = rand() % 2 + 1;//increase the randomness
	printf("%dltr %dltr\n", m.jug_capacity, n.jug_capacity);
	if(choice == 1)
		while(m.jug_water != d && n.jug_water != d){
			if(m.jug_water == m.jug_capacity)
				m.jug_water = 0;
			if(n.jug_water == 0)
				n.jug_water = n.jug_capacity;
			printf("| %d | %d |\n", m.jug_water, n.jug_water);
			x = m.jug_capacity - m.jug_water;//free space in smaller jug
			if(n.jug_water >= x){
				m.jug_water += x; //pour it to smaller jug
				n.jug_water -= x; //hence removed from larger jug
			}
			else{
				m.jug_water += n.jug_water; //pour everything remaining
				n.jug_water -= n.jug_water;//hence removed
			}
			printf("| %d | %d |\n", m.jug_water, n.jug_water);
		}
	else{
		while(m.jug_water != d && n.jug_water != d){
			if(n.jug_water == n.jug_capacity)
				n.jug_water = 0;
			if(m.jug_water == 0)
				m.jug_water = m.jug_capacity;
			printf("| %d | %d |\n", m.jug_water, n.jug_water);
			x = n.jug_capacity - n.jug_water;//free space in larger jug
			if(m.jug_water >= x){
				n.jug_water += x; //pour it to larger jug
				m.jug_water -= x; //hence removed from smaller jug
			}
			else{
				n.jug_water += m.jug_water; //pour everything remaining
				m.jug_water -= m.jug_water; //hence removed
			}
			printf("| %d | %d |\n", m.jug_water, n.jug_water);
		}
	}
}
int gcd(int no1, int no2){
	 if (no2 == 0)
       return no1;
    return gcd(no2, no1 % no2);
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
	if((d % gcd(m.jug_capacity, n.jug_capacity)) != 0){
		printf("Solution is not possible\n");
		return 1;
	}
	solve(d);
	return 0;
}