#Diccinarios
#{"key": "value", "key": "value"team")

team={
    "name": "city",
    "country": "England",
    "champions": 1,
    "players": ['Halland', 'Grealish']
}
print(type(team))
print(team)
print(team["name"])
print(team["players"])
team["players"].append("Kevin")
team["name"] = "Manchester City"
team["League"] = "Premiere League"
print(team)