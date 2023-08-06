import src.openai_toolbox.webhook_handler as webhook_handler
import pytest
import json
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001"))
    def test_get_status_resports_1(self, webhook_handler):
        result = webhook_handler.get_status_reports("investigating")
        assert result == [json.loads(get_webhook("text-curie-001"))["incident"]["incident_updates"][-1]]