import streamlit as st
import instaloader

def get_instagram_info(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return profile
    except instaloader.exceptions.ProfileNotExistsException:
        return None

def main():
    st.title("Instagram User Info")

    user_message = st.text_input("Enter Instagram Username:", "")

    if st.button("Get Info"):
        if user_message:
            profile_info = get_instagram_info(user_message)
            if profile_info:
                bot_response = (
                    f"{profile_info.full_name} (@{profile_info.username}) is an Instagram user with {profile_info.followers} followers, "
                    f"{profile_info.followees} following, and {profile_info.mediacount} posts. "
                    f"Their bio: {profile_info.biography}"
                )
                st.text_area("Myly:", bot_response, key="bot_response", height=300)
            else:
                st.warning("Profile not found. Please enter a valid Instagram username.")
        else:
            st.warning("Please enter an Instagram username.")

if __name__ == "__main__":
    main()
