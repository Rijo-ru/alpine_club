import os
import django
from faker import Faker  # Библиотека для генерации тестовых данных
import random
from datetime import datetime, timedelta

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpineclub.settings')
django.setup()

from climbs.models import Mountain, Climber, Climb

# Инициализация Faker
fake = Faker()

def create_mountains(num=15):
    """Создание гор."""
    for _ in range(num):
        Mountain.objects.create(
            name=fake.unique.city(),
            height=random.randint(1000, 9000),
            country=fake.country(),
            region=fake.state()
        )
    print(f"Создано {num} гор.")

def create_climbers(num=20):
    """Создание альпинистов."""
    for _ in range(num):
        Climber.objects.create(
            name=fake.unique.name(),
            address=fake.address()
        )
    print(f"Создано {num} альпинистов.")

def create_climbs(num=20):
    """Создание восхождений."""
    mountains = list(Mountain.objects.all())
    climbers = list(Climber.objects.all())

    for _ in range(num):
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = start_date + timedelta(days=random.randint(1, 14))
        climb = Climb.objects.create(
            start_date=start_date,
            end_date=end_date,
            mountain=random.choice(mountains)
        )
        # Добавление случайных альпинистов к восхождению
        num_climbers = random.randint(1, 5)
        climb.climbers.set(random.sample(climbers, num_climbers))
    print(f"Создано {num} восхождений.")

def load_data():
    """Основная функция для загрузки данных."""
    create_mountains()
    create_climbers()
    create_climbs()
    print("Тестовые данные успешно добавлены!")

if __name__ == "__main__":
    load_data()
