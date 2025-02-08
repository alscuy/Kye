from TikTokApi import TikTokApi

def stalk_tiktok_profile(username):
    try:
        api = TikTokApi.get_instance()
        user = api.get_user(username)
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None