---
layout: post
title: 뉴스크롤링과 WordCloud
description: >
    PlayData 과정 Mini Project 1
# image: /assets/img/pythonLogo.png
sitemap: false
categories:
  - projects
---

# 웹크롤링으로 뉴스 가져와서 WordCloud로 만들기

Project: 웹크롤링으로 가져온 뉴스로 WordCloud 만들기

Date: 2022/04/01 - 

Member: 김민서, 김휘래, 유윤식, 이동근, 전송주, 하승범

PlayData 과정에서 첫 미니 프로젝트를 하게 되었다. 오전부터 점심시간까지 수업을 마치고 오후 1시부터 5시까지 미니 프로젝트를 진행했다. 주제는 자유주제. 우리 팀은 원래 Rotten Tomato에서 각 Netflix 시리즈들의 장르와 Tomato Score들을 크롤링해와서 장르별 평균 별점을 시각화하려는 프로젝트를 하려고 했다. 먼저 그 프로젝트 시도 과정은 이러했다.

먼저 그냥 크롤링을 시작하기 전, 과정을 좀 더 쉽게 해줄 수 있는 python 라이브러리가 있을지 구글링을 먼저 해봤다. 구글링 결과 관련 파이썬 라이브러리를 쉽게 찾을 수 있었다. pip로 설치할 수 있는 [rotten-tomatoes-scraper](https://pypi.org/project/rotten-tomatoes-scraper/)라는 파이썬 패키지를 찾을 수 있있다. Documentation을 읽어본 결과 패키지 중 MovieScraper라는 클래스를 우리 프로젝트에 유용히 쓸 수 있을것 같았다. 이 클래스는 원하는 영화나 TV쇼 제목을 파라미터로 넣어주면, 결과값으로 로튼 토마토 지수, 일반 평정 지수, 그리고 장르를 dictionary 형태로 리턴해줄 수 있는 class였다.

```python
from rotten_tomatoes_scraper.rt_scraper import MovieScraper

movie_scraper = MovieScraper(movie_title='Vicky Cristina Barcelona')
movie_scraper.extract_metadata()

print(movie_scraper.metadata)
```
```
>>> {'Score_Rotten': '81', 'Score_Audience': '74', 'Genre': ['comedy', 'drama', 'romance']}
```
사용할 패키지를 정한 뒤 Documentation을 참조하여 필요한 라이브러리들(`beautifulsoup4`, `requests`, `lxml`)을 `pip`로 설치한 뒤 `rotten-tomatoes-scraper` 패키지를 설치하였다.

프로젝트 환경 설정이 끝난 뒤, 패키지를 사용하기 위해, 먼저 넷플릭스 시리즈 제목 목록을 만들어야 했다. 제목을 리스트로 만들기 위해, 먼저 Rotten Tomatoes 사이트의 [The 210 Best Netflix Series to Watch Right Now](https://editorial.rottentomatoes.com/guide/best-netflix-shows-and-movies-to-binge-watch-now/)에서 210개의 넷플릭스 시리즈를 웹크롤링으로 가져오기로 했다. 

브리우저의 Developer Tools 로 사이트를 확인해보니 시리즈의 제목, 포스터, 그리고 설명 등은 `div`태그 아래 `row coundown-item` 클래스 내에 내장되어 있었다. 그리고 제목은 하위 클래스인 `article_movie_title`의 `<a>` 태크에 내장되어 있었다. BeautifulSoup의 find_all 메소드를 사용하여 `row countdown-item` 클래스를 모두 찾은 뒤, for loop을 돌려 제목을 추출해냈다.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://editorial.rottentomatoes.com/guide/best-netflix-shows-and-movies-to-binge-watch-now/'
# 사이트의 html 크롤링
response = requests.get(url)
soup = BeautifulSoup(response.text)
boxes = soup.find_all('div', {'class':'row countdown-item'})

titles = []
for box in boxes:
  title = box.find('div',{'class':'article_movie_title'}).find('a').string
  if title != None:
    titles.append(title)
print(titles)
print(len(titles))
```
```
['Derek', 'Ratched', 'Behind Her Eyes', 'Bloodline', 'Emily in Paris', 'The Cuphead Show!', 'White Lines', 'Inventing Anna', 'The Duchess', 'Lilyhammer', 'Marco Polo', 'After Life', 'Grand Army', ...
210
```

제목 리스트를 만드는데 까지는 큰 무리 없이 제목 리스트를 만들 수 있었다. 하지만, 실제 `rotten-tomatoes-scraper` 패키지를 사용하려 할 때는 문제에 부딪혔다. Documentation에 나온대로 for loop을 돌려 각 제목을 MovieScraper 클래스를 사용하려 했다. 하지만 다섯번째 제목을 iterate 할 때 마다 코드가 `NoneTypeError`를 뱉어냈다.

```python
from rotten_tomatoes_scraper.rt_scraper import MovieScraper
import pandas as pd
import numpy as np

moviemaking = pd.DataFrame(columns=['title', 'Score_Rotten', 'Genre'])

for title in titles:
    movie_scraper = MovieScraper(movie_title=title)
    movie_scraper.extract_metadata()
    print(movie_scraper.metadata)
```


```python
{'Score_Rotten': '88', 'Score_Audience': '67', 'Genre': ['Documentary']}
{'Score_Rotten': '76', 'Score_Audience': '67', 'Rating': 'R', 'Genre': ['Drama', 'Comedy']}
{'Score_Rotten': '', 'Score_Audience': '', 'Genre': ['Drama']}
{'Score_Rotten': '50', 'Score_Audience': '56', 'Rating': 'R', 'Genre': ['Horror', 'Mystery&thriller']}
AttributeError: 'NoneType' object has no attribute 'timeout'
```
문제를 일으킨 건 `Emily in Paris`라는 시리즈. 우리는 에러 해결을 위해 documentation에 나와 있는 다른 방법으로 MovieScraper 클래스를 사용해봤다. MovieScraper는 url로도 정보를 스크래핑할 수 있으니 Emily in Paris 로튼 토마토 페이지 url을 사용해봤다. 
```python
movie_url = 'https://www.rottentomatoes.com/tv/emily_in_paris'
movie_scraper = MovieScraper(movie_url=movie_url)
movie_scraper.extract_metadata()
```
`NoneTypeError`가 어디서 나오는지 찾아내려 MovieScraper의 다른 사용법도 활용 해보고 잘 실행되는 시리즈의 웹페이지와 Emily in Paris의 웹페이지의 html 태그들도 비교도 해봤지만, 코드는 여전히 `NoneTypeError`를 뱉어냈다. rotten-tomatoes-scraper의 github을 들여다본 결과 이 패키지는 더 이상 업데이트가 되지 않는다는 것을 발견했다.


![Discontinued](/assets/img/projects/News/discontinuedPackage.png){:.centered width="700" loading="lazy"}

더 이상 지원되지 않는 rotten-tomatoes-scraper 패키지 (Source: https://github.com/pdrm83/rotten_tomatoes_scraper)
{:.figcaption}

프로젝트 시간이 약 두시간 남은 시기에 우리 팀은 두 가지 갈림길에 서 있었다. 
1. 패키지 에러 파악해셔 해결하기
2. 다시 새로운 토픽으로 프로젝트 시작하기

이미 지원이 끝난 패키지 에러를 들춰보는 것보다 새 프로젝트를 시작하는 것이 더 효율적일 것 같아 다시 새로운 주제로 프로젝트를 시작하기로 결정하였다. 

![Battlescar](/assets/img/projects/News/battlescar.png){:.centered width="700" loading="lazy"}

영광의 상처.png
{:.figcaption}

짧은 회의 끝에 우리 팀은 최근 두 대선 후보들과 관련된 뉴스들을 스크래핑 해서 