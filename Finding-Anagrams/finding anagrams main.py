def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word)!=len(anagram):
        return False
    else:
        word_list=list(word)
        anagram_list=list(anagram)
        word_list.sort()
        anagram_list.sort()
        if (word_list==anagram_list):
            return True
        else:
            return False
print(find_anagram("praise", "joy"))
print(find_anagram("meme", "eemm"))
print(find_anagram("ada", "obi"))

    