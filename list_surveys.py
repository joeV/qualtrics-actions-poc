import os
import csv
import requests

QUALTRICS_TOKEN = os.environ["QUALTRICS_TOKEN"]
DATACENTER = os.environ["QUALTRICS_DATACENTER"]

BASE_URL = f"https://{DATACENTER}.qualtrics.com/API/v3"
HEADERS = {
    "X-API-TOKEN": QUALTRICS_TOKEN,
    "Content-Type": "application/json"
}

def fetch_surveys():
    print("DEBUG BASE_URL:", repr(BASE_URL))
    resp = requests.get(f"{BASE_URL}/surveys", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()["result"]["elements"]

def write_csv(surveys, filename="surveys.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["surveyId", "name", "isActive", "lastModified"])
        for s in surveys:
            writer.writerow([
                s.get("id"),
                s.get("name"),
                s.get("isActive"),
                s.get("lastModified")
            ])

if __name__ == "__main__":
    surveys = fetch_surveys()
    write_csv(surveys)
    print(f"Wrote {len(surveys)} surveys to surveys.csv")