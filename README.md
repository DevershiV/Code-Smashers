# Code-Smashers
Team Code Smashers project in AIML domain for Sainya Ranakshetram 2.0

Problem Description: Artificial Intelligence and Machine Learning.

1. The human ear can register sound generated in the frequency range 20Hz to
20 KHz (ideally, this reduces with age and other parameters), however, audio when
transmitted over the air using Radio Frequency (RF) transmitters is compressed and
restricted to a frequency range of 300 Hz to 3.4 KHz. This is done to keep the
message intelligence intact and at the same time ensuring carrier and sampling
limitations are met. This reduced audio range with vocal phonemes being distorted
coupled with channel noise (mush, scatter, etc) poses a problem while decoding
such signals and using existing tools for voice to text conversion. The use of mixed
dialect and slangs further pushes this simple benign problem statement into the
realms of AI and ML.
2. The challenge aims to develop a software-based tool that is able to ingest
radio audio recordings (non HiFi) in common format of (.wav, FLAC, MP3 (high bit
rate) etc.) containing information in a mix of English and Hindi (Hinglish) with limited
use of local slangs and create an extract transcript information output in textual
format. This problem intrinsically contains the task of cleaning of raw audio signals,
shaping of signals and creating algo specific data required by the NLP engine.
Desired output is a text file in English with gaps and pauses incorporated providing a
high degree of legibility and possible use as an input for other software translation
tools. Data set required to train the model developed are available online and some
data will be provided by the organizers.

Initial Requirements:

1.	Check and collect dataset (from external sources if required)
2.	Radio signal data cleaning techniques (High distortion and noise might be present)
3.	Check if radio signal data decompression is required (as it is compressed audio)
4.	Language detector model to detect Hindi
5.	Sentence arrangement model to create meaningful sentence in English
6.	Adding proper commas and full stop to provide a high degree of legibility
7.	Adding the data to a text file
8.	UI component with upload and download buttons
9.	Deploy the components
Accepted extensions of files are .rar, .zip, and gz.tar, solution size will be maximum 500MB
