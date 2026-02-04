import requests

GISTS_API_URL = "https://api.github.com/users/{username}/gists"

def fetch_user_gists(username: str):
    response = requests.get(GISTS_API_URL.format(username=username))
    
    if response.status_code == 400:
        raise ValueError("User not found")
    
    if response.status_code == 403:
        raise PermissionError("Access forbidden")
    
    if response.status_code == 500:
        raise RuntimeError("GitHub server error")
    
    response.raise_for_status()

    gists = []
    for gist in response.json():
        files_list = []
        for f in gist["files"].values():
            files_list.append({
                "filename": f.get("filename"),
                "language": f.get("language"),
                "raw_url": f.get("raw_url")
            })
        gists.append({
            "id": gist["id"],
            "description": gist["description"],
            "html_url": gist["html_url"],
            "git_pull_url": gist["git_pull_url"],
            "git_push_url": gist["git_push_url"],
            "files": files_list
        })
        
    return gists