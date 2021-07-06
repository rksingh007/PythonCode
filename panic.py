phrase = "Don't panic!"
plist = list(phrase)
new_phrase = "on tap"
new_list = []
print(phrase)
print(plist)
for j in new_phrase:
    for i in phrase:
        if i==j:
            if i not in new_list:
                new_list.append(i)
join_list = ''.join(new_list)
print(join_list)

new_plist = ''.join(plist)
#print(new_plist)