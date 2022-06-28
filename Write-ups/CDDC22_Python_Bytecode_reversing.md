# Python Bytecode Reversing (Ring 4)

## CATEGORY

Reversing

## Challenge

Hello, I'm Python 3.6.9!

Can you reverse me?

[Challenge File](./Resources/python_bytecode.txt)

## Solution

[Python bytecode documentation](https://docs.python.org/3.5/library/dis.html)
(from 3.5.9 but sufficient for the bytecode encountered here)

Solved using guess and check with dis.dis(). In my opinion, the bytecode is same as postfix notation. 

Recovered python script is as follows.

```
import dis

def main():
    decrypted = ''
    original = ''
    # key = b'CDDC22{Welcome_to_Singapore_2022_DSTA_CTF}'
    key = [67,68,68,67,50,50,123,87,101,108,99,111,109,101,95,116,111,95,83,105,110,103,97,112,111,114,101,95,50,48,50,50,95,68,83,84,65,95,67,84,70,125]
    result = [19,21,21,19,0,0,0,48,48,93,86,48,46,9,15,43,31,10,103,48,23,21,0,73,61,45,84,106,109,98,6,7,51,27,22,101,120,10,4,107,121,0]

    for i in range(0,len(key)):
        decrypted += chr(result[i]^key[i])

    for i in decrypted:
        if 'a' <= i <= 'z':
            original += chr(ord(i)+13 if i<='m' else ord(i) - 13)
        elif 'A' <= i <= 'Z':
            original += chr(ord(i)+13 if i<='M' else ord(i) - 13)
        else:
            original += i
    print(decrypted)
    print(original)
dis.dis(main)
main()
```

The original variable turns out to be the flag. 

## Flag

CDDC22{tH15_PyC_cH4Llen9E_15_E45y_R19HT??}

