from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

res=YouTubeTranscriptApi.get_transcript(video_id="mvD67mzyfBU",languages=("en","hi"))

formatter=TextFormatter()

text=formatter.format_transcript(transcript=res)
print(text)