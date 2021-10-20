#2X2 HILL CYPHER
'''
mod of key should be invertible and coprime with 26 and have a modulus such that its divisible by matrix
some acceptable keys:
cbbb
fccb
feed
'''
def encryption(S,key):
        N=len(S)
        val=[]
        val_key=[]
        for i in key:
                if i.isupper():
                        val_key.append(ord(i)-ord('A'))
                elif i.islower():
                        val_key.append(ord(i)-ord('a'))
        for i in S:
                if i.isupper():
                        val.append(ord(i)-ord('A'))
                elif i.islower():
                        val.append(ord(i)-ord('a'))
                else:
                        continue
        for i in range(1,len(val),2):
                x1=(val_key[0]*val[i-1] + val_key[1]*val[i])%26
                x2=(val_key[2]*val[i-1] + val_key[3]*val[i])%26
                val[i-1]=x1
                val[i]=x2
        temp=0
        ans=""
        for i in range(N):
                if S[i].isupper():
                        ans+=chr(val[temp]+ord('A'))
                        temp+=1
                elif S[i].islower():
                        ans+=chr(val[temp]+ord('a'))
                        temp+=1
                else:
                        ans+=S[i]
                        continue
        return ans
def check_key(key):
        val_key=[]
        for i in key:
                if i.isupper():
                        val_key.append(ord(i)-ord('A'))
                elif i.islower():
                        val_key.append(ord(i)-ord('a'))
        
        div=val_key[0]*val_key[3] - val_key[1]*val_key[2]
        if div==0 or div%2==0 or div%13==0:
                return 0
        
        for i in val_key:
                if i%div!=0:
                        return 0
        val_key[0] ,val_key[3]=val_key[3] ,val_key[0]
        val_key[1]*=-1
        val_key[2]*=-1
        for i in range(4):
                val_key[i]/=div
                if val_key[i]<0:
                        val_key[i]+=26
             
        return val_key
def decrypt(S,key):
        inv_key=check_key(key)
        if(inv_key==0):
                return 0
        N=len(S)
        val=[]
        for i in S:
                if i.isupper():
                        val.append(ord(i)-ord('A'))
                elif i.islower():
                        val.append(ord(i)-ord('a'))
                else:
                        continue
        for i in range(1,len(val),2):
                x1=(inv_key[0]*val[i-1] + inv_key[1]*val[i])%26
                x2=(inv_key[2]*val[i-1] + inv_key[3]*val[i])%26
                val[i-1]=x1
                val[i]=x2
        temp=0
        ans=""
        for i in range(N):
                if S[i].isupper():
                        ans+=chr(int(val[temp])+ord('A'))
                        temp+=1
                elif S[i].islower():
                        ans+=chr(int(val[temp])+ord('a'))
                        temp+=1
                else:
                        ans+=S[i]
                        continue
        return ans
def main():
        S=input("Data:")
        while True:
                key=input("Key: ")
                f=1
                if len(key)==4 :
                        for i in key:
                                if i.isalpha():
                                        continue
                                else:
                                        f=0
                                        break
                else:
                        print ("Invalid Key try again")
                        continue
                if f==1:
                        if check_key(key)==0:
                                print ("Invalid Key try again")
                                continue
                        else:
                                break
        print("Encrypted Data:"+encryption(S,key))
        print("Decrypted Data:"+decrypt(encryption(S,key),key))
main()
