import src.openai_toolbox.webhook_handler as webhook_handler
import pytest
import json
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001  text-davinci-002"))
    def test_model_finder_1(self, webhook_handler):
        result = webhook_handler.model_finder(json.loads(get_webhook("text-curie-001"))["incident"]["incident_updates"][-1]["body"])
        assert result == [True, True, False, True]
    def test_model_finder_2(self, webhook_handler):
        result = webhook_handler.model_finder(json.loads(get_webhook("text-curie-001  text-davinci-002"))["incident"]["incident_updates"][-1]["body"])
        assert result == [True, True, False, False]
    def test_model_finder_3(self, webhook_handler):
        result = webhook_handler.model_finder(json.loads(get_webhook("text-curie-001  text-davinci-002 text-babbage-001"))["incident"]["incident_updates"][-1]["body"])
        assert result == [True, False, False, False]
    def test_model_finder_4(self, webhook_handler):
        result = webhook_handler.model_finder(json.loads(get_webhook("text-curie-001  text-davinci-002 text-babbage-001 text-ada-001"))["incident"]["incident_updates"][-1]["body"])
        assert result == [False, False, False, False]
    def test_model_finder_5(self, webhook_handler):
        result = webhook_handler.model_finder(json.loads(get_webhook(""))["incident"]["incident_updates"][-1]["body"])
        assert result == [True, True, True, True]