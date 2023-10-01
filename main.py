from collections import UserDict

class Field:
    """
    Базовий клас для представлення полів запису.
    """

    def __init__(self, value):
        """
        Ініціалізує об'єкт поля.
        :param value: Значення поля.
        """
        self.value = value

    def __str__(self):
        """
        Повертає рядкове представлення значення поля.
        :return: Рядкове представлення значення поля.
        """
        return str(self.value)

class Name(Field):
    """
    Клас для представлення імені контакту.
    """
    pass

class Phone(Field):
    """
    Клас для представлення номера телефону з валідацією.
    :param value: Значення номера телефону (рядок, що містить 10 цифр).
    """

    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)

class Record:
    """
    Клас для представлення інформації про контакт.
    :param name: Ім'я контакту.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Додає номер телефону до списку телефонів.
        :param phone: Номер телефону для додавання.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """
        Видаляє номер телефону зі списку телефонів.
        :param phone: Номер телефону для видалення.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Редагує номер телефону в записі.
        :param old_phone: Старий номер телефону для редагування.
        :param new_phone: Новий номер телефону.
        """
        if old_phone in [phone.value for phone in self.phones]:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        """
        Знаходить телефон у списку телефонів.
        :param phone: Номер телефону для пошуку.
        :return: Об'єкт Phone, якщо номер знайдено, в іншому випадку None.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """
        Повертає рядкове представлення контакту.
        :return: Рядкове представлення контакту.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Клас для представлення та управління адресною книгою.
    Успадковується від UserDict.
    """

    def add_record(self, record):
        """
        Додає запис до адресної книги.
        :param record: Запис для додавання.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Знаходить запис за ім'ям.
        :param name: Ім'я для пошуку.
        :return: Об'єкт Record, якщо знайдено, в іншому випадку None.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Видаляє запис за ім'ям.
        :param name: Ім'я для видалення.
        """
        if name in self.data:
            del self.data[name]

# Приклад використання
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
