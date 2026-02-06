#include <stdio.h>

int main(void)
{
	int n, m, i, j, num;
	int basket[100] = { 0 };

	scanf("%d %d", &n, &m);

	for (int p = 0; p < n; p++)
		basket[p] = p + 1;

	for (int p = 0; p < m; p++)
	{
		scanf("%d %d", &i, &j);
		i--; j--;
		for (int q = 0; q <= (j - i) / 2; q++)
		{
			num = basket[i + q];
			basket[i + q] = basket[j - q];
			basket[j - q] = num;
		}

	}

	for (int p = 0; p < n; p++)
		printf("%d ", basket[p]);
}