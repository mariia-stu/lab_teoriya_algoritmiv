import re

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        #Проста хеш-функція
        return hash(key) % self.size

    def insert(self, key, value):
        #Додає елемент до таблиці або оновлює існуючий
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                print(f"Оновлено запис із ключем {key}")
                return

        bucket.append([key, value])
        print(f"Додано запис із ключем {key} у бакет {index}")

    def search(self, key):
        #Пошук за ключем
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        #Видалення за ключем
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                print(f"Видалено запис із ключем {key}")
                return
        print("Елемент не знайдено.")

    def display(self):
        #Вивід усієї таблиці з декоративними роздільниками.
        print("\n===== Вміст хеш-таблиці =====")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"{i}: {bucket}")
            else:
                print(f"{i}: порожньо")
        print("==============================")


#Допоміжні функції валідації формату [E###]

ID_PATTERN = re.compile(r"^E\d{3}$")  #E + рівно 3 цифри

def normalize_emp_id(raw_id: str) -> str:
    #Очищаємо та приводимо до верхнього регістру
    return raw_id.strip().upper()

def is_valid_emp_id(emp_id: str) -> bool:
    #Перевірка чи відповідає формат [E###]
    return bool(ID_PATTERN.match(emp_id))

def get_valid_emp_id(prompt: str) -> str:
    #Код просить користувача ввести ID доти, доки не буде валідним
    while True:
        raw = input(prompt)
        emp_id = normalize_emp_id(raw)
        if is_valid_emp_id(emp_id):
            return emp_id
        print("Невірний формат ID. Потрібно ввести у форматі E### (наприклад: E001). Спробуйте ще раз.")


#Меню

def main():
    table = HashTable()

    while True:
        print("\nМеню:")
        print("1. Додати співробітника")
        print("2. Знайти співробітника")
        print("3. Видалити співробітника")
        print("4. Переглянути всю таблицю")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            emp_id = get_valid_emp_id("Введіть ID (формат E###, напр. E001): ")
            name = input("Введіть ім'я: ").strip()
            position = input("Введіть посаду: ").strip()
            salary = input("Введіть зарплату: ").strip()
            table.insert(emp_id, {"name": name, "position": position, "salary": salary})

        elif choice == "2":
            emp_id = get_valid_emp_id("Введіть ID для пошуку (формат E###): ")
            result = table.search(emp_id)
            if result:
                print(f"Знайдено: {result}")
            else:
                print("Співробітника не знайдено.")

        elif choice == "3":
            emp_id = get_valid_emp_id("Введіть ID для видалення (формат E###): ")
            table.delete(emp_id)

        elif choice == "4":
            table.display()

        elif choice == "0":
            break

        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()
