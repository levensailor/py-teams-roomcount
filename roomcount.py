from webexteamssdk import WebexTeamsAPI, ApiError

token = 'my_webex_api_token'
api = WebexTeamsAPI(access_token=token)

def find_rooms():
    myspaces = []
    each = {}
    count = 0
    rooms = api.rooms.list(type='group')
    spaces = [room for room in rooms if room.teamId is None]
    team_spaces = [room for room in rooms if room.teamId is not None]
    if team_spaces:
        for team_space in team_spaces:
            team = api.teams.get(team_space.teamId)
            if team_space.title == team.name:
                each['title'] = 'General'
            else:
                each['title'] = team_space.title
            each['lastActivity'] = team_space.lastActivity
            each['created'] = team_space.created
            each['team'] = team.name
            members = api.memberships.list(roomId=team_space.id)
            for member in members:
                count+=1
            each['count'] = count
            myspaces.append(each)
            each = {}
            count = 0
    if spaces:
        for space in spaces:
            each['title'] = space.title
            each['lastActivity'] = space.lastActivity
            each['created'] = space.created
            each['team'] = ''
            members = api.memberships.list(roomId=space.id)
            for member in members:
                count+=1
            each['count'] = count
            myspaces.append(each)
            each = {}
            count = 0
    return myspaces

myspaces = find_rooms()
for space in myspaces:
    print('name: '+space['title'])
    print('team: '+space['team'])
    print('last activity: '+str(space['lastActivity']))
    print('created: '+str(space['created']))
    print('count: '+str(space['count']))
    print('')