#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=161967&page=1"
movie_code = 161967
page = 1

result = requests.get(url)
soup = BeautifulSoup(result.content, "html.parser")

page = soup.find("div", {"class": "paging"})
page = page.find("div", {"class": "pg_next"})

print('page:', page)

score_result = soup.find("div", {"class": "score_result"})
score_results = score_result.find_all("li")

"""
TODO

<span id="_filtered_ment_9">
    <span class="_unfold_ment" id="_unfold_ment9">
        <a onclick="unfoldPointMent(this);" href="javascript:void(0);" data-src="네임빨 장기상영으로 겨우 천만 넘은 희대의 개거품영화 ㅎ 평론가들이 극찬한 영화치고 정상적인걸 못 봄. 보잘것 없던 조여정은 졸지에 주연으로 올라서고 시대 잘 탄 못 생긴 박소담 최우식도 몸값 올라서 좋겠네 ㅋ 이제 한국영화는 봉준호 천하가 됐군 그러다 김기덕 처럼 될까 염려됨 ㅋ ">
            네임빨 장기상영으로 겨우 천만 넘은 희대의 개거품영화 ㅎ 평론가들이 극찬한 영화치고 정상적인걸 못 봄. 보잘것 없던 조여정은 졸지에 주연으로 올라서고 시대 잘 탄 못 생긴 박소담 최우식도 몸값 올라서 좋겠네 ㅋ 이제...
        </a>
    </span>
</span>
"""

for score_result in score_results:
    star_score = score_result.find("div", {"class": "star_score"})
    star_score = star_score.find("em")
    score_reple = score_result.find("div", {"class": "score_reple"})
    score_reple = score_reple.find("span", id=lambda x: x and x.startswith('_filtered_ment_'))

    print(star_score.text.strip(), score_reple.text.strip())
