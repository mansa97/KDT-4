import random
import requests
from selenium import webdriver

# url에 있는 사진을 내가 지정한 경로에 저장하는 함수
def save_image_from_url(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors

        with open(file_path, "wb") as f:
            f.write(response.content)

        print("Image saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


# linkareer에서 현재 진행중인 공모전들 중 제목에 빅데이터가 포함된 공모전들의 포스터를 가져와서 파일에 저장하는
for i in range(1,11):
    cnt = []
    driver = webdriver.Chrome()
    driver.get(f"https://linkareer.com/list/contest?filterType=CATEGORY&orderBy_direction=DESC&orderBy_field=VIEW_COUNT&page={i}")
    driver.implicitly_wait(random.randint(1,5))

    result = driver.find_elements_by_tag_name('h5')
    images = driver.find_elements_by_tag_name('img')
    for i in images:
        cnt.append(i.get_attribute('src'))
    cnt = cnt[5:25]
    for i in range(len(result)):
        if '데이터' in result[i].text:
            print(result[i].text)
            image_url = cnt[i]
            file_path = f"{result[i].text}.png"
            save_image_from_url(image_url, file_path)
    driver.quit()