#include <iostream>
#include <string>

using namespace std;

int main()
{
    string wyraz;
    int dlugosc;


    cout<<"Podaj wyraz: ";
    cin>>wyraz;

    dlugosc = wyraz.length();

    cout<<endl<<"Pierwsza litera: "<<wyraz[0]<<endl;
    cout<<"Ostatnia litera: "<<wyraz[dlugosc-1];

    return 0;
}