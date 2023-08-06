from src.webhook_handler import Webhook_Handler
import pytest
from test.webhook_consts import get_webhook

class Test_Webhook_handler_Find_model_index:
    @pytest.fixture()
    def webhook_handler_curie(self):
        return Webhook_Handler(webhook=get_webhook("text-curie-001"))
    @pytest.fixture()
    def webhook_handler_davinci(self):
        return Webhook_Handler(webhook=get_webhook("text-curie-001"), first_choice_model='davinci')
    def test_choose_backup_1(self, webhook_handler_curie):
        result = webhook_handler_curie.choose_backup_model([True, True, False, True])
        assert result == 3
    def test_choose_backup_2(self, webhook_handler_curie):
        result = webhook_handler_curie.choose_backup_model([True, True, False, False])
        assert result == 1
    def test_choose_backup_3(self, webhook_handler_curie):
        result = webhook_handler_curie.choose_backup_model([True, False, False, False])
        assert result == 0
    def test_choose_backup_4(self, webhook_handler_curie):
        result = webhook_handler_curie.choose_backup_model([True, False, True, True])
        assert result == 2
    def test_choose_backup_5(self, webhook_handler_curie):
        result = webhook_handler_curie.choose_backup_model([True, False, False, True])
        assert result == 3

    def test_choose_backup_1_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, True, False, True])
        assert result == 3
    def test_choose_backup_2_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, True, False, False])
        assert result == 1
    def test_choose_backup_3_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, False, False, False])
        assert result == 0
    def test_choose_backup_4_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, True, True, True])
        assert result == 3
    def test_choose_backup_5_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, False, False, True])
        assert result == 3
    def test_choose_backup_6_d(self, webhook_handler_davinci):
        result = webhook_handler_davinci.choose_backup_model([True, False, True, True])
        assert result == 3