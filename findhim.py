#
# if you took it, mention @J4son0
#

from colorama import Fore, Back, Style
import time
import requests
import urllib.request
import os
import datetime
import sys


TESTING_MODE = True
APITOKEN = 'lxe21fdIhqTQl61tYUfuPVdEys8Mbuk7f5rSNJD1ReMGb11EjWk51co56oQzi9GdgxJQGzIxp1E='

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("")
time.sleep(0)
os.system('clear')

print(Fore.RED + """

███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

- Babyl0n -

Created by @J4son0

Be the almighty lion

usdt:
0x8867E288f9dEbDBD4aF9342AAD2CeA83101Bd16C
\n\n

""")


# تنزيل الصورة للهدف
urllib.request.urlretrieve(input('[ꖦ]Enter the url of the target\'s img:\n\n'),input("put a name to the new image (ex:test1.jpg): "))
image_file = input('\n\n[ꖦ]Enter the path of the new image: (home/babyl0n/Desktop/test1.png)\n\n')

def search_by_face(image_file):
    if TESTING_MODE:
        print('****** TESTING MODE search, results are bad, but credits are NOT deducted ******')

    site='https://facecheck.id'
    headers = {'accept': 'application/json', 'Authorization': APITOKEN}
    files = {'images': open(image_file, 'rb'), 'id_search': None}
    response = requests.post(site+'/api/upload_pic', headers=headers, files=files).json()

    if response['error']:
        return f"{response['error']} ({response['code']})", None

    id_search = response['id_search']
    print(response['message'] + ' id_search='+id_search)
    json_data = {'id_search': id_search, 'with_progress': True, 'status_only': False, 'demo': TESTING_MODE}

    while True:
        response = requests.post(site+'/api/search', headers=headers, json=json_data).json()
        if response['error']:
            return f"{response['error']} ({response['code']})", None
        if response['output']:
            return None, response['output']['items']
        print(f'{response["message"]} progress: {response["progress"]}%')
        time.sleep(1)


# ابحث بالانترنت على الصورة
error, urls_images = search_by_face(image_file)

if urls_images:
    for im in urls_images:      # Iterate search results
        score = im['score']     # 0 to 100 score how well the face is matching found image
        url = im['url']         # url to webpage where the person was found
        image_base64 = im['base64']     # thumbnail image encoded as base64 string
        print(f"{score} {url} {image_base64[:32]}...")
else:
    print(error)
