# 3. Given a string s, reverse the string according to the following rules:
# - All the characters that are not English letters remain in the same position.
# - All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
# Example 1:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 2:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

sample_str="Test1ng-Leet=code-Q!"

count=0
# to store special char with index no. as a list
d={}
ans=[]
sample=''

for i in range(len(sample_str)):
    # add element 1 by 1 in sample
    sample+=sample_str[i]
    # print('sample =>',sample)
    if sample_str[i].isupper() or sample_str[i].islower() or sample_str[i]==' ':
        pass
    else:
        # create list to store indexes
        count=[]
        # count occurance of char and store in d
        for j in range(len(sample_str)):
            if sample_str[i]==sample_str[j]:
                count.append(j)
        d[sample_str[i]]=count
        sample_str= sample_str.translate(sample_str.maketrans(sample_str[i], ' '))


# create function to add special char in reverse string
def add_dict():
    val={}
    for i in d:
        for j in d[i]:
            val[j]=i

    for i in sorted(val):

        ans.insert(i,val[i])

# split string from space
l=sample_str.split(' ')
s=''

# copy in s
for i in l:
    s+=i
#  reverse string
sample_str=s[::-1]

# convert reverse string in list
for i in sample_str:
    ans.append(i)
# print(sample_str)


add_dict()

# convert list in string
a=''
for i in ans:
    a+=i
print(a)