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
    """
    Identifies all the possible phrases from a section of text.

    :words: a list of all the words (in order) that make up the text.
    :length: length of the phrases we're looking for.
    """
    word_count = len(words)
    phrases = []

    # Iterate over all x length sequences in the text.
    for i in range(word_count-length):
        phrase_words = []
        # Collect all the words from the phrase.
        for j in range(length):
            phrase_words.append(words[i+j])
        
        # Join all the words into a phrase.
        phrases.append(TEXT_SEPERATOR.join(phrase_words))

    return phrases

def count_phrase_appearances(text, phrase):
    """
    Counts the number of times a phrase appears in a text.

    :text: string to search within
    :phrase: phrase to search for
    :returns: number of matches
    """
    pattern = r"(?:^|\W)" + re.escape(phrase) + r"(?:^|\W)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

    word_list = transcript_to_word_list(video_transcript)
    text = " ".join(word_list)

    # Store all the potential phrases.
    phrases = []
    for length in PHRASE_LENGTHS:
        phrases.extend(identify_phrases(word_list, length))

    # Filter out the most common phrases.
    most_frequent = []
    highest_frequency = 0
    for phrase in phrases:
        phrase_count = count_phrase_appearances(text, phrase)
        if phrase_count == highest_frequency:
            if phrase not in most_frequent:
                most_frequent.append(phrase)
        elif phrase_count > highest_frequency:
            highest_frequency = phrase_count
            most_frequent = [phrase]

    print(most_frequent)
    print(highest_frequency)

    
    
