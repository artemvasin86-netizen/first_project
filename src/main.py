print('Hello from repository!!!')
import os
from dotenv import load_dotenv

load_dotenv()

def print_author():
    author = os.getenv("AUTHOR")
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Автор проекта не установлен в .env")

# Проверка работы функции
if __name__ == "__main__":
    print_author()
