import pytest
import allure
import test_runner
from custom_steps import stp

@allure.epic("Модуль МЭР")
@allure.tag("negativ","manual","")
@allure.feature("История расчётов")
@allure.story("История пользовательских расчётов")
@allure.link("http://example-link", name="Пересчет замерных параметров по характерам скважин за период")

class Test_open_history_test_pos:
    @allure.title("Открытие истории истории")
    @stp("Отркыть страницу модуля МЭР")
    @stp("Открыть историю расчетов")
    @stp("Настроить период отображения и другие фильтры")
    @stp("Выбрать расчет посредством даблклика")
    @stp("Проверка: Откроется новый расчет")
    def test_open_history_test(self):
        assert test_runner.user_input(), "При открытии сайдбара пользователь видит свой расчёт с шаблонным названием [Расчёт-дата.нач-дата.кон]"
