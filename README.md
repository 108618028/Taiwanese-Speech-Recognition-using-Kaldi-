# Taiwanese-Speech-Recognition-using-Kaldi-

### 1. Install Kaldi toolkit

	cd ~

	git clone https://github.com/kaldi-asr/kaldi.git

### 2. Prepare the data

	cd ~/kaldi/egs

	mkdir taiwanese

>Copy the documents from formosa

	cp formosa/. taiwanese

	rm taiwanese/s5/steps

	rm taiwanese/s5/utils

	cp wsj/s5/steps taiwanese/s5/

	cp wsj/s5/utils taiwanese/s5/

>Create test and train

	mkdir taiwanese/s5/data/train

	mkdir taiwanese/s5/data/test

>Create the wav folder

	mkdir taiwanese/s5/test/wav

	mkdir taiwanese/s5/train/wav

### 3. Download the dataset

	cd ~/kaldi/egs/taiwanese/s5

	wget dropbox.com/s/l9lczxe2189wfv7/ntut-dl-2020-spring-taiwanese-asr.zip

>Move files to the corresponding path

	cp train/. train/wav

	cp test/. test/wav

### 4. Transform the wav frequency to 16kHz

	run the 22kto16k.sh

### 5. Convert csv to txt

	run the csv2txt.py

### 6. Training

	./run.sh

### 7. Get your result

I got the score of 4.50205 and ranked 20th.





