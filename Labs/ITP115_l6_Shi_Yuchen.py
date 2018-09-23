word1=input("Enter word 1: ")
word2=input("Enter word 2: ")

word1List=word1.strip()
word2List=word2.strip()
word1List=list(word1List.lower())
word2List=list(word2List.lower())
word1List.sort()
word2List.sort()
if word1List==word2List:
    print("The two words you entered are anagrams.")
else:
    print("The two words you entered are not anagrams.")

list1=word1.strip()
list2=word2.strip()
list1=list(list1.lower())
list2=list(list2.lower())

counter1=0
counter2=0
newList1=[]
newList2=[]
while counter1<len(list1):
    newList1.append(list1[len(list1)-counter1-1])
    counter1=counter1+1
while counter2<len(list2):
    newList2.append(list2[len(list2)-counter2-1])
    counter2=counter2+1
if newList1==list1:
    print("The first word is a palindrome.")
else:
    print("The first word is not a palindrome.")
if newList2==list2:
    print("The second word is a palindrome.")
else:
    print("The second word is not a palindrome.")
