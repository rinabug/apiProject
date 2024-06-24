import requests

def recent_story():
  max_url = 'https://hacker-news.firebaseio.com/v0/maxitem.json'
  max_id = requests.get(max_url).json()

  item_url = f'https://hacker-news.firebaseio.com/v0/item/{max_id}.json'
  item_details = requests.get(item_url).json()

  if item_details.get('type') == 'story':
    title = item_details.get('title')
    author = item_details.get('by')
    link = item_details.get('url')
        
    # Print out the story details
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Link: {link}")
  else:
    print("The most recent item is not a story.")

if __name__ == "__main__":
  recent_story()