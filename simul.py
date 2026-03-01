#simple returning home simulation --> trying to calculate different circumstances when going home 
import random as rd

def get_rdtype (season):
    if season == "winter":
        get_rdtype = "ice", 
    elif season == "summer" or "autumn": 
        get_rdtype = "cement", 
    elif season == "spring": 
        get_rdtype = "wet", 
    return get_rdtype 

def get_rdtext (): 
    if get_rdtype == "ice": 
        get_rdtext = "slippery", 
    elif get_rdtype == "cement" or "wet": 
        get_rdtext = "smooth", 
    return get_rdtext 

def get_rdlgth (meters):
    meters = rd.choice [200, 500]
    return print(f"{meters} + m")

if get_rdlgth =="200m":
   walking_time = 20, 
elif get_rdlgth == "500m": 
    walking_time = 50

get_terrain = rd.choice ["mild", "flat", "high"]

        
def road_profile (road_texture, road_length, terrain):
    road_texture = get_rdtext() #depending on road type, road texure differs 
    road_length = get_rdlgth  #someone can pick a random road 
    terrain = get_terrain #three differnt terrains possible 
    return road_texture +  road_length + terrain 
def calculate_walking_time (road_textire, terrain):
    if ("ice" ,"high"): 
        walking_time += 60, 
    elif ("ice" + "mild"): 
        walking_time += 40, 
    elif ("ice" + "flat"): 
        walking_time += 10, 
    elif ("smooth", "high"): 
        walking_time += 30,
    elif ("smooth", "mild"): 
        walking_time += 15, 
    else: 
        walking_time +=5
    return (f"{walking_time} + min")





