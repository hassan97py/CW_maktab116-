sample_dict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york" }

# sample_dict.pop("city")
# sample_dict.update({"location": "New york"})
# print(sample_dict)


sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)