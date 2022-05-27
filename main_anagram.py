def find_anagram(word,anagram):
    if(sorted(word) != sorted(anagram)):
        return False
    else:
        return True
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))
