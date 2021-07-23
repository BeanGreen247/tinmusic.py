tinmusic.py
===
|name|version|state|
|:---:|:---:|:---:|
|tinmusic.py|devduild_alpha_0.0.1|testing|

States explained

* stable - fully working release
* unstable - somewhat working, with a few bugs
* testing - developing and testing new features

Screen

![](screen.png)

Dependencies
```bash
sudo apt install python3-tk python3-dev python3
python3 -m pip install pygame
```
To run
```bash
python3 tinmusic.py
```

Features

Current
* play and pause
* volume control
* play files from directory
* directory navigation

Supported files (more will not be added)
* wav

### Bugs
* Emotes cause app to crash if present in file name
### filename changing scripts
Go into the directory with your music files and run one of the following depending on the file format. It will convert the files to WAVs in a directory called Converted.

mp3
```bash
bash ffmpeg_mp3_to_wav.sh
```
```bash
mkdir Converted
for f in *.mp3; do ffmpeg -i "$f" -acodec pcm_s16le -ac 2 -ar 44100 "${f%}.wav"; done
mv *.wav Converted/
cd Converted/
for file in ./*.wav
do
  infile=`echo "${file:2}"|sed  \
         -e 's|"\"|"\\"|g' \
         -e 's| |\ |g' -e 's|!|\!|g' \
         -e 's|@|\@|g' -e 's|*|\*|g' \
         -e 's|&|\&|g' -e 's|]|\]|g' \
         -e 's|}|\}|g' -e 's|"|\"|g' \
         -e 's|,|\,|g' -e 's|?|\?|g' \
         -e 's|=|\=|g'  `
  outfile=`echo "${file:2}"|sed -e 's|[^A-Za-z0-9._-]|_|g'`
  mv "$infile" ${outfile} &
done
cd ..
```
flac
```bash
bash ffmpeg_flac_to_wav.sh
```
```bash
mkdir Converted
for f in *.flac; do ffmpeg -i "$f" -acodec pcm_s16le -ac 2 -ar 44100 "${f%}.wav"; done
mv *.wav Converted/
cd Converted/
for file in ./*.wav
do
  infile=`echo "${file:2}"|sed  \
         -e 's|"\"|"\\"|g' \
         -e 's| |\ |g' -e 's|!|\!|g' \
         -e 's|@|\@|g' -e 's|*|\*|g' \
         -e 's|&|\&|g' -e 's|]|\]|g' \
         -e 's|}|\}|g' -e 's|"|\"|g' \
         -e 's|,|\,|g' -e 's|?|\?|g' \
         -e 's|=|\=|g'  `
  outfile=`echo "${file:2}"|sed -e 's|[^A-Za-z0-9._-]|_|g'`
  mv "$infile" ${outfile} &
done
cd ..
```
aac
```bash
bash ffmpeg_aac_to_wav.sh
```
```bash
mkdir Converted
for f in *.aac; do ffmpeg -i "$f" -acodec pcm_s16le -ac 2 -ar 44100 "${f%}.wav"; done
mv *.wav Converted/
cd Converted/
for file in ./*.wav
do
  infile=`echo "${file:2}"|sed  \
         -e 's|"\"|"\\"|g' \
         -e 's| |\ |g' -e 's|!|\!|g' \
         -e 's|@|\@|g' -e 's|*|\*|g' \
         -e 's|&|\&|g' -e 's|]|\]|g' \
         -e 's|}|\}|g' -e 's|"|\"|g' \
         -e 's|,|\,|g' -e 's|?|\?|g' \
         -e 's|=|\=|g'  `
  outfile=`echo "${file:2}"|sed -e 's|[^A-Za-z0-9._-]|_|g'`
  mv "$infile" ${outfile} &
done
cd ..
```
