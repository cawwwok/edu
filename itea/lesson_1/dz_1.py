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

#add list deal 2
list_deal_2 = {
    '14.02.2022': [
        {
            "name": "купить молоко",
            "desc": "простоквашино 2,5%"
        },
        {
            "name": "купить пиво",
            "desc": "оболонь"
        },
        {
            "name": "хлеб",
            "desc": "белый хлеб"
        }
    ],
    '16.02.2022': [

        {
            "name": "tomato",
            "desc": "cherry"
        },
        {
            "name": "chips",
            "desc": "cheese"
        }
    ],
    '22.02.2022': [
        {
            "name": "pineapple",
            "desc": "yellow"
        }
    ]
}
#print
print(list_deal_2)
add_deal_3 = {
    dt: {
        "name": "banana",
        "desc": "small"
    }
}
#update list deal
list_deal_2.update(add_deal_3)

#test append
add_deal_4 = {
        "name": "potato",
        "desc": "big"
    }
new_dt = '14.02.2022'
list_deal_2[new_dt].append(add_deal_4)

#print_deal now
print(list_deal_2[dt])

#input add
add_deal_date = input('Какая дата?')
add_name = input ('Название ?')
add_desc = input ('Описание')
add_deal_input = {
    add_deal_date: {
        "name": add_name,
        "desc": add_desc
    }
}
#update list input
list_deal_2.update(add_deal_input)
print(list_deal_2)

#olololo

