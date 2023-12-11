import whois


def get_domain_info(domain_name):
  try:
    domain_info = whois.whois(domain_name)
    return domain_info
  except e:
    return f"Error has occured"


if __name__ == "__main__":
  domain_name = "adnansh.in"
  result = get_domain_info(domain_name)
  print(result)
  # if isinstance(result, dict):
  #     print("\nDomain Information:")
  #     pprint(result)
  # else:
  #     print(result)
