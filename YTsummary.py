from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

video_id = "mvD67mzyfBU"

try:
    # Fetch transcript in preferred languages
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en", "hi"])
    
    # print(transcript)
    text=" ".join([token["text"] for token in transcript])
    # print(text)


except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("No transcript found for this video in the requested languages.")
except Exception as e:
    print(f"An error occurred: {e}")
