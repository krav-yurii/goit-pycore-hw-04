import os

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
           
        total_salary = 0
        count = len(lines)
    
    
        for line in lines:
            full_name, salary = line.strip().split(',')
            total_salary += float(salary)
        
        average_salary = total_salary / count if count > 0 else 0
        
        total_salary = round(total_salary, 1)
        average_salary = round(average_salary, 1)
        
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")