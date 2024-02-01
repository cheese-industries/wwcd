import requests
import json
import time
import rumps

class RadioApp(rumps.App):
    def __init__(self):
        super(RadioApp, self).__init__("")  # Set an empty string to remove the default "Radio App" label
        self.title = "Fetching..."
        self.update_menu()

    def get_current_song_info(self):
        url = "https://cd929fm.com/wp-json/metaradio/v1/stationnow/?station=3"
        response = requests.get(url)
        data = response.json()
        current_song = data["recent"][0]
        return current_song["artist"].title(), current_song["title"].title()

    def update_menu(self):
        artist, title = self.get_current_song_info()
        self.title = f"Now playing on WWCD: {artist} - {title}"

    @rumps.timer(40)  # Update every 40 seconds
    def update(self, _):
        self.update_menu()

if __name__ == "__main__":
    RadioApp().run()

