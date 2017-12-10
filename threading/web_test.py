import threading
import requests
import os
import time

def main():
    threads_list = []
    creds = []
    how_many = input("how many student do u want to retrieve:\n")
    for i in range(how_many):
        user_cred = raw_input("Credentials in format [username:password]:\n")
        creds.append(user_cred)
    for i in range(how_many):
        user_credential = creds[i].split(":")
        username = user_credential[0]
        password = user_credential[1]
        create_thread = threading.Thread(target=login, args=(username, password))
        threads_list.append(create_thread)
    for thread in threads_list:
        thread.start()

def login(username, password):
    payload={"username":username, "password":password}
    with requests.Session() as s:
        login = s.post("https://portal.abu.edu.ng/index.php", data=payload)
    with open(os.getcwd()+"/%s_page.html"%username, "w") as f:
        f.write(login.content)
    print("Done for %s at time %s" % (username, time.ctime()))


if __name__=="__main__":
    main()
