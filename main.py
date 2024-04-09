# Print specific key-value pairs of a dictionary in Python

my_dict = {
    'name': 'Borislav Hadzhiev',
    'fruit': 'apple',
    'number': 5,
    'website': 'bobbyhadz.com',
    'topic': 'Python'
}

# ✅ Print key-value pairs of dict that meet a condition
for key, value in my_dict.items():
    if str(value).startswith('bo'):
        print(key, value)  # 👉️ website bobbyhadz.com