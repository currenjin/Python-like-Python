import csv
import collections

# name = input('안녕하세요! 저는 식당추천 봇이에요. 이름이 무엇인가요?\n')
def init():
    with open('restaurant.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames)
        wirter.writeheader()

def in_csv(restaurant):
    with open('restaurant.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writerow({'Name': restaurant, 'Count': 1})

def out_csv():
    with open('restaurant.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Name'])

in_csv('Apple Restaurant')
out_csv()





# restaurant = input('안녕하세요 {}씨, 좋아하는 레스토랑의 이름은 무엇인가요?\n'.format(name))

# 레스토랑 입력 전에 있는지 확인을 해야한다.
# 만약 있다면(if) 값을 입력하지 않고 일단 물어본다. NO라고하면 값을 입력
# 없다면 바로 값을 입력
