#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n, a;
    cout << "Enter number: ";
    cin >> n;
    vector<int> arr;
    while (n != 0)
    {
        a = n % 10;
        arr.push_back(a);
        n = n / 10;
    }
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
    }
}