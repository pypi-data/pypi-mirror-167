import src.openai_toolbox.webhook_handler as webhook_handler
import pytest
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001"))
    def test_indices_of_usable_1(self, webhook_handler):
        result = webhook_handler.indices_of_usable_models(models_involved_flags = [False, False, False, False])
        assert result == []
    def test_indices_of_usable_2(self, webhook_handler):
        result = webhook_handler.indices_of_usable_models(models_involved_flags = [False, False, False, True])
        assert result == [3]
    def test_indices_of_usable_3(self, webhook_handler):
        result = webhook_handler.indices_of_usable_models(models_involved_flags = [True, False, False, True])
        assert result == [0,3]
    def test_indices_of_usable_4(self, webhook_handler):
        result = webhook_handler.indices_of_usable_models(models_involved_flags = [True, False, True, True])
        assert result == [0,2,3]
    def test_indices_of_usable_5(self, webhook_handler):
        result = webhook_handler.indices_of_usable_models(models_involved_flags = [True, True, True, True])
        assert result == [0,1,2,3]