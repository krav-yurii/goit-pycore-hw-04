import os

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        cats_info = []
        
        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cat_dict = {
                "id": cat_id,
                "name": name,
                "age": age
            }
            cats_info.append(cat_dict)
        
        return cats_info
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

cats_info = get_cats_info("cats_file.txt")
print(cats_info)