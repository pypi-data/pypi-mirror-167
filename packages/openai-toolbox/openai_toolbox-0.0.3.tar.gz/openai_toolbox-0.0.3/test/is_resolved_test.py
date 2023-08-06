import src.openai_toolbox.webhook_handler as webhook_handler
import pytest
import json
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler_nr(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("", is_resolved=False))
    @pytest.fixture()
    def webhook_handler_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("", is_resolved=True))
    def test_is_resolved_1(self, webhook_handler_nr):
        result = webhook_handler_nr.is_resolved()
        assert result == False
    def test_is_resolved_2(self, webhook_handler_r):
        result = webhook_handler_r.is_resolved()
        assert result == True