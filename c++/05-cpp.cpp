#include <iostream>
#include <string>

using namespace std;

string zamiana(string napis) {
    int dlugosc = napis.length();
    string pomoc = "";
    
    pomoc += napis[dlugosc-1];
    
    for(int i = 1; i < dlugosc - 1; i++) {
        pomoc += napis[i];
    }
    
    pomoc += napis[0];
    return pomoc;
}

int main()
{
    string wyraz;

    cout<<"Podaj wyraz: ";
    cin>>wyraz;

    cout<<endl<<"Wyraz po zamianie liter: "<<zamiana(wyraz)<<endl;

    system("pause");
    
    return 0;
}
