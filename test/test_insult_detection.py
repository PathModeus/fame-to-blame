from src.insult_detection.insult_detection import detect_insult_tweet
tweet1={"Texte":'shit! you are a hot chick' }
tweet2={"Texte": 'Hot ! blabla chick'}
tweet3={"Texte": 'Shit you SUCK'}
tweet4={"Texte": 'Shit he sucks'}

def test_detect_insult_tweet():
    assert detect_insult_tweet(tweet1)==['shit','hot chick']
    assert detect_insult_tweet(tweet2)==[]

print(detect_insult_tweet(tweet1))
test_detect_insult_tweet()
