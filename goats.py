import requests

# Function to read tokens from file
def read_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = file.read().splitlines()
    return tokens

# Function to fetch tasks using each token
def fetch_tasks(token):
    url = "https://api-mission.goatsbot.xyz/missions/user"
    
    headers = {
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {token}",
        "origin": "https://dev.goatsbot.xyz",
        "referer": "https://dev.goatsbot.xyz/",
        "user-agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch tasks, Status Code: {response.status_code}")
        return None

# Function to simulate clicking on the link
def click_on_link(mission):
    if mission.get("action_link"):
        print(f"Simulating click on: {mission['action_link']}")
        # Simulate clicking on the link (this could be opening the link in a browser or doing some action)
        # You can use requests to send a GET request to simulate the click
        response = requests.get(mission['action_link'])
        if response.status_code == 200:
            print(f"Successfully clicked on link: {mission['action_link']}")
        else:
            print(f"Failed to click on link: {mission['action_link']}, Status Code: {response.status_code}")
    else:
        print(f"No action link found for mission: {mission['name']}")

# Function to post action to the API after clicking
def post_action(mission_id, token):
    post_url = f"https://dev-api.goatsbot.xyz/missions/action/{mission_id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {token}",
        "origin": "https://dev.goatsbot.xyz",
        "referer": "https://dev.goatsbot.xyz/",
        "user-agent": "Mozilla/5.0"
    }
    
    # Sending the POST request to the API after the action
    response = requests.post(post_url, headers=headers)
    if response.status_code == 201:
        print("[Join Group](https://t.me/dasarpemulung)")
        print(f"Successfully posted action for mission {mission_id}")
        return response.json()  # Return the result of the action
    else:
        print(f"Failed to post action for mission {mission_id}, Status Code: {response.status_code}")
        return None

# Function to handle the complete flow for each mission
def handle_missions(token):
    missions_data = fetch_tasks(token)
    
    if missions_data:
        for category, missions in missions_data.items():
            for mission in missions:
                # Simulate clicking the action link
                click_on_link(mission)
                # Post to the action API
                post_result = post_action(mission['_id'], token)
                print("[Join Group](https://t.me/dasarpemulung)")
                if post_result:
                    print(f"Post action result for mission {mission['_id']}: {post_result}")

if __name__ == "__main__":
    # Path to the file containing the tokens
    token_file = "token.txt"
    
    # Read tokens from file
    tokens = read_tokens(token_file)
    
    # Assuming you want to use the first token in the list
    if tokens:
        handle_missions(tokens[0])
