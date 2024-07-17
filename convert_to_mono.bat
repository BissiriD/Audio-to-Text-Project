@echo off
setlocal enabledelayedexpansion

:: Define the base directory containing the playlists
set "base_dir=Path to audio files"

:: Define the playlists
set "playlists=playlist_1 playlist_2 playlist_3"

:: Iterate over each playlist directory
for %%p in (%playlists%) do (
    set "input_dir=!base_dir!\%%p"
    set "output_dir=!input_dir!\mono"

    :: Create output directory if it doesn't exist
    if not exist "!output_dir!" mkdir "!output_dir!"

    :: Convert each WAV file from stereo to mono
    for %%f in ("!input_dir!\*.wav") do (
        ffmpeg -i "%%f" -ac 1 "!output_dir!\%%~nf_mono.wav"
    )
)

echo Conversion complete!
pause

