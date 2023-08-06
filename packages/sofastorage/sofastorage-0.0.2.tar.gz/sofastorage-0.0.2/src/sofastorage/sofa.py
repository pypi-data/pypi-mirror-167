import time
import os.path
from .key import KEY
from deta import Deta
from tabulate import tabulate

class Online:
    def __init__(self, base: Deta.Base, silent: bool = False):
        self.base = base
        self.silent = silent

    def __repr__(self):
        return f"<SofaStorage>"

    def __log__(self, prompt: str) -> None:
        if not self.silent:
            print(prompt)    

    @classmethod
    def create(cls, username: str, password: str, private: str = None, silent: bool = False):
        key = private if private else KEY
        if len(username) < 5:
            raise ValueError("Use at least 5 characters!")
        if password == KEY:
            raise ValueError("Don't use project key as password!")
        if len(password) < 8:
            raise ValueError("Use at least 8 characters!")
        if username == password:
            raise ValueError("Username and password can't be the same!")
        try:
            base = Deta(key).Base(f'{username}-{password}')
            sofa = base.get(key='.sofa')
            if sofa:
                return cls.login(username, password, private, silent)
            if not silent:
                print(f'Account ({username}) created!')
            storage = base.put({'sofastorage':'.sofa'}, key='.sofa')
            return cls(base=base, silent=silent)
        except:
            raise ValueError("Used an invalid login token!")


    @classmethod
    def login(cls, username: str, password: str, private: str = None, silent: bool = False):
        key = private if private else KEY
        try:
            base = Deta(key).Base(f'{username}-{password}')
            sofa = base.get(key='.sofa')
            if sofa:
                if not silent:
                    print(f"Logged in as ({username})")
                    print('-------')
                return cls(base=base, silent=silent)
            else:
                raise Exception(f"Account ({username}) doesn't exist!")
        except AssertionError:
            raise ValueError("Used an invalid login token!")

    def all_raw(self):
        '''
        Similar to all() but it returns a Dict for every saved login instead
        :return: SofaStorage object
        '''
        timer_start = time.perf_counter()
        fetch = self.base.fetch({'sofastorage': '.website'})
        for item in fetch.items:
            self.__log__(item)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'   
        self.__log__(f'[•] Found {fetch.count} result(s) | {elapsed}s') 


    def interactive(self):
        '''
        Interactive login saving
        '''
        username = input('Username: ')
        password = input('Password: ')
        website = input('Website: ')
        address = website.replace('https://', '').replace('http://', '')
        self.__log__(f'[↑] Saving | {website} | ...')
        timer_start = time.perf_counter()
        self.base.insert(
            {'username': username, 'password': password, 'website': address, 'sofastorage': '.website'}
        )
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f'[•] Completed | {website} | {elapsed}s')

    def all(self):
        '''
        Returns all saved logins
        :return: SofaStorage object
        '''
        timer_start = time.perf_counter()
        fetch = self.base.fetch({'sofastorage': '.website'})
        data = []
        for item in fetch.items:
            store = []
            store.append(item['key'])
            store.append(item['username'])
            store.append(item['password'])
            store.append(item['website'])
            data.append(store)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(
            tabulate(data, headers=["Key", "Username", "Password", "Website"], tablefmt="pretty")
        )   
        self.__log__(f'[•] Found {fetch.count} result(s) | {elapsed}s')         

    def find(self, query: str):
        '''
        Search for logins
        :param query: This can be the website url/name or the websites username
        :return: SofaStorage object
        '''
        try:
            if query:
                try:
                    fetch = self.base.fetch({'username', query})
                except:
                    fetch = self.base.fetch({'website': query})
            timer_start = time.perf_counter()
            data = []
            for item in fetch.items:
                store = []
                store.append(item['key'])
                store.append(item['username'])
                store.append(item['password'])
                store.append(item['website'])
                data.append(store)
                table = tabulate(data, headers=["Key", "Username", "Password", "Website"], tablefmt="pretty")
            timer_end = time.perf_counter()
            elapsed = f'{timer_end - timer_start:0.4f}'      
            self.__log__(
                tabulate(data, headers=["Key", "Username", "Password", "Website"], tablefmt="pretty")
            )    
            self.__log__(f'[•] Found {fetch.count} result(s) | {elapsed}s')
        except:
            raise Exception('Missing website or username search query!')

    def add(self, username: str, password: str, website: str): 
        '''
        Add a login
        :param username: This can also be an email
        :param password: The password
        :param website: Website url 
        :return: SofaStorage object
        '''
        address = website.replace('https://', '').replace('http://', '')
        self.__log__(f'[↑] Saving | {website} | ...')
        timer_start = time.perf_counter()
        self.base.insert(
            {'username': username, 'password': password, 'website': address, 'sofastorage': '.website'}
        )
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f'[•] Completed | {website} | {elapsed}s')

    def remove(self, key: str):
        '''
        Remove logins
        :param key: Key from the saved login
        '''
        self.base.delete(key)
        self.__log__(f'[!] Deleted | {key}')

    def download(self):
        '''
        Downloads your saved logins as a txt file
        '''
        self.__log__(f'[↓] Downloading | ...')
        timer_start = time.perf_counter()
        fetch = self.base.fetch({'sofastorage': '.website'})
        data = []
        for item in fetch.items:
            store = []
            store.append(item['key'])
            store.append(item['username'])
            store.append(item['password'])
            store.append(item['website'])
            data.append(store)
        table = tabulate(data, headers=["Key", "Username", "Password", "Website"], tablefmt="pretty")
        file = os.path.exists('logins.txt')
        with open('logins.txt', 'x') as f:
            f.write(table)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f"[•] Completed | {elapsed}s")


class Local:
    def __init__(self, silent: bool = False, local: bool = False):
        self.silent = silent
        self.local = local

    def __repr__(self):
        return f"<SofaStorage>"

    def __log__(self, prompt: str) -> None:
        if not self.silent:
            print(prompt)    

    def __local__(self, table: str) -> None:
        if self.local == True:
            file = os.path.exists('logins.txt')
            if file == True:
                with open('logins.txt', 'r+') as f:
                    f.truncate()
                    f.write(table)
            elif file == False:
                with open('logins.txt', 'x') as f:
                    f.write(table)

    @classmethod
    def manager(cls, silent: bool = False, local: bool = True):
        if not silent:
            print(f"Local SofaStorage")
            print('-------')
            return cls(local=local, silent=silent)

    def setup(self):
        '''
        Creates txt file for local password manager
        '''
        timer_start = time.perf_counter()
        self.__log__(f'[↓] Setting up local | ...')
        data = ''
        table = tabulate(data, headers=["Username", "Password", "Website"], tablefmt="pretty")
        self.__local__(table)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f'[•] Setup completed | {elapsed}s')

    def interactive(self):
        '''
        Interactive login saving
        '''
        username = input('Username: ')
        password = input('Password: ')
        website = input('Website: ')
        address = website.replace('https://', '').replace('http://', '')
        self.__log__(f'[↓] Saving | {website} | ...')
        timer_start = time.perf_counter()
        data = [[username, password, address]]
        table = tabulate(data, headers=["Username", "Password", "Website"], tablefmt="pretty")
        self.__local__(table)
        timer_end = time.perf_counter()
        elapsed = f'{timer_end - timer_start:0.4f}'
        self.__log__(f'[•] Completed | {website} | {elapsed}s')