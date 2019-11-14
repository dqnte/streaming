#THE PLAN

The problem is twofold. First I need to set up the server that contains a manifest file and a movie file in different formats. This can probably be done using DASH and ffmpeg (1). From what I understand, this is only done once. The server file system is set up.

The second part of the problem is the client then asking for the right file given that there is a manifest. I need to generate a "media presentation description" which tells the server the quality of the connection. That way the server will know what file size to send back.

---

New plan, server is them same. On the client side, I want to be the one to choose. So the client will have to figure out its own latency speed. A naive way to do this would be using a timestap, to see how fast it took the video to download. Each server response will then need a timestamp. I can then calcualte bit rate by kb/(t2-t1).

I would also need to create blob files on the client for each chunk I get, and have a video tag point to these chunks for a specific amount of time. This can be done using some blob stuff (2).

#GOALS

Back End

    a. be able to split a video file into different sized files

        - [ ] figure out ffmpeg

        - [ ] do it myself (?)

    b. get a specific chunk from an mov file and send it as binary

    c. figure out what files to send when

Front End

    a. be able to measure connection speed

        - [x] send an image file to a blob

        - [ ] send a video file to a blob url

        - [x] send a file with an allocated size and a time stamp, then measure how long it took to load

        - [ ] conditionally point to a given image depending on connection

    b. play a video

        - [ ] be able to point a video file at a blob and have it play

        - [ ] be able to switch between blobs depending on where the video is being played

#INFO

##Dash.js Main Docs:

- Github: https://github.com/Dash-Industry-Forum/dash.js/

- Explanation: https://www.encoding.com/mpeg-dash/

- http://cdn.dashjs.org/latest/jsdoc/index.html

  The actual media player -> http://cdn.dashjs.org/latest/jsdoc/streaming_MediaPlayer.js.html

- (1) https://developer.mozilla.org/en-US/docs/Web/HTML/DASH_Adaptive_Streaming_for_HTML_5_Video
  Need to find some kind of player switching algorithm to choose which file to read

Netflix backend video -> https://www.youtube.com/watch?v=psQzyFfsUGU

Dream finish line -> https://www.npmjs.com/package/node-media-server

##God Bless Mozilla

- https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Setting_up_adaptive_streaming_media_sources

- live streaming stuff: https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Live_streaming_web_audio_and_video

- (2) Pointing a video tag at a blob: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

##FFMPG

- Possible way to split files into chunks -> https://unix.stackexchange.com/questions/1670/how-can-i-use-ffmpeg-to-split-mpeg-video-into-10-minute-chunks
