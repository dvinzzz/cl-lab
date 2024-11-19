import math

def main():
    alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Enter two prime numbers p and q:")
    
    p = int(input("eter p val"))
    q = int(input("enter q val"))

    n = p * q
    z = (p - 1) * (q - 1)
    print("Enter the value of d:")
    d = int(input())
       

   
    e = None  
    for j in range(1, z):
        if (j * d) % z == 1:
            e = j
            break

    if e is None:
        print("No valid public key e found. Please check the value of d.")
        return

    print(f"n={n}, z={z}, e={e}")

    print("ENCRYPTION-CIPHERTEXT")
    print("Enter the plain text:")
    plaintext = input().upper()
    print("Cipher: ", end="")
    ciphertext = []
    for char in plaintext:
        if char in alphabet:
            s = alphabet.index(char)
            k2 = pow(s, e, n)  
            ciphertext.append(k2)
            print(k2, end=" ")

    print()

    print("Decipher: ", end="")
    for k2 in ciphertext:
        m = pow(k2, d, n)  
        print(alphabet[m], end="")
    
    print()

if __name__ == "__main__":
    main()
