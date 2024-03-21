import random

user_duties={
    "preacher": ["Sermon","Bible teachings","Prayers"],
    "brother": ["Bible reading","Lord's supper helper","Lord's super leader","Prayers","Devotion","MC"]
}
people={
    "Bekoe": "preacher",
    "Obeng": "preacher",   
    "Buabeng": "preacher",
    "Stephen": "brother",
    "Atta Boateng": "brother",
    "Essiew": "brother",    
    "Bismark": "brother",
    "Kwaku": "brother",
    "Francis": "brother"
}
def assign_duties(people, user_duties):
    duties_assigned = {}
    for name, title in people.items():
        available_duties = user_duties[title]
        duty_assigned = random.choice(available_duties)
        duties_assigned[name] = duty_assigned
    return duties_assigned
assigned_duties = assign_duties(people, user_duties)
for name, duty in assigned_duties.items():
    print(f"{name} is assigned to: {duty}")
