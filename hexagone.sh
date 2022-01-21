rm hgone*
./hexagone.py
#convert -delay 10 -loop 0 *.eps animated.gif
#convert animated.gif -coalesce -background white -alpha background -alpha off -layers optimize animated2.gif
for f in `ls *.eps`; do
        convert -density 100 $f -flatten ${f%.*}.png;
done

#mogrify -format png -depth 8 -alpha off -density 600 -resample 150 *.eps
ffmpeg -framerate 10 -pattern_type glob -i '*.png' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"  -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
