for i in {1..3119}
do
	sox $i.wav -r 16000 -e signed-integer -b 16 out_$i.wav
done
