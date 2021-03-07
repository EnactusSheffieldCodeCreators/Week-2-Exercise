# Part 1 Breakdown

## Libraries

In this code we used the library `youtube_transcript_api` because it makes it easy to pull down all the information about the video's subtitles that we need. If you don't have this installed and are getting an error when trying to run the code then you need to run `pip install youtube_transcript_api`. We are also using the `re` library but we'll come back to that later.

## Counting Words

```python
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
```

Above we have the function that counts the code in the number of times that one of the words appears in the text. I even added a docstring so you can see what each of the variables do but the lines that are probably the most confusing are likely to be:

```python
pattern = "(?:^|\W)" + word + "(?:^|\W)" # Regex pattern matching
matches = re.findall(pattern, text, re.IGNORECASE)
```

Which is fair if you haven't encountered Regex before. The idea of Regex, in this situation is to make search operations easy to write out in a few lines of code. Here's a quick explainer of what this Regex string does:

Say the word is "um" then the pattern variable stores the string `(?:^|\W)um(?:^|\W)` which looks like utter nonsense. But breaking it down we can see we have these two brackets `(?:^|\W)` which surround the `um` and what these do is to check if the word `um` isn't surrounded by other letters because if it is then we don't want to count it, say the um was part of the word `umpteen`. If you wish to look into Regex more [mozilla have an excellent guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).

The second line in this just tells the re library to give us a list of all the matches in the text string and to ignore case while it does this. We then just count the number of items in this returned list to get the number of matches in a string.

## The Transcript

```python
video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
```

The above line tells us to get the transcript, but what format is it in. Well try printing it if you want to, or you can take a look at the example showing how it comes out in the [documentation](https://pypi.org/project/youtube-transcript-api/). But to summarize it gives us a list of individual captions, each one as a dictionary containing the text, start time and duration of the caption.

This is why we have to loop over the video transcript because it doesn't give us all the text as one giant string.

## That's All

Please come along to the mentoring session if any of this isn't clear or drop us a message on the discord server. Don't worry if it was hard, that was the idea of this week, getting stuck is good because you learn the process of getting un-stuck.