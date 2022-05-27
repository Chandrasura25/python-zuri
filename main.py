# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt') as f:
     contents = f.read()
     return "Hello World"
print(read_file_content('story.txt'))

def count_words():
   text = read_file_content("story.txt")
    # [assignment] Add your code here
   unique_keys ={}
   with open ('story.txt', 'r') as f:
       for i,line in enumerate(f):
        words = line.strip().split()
        for word in set(words):
            unique_keys.setdefault(word, []).append(i+1) 
            return unique_keys
print(count_words())            
#     return {"as": 10, "would": 20}
