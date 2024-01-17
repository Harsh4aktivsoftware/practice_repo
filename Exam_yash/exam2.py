# 2. You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity. For
# example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a. Return an
# array of all the universal strings in words1. You may return the answer in any order.
# For Example:
# Input: words1 = ["amazon","apple","facebook","google"], words2 = ["e","o"]
# Output: ["facebook","google"]

words1 = ["amazon","apple","facebook","google"]
words2 = ["e","o",'c']


# create function to compare elements of word1 with word2
def check(word,check_list):
    count=0
    # store word in temp
    temp=word
    for i in range(len(check_list)):
        if check_list[i] in temp:
            # replace special char with space
            temp = temp.translate(temp.maketrans(check_list[i], ' '))
            count+=1
    if count==len(check_list):
        return True
    return False

ans=[]
for word in words1:
    if check(word,words2) :
        ans.append(word)
print(ans)
