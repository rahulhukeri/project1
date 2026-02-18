import os
from monday import MondayClient
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")

monday = MondayClient(API_TOKEN)

print(monday.get_user_by_id(50930572))

query = '''
{
  boards(limit: 5) {
    id
    name
    state
  }
}
'''
try:
    response = monday.execute_query(query)
    print("✅ Success! Connected to Monday.com")
    print("\nYour boards:")
    print(response)
except Exception as e:
    print(f"❌ Error: {e}")