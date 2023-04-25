import csv

with open('en-ru.txt', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='-')
    result = sorted(
        [row[::-1] for row in reader],
        key=lambda word: word[0]
    )

with open('ru-en.txt', 'w', encoding='utf-8') as file_output:
    writer = csv.writer(file_output, delimiter='-')
    [writer.writerow(data) for data in result]
