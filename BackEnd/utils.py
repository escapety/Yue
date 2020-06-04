import requests
headers = {"User-Agent":\
               "Mozilla/5.0 (Windows NT 6.1; WOW64)"
               + " AppleWebKit/537.36 (KHTML, like Gecko) "
               + "Chrome/67.0.3396.87 Safari/537.36"}
base_url = "http://127.0.0.1:8888/BackEnd/"
tem_url = base_url + "%s/"
def increase_new_user():
    m = "new_user"
    r_url = tem_url % m
    cnt = 1
    for i in range(0, cnt):
        params = {}
        params["name"] = "test_521_" + str(i)
        params["password"] = "fake_pwd_" + str(i)
        res = requests.get(r_url, params)
        if res.status_code != 200:
            print("increase error!")
            break

def increase_act():
    m = "new_activity"
    r_url = tem_url % m
    cnt = 1
    time_s = "2020-05-30 13:00"
    time_e = "2020-05-30 19:00"
    for i in range(0, cnt):

        params = {}
        params["name"] = "test_521_" + str(i)
        params["theme"] = "boring_theme" + str(i)
        params["location"] = "PKU"
        params["time"] = ""
