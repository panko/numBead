#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
	int d;
	double res = 0;
	std::cin >> d;
	std::vector<double> v;
	for (int i = 0; i < d; ++i)
	{
		double f;
		std::cin >> f;
		v.push_back(f);
	}
	for (int i = 0; i < d; ++i)
	{
		double f;
		std::cin >> f;
		res += v[i] * f;
	}

	printf("%.12f\n", res);

	return 0;
}