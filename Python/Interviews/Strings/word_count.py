def word_count(text):
    arr = text.split(" ")

    freq = {}
    
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    maxval = 0
    ans = ""
    for key,value in freq.items():
        if freq[key] > maxval:
            ans = key
            maxval = freq[key]
    print(f"maximum frequency word is: '{ans}' it is used {maxval} times.")
        
    return freq



print(word_count("this is a sentence for word count. this a for a "))