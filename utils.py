from data.users import *

def get_user_by_id(id_user):
    if id_user in USERS:
        tmp_dic = USERS[id_user].copy()
        tmp_dic["id"] = id_user
        tmp_dic["phone"] = tmp_dic["phone"][-10:]
        return tmp_dic
    return {}


def get_user_by_phone(phone):
    #Only work with last 10 digits
    this_phone = phone.replace(" ","")[-10:]
    for key in USERS.keys():
        if USERS[key]["phone"] == "+52"+this_phone:
            tmp_dic = USERS[key].copy()
            tmp_dic["id"] = key
            tmp_dic["phone"] = tmp_dic["phone"][-10:]
            return tmp_dic
    return {}
