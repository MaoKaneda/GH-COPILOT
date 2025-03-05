import unittest
from unittest.mock import patch, mock_open, MagicMock
import shutil
import logging
import db_backup

class TestDBBackup(unittest.TestCase):

  @patch('db_backup.shutil.copy')
  @patch('db_backup.logging.info')
  @patch('db_backup.logging.error')
  def test_backup_db_success(self, mock_error, mock_info, mock_copy):
    db_backup.backup_db()
    mock_copy.assert_called_once_with('app.db', 'backup.db')
    mock_info.assert_called_once_with('Backup created: backup.db')
    mock_error.assert_not_called()

  @patch('db_backup.shutil.copy', side_effect=FileNotFoundError)
  @patch('db_backup.logging.error')
  def test_backup_db_file_not_found(self, mock_error, mock_copy):
    db_backup.backup_db()
    mock_copy.assert_called_once_with('app.db', 'backup.db')
    mock_error.assert_called_once_with('Error: app.db not found.')

  @patch('db_backup.shutil.copy', side_effect=PermissionError)
  @patch('db_backup.logging.error')
  def test_backup_db_permission_error(self, mock_error, mock_copy):
    db_backup.backup_db()
    mock_copy.assert_called_once_with('app.db', 'backup.db')
    mock_error.assert_called_once_with('Error: Permission denied while accessing app.db or backup.db')

  @patch('db_backup.shutil.copy', side_effect=Exception('Unexpected error'))
  @patch('db_backup.logging.error')
  def test_backup_db_unexpected_error(self, mock_error, mock_copy):
    db_backup.backup_db()
    mock_copy.assert_called_once_with('app.db', 'backup.db')
    mock_error.assert_called_once_with('An unexpected error occurred: Unexpected error')

  @patch('db_backup.shutil.copy')
  @patch('db_backup.logging.info')
  @patch('db_backup.logging.error')
  def test_restore_db_success(self, mock_error, mock_info, mock_copy):
    db_backup.restore_db()
    mock_copy.assert_called_once_with('backup.db', 'app.db')
    mock_info.assert_called_once_with('Database restored: app.db')
    mock_error.assert_not_called()

  @patch('db_backup.shutil.copy', side_effect=FileNotFoundError)
  @patch('db_backup.logging.error')
  def test_restore_db_file_not_found(self, mock_error, mock_copy):
    db_backup.restore_db()
    mock_copy.assert_called_once_with('backup.db', 'app.db')
    mock_error.assert_called_once_with('Error: backup.db not found.')

  @patch('db_backup.shutil.copy', side_effect=PermissionError)
  @patch('db_backup.logging.error')
  def test_restore_db_permission_error(self, mock_error, mock_copy):
    db_backup.restore_db()
    mock_copy.assert_called_once_with('backup.db', 'app.db')
    mock_error.assert_called_once_with('Error: Permission denied while accessing backup.db or app.db')

  @patch('db_backup.shutil.copy', side_effect=Exception('Unexpected error'))
  @patch('db_backup.logging.error')
  def test_restore_db_unexpected_error(self, mock_error, mock_copy):
    db_backup.restore_db()
    mock_copy.assert_called_once_with('backup.db', 'app.db')
    mock_error.assert_called_once_with('An unexpected error occurred: Unexpected error')

if __name__ == '__main__':
  unittest.main()