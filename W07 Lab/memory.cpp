#include <iostream>
#include <iomanip>

using namespace std;

void one(long number);
void two(long number);
void pass() { cout << "You pass :)\n"; }
void fail() { cout << "You've failed :(\n"; }
const char* passMessage = ":)";
const char* failMessage = ":(";

/**********************************************
 * MAIN : The top of the callstack.
 **********************************************/
int main()
{
    char text[8] = "*MAIN**";
    long number = 123456;
    void (*pointerFunction)() = fail;
    const char* message = failMessage;

    // display the initial values of the local variables
    cout << "main() : " << (void*)main << endl;
    cout << "\ttext:             " << text << endl;
    cout << "\tnumber:           " << number << endl;
    cout << "\tmessage:          " << message << endl;
    cout << "\tfunction pointer: ";
    pointerFunction();

    // call the other functions
    one(number + 111111);     // 234567

    // display the new values of the local variables
    cout << "main() - after\n";
    cout << "\ttext:             " << text << endl;
    cout << "\tnumber:           " << number << endl;
    cout << "\tmessage:          " << message << endl;
    cout << "\tfunction pointer: ";
    pointerFunction();

    return 0;
}

/************************************************
 * CONVERT TO STRING
 * Convert the data from p into a human-readable string
 * by removing all the unprintable characters and replacing
 * them with a dot
 ***********************************************/
string displayCharArray(const char* p)
{
    string output;
    for (int i = 0; i < 8; i++)
        output += string(" ") + (p[i] >= ' ' && p[i] <= 'z' ? p[i] : '.');
    return output;
}

/**********************************************
 * ONE : The next item on the call stack
 **********************************************/
void one(long number)               // 234567
{
    char text[8] = "**ONE**";

    cout << "one() : " << (void*)one << endl;
    cout << "\tmessage: " << (void*)failMessage << endl;
    cout << "\tfail():  " << (void*)fail << endl;

    two(number + 111111);    // 345678
}

/**********************************************
 * TWO : The bottom of the call stack
 **********************************************/
void two(long number)              // 345678
{
    // start your display of the stack from this point
    long bow = number + 111111;     // 456789
    char text[8] = "**TWO**";
    long* pLong = NULL;
    char* pChar = NULL;

    // header for our table. Use these setw() offsets in your table
    cout << '[' << setw(2) << 'i' << ']'
        << setw(15) << "address"
        << setw(20) << "hexadecimal"
        << setw(20) << "decimal"
        << setw(18) << "characters"
        << endl;
    cout << "----+"
        << "---------------+"
        << "-------------------+"
        << "-------------------+"
        << "-----------------+\n";
    //**********************************************************************************************
    //This section displays the stack. This was helpful in seeing how the stack presents its self.
    //**********************************************************************************************
    for (long i = 65; i >= -8; i--)
    {
        pLong = &bow + (i * 2);

        cout << '[' << setw(2) << i << ']'
            << setw(15) << pLong                                //Plain address
            << setw(20) << hex << *pLong                        //Decimal value converted to hexidecimal value
            << setw(20) << dec << *pLong                        //Decimal value
            << setw(18) << displayCharArray((char*)pLong)       //Char value
            << endl;
    }
    
    //***************************************************
    // change text in main() to "*main**"
    //***************************************************
    pChar = (char*)&bow;
    int i = 0; //used to stop crazy loops

    //finds the char string *MAIN**
    while (string(pChar) != "*MAIN**" || i >= 1000) {
        pChar++;
        i++;
        if (i >= 1000) {
            cout << "You have gone too far back searching for *MAIN**" << endl;
        }
    }

    //creates what we want it to be
    char newMain[8] = "*main**";

    //because it's a char we have to loop through to put chars in one at a time into the array.
    for (i = 0; i < 7; i++)
    {
        pChar[i] = newMain[i];
    }

    //***************************************************
    // change number in main() to 654321
    //***************************************************
    pLong = (long*)&bow;
    i = 0; //used to stop crazy loops

    //finds 123456
    while (*pLong != 123456 || i >= 1000) {
        pLong++;
        i++;
        if (i >= 1000) {
            cout << "You have gone too far back searching for 123456" << endl;
        }
    }
    //changes it.
    *pLong = 654321;

    //***************************************************
    // change pointerFunction in main() to point to pass
    //***************************************************
    pLong = (long*)&bow;
    i = 0; //used to stop crazy loops

    //finds the long value of the fail function.
    while (*pLong != (long)fail || i >= 1000) {
        pLong++;
        i++;
        if (i >= 1000) {
            cout << "You have gone too far back searching for fail" << endl;
        }
    }

    //changes it to pass
    *pLong = (long)pass;

    //***************************************************
    // change message in main() to point to passMessage
    //***************************************************

    pLong = (long*)&bow;
    i = 0; //used to stop crazy loops

    //finds the long value of fail function
    while (*pLong != (long)failMessage || i >= 1000) {
        pLong++;
        i++;
        if (i >= 1000) {
            cout << "You have gone too far back searching for failMessage" << endl;
        }
    }

    //changes it to passMessage
    *pLong = (long)passMessage;
    
    //displays addresses for examples of where the code is stored where the stack is stored and where the heap is stored in memory.
    cout << "Code:  " << main << endl;
    cout << "Stack: " << &text << endl;
    cout << "Heap:  " << pLong << endl;
}
