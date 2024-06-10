lst1 = ["Mike", "Danny", "Jim", "Annie"] 
lst2 = [4, 12, 7, 19]

merged_list = [(lst1[i], lst2[i]) for i in range(0, len(lst1))]
merged_list.sort()
print(merged_list)