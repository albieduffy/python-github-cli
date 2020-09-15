from .api import fetch_repos
from .repo import Repo
from progress.spinner import PieSpinner
import time

class Format():
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

class CLI():
    ''' User Interface '''
    def __init__(self):
        self._username = ""
        self._user_input = ""
        self._state = ""
        self._timer = 5
    
    def start(self):
        self._username = input(f'''\n{Format.GREEN}{Format.BOLD}Which GitHub user would you like to view?\n{Format.CLEAR}''')
        print('')
        fetch_repos(self._username)
        loading = f'''{Format.GREEN}{Format.BOLD}Loading{Format.CLEAR}'''
        spinner = PieSpinner(loading)
        while self._state != 'FINISHED':
            while self._timer != 0:
                time.sleep(0.4)
                self._timer -= 1
                spinner.next()
            self._state = "FINISHED"
        self.menu(0, 10)
    
    def menu(self, input=0, end=10):
        print(f'\n{Format.GREEN}{Format.BOLD}\nGitHub Repositories:{Format.CLEAR}')
        for idx, repo in enumerate(Repo.all[input:end], start=input+1):
            print(f'{idx}. {repo.get_name()}')
        if end == 10:
                print('Type more to view additional repositories')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'''\n{Format.GREEN}{Format.BOLD}Which Repo would you like see more info for?\n{Format.CLEAR}''')
            if self._user_input == 'more': return self.menu(0, -1)
            if self._user_input == 'exit': return self.goodbye()
            if not self.valid_input(self._user_input) : raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def show_repo(self):
        repo = Repo.find_by_input(self._user_input)
        print(f'\n{Format.GREEN}{Format.BOLD}{repo.get_name()}{Format.CLEAR}')
        print(f'\tDescription: {repo.get_description()}')
        print(f'\tLanguage: {repo.get_language()}')
        print(f'\t⭐️ Count: {repo.get_stargazers()}')
        print(f'\t⑂ Count: {repo.get_forks()}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repo.all)

    @staticmethod
    def goodbye():
        print(f'\n{Format.GREEN}{Format.BOLD}See you soon!{Format.CLEAR}\n')

app = CLI()