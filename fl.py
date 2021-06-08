import logging

logging.basicConfig(level=logging.INFO)


def summa(number1, number2):
    logging.info(number1 + number2)


def sub(number1, number2):
    logging.info(number1 - number2)


def mul(number1, number2):
    logging.info(number1 * number2)


def deg(number1, number2):
    logging.info(number1 ** number2)


def main():
    logging.info("введите 2 числа")
    try:
        array = list(map(int, input().split()))
        logging.info("выберите одну из  операций:+,-,*,^")
        oper = input()
        if oper == "+":
            summa(array[0], array[1])
        elif oper == "-":
            sub(array[0], array[1])
        elif oper == "*":
            mul(array[0], array[1])
        elif oper == "^":
            deg(array[0], array[1])
    except ValueError:
        logging.info("ошибка ввода, попробуйте в следующий раз")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("вы прервали операцию")


