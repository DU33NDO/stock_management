import csv
from uuid import UUID
from datetime import datetime, timedelta


users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"

with open(
    users_filepath, encoding="UTF-8", mode="r"
) as users_file:  # для открытия файлв текстового
    users = csv.DictReader(users_file)
    # users = csv.reader(users_file)
    print("Users: ")
    for user in users:
        user_id = user["user_id"]
        try:
            user_id = UUID(user_id)
            print(user_id)
        except ValueError:
            print("невалидный тип данных")


with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    print("Stocks: ")
    for stock in stocks:
        stock_id = stock["stock_id"]
        capacity_sq_m = stock["capacity_sq_m"]
        owner_id = stock["owner_id"]
        try:
            stock_id = int(stock_id)
            print(stock_id)
        except ValueError:
            print("невалидный тип данных для stock_id")

        try:
            capacity_sq_m = float(capacity_sq_m)
            print(capacity_sq_m)
        except ValueError:
            print("невалидный тип данных для capacity")

        try:
            owner_id = str(owner_id)
            print(owner_id)
        except ValueError:
            print("невалидный тип данных для owner_id")


with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    print("Items: ")
    for item in items:
        item_id = item["item_id"]
        stock_id = item["stock_id"]
        size = item["size"]
        arrive_at = item["arrive_at"]
        expiration_time = item["expiration_time"]
        try:
            item_id = int(item_id)
            print(item_id)
        except ValueError:
            print("невалидный тип данных для item_id")
        try:
            stock_id = int(stock_id)
            print(stock_id)
        except ValueError:
            print("невалидный тип данных для stock_id")
        try:
            size = float(size)
            print(size)
        except ValueError:
            print("невалидный тип данных для size")
        try:
            arrive_at = datetime.strptime(arrive_at, "%Y-%m-%d")
            print(arrive_at)
        except ValueError:
            print("невалидный тип данных для arrive_at")
        try:
            expiration_time = timedelta(days=int(expiration_time))
            print(expiration_time)
        except ValueError:
            print("невалидный тип данных для expiration_time")
