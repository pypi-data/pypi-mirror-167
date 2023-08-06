import src.webhook_handler as webhook_handler
import pytest
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:

    @pytest.fixture()
    def webhook_handler_c(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001"))
    @pytest.fixture()
    def webhook_handler_cd(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001 text-davinci-002"))
    @pytest.fixture()
    def webhook_handler_d(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-davinci-002"))
    @pytest.fixture()
    def webhook_handler_(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook(""))
    @pytest.fixture()
    def webhook_handler_acd(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-curie-001 text-davinci-002"))
    @pytest.fixture()
    def webhook_handler_bcd(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-babbage-001 text-curie-001 text-davinci-002"))
    @pytest.fixture()
    def webhook_handler_abc(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-babbage-001 text-curie-001"))
    @pytest.fixture()
    def webhook_handler_abd(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-babbage-001 text-davinci-002"))
    def test_handle_incident_1(self, webhook_handler_c):
        result = webhook_handler_c.handle_incident()
        assert result == "text-davinci-002"
    def test_handle_incident_2(self, webhook_handler_cd):
        result = webhook_handler_cd.handle_incident()
        assert result == "text-babbage-001"
    def test_handle_incident_3(self, webhook_handler_d):
        result = webhook_handler_d.handle_incident()
        assert result == "text-curie-001"
    def test_handle_incident_4(self, webhook_handler_):
        result = webhook_handler_.handle_incident()
        assert result == "text-curie-001"
    def test_handle_incident_5(self, webhook_handler_acd):
        result = webhook_handler_acd.handle_incident()
        assert result == "text-babbage-001"
    def test_handle_incident_6(self, webhook_handler_bcd):
        result = webhook_handler_bcd.handle_incident()
        assert result == "text-ada-001"
    def test_handle_incident_7(self, webhook_handler_abc):
        result = webhook_handler_abc.handle_incident()
        assert result == "text-davinci-002"
    def test_handle_incident_8(self, webhook_handler_abd):
        result = webhook_handler_abd.handle_incident()
        assert result == "text-curie-001"