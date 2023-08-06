# SofaStorage
Easy to use password manager

## Installation

```py
pip install git+https://github.com/SlumberDemon/SofaStorage
```

## Examples

#### Online

```py
from sofastorage import Online

# Create Account

sofa = Online.create('USERNAME', 'PASSWORD')

# Add Logins 

sofa.add('USERNAME', 'PASSWORD', 'https://bob.com')

# All Saved Logins

sofa.all()

# Find Logins

sofa.find('bob.com')
```

#### Local

```py
from sofastorage import Local

# Launch into Local mode

sofa = Local.manager()

# Easy setup (not required)

sofa.setup()

# Interactive way of adding logins

sofa.interactive()
```


### WORK IN PROGESS ###

Making this public so I can test it!

Also a lot of the code was based of AirDrives code!

## Todo:
- [x] Remove https and http from website url 
- [ ] Add abilitly to find out how many website use the same password
- [ ] Maybe add a password generator as well
- [ ] Remove storage in main db make it private db online for more security
- [x] Add ability to download saved passwords in a txt file 
- [x] Maybe make it eaiser to navigate between local and online password manager also polish interactive password creation
- [ ] Add validation to check if website link is real website link
- [ ] Finish Local sofastorage

## Working Features:
- [x] Account Creation
- [x] Logining In
- [x] Private Datebase
- [x] Local Manager
#### Online
   - [x] Adding Logins
   - [x] Removing Logins
   - [x] Interactive 
   - [x] Finding Logins
   - [x] Getting All Logins
   - [x] Download Logins As Text File
#### Local
   - [x] Setup
   - [x] Interactive 
