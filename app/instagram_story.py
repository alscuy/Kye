from instaloader import Instaloader, Profile

def stalk_instagram_story(username):
    try:
        L = Instaloader()
        profile = Profile.from_username(L.context, username)
        stories = list(profile.get_stories())
        return stories
    except Exception as e:
        print(f"Error: {e}")
        return None