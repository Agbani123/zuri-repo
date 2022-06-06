# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
#to open file
#openfile= open("./story.txt", "r")
#print(openfile)
# or with open("./story.txt") as openfile
# print("This file is true")

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt") as f:
        content= f.read()
        #print(content)
#read_file_content("story.txt")
    return content

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    text_list = text.split()
    print(text_list)
    count={}
    for i in text_list:
        if i in count:
            count[i] += 1
        else:
            count[i]=1
    return count
print(count_words())
    #return {"as": 10, "would": 20}
  