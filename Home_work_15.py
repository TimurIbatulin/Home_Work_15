"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров
"""
import logging
import argparse

logging.basicConfig(filename='logi.log',
                    encoding='UTF-8',
                    level=logging.NOTSET)

logger = logging.getLogger(__name__)



def fibonachi(z: int):
    try:
        f1 = f2 = 1
        for i in range (2, int(z)):
            f1, f2 = f2, f1 + f2
            logger.info(f' {i+1} = {f2}')
        yield f2
    except (TypeError):
        logger.error(f'{z} не корректное значение, {type(z)}')

def pars():
    parser = argparse.ArgumentParser(description='Найдем число фибоначи')
    parser.add_argument('-z', '--fibonachi_number', type = int, help = 'Ввидите целое число')
    args = parser.parse_args()
    return fibonachi(f'{args.fibonachi_number}')

if __name__ == '__main__':
    print(*pars())

    # print(*fibonachi(7))