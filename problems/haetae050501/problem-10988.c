#include <stdio.h>
#include <string.h>

int main(void)
{
	char c[100];
	int count = 0;
	scanf("%s", c);

	for (int i = 0; i <= strlen(c) / 2; i++)
	{
		if (c[i] != c[strlen(c) - i - 1])
			count++;
	}
	if (count == 0)
		printf("1");
	else
		printf("0");
}