py .py;ffmpeg -stream_loop -1 -f concat -i .txt -f flv -q 7 -v 0 -stats rtmp://a.rtmp.youtube.com/live2/jcmk-zhef-7ekc-z9sq-7fp5