"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров
"""
import logging

logging.basicConfig(filename='logi.log',
                    encoding='UTF-8',
                    level=logging.NOTSET)

logger = logging.getLogger(__name__)



def fibonachi(z: int):
    try:
        f1 = f2 = 1
        logger.info(f'{f2 = }')
        for i in range (2, z):
            f1, f2 = f2, f1 + f2
            logger.info(f'  <- + {f1} = {f2}')
        yield f2
    except (TypeError):
        logger.error(f'{z} не корректное значение')
    


if __name__ == '__main__':
    print(*fibonachi(7))