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