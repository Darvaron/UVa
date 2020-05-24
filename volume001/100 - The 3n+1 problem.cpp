#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int i, j, counter, ic, n, c, jc;
	while(scanf("%d %d", &i, &j) == 2) {
		ic = i;
		jc = j;
		if(i > j) {
			int temp = j;
			j = i;
			i = temp;
		}
		c = 0;
		for(i; i<=j; i++) {
			counter = 1;
			n = i;
			while(n != 1) {
				if(n % 2 != 0) {
					n = 3*n+1;
				} else {
					n /= 2;
				}
				counter++;
			}
			if(counter > c) {
				c = counter;
			}
		}
		cout << ic << " " << jc << " " << c << endl;
	}
	return 0;
}
