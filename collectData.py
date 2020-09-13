import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 순위 : td > div.wrap.t_center > span.rank
# 앨범 사진 : div.wrap > a > img
# 곡명 : div.ellipsis.rank01 a
# 아티스트명 : div.ellipsis.rank02 > a:nth-of-type(1)
# 앨범명 : div.ellipsis.rank03 a
# 좋아요 수 : div.wrap span.cnt
