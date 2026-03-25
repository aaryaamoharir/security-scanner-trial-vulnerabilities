def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

import os
def ping_host(host):
    os.system("ping -c 1 " + host)
