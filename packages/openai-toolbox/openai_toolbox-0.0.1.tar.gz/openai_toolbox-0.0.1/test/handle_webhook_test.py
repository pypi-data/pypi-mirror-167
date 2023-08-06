import src.webhook_handler as webhook_handler
import pytest
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:
    """Un resolved Fixtures"""
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
    """Resolved Fixtures"""
    @pytest.fixture()
    def webhook_handler_c_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_cd_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-curie-001 text-davinci-002", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_d_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-davinci-002", is_resolved=True))
    @pytest.fixture()
    def webhook_handler__r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_acd_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-curie-001 text-davinci-002", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_bcd_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-babbage-001 text-curie-001 text-davinci-002", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_abc_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-babbage-001 text-curie-001", is_resolved=True))
    @pytest.fixture()
    def webhook_handler_abd_r(self):
        return webhook_handler.Webhook_Handler(webhook=get_webhook("text-ada-001 text-babbage-001 text-davinci-002", is_resolved=True))
    """Un-resolved tests"""
    def test_handle_webhook_1(self, webhook_handler_c):
        result = webhook_handler_c.handle_webhook()
        assert result == "text-davinci-002"
    def test_handle_webhook_2(self, webhook_handler_cd):
        result = webhook_handler_cd.handle_webhook()
        assert result == "text-babbage-001"
    def test_handle_webhook_3(self, webhook_handler_d):
        result = webhook_handler_d.handle_webhook()
        assert result == "text-curie-001"
    def test_handle_webhook_4(self, webhook_handler_):
        result = webhook_handler_.handle_webhook()
        assert result == "text-curie-001"
    def test_handle_webhook_5(self, webhook_handler_acd):
        result = webhook_handler_acd.handle_webhook()
        assert result == "text-babbage-001"
    def test_handle_webhook_6(self, webhook_handler_bcd):
        result = webhook_handler_bcd.handle_webhook()
        assert result == "text-ada-001"
    def test_handle_webhook_7(self, webhook_handler_abc):
        result = webhook_handler_abc.handle_webhook()
        assert result == "text-davinci-002"
    def test_handle_webhook_8(self, webhook_handler_abd):
        result = webhook_handler_abd.handle_webhook()
        assert result == "text-curie-001"
    """Resolved tests"""
    def test_handle_webhook_9(self, webhook_handler_c_r):
        result = webhook_handler_c_r.handle_webhook()
        assert result == "text-davinci-002"
    def test_handle_webhook_10(self, webhook_handler_cd_r):
        result = webhook_handler_cd_r.handle_webhook()
        assert result == "text-babbage-001"
    def test_handle_webhook_11(self, webhook_handler_d_r):
        result = webhook_handler_d_r.handle_webhook()
        assert result == "text-curie-001"
    def test_handle_webhook_12(self, webhook_handler__r):
        result = webhook_handler__r.handle_webhook()
        assert result == "text-curie-001"
    def test_handle_webhook_13(self, webhook_handler_acd_r):
        result = webhook_handler_acd_r.handle_webhook()
        assert result == "text-babbage-001"
    def test_handle_webhook_14(self, webhook_handler_bcd_r):
        result = webhook_handler_bcd_r.handle_webhook()
        assert result == "text-ada-001"
    def test_handle_webhook_15(self, webhook_handler_abc_r):
        result = webhook_handler_abc_r.handle_webhook()
        assert result == "text-davinci-002"
    def test_handle_webhook_16(self, webhook_handler_abd_r):
        result = webhook_handler_abd_r.handle_webhook()
        assert result == "text-curie-001"