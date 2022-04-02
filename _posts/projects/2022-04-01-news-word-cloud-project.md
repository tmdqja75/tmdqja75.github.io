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

PlayData 과정에서 첫 미니 프로젝트를 하게 되었다. 주제는 자유주제.우리 팀은 원래 Rotten Tomato에서 각 Netflix 시리즈들의 장르와 Tomato Score들을 크롤링해와서 장르별 평균 별점을 시각화하려는 프로젝트를 하려고 했다. 먼저 그 프로젝트 시도 과정은 이러했다.

먼저 그냥 크롤링을 시작하기 전, 과정을 좀 더 쉽게 해줄 수 있는 python 라이브러리가 있을지 구글링을 먼저 해봤다. 구글링 결과 관련 파이썬 라이브러리를 쉽게 찾을 수 있었다. pip로 설치할 수 있는 [rotten-tomatoes-scraper](https://pypi.org/project/rotten-tomatoes-scraper/)라는 파이썬 패키지를 찾을 수 있있다. Documentation을 읽어본 결과 패키지 중 MovieScraper라는 클래스를 우리 프로젝트에 유용히 쓸 수 있을것 같았다. 이 클래스는 원하는 영화나 TV쇼 제목을 파라미터로 넣어주면, 결과값으로 로튼 토마토 지수, 일반 평정 지수, 그리고 장르를 dictionary 형태로 리턴해줄 수 있는 class였다.

```python
from rotten_tomatoes_scraper.rt_scraper import MovieScraper

movie_url = 'https://www.rottentomatoes.com/m/marriage_story_2019'
movie_scraper = MovieScraper(movie_url=movie_url)
movie_scraper.extract_metadata()

print(movie_scraper.metadata)
>>> {'Score_Rotten': '94', 'Score_Audience': '85', 'Genre': ['comedy', 'drama']}
```


