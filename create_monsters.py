from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import random

cloud_config= {
    'secure_connect_bundle': 'secure-connect-ds-test.zip'
}
auth_provider = PlainTextAuthProvider(
    'DjCUeBbJAcMQldAhhlWfrTzE', 
    'xAk-Md7FhIU07TCt-sb9DRZKO-nd5LdEOv1-QsnnrQ.Bgue1HaQ-Nyscq754Q5BSGDAKdrMD-nzEI+RXa5GAkPTX8POBrLq3ocGL+m3E+ZSneb_7lS,6NCSkEH09auRm')



def generate_monster():
    name = random.choice(["Gnoll", "Orc", "Troll", "Ogre", "Dragon"])
    color = random.choice(["Red", "Green", "Blue", "Black", "White"])
    hitpoints = random.randint(100, 1000)
    strength = random.randint(10, 50)
    endurance = random.randint(10, 50)
    willpower = random.randint(10, 50)
    intelligence = random.randint(10, 50)
    aura = random.choice(["Red", "Green", "Blue", "Black", "White"])
    description = "A powerful monster with {} skin and a {} aura.".format(
        color, aura)
    location = random.choice(
        ["The Mountains", "The Forest", "The Swamp",
         "The Desert", "The Underworld"])
    return {
        "name": name,
        "color": color,
        "hitpoints": hitpoints,
        "strength": strength,
        "endurance": endurance,
        "willpower": willpower,
        "intelligence": intelligence,
        "aura": aura,
        "description": description,
        "location": location
    }
    
CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS monsters (
        name TEXT PRIMARY KEY,
        color TEXT,
        hitpoints INT,
        strength INT,
        endurance INT,
        willpower INT,
        intelligence INT,
        aura TEXT,
        description TEXT,
        location TEXT );
"""

if __name__ == '__main__':
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.set_keyspace("default")
    session.execute(CREATE_TABLE)
    for i in range(0, 10):
        monster = generate_monster()
#        print("""
#            INSERT INTO monsters (
#                name,
#                color,
#                hitpoints,
#                strength,
#                endurance,
#                willpower,
#                intelligence,
#                aura,
#                description,
#                location
#            ) VALUES (
#                '{name}',
#                '{color}',
#                {hitpoints},
#                {strength},
#                {endurance},
#                {willpower},
#                {intelligence},
#                '{aura}',
#                '{description}',
#                '{location}'
#            );""".format(**monster))
        session.execute("""
            INSERT INTO monsters (
                name,
                color,
                hitpoints,
                strength,
                endurance,
                willpower,
                intelligence,
                aura,
                description,
                location
            ) VALUES (
                '{name}',
                '{color}',
                {hitpoints},
                {strength},
                {endurance},
                {willpower},
                {intelligence},
                '{aura}',
                '{description}',
                '{location}'
            )""".format(**monster))
        print("Created {0}".format(monster))
        
