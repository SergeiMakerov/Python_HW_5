# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.

# из решения
#result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
#print(result)

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    result = {name: round(salary * (float(bonus.strip('%')) / 100), 1) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}
    return result

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]


names = ["Eva", "David", "Frank"]
salary = [7500, 8000, 9000]
bonus = ["8%", "12%", "7%"]

salary_dict = generate_salary_dict(names, salary, bonus)
print(salary_dict)