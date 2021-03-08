# ===== Imports =====
from youtube_transcript_api import YouTubeTranscriptApi
import re

# ===== Constants =====
VIDEO_ID = "alTRvtmWi7k"
TEXT_SEPERATOR = " "
PHRASE_LENGTHS = range(2, 7)

def transcript_to_word_list(transcript):
    """
    Converts a transcript object into a list of words.

    :transcript: transcript from youtube_transcript_api
    :returns: list of words
    """
    captions = [x["text"] for x in transcript]
    return TEXT_SEPERATOR.join(captions).split(TEXT_SEPERATOR)

def identify_phrases(words, length):
    word_count = len(words)
    phrases = []

    for i in range(word_count-length):
        phrase_words = []
        for j in range(length):
            phrase_words.append(words[i+j])
        phrases.append(TEXT_SEPERATOR.join(phrase_words))

    return phrases

def count_phrase_appearances(text, phrase):
    pattern = r"(?:^|\W)" + phrase + r"(?:^|\W)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

    word_list = transcript_to_word_list(video_transcript)
    text = " ".join(word_list)

    catchphrases = []
    for length in PHRASE_LENGTHS:
        catchphrases.extend(identify_phrases(word_list, length))

    most_frequent = []
    highest_frequency = 0
    for catchphrase in catchphrases:
        catchphrase_count = count_phrase_appearances(text, catchphrase)
        if catchphrase_count == highest_frequency:
            if catchphrase not in most_frequent:
                most_frequent.append(catchphrase)
        elif catchphrase_count > highest_frequency:
            highest_frequency = catchphrase_count
            most_frequent = [catchphrase]

    print(most_frequent)
    print(highest_frequency)

    
    
