import os
import pytest
from unittest.mock import MagicMock, AsyncMock
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
from bot import start_command, help_command

def test_dotenv_variable_existence():
    load_dotenv()
    test_variable = 'BOT_TOKEN'
    token = os.getenv(test_variable)
    assert token is not None, f'Testing variable: "{test_variable}" does not exist'
    assert token != '', f'Testing variable: "{test_variable}" is set but empty'
    print(f'The environment variable "{test_variable}" exists and has some value')


@pytest.mark.asyncio
async def test_start_command():
    mock_update = MagicMock(spec=Update)
    mock_message = MagicMock()
    mock_update.message = mock_message
    mock_message.reply_text = AsyncMock()
    await start_command(mock_update, ContextTypes.DEFAULT_TYPE)
    mock_message.reply_text.assert_awaited()

    args, _ = mock_message.reply_text.call_args
    response_text = args[0] if args else None
    print(f'Test start_command: reply_text called with: "{response_text}"')

@pytest.mark.asyncio
async def test_help_command():
    mock_update = MagicMock(spec=Update)
    mock_message = MagicMock()
    mock_update.message = mock_message
    mock_message.reply_text = AsyncMock()
    await help_command(mock_update, ContextTypes.DEFAULT_TYPE)
    mock_message.reply_text.assert_awaited()

    args, _ = mock_message.reply_text.call_args
    response_text = args[0] if args else None
    print(f'Test help_command: reply_text called with: "{response_text}"')

    expected_words = ['Help', 'Support']
    assert any(word in response_text for word in expected_words), \
        f'Expected one of {expected_words} in the response text, but got: "{response_text}"'


