def decrypt_story():
    encryptedStory = CiphertextMessage(get_story_string())
    return encryptedStory.decrypt_message()