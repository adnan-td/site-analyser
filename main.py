from ping import compare_ping
from loading_speed import compare_load_times
from tabulate import tabulate

default_hosts = ['www.google.com', 'www.instagram.com', 'www.amazon.com', 'chat.openai.com']
# url = input("Enter the url to test: ")
url = "adnansh.in"

scores = []

for site in default_hosts:
  scores.append((site, compare_ping(site), compare_load_times(site)))

scores.append((url, compare_ping(url, show=True), compare_load_times(url, show=True)))

def print_table(data):
  table = tabulate(data, headers=["Site", "Ping Score", "Loading Score"], tablefmt="grid")
  print(table)

print_table(scores)
print()