from selenium import webdriver
from generate_score import generate_score

url = 'adnansh.in'
driver = webdriver.Firefox()
default_hosts = ['google.com', 'instagram.com', 'amazon.com', 'chat.openai.com']
default_scores = [85, 97, 85, 100]

def get_load_time(url: str, show=False):
  driver.get('https://' + url)
  load_time = driver.execute_script('return performance.timing.loadEventEnd - performance.timing.navigationStart') / 1000
  if show:
    print(f"Page load time for {url}: {load_time} seconds")
  return load_time

def compare_load_times(url: str, show=False):
  default_load_times = []
  for default_host in default_hosts:
    default_load_times.append(get_load_time(default_host, show))

  actual_load_time = get_load_time(url, show)
  score = generate_score(sorted(default_load_times, reverse=True), actual_load_time, sorted(default_scores))
  return score

if __name__ == "__main__":
  score = compare_load_times(url)
  print("\n\n*****")
  print("Loading Time Score: ", score)
  driver.quit()
