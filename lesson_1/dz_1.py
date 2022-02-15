"""Розробити структуру для зберігання інформації для відображення списку справ із
прив’язкою до дат. Враховуйте, що до однієї дати можуть відноситись одразу декілька
справ. Спробуйте погратися із цим списком - програмно додайте нову справу або
видаліть її. Програмно спробуйте видалити усі справи за обрану дату."""

#list deal
list_deal = {
    '14.02.2022': {
    "name": "купить молоко",
    "desc": "простоквашино 2,5%"
},
    '16.02.2022': {
    "name": "купить пиво",
    "desc": "оболонь"
},
    '17.02.2022' : {
    "name": "хлеб",
    "desc": "белый хлеб"
}
}

#показать на одну дату
print(list_deal['17.02.2022']["name"])

#print
print(list_deal['14.02.2022']["name"],list_deal['16.02.2022']["name"])

#print all
print(list_deal)

#add new deal x.update()
add_deal_1 = {
    '20.02.2022': {
        "name": "колбасу",
        "desc": "салями 500 грамм, нарезкой"
    }
}
list_deal.update (add_deal_1)

#list deal 20-02-2022
print(list_deal['20.02.2022']["name"])

#add deal date now
from datetime import datetime
dt = datetime.today().strftime('%d.%m.%Y')
add_deal_2 = {
        dt: {
        "name": "колбасу 2",
        "desc": "докторскую 100гр"
        }
}

#error add dict
#list_deal[dt].append(add_deal_2)
list_deal.update (add_deal_2)
#print datetime now
print(list_deal[dt]["name"])

#del
list_deal.pop('17.02.2022')

#print all
print(list_deal)

#update test git