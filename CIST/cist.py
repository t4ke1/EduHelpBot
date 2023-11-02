import sys
from datetime import datetime, timedelta
from cist_libs.csvlibb import *
from cist_libs.dbglib import *
from cist_libs.reqlib import *

def get_date_now() -> str:
    return datetime.today().strftime('%d.%m.%Y')

def get_prev_date() -> str:
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday.strftime("%d.%m.%Y")
    return yesterday_date

def get_time_now() -> str:
    current_time = datetime.now().strftime("%H:%M")
    return current_time


def classes_today(group_namec, grade_t, group_id = 00000) -> str:

    date_now = get_date_now()
    yest_date = get_prev_date()
    time_now = get_time_now()

    conn, cursor = connect_db("groups.db")
    group_name = group_namec.lower()
    group_id = find_group_id(group_name, grade_t, cursor)
    conn.close()

    if group_id == 00000:
        return f"<u><b>There is no timatable for the group {group_name}!</b></u>"
    else:
        url = f"{url_n}{group_id}{url_k}"

    check = check_for_download(group_name, date_now, yest_date, time_now)
    if(check):
        download_table_url(url, f"{group_name}_{date_now}.csv")
    else:
        pass
    classes_t = open_and_read(f"{group_name}_{date_now}.csv", date_now)
    return classes_t