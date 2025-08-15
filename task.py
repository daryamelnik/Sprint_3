import datetime

class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

#1
    @property
    def name_items(self):
        return self.__name_items
    @property
    def number_items(self):
        return self.__number_items

# 2
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

# 3
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

# 4
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        amount = sum(total)
        if self.__number_items > 10:
            return amount * 0.9
        else:
            return amount

# 5
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        amount = sum(total)
        if self.__number_items > 10:
            amount *= 0.9
        return amount * 0.2

# 6
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        amount = sum(total)
        if self.__number_items > 10:
            amount *= 0.9
        return amount * 0.1

# 7
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

# 8
    def get_telephone_number(self, telephone_number):
        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10 or len(str(telephone_number)) < 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'
    
        # ...existing code...

if __name__ == "__main__":
    kass = OnlineSalesRegisterCollector()
    kass.add_item_to_cheque('чипсы')
    kass.add_item_to_cheque('кола')
    print("Товары в чеке:", kass.name_items)
    print("Количество товаров:", kass.number_items)
    print("Сумма чека:", kass.check_amount())
    print("НДС 20%:", kass.twenty_percent_tax_calculation())
    print("НДС 10%:", kass.ten_percent_tax_calculation())
    print("Общий НДС:", kass.total_tax())
    print("Телефон:", kass.get_telephone_number("1234567890"))