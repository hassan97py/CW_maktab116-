

def top_three_items(shop_items):
    sorted_items = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)
    top_three = dict(sorted_items[:3])
    return top_three

shop_items = {'T-shirt': 45.50, 'Pants': 35, 'Sneakers': 41.30, 'Hat': 55, 'Backpack': 24}
result = top_three_items(shop_items)
print(result)
