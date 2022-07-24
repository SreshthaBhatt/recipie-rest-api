""""
Test custom Django management command

"""

from django.test import SimpleTestCase
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2error
from django.db.utils import OperationalError
from django.core.management import call_command

@patch('core.management.commands.waiting_for_db.Command.check')
class TestCommand(SimpleTestCase):
    def test_wait_for_db_ready(self,patched_data):
        patched_data.return_value = True

        call_command('waiting_for_db')

        patched_data.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self,patched_sleep,patched_data):

        patched_data.side_effect= [Psycopg2error] * 2 + \
            [OperationalError] * 3 + [True]
        
        call_command('waiting_for_db')

        self.assertEqual(patched_data.call_count, 6)

        patched_data.assert_called_with(databases=['default'])

