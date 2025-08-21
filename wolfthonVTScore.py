# think about a security case, when you have to scan mass domains, or also IPs (IOCs), or you are reviewing the allowed domains or ips in MDE indicator, or in PaloAlto firewall
# there will be 100s or even 1000s to go through, which could take days to go manually, so this will help you to get the Virus Total malicious score.. 

import requests
import time
import csv
import os

# Your VirusTotal API key (replace with your actual key)
vt_api_key = "your api key here"

# domain can be in a list here
# Input CSV file containing the list of domains
csv_file = "domain_list.csv" 

# Output folder and file
output_folder = "results"
output_file = os.path.join(output_folder, "domain_scores.csv")

# VirusTotal API setup
main_url = "https://www.virustotal.com/api/v3/domains/"
headers = {
    "x-apikey": vt_api_key
}

# Create the results folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to read domains from CSV file
def read_domains_from_csv(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        return [line.strip() for line in f if line.strip()]

# Function to get malicious score from VirusTotal
def malicious_score(domain):
    url = main_url + domain
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
            return malicious
        elif response.status_code == 404:
            return "n/a"
        else:
            print(f"Unexpected status code {response.status_code} for {domain}")
            return "n/a"
    except Exception as e:
        print(f"Error occurred for {domain}: {e}")
        return "n/a"

# Read domains
domains = read_domains_from_csv(csv_file)

# Check if output file exists (to decide whether to write headers)
write_headers = not os.path.exists(output_file)

# Open output CSV for appending
with open(output_file, mode="a", newline="", encoding="utf-8") as out_csv:
    writer = csv.writer(out_csv)

    if write_headers:
        writer.writerow(["Domain", "Malicious Score"])

    # Process each domain
    for domain in domains:
        score = malicious_score(domain)
        print(f"{domain}: {score}")
        writer.writerow([domain, score])
        time.sleep(15)  # Keep this at 15 seconds to be safe with free-tier limits
