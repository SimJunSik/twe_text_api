import tweepy
import re
from retrying import retry

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def tweepy_function() :
    # 트위터 앱의 Keys and Access Tokens 탭 참조(자신의 설정 값을 넣어준다)
    consumer_key = "kuqHstNLfBBCAUIuRM0q3a4Fh"
    consumer_secret = "EEJUvMNRZ6H4CHH4DPtqee89O8E1QcGdcHRKQLX4uZels9RQVU"

    # 1. 인증요청(1차) : 개인 앱 정보
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    access_token = "1096344368963670017-5Y4xbveKfTqZKWvbSn2HU7pqi0kN7O"
    access_token_secret= "GnFqNG3UQUgAlyVKavoa1jVF8fJjDjDxweOSJemiYh5ZF"

    # 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
    auth.set_access_token(access_token, access_token_secret)

    # 3. twitter API 생성
    api = tweepy.API(auth)

    """
    Tweets containing all words in any position (“Twitter” and “search”)  
    Tweets containing exact phrases (“Twitter search”)
    Tweets containing any of the words (“Twitter” or “search”)
    Tweets excluding specific words (“Twitter” but not “search”)
    Tweets with a specific hashtag (#twitter)
    Tweets in a specific language (written in English)
    
    
    연산자	아래와 같은 트윗을 검색합니다...
    트위터 검색	"트위터"와 "검색"을 모두 포함. 검색의 기본 설정
    "한정 판매"	"한정 판매"라는 문구를 그대로 포함
    사랑 OR 증오	"사랑" 또는 "증오" 중 한 단어를 포함
    검색 -고급	"검색"은 포함하지만 "고급"은 포함하지 않음
    #twitter	해시태그 "twitter"를 포함
    from:twitter_kr	"twitter_kr"님이 작성
    to:twitter_kr	"twitter_kr"님에게 보냄
    "한정 판매" near:서울	"한정 판매"라는 문구를 포함하며 서울 주변에서 작성
    near:NYC within:15mi	"NYC" 인근 15마일 내에서 작성
    트위터 since:2010-12-27	"2010-12-27"(년-월-일)이후 "트위터"를 포함
    트위터 until:2010-12-27	"2010-12-27" 이전 "트위터"를 포함
    영화 -공포 :)	"영화"를 포함하나 "공포"는 포함하지 않고, 긍정적인 분위기
    방송 :(	"방송"을 포함하며 부정적인 분위기
    교통 ?	"교통"을 포함하며 의문형
    웃긴 filter:links	"웃긴"을 포함하며 URL 링크가 있음
    뉴스 source:twitterfeed	"뉴스"를 포함하고 "TwitterFeed"로 작성됨
    """

    keyword = "전여친"
    cursor = tweepy.Cursor(api.search,
                           q=keyword,
                           since='2018-01-01',
                           count=1000,
                           include_entities=True)

    result = []
    for i, tweet in enumerate(cursor.items(15000)):
        tmp = re.sub('[^0-9가-힣 ]+', '', tweet.text)
        if tmp not in result :
            result.append(tmp)
        print("{}: {}".format(i, tmp))

    filename = "./cates/twitter_" + keyword.replace(" ","") + ".txt"
    wfile = open(filename, mode='w', encoding='utf-8')
    for text in result :
        wfile.write(text + '\n')
    wfile.close()

tweepy_function()