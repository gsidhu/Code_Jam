def audio_phil(filename):
    file = open(filename)
    out = open("output.txt", 'w+')
    testcases = int(file.readline())
    for i in range(0, testcases):
        M = int(file.readline())
        songs = []
        for j in range(0, M):
            songs.append(file.readline().strip('\n'))
        for j in range(0, M):
            for k in range(1, M):
                songs[j] 
