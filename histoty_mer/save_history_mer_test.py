import pytest
import allure
import test_runner
from custom_steps import stp

@allure.epic("Модуль МЭР")
@allure.feature("История расчётов")
@allure.story("История пользовательских расчётов")
@allure.link("http://example-link", name="Пересчет замерных параметров по характерам скважин за период")

class Test_save_history_test:
    @allure.title("Сохранение истории")
    @stp("Отркыть страницу модуля МЭР")
    @stp("Выбирать характер скважины")
    @stp("Нажимать на кнопку \"Пересчёт\" замерной")
    @stp("Открывыть сайдбар истории расётов")
    @stp("Проверка: При открытии сайдбара появляется список расчетов. Активный расчёт тот, на котором сейчас находимся")
    def test_save_history(self):
        assert test_runner.user_input(), "При открытии сайдбара пользователь видит свой расчёт с шаблонным названием [Расчёт-дата.нач-дата.кон]"
