import requests
from bs4 import BeautifulSoup


for year in range(2017, 2023):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        year)
    res = requests.get(url=url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:"+image_url
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open(f"movie_{year}_{idx+1}.jpg", "wb") as f:
            f.write(image_res.content)
        if idx>=5:
          break
