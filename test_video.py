import skvideo.io

videogen = skvideo.io.vreader('./data/driving.mp4')

writer = skvideo.io.FFmpegWriter("./runs/results.mpeg")
for i, frame in enumerate(videogen):
    print("frame:", i)
    #new_frame = imp.pipeline(frame)
    writer.writeFrame(frame)

writer.close()
