from Utils.db_utils import client
import main


# We are going to go ahead and create our admin user on startup
client.query("CREATE user:admin set username='admin', password='admin';")