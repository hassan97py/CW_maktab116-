sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = dict.fromkeys(keys , 0)
# for i in keys:
#     result[i]=sample_dict.get(i)
# print(result)


result["name"] = sample_dict.get("name")
result["salary"] = sample_dict.get("salary")
print(result)