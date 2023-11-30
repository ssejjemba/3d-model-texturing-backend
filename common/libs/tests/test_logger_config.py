# tests/test_logger_config.py
import pytest
from libs.logging.logger_config import setup_logger, setup_external_logging
from loguru import logger as loguru_logger
import sys

def test_setup_logger_default(mocker):
    mock_add = mocker.patch.object(loguru_logger, "add")
    setup_logger()
    # Verify default logger setup
    mock_add.assert_called()
    assert any(call for call in mock_add.call_args_list if call[1]['level'] == "INFO")

def test_setup_logger_custom_level(mocker):
    mock_add = mocker.patch.object(loguru_logger, "add")
    setup_logger(log_level="DEBUG")
    # Verify custom log level setup
    assert any(call for call in mock_add.call_args_list if call[1]['level'] == "DEBUG")

def test_setup_logger_file_logging(mocker, tmp_path):
    mock_add = mocker.patch.object(loguru_logger, "add")
    log_file = tmp_path / "test.log"
    setup_logger(log_to_file=True, file_path=str(log_file))
    # Verify file logging setup
    assert any(call for call in mock_add.call_args_list if str(log_file) in call[0])

def test_setup_external_logging_sentry(mocker):
    mock_init = mocker.patch('sentry_sdk.init')
    config = {"sentry_dsn": "fake_dsn", "sentry_level": "WARNING"}
    setup_external_logging(loguru_logger, config)
    # Assertions to verify Sentry initialization
    mock_init.assert_called_once()

# More tests can be added as needed
