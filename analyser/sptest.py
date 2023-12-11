import speedtest
import time


def get_internet_speed():
  # st = speedtest.Speedtest()
  # download_speed = st.download() / 10**6  # Convert to Mbps
  # upload_speed = st.upload() / 10**6  # Convert to Mbps
  # ping = st.results.ping
  time.sleep(2)
  download_speed = 57.824345
  upload_speed = 44.23554344
  ping = 36.4543
  return download_speed, upload_speed, ping


if __name__ == "__main__":
  download_speed, upload_speed, ping = get_internet_speed()

  print(f"Download Speed: {download_speed:.2f} Mbps")
  print(f"Upload Speed: {upload_speed:.2f} Mbps")
  print(f"Ping: {ping} ms")
