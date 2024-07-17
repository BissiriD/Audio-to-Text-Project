@echo off
setlocal enabledelayedexpansion

:: Define the directory containing the downloaded WAV files
set "input_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_1"
set "output_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_1\\mono"

:: Create output directory if it doesn't exist
if not exist "!output_dir!" mkdir "!output_dir!"

:: Convert each WAV file from stereo to mono
for %%f in ("!input_dir!\*.wav") do (
    ffmpeg -i "%%f" -ac 1 "!output_dir!\%%~nf_mono.wav"
)

:: Repeat for other playlists

@echo off
setlocal enabledelayedexpansion

:: Define the directory containing the downloaded WAV files
set "input_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_2"
set "output_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_2\\mono"

:: Create output directory if it doesn't exist
if not exist "!output_dir!" mkdir "!output_dir!"

:: Convert each WAV file from stereo to mono
for %%f in ("!input_dir!\*.wav") do (
    ffmpeg -i "%%f" -ac 1 "!output_dir!\%%~nf_mono.wav"
)


@echo off
setlocal enabledelayedexpansion

:: Define the directory containing the downloaded WAV files
set "input_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_3"
set "output_dir=C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\videos\\playlist_3\\mono"

:: Create output directory if it doesn't exist
if not exist "!output_dir!" mkdir "!output_dir!"

:: Convert each WAV file from stereo to mono
for %%f in ("!input_dir!\*.wav") do (
    ffmpeg -i "%%f" -ac 1 "!output_dir!\%%~nf_mono.wav"
)
