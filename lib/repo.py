class Repo():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._language = data['language']
        self._description = data['description']
        self._stargazers = data['stargazers_count']
        self._forks = data['forks']
        self._save()
    
    def _save(self):
        self.all.append(self)

    def get_name(self):
        return self._name
    
    def get_language(self):
        return self._language

    def get_description(self):
        return self._description
        
    def get_stargazers(self):
        return self._stargazers

    def get_forks(self):
        return self._forks

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]    
