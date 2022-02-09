#include <iostream>
#include <string>

using namespace std;

int zlicz(string wyraz){
    int dlugosc, liczba;
    dlugosc = wyraz.length();
    liczba = 0;
    for(int i=0; i<dlugosc; i++) {
        if (wyraz[i] == 'a')
        liczba += 1;
    }
    return liczba;
}

int main()
{
    string tekst;
    int dlugosc, liczba = 0;
    cout<<"Podaj wyraz: ";
    cin>>tekst;
    
    cout<<"Liczba a w wyrazie wynosi: "<<zlicz(tekst)<<endl;
    
    system("pause");
    
    return 0;
}   
