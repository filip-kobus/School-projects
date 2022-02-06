#include <iostream>
#include <string>

using namespace std;

bool teksty_sa_identyczne(string t1, string t2) {
    int i, dl1, dl2;
    dl1=t1.length();
    dl2=t2.length();
    while (i<dl1 && i<dl2 && t1[i] == t2[i])
        i++;
    return i==dl1 && i==dl2;
}

int main()
{
    string tekst1,tekst2;
    int dlugosc;
    cout<<"Podaj pierwszy tekst: ";
    cin>>tekst1;
    cout<<"Podaj drugi tekst: ";
    cin>>tekst2;
    if(teksty_sa_identyczne(tekst1, tekst2))
    cout<<"Teksty sa identyczne!";
    else
    cout<<"teksty sa rozne!";
    cout<<endl;
    system("pause");
    return 0;
}