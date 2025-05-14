# test_db.py

from database import save_ticket_to_mysql

# Dummy test data (you can modify this)
test_title = "Test Ticket from Script"
test_body = "This is a test ticket body added manually via test script."
test_requester_id = 46  # make sure this ID exists in your `requester` table
test_team_id = 1
test_team_member_id = 1

try:
    save_ticket_to_mysql(
        title=test_title,
        body=test_body,
        requester_id=test_requester_id,
        team_id=test_team_id,
        team_member_id=test_team_member_id
    )
    print("✅ Ticket inserted successfully into MySQL!")
except Exception as e:
    print(f"❌ Error inserting ticket: {e}")
