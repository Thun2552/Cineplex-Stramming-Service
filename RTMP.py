import vlc
import time
from colorama import Fore, Style, init

def print_status(player):
    state = player.get_state()
    state_str = str(state).split('.')[1]
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"{time_str}: Player status: {state_str}")

def main():
    # Initialize colorama
    init()

    # Print program title in blue
    print(Fore.BLUE + "Cineplex Streaming System Version 3.14 Developed By Lemonito Services" + Style.RESET_ALL)

    # Replace the URL with your RTMP stream URL
    rtmp_url = "rtmp://192.168.2.52/Cineplex"

    # Create an instance of VLC player
    instance = vlc.Instance()
    player = instance.media_player_new()

    # Set the media to the RTMP stream URL
    media = instance.media_new(rtmp_url)
    player.set_media(media)

    # Play the stream
    player.play()

    # Set the player to fullscreen
    time.sleep(1)  # Wait a moment for the player to start before setting fullscreen
    player.set_fullscreen(True)

    # Print player status
    print_status(player)

    # Keep the player running and print status updates until the user stops it
    try:
        while True:
            time.sleep(60)  # Log every minute
            print_status(player)
    except KeyboardInterrupt:
        player.stop()
        print("Player stopped.")

if __name__ == "__main__":
    main()
