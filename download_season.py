## Download entire season ##
import fastf1 as f1
import os
import time



def download_session_data(year, grand_prix, session_name):
    try:
        session = f1.get_session(year, grand_prix, session_name)
        session.load()
        print(f"Downloaded {year} {grand_prix} {session_name}")
    except Exception as e:
        print(f"Failed:  {year} {grand_prix} {session_name}")

def download_race_data(year, race):
    for session_name in ["Race"]:
        download_session_data(year, race['EventName'], session_name)

def download_season_data(year):
    schedule = f1.get_event_schedule(year)
    for i, race in schedule.iterrows():
        download_race_data(year, race)
        time.sleep(5)


if __name__ == "__main__":

    ## SELECT YEAR ##
    year=2023
    dir = os.getcwd()+"/"+str(year)

    if not os.path.exists(dir):
        os.makedirs(dir)
    f1.Cache.enable_cache(dir)

    print(f"Downloading {year} season...")

    download_season_data(year)