from neo4j import GraphDatabase
from datetime import datetime
import os

uri = "bolt://localhost:7687"
username = "neo4j"
password = "Ola3Ola3"

backup_dir = "C:\Users\Søren Merved\Documents\Ola3_backups"

def backup_db():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.dump")
    
    driver = GraphDatabase.driver(uri, auth=(username, password))
    session = driver.session()

    cypher_query = f"CALL apoc.export.cypher.all('{backup_file}')"
    session.run(cypher_query)

    session.close()
    driver.close()

    print(f"Backup created: {backup_file}")

def restore_db(backup_file):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    session = driver.session()

    cypher_query = f"CALL apoc.cypher.runFile('{backup_file}')"
    session.run(cypher_query)

    session.close()
    driver.close()

    print(f"Database restored from {backup_file}")

if __name__ == "__main__":
    backup_db()

    # backup_file_to_restore = "backup file path"
    # restore_db(backup_file_to_restore)
