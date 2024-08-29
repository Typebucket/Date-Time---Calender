def hotel_cost(nights):
    return nights*60

def plane_ride(city):
    if city == "San Francisco":
        return 650
    elif city == "Miami":
        return 800
    elif city == "California":
        return 850
    else:
        return 500
    
def car_rental(days):
    if days >= 7:
        return (40*days)-50
    elif days >= 3:
        return (40*days)-20
    else:
        return(40*days)
    
print("The Total cost for the trip to Miami for 5 days is: ", hotel_cost(5)+plane_ride("Miami")+car_rental(5))