import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="my_log.log",
    filemode="a",
    encoding="utf-8",
)


def happy_birthday(name, age, wish):
    print(f"Happy birth dear {name} !!!")
    print(f"You are {age} old!!")
    print(f"{wish}")


my_name = str(input("Enter your name: "))
my_age = int(input("Enter your age: "))
my_wish = str(input("Enter your wish: "))

try:
    if my_age < 0:
        raise BaseException("Sorry, no numbers below zero")
    elif my_age > 100:
        raise BaseException("Sorry, no numbers above 100")
    elif my_age < 10:
        raise BaseException("Incorrect value")
    else:
        happy_birthday(my_name, my_age, my_wish)
except BaseException as e:
    print(e)
    logging.error(e)


with open("my_log.log", "a", encoding="utf-8") as filename:
    filename.write("Code finished!!!\n")