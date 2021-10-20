def cypher_attack(S):
        T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
        ans = [0] * 10
        alphabet_count = [0] * 26
        sorted_count = [0] * 26
        used = [0] * 26
        N=len(S)
        for i in range(N):
                if S[i].isupper():
                        alphabet_count[ord(S[i]) - ord('A')] += 1
                elif S[i].islower():
                        alphabet_count[ord(S[i]) - ord('a')] += 1           
        for i in range(26):
                sorted_count[i] = alphabet_count[i]	

        sorted_count.sort(reverse = True)
        for i in range(10):
                ch = -1
                for j in range(26):
                        if sorted_count[i] == alphabet_count[j] and used[j] == 0:
                                used[j] = 1
                                ch = j
                                break
                        
                if ch == -1:
                        break
                x = ord(T[i]) - ord('A')
                x = x - ch
                curr = ""
                for k in range(N):
                        if S[k].islower():
                                y = ord(S[k]) - ord('a')
                        elif S[k].isupper():
                                y = ord(S[k]) - ord('A')
                        else:
                                curr+=S[k]
                                continue
                        y += x
                        if y<0:                 #x can be -ive
                                y+=26
                        if y > 25:
                                y -= 26
                        if S[k].islower():
                                curr+=chr(y+ord('a'))
                        else:
                                curr += chr(y + ord('A'))
                ans[i] = curr
        print("Possible Decryptions")
        for i in range(10):
                print(ans[i])
def main():
        S = input("Enter a string : ")
        cypher_attack(S)
main()
