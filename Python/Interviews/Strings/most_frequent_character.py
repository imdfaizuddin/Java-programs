#  Find the Most Frequent Character:

#     Problem: Write a function to find the most frequent character in a string.
#     Solution 1 (Using a dictionary): Iterate through the string, building a dictionary where keys are characters and values are their frequencies. Then, iterate through the dictionary to find the character with the maximum frequency.

text = "Mississippi"
def most_freq_char(text):
    freq = {}
    for item in text:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    print(freq)
    most = 0
    answer = ''
    for key in freq:
        if freq[key] > most:
            answer = key
            most = freq[key]
            
    print(answer)

most_freq_char(text)

def most_and_second_most_freq():
    s = 'mississeiepepei'
    f = dict()
    for char in s:
        if char in f:
            f[char] += 1
        else:
            f[char] = 1
            
    print(f)
    max1 = 0
    max2 = 0
    val = ''
    val2 = ''
    for key in f:
        
        if f[key] > max1 or (key < val and f[key] == max1):
            if max1 != f[key]:
                max2 = max1
            max1 = f[key]
            val = key
        elif f[key] > max2 and f[key] != max1:
            max2 = f[key]
            val2 = key
    print(val,max1,val2,max2)

most_and_second_most_freq()