from ping3 import ping, verbose_ping
from generate_score import generate_score

host = 'www.ebay.com'
default_hosts = ['www.google.com', 'www.instagram.com', 'www.amazon.com', 'chat.openai.com']
default_scores = [97, 85, 95, 100]


def check_ping(host: str, show=False):
  response_time = ping(host)
  if show:
    print(f"Response time to {host}: {response_time} ms")
  return response_time

def compare_ping(host: str, show=False):
  default_response_time = []
  for default_host in default_hosts:
    default_response_time.append(check_ping(default_host, show))
  actual_response_time = check_ping(host, show)

  score = generate_score(sorted(default_response_time, reverse=True), actual_response_time, sorted(default_scores))
  return score


if __name__ == "__main__":
  score = compare_ping(host)
  print('\n\n*******')
  print("Ping score: ", score)

# For verbose output
# verbose_ping(host)
