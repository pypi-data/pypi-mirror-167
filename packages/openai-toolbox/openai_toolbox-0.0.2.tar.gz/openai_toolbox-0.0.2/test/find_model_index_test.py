import src.webhook_handler as webhook_handler
import pytest
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001"))
    def test_find_model_index_1(self, webhook_handler):
        result = webhook_handler.find_model_index("curie")
        assert result == 2
    def test_find_model_index_2(self, webhook_handler):
        result = webhook_handler.find_model_index("davinci")
        assert result == 3
    def test_find_model_index_3(self, webhook_handler):
        result = webhook_handler.find_model_index("ada")
        assert result == 0
    def test_find_model_index_4(self, webhook_handler):
        result = webhook_handler.find_model_index("babbage")
        assert result == 1
