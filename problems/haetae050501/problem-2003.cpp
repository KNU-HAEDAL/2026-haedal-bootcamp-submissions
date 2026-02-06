#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);

	int arr[10001] = { 0, };
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}

	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		int j = i + 1;
		int sum = arr[i];
		while (1)
		{
			if (sum == m)
			{
				cnt++;
				break;
			}
			else if (sum > m)
			{
				break;
			}

			if (j == n)
			{
				break;
			}

			sum += arr[j];
			j++;
		}
	}
	printf("%d", cnt);

	return 0;
}