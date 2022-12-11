from serpapi import GoogleSearch

API_KEY="fe3e1e6c843b7cd1f375a5ba0fc399a12cf7e594b0a3cb111d7bb90ab1724799"
params = {
    "engine": "google",
    "q": "Школа 2114 О нас",
    "api_key": API_KEY,
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(f"Title: {result['title']}\nLink: {result['link']}\n")
