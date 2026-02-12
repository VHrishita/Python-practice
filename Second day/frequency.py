sentence = "Happy dog"
freq = {}
for ch in sentence:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
