#импорт всех модулей
import string
import random

#в этой строке содержатся символы, из которых состоят пароли
characters = string.ascii_letters + string.digits + string.punctuation

#функция-генератор паролей
def generate_password(length: int) -> str:
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

password_length = int(input("Введите желаемую длину пароля: "))
print(f"Ваш сгенерированный пароль: {generate_password(password_length)}")
