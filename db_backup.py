import shutil
import logging
from util import authenticate_user, hash_password

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

activate_db_file = 'app.db'
backup_db_file = 'backup.db'

user_db = {
    'admin': hash_password('admin123')
}

def backup_db():
    try:
        shutil.copy(activate_db_file, backup_db_file)
        logging.info(f'Backup created: {backup_db_file}')
    except FileNotFoundError:
        logging.error(f'Error: {activate_db_file} not found.')
    except PermissionError:
        logging.error(f'Error: Permission denied while accessing {activate_db_file} or {backup_db_file}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

def restore_db():
    try:
        shutil.copy(backup_db_file, activate_db_file)
        logging.info(f'Database restored: {activate_db_file}')
    except FileNotFoundError:
        logging.error(f'Error: {backup_db_file} not found.')
    except PermissionError:
        logging.error(f'Error: Permission denied while accessing {backup_db_file} or {activate_db_file}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

def main():
    username = input('Username: ')
    password = input('Password: ')
    if not authenticate_user(username, password, user_db):
        print('Authentication failed')
        return

    print('1. Backup database')
    print('2. Restore database')
    print('3. Exit')
    choice = input('Enter your choice: ') 
    if choice == '1':
        backup_db()
    elif choice == '2':
        restore_db()
    elif choice == '3':
        print('Exiting...')
    else:
        print('Invalid choice') 

      if __name__ == '__main__':
          main()

