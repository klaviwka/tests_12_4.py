import logging
import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('runner_tests.log', mode='w', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для контроля выполнения тестов

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты временно отключены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run_invalid_name(self):
        try:
            runner = Runner(123, 10)  # Передаем неверный тип для name
            logger.info('"test_run_invalid_name" выполнен успешно')
        except TypeError:
            logger.warning("Неверный тип данных для объекта Runner")

    @skip_if_frozen
    def test_walk_negative_speed(self):
        try:
            runner = Runner("Runner1", -5)  # Передаем отрицательное значение для speed
            logger.info('"test_walk_negative_speed" выполнен успешно')
        except ValueError:
            logger.warning("Неверная скорость для Runner")

    @skip_if_frozen
    def test_invalid_name_string(self):
        try:
            runner = Runner("Runner1", 10)
            runner.name = ""  # Проверяем пустую строку
            if not runner.name:
                raise ValueError("Имя не может быть пустым")
            logger.info('"test_invalid_name_string" выполнен успешно')
        except ValueError as e:
            logger.warning(f"Ошибка: {e}")

    @skip_if_frozen
    def test_tournament(self):
        runner1 = Runner("Runner1", 10)
        runner2 = Runner("Runner2", 5)
        tournament = Tournament(30, runner1, runner2)
        finishers = tournament.start()
        logger.info(f'Финишеры: {finishers}')
        self.assertIn(1, finishers)  # Проверяем, что есть хотя бы один финишер

if __name__ == '__main__':
    unittest.main()
