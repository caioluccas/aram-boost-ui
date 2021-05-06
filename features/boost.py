import api


api = api.LeagueOfLegendsClientAPI()
def Boost():
    champSelect = api.get('/lol-champ-select/v1/session')
    data = api.get('/lol-lobby/v2/lobby').json()
    partyId = data["partyId"]
    champSelect = api.get('/lol-champ-select/v1/session').json()
    boost = api.postBoost('/lol-login/v1/session/invoke?destination=lcdsServiceProxy&method=call', 'args=["{}", "teambuilder-draft", "activateBattleBoostV1", ""]'.format(partyId))

