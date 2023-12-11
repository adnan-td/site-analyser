from selenium import webdriver
from . generate_score import generate_score

url = 'adnansh.in'
driver = None
default_hosts = ['google.com', 'instagram.com',
                 'amazon.com', 'chat.openai.com']
default_scores = [85, 97, 85, 100]


def get_load_time(url: str, show=False):
  driver.get('https://' + url)
  load_time = driver.execute_script(
      'return performance.timing.loadEventEnd - performance.timing.navigationStart') / 1000
  if show:
    print(f"Page load time for {url}: {load_time} seconds")
  return load_time


def compare_load_times(url: str, show=False):
  global driver
  driver = webdriver.Firefox()
  default_load_times = []
  data = []
  for default_host in default_hosts:
    lt = get_load_time(default_host, show)
    default_load_times.append(lt)
    data.append((default_host, lt))

  actual_load_time = get_load_time(url, show)
  data.append((url, actual_load_time))
  score = generate_score(sorted(default_load_times, reverse=True),
                         actual_load_time, sorted(default_scores))
  driver.quit()
  return score, data


if __name__ == "__main__":
  score = compare_load_times(url)
  print("\n\n*****")
  print("Loading Time Score: ", score)
