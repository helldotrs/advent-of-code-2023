original_list = ["prefix1: text1", "prefix2: text2", "prefix3: text3"]

stripped_list = [item.split(": ", 1)[1] for item in original_list]

print(stripped_list)
