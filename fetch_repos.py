import github3
import os
from dotenv import load_dotenv
from check_flags import search_in_repo
import time

# Load the environment variables
load_dotenv()


# For fetching all the repos of an organization
def fetch_repos(GITHUB_ACCESS_TOKEN, org_name):

    # As they are private reos, we need to authenticate. It will be added in header of http requests
    gh = github3.login(token=GITHUB_ACCESS_TOKEN)

    # Fetching the organization
    org = gh.organization(org_name)

    # Fetching all the repositories inside the organization
    repos = list(org.repositories(type="all"))

    # Store all the repo names in side the array and return it
    arr =[str(repo.name) for repo in repos]

    print("finished fetching repos")

    return arr

if __name__ == "__main__":
    arr = fetch_repos(os.environ['GITHUB_ACCESS_TOKEN'], "hinge-health")
    with open('/Users/amshu.gm/untitled folder/data/flag_data.txt', 'r') as file:
        lines = file.readlines()
        lines = list(set(lines))
        lines = [line.strip() for line in lines]
    print(lines[0], len(lines))
    print("finshed reading flag")
    flags = []
    for i in lines:
        flag = search_in_repo(i, "hinge-health", arr[0], os.environ['GITHUB_ACCESS_TOKEN'])
     
        if(flags==None):
            print("Error in searching the repo")
            exit(1)
        flags.append(flag)
        time.sleep(1)
    
    print(arr[0], " has the follwoing flags")
    for i in range(len(flags)):
        print(lines[i])
    

