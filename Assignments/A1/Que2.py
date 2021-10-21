
 #function to encode 
def encode(text,a,b):
    result=""
    
    for i in range(0,len(text)):
        if text[i]>='a' and text[i]<='z':
            n=ord(text[i])-ord('a')
            n=a*n + b
            result+=chr(((n)%26)+ord('a'))
        elif text[i]>='A' and text[i]<='Z':
            n=ord(text[i])-ord('A')
            n=a*n + b
            result+=chr(((n)%26)+ord('A'))
        else:
            result+=text[i]
    return result

#function to find inverse
def find_inv(a):
    ans=1
    while True:
        if (ans*a)%26==1:
            return ans
        ans+=1
#function to decode

def decode(text,a,b):
    result=""
    a_inverse=find_inv(a)
    for i in range(0,len(text)):
        if text[i]>='a' and text[i]<='z':
            n=ord(text[i])-ord('a')
            n=a_inverse*(n-b)
            result+=chr(((n)%26)+ord('a'))
        elif text[i]>='A' and text[i]<='Z':
            n=ord(text[i])-ord('A')
            n=a_inverse*(n-b)
            result+=chr(((n)%26)+ord('A'))
        else:
            result+=text[i]
    return result
       

def main():
    while True:
        print("MENU")
        print("1.Encode")
        print("2.Decode")
        print("3.Exit")
        while True:
            try:
                choice=int(input('Enter choice: '))            
                if choice <1 or choice >3:
                    print("Input not in range 1-3 !! Try Again")
                    continue
                break
            except:
                print("Invalid Choice")
        if choice<3:
            text=input("Enter a string : ")  #Input string
            while True:
                try:
                    a=int(input('Enter a: '))            #input a
                    if a%2==0 or a%13==0:
                        print("a must be coprime with 26. try again!!")
                        continue
                    break
                except:
                    print("Please enter a number")
            while True:
                try:
                    b=int(input('Enter b: '))            #input b
                    break
                except:
                    print("Please enter a number")
        if choice==1:
            print("Encoded String : ",encode(text,a,b))
        elif choice==2:
            print("Decoded String : ",decode(text,a,b))
        else:
            break
                
main()
        
    
