import csv

name = input('안녕하세요! 저는 식당추천 봇이에요. 이름이 무엇인가요?\n')

'''
def in_csv(restaurant):
    with open('restaurant.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': restaurant, 'Count': 1})

def out_csv():
    with open('restaurant.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Name'])

in_csv('Apple Restaurant')
out_csv()
'''

with open('restaurant.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        answer = input('이 레스토랑은 어떤가요? {}, [YES/NO]\n'.format(row['Name']))
        if answer == 'NO':
            break

restaurant = input('{}님, 좋아하는 레스토랑의 이름은 무엇인가요?\n'.format(name))
