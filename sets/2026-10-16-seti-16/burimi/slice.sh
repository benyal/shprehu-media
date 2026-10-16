#!/bin/bash
# përdorimi: slice.sh pano-f.png f-fqinji
FF=$(python3 -c "import imageio_ffmpeg as f; print(f.get_ffmpeg_exe())")
P=$1; N=$2; OUT=${3:-..}
for i in 0 1 2 3 4 5; do $FF -loglevel error -i $P -vf "crop=1080:1920:$((i*1080)):0" -y $OUT/$N-$((i+1)).png; done
for i in 1 2 3 4 5 6; do $FF -loglevel error -i $OUT/$N-$i.png -vf scale=360:-1 -y /tmp/th-$N-$i.png; done
$FF -loglevel error -i /tmp/th-$N-1.png -i /tmp/th-$N-2.png -i /tmp/th-$N-3.png -i /tmp/th-$N-4.png -i /tmp/th-$N-5.png -i /tmp/th-$N-6.png -filter_complex hstack=inputs=6 -y prev-$N.png
