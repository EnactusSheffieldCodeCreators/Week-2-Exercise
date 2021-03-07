# Solution to part 1.

# ==== Imports =====
from youtube_transcript_api import YouTubeTranscriptApi # pip install youtube_transcript_api
import re

# ===== Constants =====
VIDEO_ID = "alTRvtmWi7k"
SEARCH_WORDS = ["um", "uh"]

def count_words(words, text):
    """
    Counts the number of times each of the words appears in the text.

    :words: array of words to count
    :text: string to count words in
    :returns: number of times any of the words were detected in the text
    """
    count = 0
    for word in words:
        pattern = "(?:^|\W)" + word + "(?:^|\W)" # Regex pattern matching
        matches = re.findall(pattern, text, re.IGNORECASE)
        count += len(matches)
    return count
    

video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
um_uh_counter = 0

for section in video_transcript: # Transcript is separated into sections.
    um_uh_counter += count_words(SEARCH_WORDS, section['text'])

print("Counted {} \"ums\" or \"uhs\"".format(um_uh_counter))