import os
import shutil
import datetime

class SCRYPT:
    def __init__(self, path):
        self.path = path
        self.backup_path = os.path.join(path, 'backup')
        self.logfile = os.path.join(path, 'log.txt')

    def log_action(self, action_name):
        mode = 'a' if os.path.exists(self.logfile) else 'w'
        with open(self.logfile, mode) as f:
            f.write(f'{datetime.datetime.now()} - {action_name}\n')

    def search_copy_files(self):
        if os.path.isdir(self.path):
            os.makedirs(self.backup_path, exist_ok=True)
            for file in os.listdir(self.path):
                full_path = os.path.join(self.path, file)
                if os.path.isfile(full_path) and file.endswith('.txt') and file != 'log.txt':
                    new_name = file[:-4] + '_backup.txt'
                    shutil.copy(full_path, os.path.join(self.backup_path, new_name))
            self.log_action("search_copy_files")
            return True
        else:
            return False

    def del_old_files(self):
        if os.path.isdir(self.path):
            for file in os.listdir(self.path):
                full_path = os.path.join(self.path, file)
                if os.path.isfile(full_path) and file.endswith('.txt') and file != 'log.txt':
                    os.remove(full_path)
            self.log_action("del_old_files")
            return True
        else:
            return False

    def run(self):
        self.search_copy_files()
        self.del_old_files()
