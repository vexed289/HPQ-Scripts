import requests
import queryTracker
endpoint = "https://codeforces.com/api/user.ratedList"

def getData():
    data = requests.get(endpoint).json()
    queryTracker.snapshot(data)
    data = data["result"]
    total_elo = sum(user["rating"] for user in data)
    total_users = len(data)
    average_elo = round(total_elo/total_users, 1)
    print(f"Total users: {total_users}")
    print(f"Average elo: {average_elo}")
    return total_users, average_elo


    
