#include<stdio.h>
#include<string.h>
typedef struct jugs{
	int jug_capacity;
	int jug_water;
}jug;
jug m, n;
void solve(int d){ //d is the required ltr of water in either of the jug
	int x;
	printf("%dltr jug\t%dltr jug\n", m.jug_capacity, n.jug_capacity);
	while(m.jug_water != d && n.jug_water != d){
		if(m.jug_water == m.jug_capacity)
			m.jug_water = 0;
		if(n.jug_water == 0)
			n.jug_water = n.jug_capacity;
		x = m.jug_capacity - m.jug_water;//free space in smaller jug
		if(n.jug_water >= x){
			m.jug_water += x; //pour it to smaller jug
			n.jug_water -= x; //hence removed from larger jug
		}
		else{
			m.jug_water += n.jug_water; //pour everything remaining
			n.jug_water -= n.jug_water;//hence removed
		}
		printf("%d\t%d\n", m.jug_water, n.jug_water);
	}
	//fill n
	//put it into m
	//if m is full, empty it
	//if n is empty, full it
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
	solve(d);
	return 0;
}