import sqlite3


def create_database(data):
    conn = sqlite3.connect('notices.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS notices (id VARCHAR(15),"
        " date VARCHAR(15), number VARCHAR(15), name VARCHAR(15),"
        " procedure_state VARCHAR(15), contract_type VARCHAR(15),"
        " procurement_type VARCHAR(15), estimated_value VARCHAR(15))")

    if len(data) > 0:
        print("Adding entries to database...")
        for id, value in data.items():
            c.execute("SELECT id FROM notices where id = ?", (id,))
            data = c.fetchone()
            if data is None:
                c.execute("INSERT INTO notices VALUES (?,?,?,?,?,?,?,?)",
                            [id, value['date'], value['number'], value['name'],
                            value['procedure_state'], value['contract_type'],
                            value['procurement_type'], value['estimated_value']])
        print("Job done.")
        conn.commit()
    else:
        print("No entries to be added.")
    conn.close()
    return None