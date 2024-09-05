import json

class Converter:
    @classmethod
    def json_to_dict(cls, json_string):

        try:
            return json.loads(json_string)
        except (ValueError, TypeError):
            return {}
        
json_data = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = Converter.json_to_dict(json_data)
print(python_dict)


