import requests, time, json

def speedProcess(speed):
    if speed < 0:
        return 0.0
    else:
        return speed

def binary_string(data):
    if data == 0:
        return False
    else:
        return True

def convert(data):
    return tuple(x for x in data)

def getAccessToken(username, password):
    headers = {
                'Accept': 'application/json',
                'Authorization': 'Basic U3dlcUFOQWdFVkVoVWt1cGVjcmVrYXN0ZXFhVGVXckFTV2E1dXN3MzpXMnZBV3JlY2hhUHJlZGFoVVJhZ1VYYWZyQW5hbWVqdQ==',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
    data = f'username={username}&password={password}&grant_type=password'
        
    return requests.post('https://www.life360.com/v3/oauth2/token', headers=headers, data=data).json()['access_token']

def start_message():
    print("Start by setting the circle you want to track(set_circle).")
    print("Type: 'help' for a list of commands.")

class Life360:

    def __init__(self, username, password):
        self.start_message = start_message()
        self.username = username
        self.password = password
        self.circleID = ''
        self.access_token = getAccessToken(self.username, self.password)
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
            }
        self.stopCircle = True
    
    def set_circle(self):
        circles = self.circles()['circles']
        circleData = {}
        for circle in circles:
            circleData[circle['name']] = circle['id']
        print(circleData)
        user_input = input('Enter circle name: ')
        self.circleID = circleData[user_input]
        return f'{user_input} has been set as the active cirle'

    def me(self):
        return requests.get('https://www.life360.com/v3/users/me', headers=self.headers).json()

    def circles(self):
        return requests.get('https://www.life360.com/v3/circles.json', headers=self.headers).json()
    
    def code(self):
        return requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/code', headers=self.headers).json()

    def messages(self):
        return requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/messages', headers=self.headers).json()

    def history(self):
        return requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/members/history', headers=self.headers).json()['locations']

    def emergency_contacts(self):
        return requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/emergencyContacts', headers=self.headers).json()

    def circle_data(self):
        data = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}', headers=self.headers).json()
        group = {
            'ID': data['id'],
            'Group Name': data['name'],
            'Member Count': data['memberCount'],
            'unreadMessages': data['unreadMessages'],
            'unreadNotification': data['unreadNotifications'],
            'members': [{'firstName': person['firstName'], 'lastName': person['lastName']} for person in data['members']]
        }
        return group

    def circle_live(self):
        if self.stopCircle == True:
            print('control-c to break loop')
            print('beginning...')
            time.sleep(3)
            self.stopCircle = False
        
        users = []

        data = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}', headers=self.headers).json()
        for person in group['members']:

            user = {
                'ID': person['id'],
                'First': person['firstName'],
                'Last': person['lastName'],
                'Address1': person['location']['address1'],
                'Address2': person['location']['address2'],
                'Since': time.ctime(person['location']['since']),
                'inTransit': binary_string(person['location']['inTransit']),
                'isDriving': binary_string(person['location']['isDriving']),
                'Speed': speedProcess(person['location']['speed']*2.23),        # 2.23 is an approximation of the conversion rate to MPG
                'Sharing': binary_string(person['features']['shareLocation']),
                'Battery': person['location']['battery'],
                'wifiState': binary_string(person['location']['wifiState']),
                'Phone': person['loginPhone'],
                'Email': person['loginEmail'],
                'Latitde': person['location']['latitude'],
                'Longitude': person['location']['longitude'],
                'createAt': time.ctime(int(person['createdAt']))
            }
            users.append(user)
        return users

    def help(self):
        return '[COMMANDS]\n'\
               'set_circle:\t\t\tSet the active circle to get additional information.\n'\
               'me:\t\t\t\tGet information about account used to login.\n'\
               'circles:\t\t\tGet users circle information.\n'\
               'code:\t\t\t\tGet active code if any.\n'\
               'messages:\t\t\tGet all messages of the account user to login.\n'\
               'history:\t\t\tGet history of users in the circle.\n'\
               'emergency_contacts:\t\tGet emergency contact information of account used to login.\n'\
               'circle_data:\t\t\tGet circle data.\n'\
               'circle_live:\t\t\tGet current information of all users in the circle.'