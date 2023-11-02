import requests
import os
from datetime import datetime

url_n = "https://cist.nure.ua/ias/app/tt/WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=3&Aid_group="
url_k = "&Aid_potok=0&ADateStart=01.02.2023&ADateEnd=30.06.2023&AMultiWorkSheet=0"

def delete_files_without_current_date(current_date, current_time, folder_path = "csvFiles\\"):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if str(current_date) not in filename and int(current_time.split(':')[0]) >= 5 and int(current_time.split(':')[1]) >= 10:
                os.remove(file_path)
                #print(f"File deleted: {file_path}")

def check_for_download(group_name : str, date_now : str, yest_date : str, time_now : str) -> bool:
    delete_files_without_current_date(date_now, time_now)
    filename_path = f"csvFiles\\{group_name}_{date_now}.csv"
    if os.path.exists(filename_path):
       return False;
    else:
        return True;

def download_table_url(link : str, filename : str):
    try:
        print(f"Downloading file -> {filename}")
        response = requests.get(link, allow_redirects=True)
        response.raise_for_status()
        print(f"HTTP status code: {response.status_code}")

        if response.ok:
            with open(f"csvFiles\\{filename}", "wb") as file:
                file.write(response.content)
            #print("File download is OK!")

    except requests.exceptions.RequestException as e:
        print(f"Error while downloading: {e}")
