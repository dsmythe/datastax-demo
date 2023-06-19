from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
    'secure_connect_bundle': 'secure-connect-ds-test.zip'
}
auth_provider = PlainTextAuthProvider(
    'DjCUeBbJAcMQldAhhlWfrTzE', 
    'xAk-Md7FhIU07TCt-sb9DRZKO-nd5LdEOv1-QsnnrQ.Bgue1HaQ-Nyscq754Q5BSGDAKdrMD-nzEI+RXa5GAkPTX8POBrLq3ocGL+m3E+ZSneb_7lS,6NCSkEH09auRm')


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
    
    rows = session.execute("SELECT * FROM monsters")
    for row in rows:
        print(row)
        
