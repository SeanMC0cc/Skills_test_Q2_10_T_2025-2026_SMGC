from pyscript import document, display

def Badminton(event):
    Badminton = {
    'Name': 'Badminton Club',
    'Description': 'A club for badminton to play and improve their skills.',
    'meeting_time': 'Every Wednesday at 2 PM',
    'Location': 'MM hall',
    'Club Moderator': 'Mr. Cgervacio',
    'Number of members': 12
}
    document.getElementById("output").innerHTML = ""
    display(f'{Badminton["Name"]}\n{Badminton["Description"]}\nMeeting Time: {Badminton["meeting_time"]}\nLocation: {Badminton["Location"]}\nClub Moderator: {Badminton["Club Moderator"]}\nNumber of members: {Badminton["Number of members"]}', target='output')

def Robotics(event):
    Robotics = {
    'Name': 'Robotics Club',
    'Description': 'A club for Robot lovers to Create and Program robots.',
    'meeting_time': 'Every Monday and friday at 3 PM',
    'Location': 'Room 503',
    'Club Moderator': 'Mr. Ortiz',
    'Number of members': 8
}
    document.getElementById("output").innerHTML = ""
    display(f'{Robotics["Name"]}\n{Robotics["Description"]}\nMeeting Time: {Robotics["meeting_time"]}\nLocation: {Robotics["Location"]}\nClub Moderator: {Robotics["Club Moderator"]}\nNumber of members: {Robotics["Number of members"]}', target='output')

def ART(event):
    Art = {
    'Name': 'ART Club',
    'Description': 'A club for people to draw their best and bring out their talent.',
    'meeting_time': 'Every Tue and Thurs at 4 PM',
    'Location': 'room 306',
    'Club Moderator': 'Ms. Salve',
    'Number of members': 23
}
    document.getElementById("output").innerHTML = ""
    display(f'{Art["Name"]}\n{Art["Description"]}\nMeeting Time: {Art["meeting_time"]}\nLocation: {Art["Location"]}\nClub Moderator: {Art["Club Moderator"]}\nNumber of members: {Art["Number of members"]}', target='output')