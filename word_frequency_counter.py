words = input().lower().split()
special_char = ['.',',','-','_']
clean_words = []
for word in words:
    for ch in special_char:
        word = word.replace(ch," ")
        clean_words.append(word)
unique =[]
for word in words:
     if word not in unique:
        unique.append(word)
freq = []
for word in unique:
    counter = words.count(word)
    freq.append([counter,word]) 
freq.sort(reverse="true")   
for item in freq[:5] :
    print(item[0],":",item[1])
              
