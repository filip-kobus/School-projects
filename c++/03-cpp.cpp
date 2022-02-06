#include <iostream>
#include <string>

using namespace std;

string transformator( string wyraz, 
					char litera1, 
					char litera2) {
	
	int dlugosc = wyraz.length();

    for(int i=0; i<dlugosc; i++) {
        if(wyraz[i] == litera1)
            wyraz[i] = litera2;
		}
	return wyraz;
}

int main()
{
    string zmienna;
    cout << "Podaj wyraz: ";
    cin>>zmienna;
    

    cout<<endl<<"Wyraz po transformacji: "<<transformator(zmienna, 'a', 'b')<<endl;

    system("pause");

    return 0;
}
