from pyyoutube import Api

# Initialize the API client
api_key = 'AIzaSyAGGv_s75zXa2m9a5j4X7jnw8iy1fHA-Hw'
api = Api(api_key=api_key)

# Function to get video details by video ID
def get_video_details(video_id):
  # Make a request to the YouTube API to get video details
  video_response = api.get_video_by_id(video_id=video_id)
    
  if video_response.items:
    video = video_response.items[0]
    title = video.snippet.title
    author = video.snippet.channelTitle
    link = f"https://www.youtube.com/watch?v={video_id}"
        
    # Print video details
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Link: {link}")
  else:
    print(f"No video found for ID: {video_id}")

if __name__ == "__main__":
  video_id = 'nvVxnxoBu3U'
  get_video_details(video_id)