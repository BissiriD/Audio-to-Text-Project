import os

def create_results_dir_with_txt_files(audio_dir, results_dir):
    os.makedirs(results_dir, exist_ok=True)

    for playlist in os.listdir(audio_dir):
        playlist_path = os.path.join(audio_dir, playlist)

        if os.path.isdir(playlist_path):
            results_playlist_path = os.path.join(results_dir, playlist)
            os.makedirs(results_playlist_path, exist_ok=True)
            print(f"Created directory: {results_playlist_path}")

            # Check if 'mono' directory exists inside the playlist directory
            mono_path = os.path.join(playlist_path, 'mono')
            if os.path.isdir(mono_path):
                for audio_file in os.listdir(mono_path):
                    print(f"Checking file: {audio_file}")  # Debugging line
                    if audio_file.endswith(".wav"):  # Check if the file is a WAV file
                        audio_file_name = os.path.splitext(audio_file)[0]  # Get the file name without extension
                        empty_txt_file_path = os.path.join(results_playlist_path, f'{audio_file_name}.txt')
                        with open(empty_txt_file_path, 'w') as f:
                            pass  # Create an empty file
                        print(f"Created empty file: {empty_txt_file_path}")
                    else:
                        print(f"Skipped file: {audio_file}")  # Debugging line

if __name__ == "__main__":
    audio_directory = "Path to Audio Directory"
    results_directory = "Path to Results Directory"
    create_results_dir_with_txt_files(audio_directory, results_directory)

