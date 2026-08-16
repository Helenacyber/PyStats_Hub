#This program checks wherether given two strings are anagram or not. 
#Anagram words are words that contain the same characters in any order.

def are_anagrams(str_1 ,str_2):
     list_1 =[]
     list_2 =[]
     result_1 =[]
     result_2 = []
     for s1 in str_1.lower():
          list_1.append(s1)
     result_1 = sorted(list_1)
     for s2 in str_2.lower():
               list_2.append(s2)
     result_2 = sorted(list_2)
     if result_1 == result_2:
            return True
     return False

print(are_anagrams("listen","silent"))  
print(are_anagrams("School master", "The classroom"))   
print(are_anagrams("A gentleman", "Elegant man"))  
print(are_anagrams("Hello",'world'))  
print(are_anagrams("apple", "banana"))
print(are_anagrams("cat", "dog"))  
  
