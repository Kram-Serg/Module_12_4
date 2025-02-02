import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False


    def test_walk(self):
        try:
            func_runner = Runner('Walk', speed=-5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                func_runner.walk()
            self.assertEqual(func_runner.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            func_runner = Runner(54)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                func_runner.run()
            self.assertEqual(func_runner.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_chellenger(self):
        func_runner = Runner('Walk_1')
        func_runner_1 = Runner('Run_1')
        for i in range(10):
            func_runner.walk()
            func_runner_1.run()
        self.assertNotEqual(func_runner.distance, func_runner_1.distance)


if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')
# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())