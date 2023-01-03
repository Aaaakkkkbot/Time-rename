import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "15794380")

API_HASH = os.environ.get("API_HASH", "3818be5c4934a0d05cc1a603cad2035a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5981080241:AAGScS4IzIykxdF_JxNL9rBRoXk4_8uNtU4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

