import mysql.connector
from datetime import datetime

def save_ticket_to_mysql(title, body, requester_id, team_id, team_member_id=1):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # your MySQL password here
        database="helpdesk_core_php"
    )

    cursor = conn.cursor()

    insert_query = """
        INSERT INTO ticket (title, body, requester, team, team_member, status, priority, rating, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (
        title,
        body,
        requester_id,
        team_id,
        team_member_id,
        "open",       # status
        "medium",     # priority
        0,            # rating
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()
