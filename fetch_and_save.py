from db import init_db, save_countries
from gql_client import get_countries_by_continent

def main():
    init_db()

    continent_code = input("Введите код континента (например: EU, AS, AF, NA, SA, OC): ").strip().upper()
    continent_data = get_countries_by_continent(continent_code)

    if continent_data is None:
        print("Континент не найден.")
        return

    print(f"Загружено стран: {len(continent_data['countries'])} для континента {continent_data['name']}")

    save_countries(continent_data['countries'], continent_data['name'])
    print("✅ Данные сохранены в БД.")

if __name__ == "__main__":
    main()
