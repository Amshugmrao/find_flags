import requests

def search_in_repo(search_word, owner, repo, access_token):
    # GitHub API endpoint for code search
    #URL for Github code search API
    #type=code => search in code files
    search_url = f"https://api.github.com/search/code?q={search_word}+repo:{owner}/{repo}&type=Code"
    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # Make the GET request to the GitHub API
    response = requests.get(search_url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        search_results = response.json()
        total_count = search_results.get('total_count', 0)
        if total_count > 0:
            return True
        else:
            return False
    else:
        print(f"Failed to search the repository. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None