import pytest
import allure
from conftest import driver
from data import Answers
from pages.main_page import MainPage



class TestQuestions:
    @allure.title("Проверка ответов на важные вопросы")
    @pytest.mark.parametrize("question_num, expected_answer",
                             [(0, Answers.answer_1),
                              (1, Answers.answer_2),
                              (2, Answers.answer_3),
                              (3, Answers.answer_4),
                              (4, Answers.answer_5),
                              (5, Answers.answer_6),
                              (6, Answers.answer_7)
                              ]
                             )
    def test_questions(self, question_num, expected_answer, driver):
        main_page = MainPage(self, driver)
        result = main_page.click_on_question_and_get_answer(question_num)
        assert main_page.check_answer(result, expected_answer)
