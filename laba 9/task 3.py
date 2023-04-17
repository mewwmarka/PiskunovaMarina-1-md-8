import csv

filename = 'products.csv'
summary_str = 'Нужно купить:\n'
summ = 0

with open(filename, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        summ += int(row[2]) * int(row[1])
        summary_str += f'{row[0]} - {row[1]} шт. за {row[2]} руб.\n'
    summary_str += f'Итоговая сумма: {summ} руб.'
print(summary_str)
