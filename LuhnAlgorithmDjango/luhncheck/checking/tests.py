from django.test import TestCase
from selenium import webdriver

# class AcceptanceTest(TestCase):
    
#     browser = None

#     def setUp(self) -> None:
#         return super().setUp()
#         self.browser = webdriver.FireFox()

#     def test_p(self):
#         pass   

#     def tearDown(self) -> None:
#         return super().tearDown()
#         self.browser.quit()


class UnitTest(TestCase):
    browser = None

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_checkpage_template(self):
        response = self.client.get('/checking/')
        self.assertTemplateUsed(response, 'checking.html')

    def test_if_in_checkpage_is_textfield(self):
        response = self.client.get('/checking/')
        self.assertTemplateUsed(response, 'checking.html')

    def tearDown(self):
        self.browser.quit()

