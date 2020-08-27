import csv

name = input('안녕하세요! 저는 식당추천 봇이에요. 이름이 무엇인가요?\n')

with open('restaurant.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row:
            answer = input('이 레스토랑은 어떤가요? ({}), [YES/NO]\n'.format(row['Name']))
        else:
            break
        if answer == 'YES':
            break

restaurant = input('{}님, 좋아하는 레스토랑의 이름은 무엇인가요?\n'.format(name))

with open('restaurant.csv', 'a+') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    reader = csv.DictReader(csv_file)
    csv_file.seek(0)
    for row in reader:
        if restaurant in row['Name']:
            csv_file.write(row)
            break
        else:
            writer.writerow({'Name': restaurant, 'Count': 1})
            break
    else:
        writer.writeheader()
        writer.writerow({'Name': restaurant, 'Count': 1})

print('감사합니다. {}님, 좋은 하루 보내세요!'.format(name))
