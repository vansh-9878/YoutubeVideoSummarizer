from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from summary import summaryText
import re

link="https://www.youtube.com/watch?v=aKq8bkY5eTU"

def getText(link):
    
    # video_id = "mvD67mzyfBU"
    video_id=re.search("v=(.*)",link)
    video_id=video_id.group(1)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en", "hi"])
        
        text=" ".join([token["text"] for token in transcript])
        # print(text)
        print(summaryText(text))

    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("No transcript found for this video in the requested languages.")
    except Exception as e:
        print(f"An error occurred: {e}")


getText(link)