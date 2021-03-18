i = 1
while i < 10:
    j = 1
    while j < 10:
        k = 1
        while k < 10:
            print("%d * %d * %d = %3d" % (k, j, i, k * j * i), end="\t\t")
            k += 1
        print()
        j += 1
    print()
    print()
    i += 1

"""
1 * 1 * 1 =   1         2 * 1 * 1 =   2         3 * 1 * 1 =   3         4 * 1 * 1 =   4         5 * 1 * 1 =   5         6 * 1 * 1 =   6         7 * 1 * 1 =   7         8 * 1 * 1 =   8         9 * 1 * 1 =   9
1 * 2 * 1 =   2         2 * 2 * 1 =   4         3 * 2 * 1 =   6         4 * 2 * 1 =   8         5 * 2 * 1 =  10         6 * 2 * 1 =  12         7 * 2 * 1 =  14         8 * 2 * 1 =  16         9 * 2 * 1 =  18
1 * 3 * 1 =   3         2 * 3 * 1 =   6         3 * 3 * 1 =   9         4 * 3 * 1 =  12         5 * 3 * 1 =  15         6 * 3 * 1 =  18         7 * 3 * 1 =  21         8 * 3 * 1 =  24         9 * 3 * 1 =  27
1 * 4 * 1 =   4         2 * 4 * 1 =   8         3 * 4 * 1 =  12         4 * 4 * 1 =  16         5 * 4 * 1 =  20         6 * 4 * 1 =  24         7 * 4 * 1 =  28         8 * 4 * 1 =  32         9 * 4 * 1 =  36
1 * 5 * 1 =   5         2 * 5 * 1 =  10         3 * 5 * 1 =  15         4 * 5 * 1 =  20         5 * 5 * 1 =  25         6 * 5 * 1 =  30         7 * 5 * 1 =  35         8 * 5 * 1 =  40         9 * 5 * 1 =  45
1 * 6 * 1 =   6         2 * 6 * 1 =  12         3 * 6 * 1 =  18         4 * 6 * 1 =  24         5 * 6 * 1 =  30         6 * 6 * 1 =  36         7 * 6 * 1 =  42         8 * 6 * 1 =  48         9 * 6 * 1 =  54
1 * 7 * 1 =   7         2 * 7 * 1 =  14         3 * 7 * 1 =  21         4 * 7 * 1 =  28         5 * 7 * 1 =  35         6 * 7 * 1 =  42         7 * 7 * 1 =  49         8 * 7 * 1 =  56         9 * 7 * 1 =  63
1 * 8 * 1 =   8         2 * 8 * 1 =  16         3 * 8 * 1 =  24         4 * 8 * 1 =  32         5 * 8 * 1 =  40         6 * 8 * 1 =  48         7 * 8 * 1 =  56         8 * 8 * 1 =  64         9 * 8 * 1 =  72
1 * 9 * 1 =   9         2 * 9 * 1 =  18         3 * 9 * 1 =  27         4 * 9 * 1 =  36         5 * 9 * 1 =  45         6 * 9 * 1 =  54         7 * 9 * 1 =  63         8 * 9 * 1 =  72         9 * 9 * 1 =  81


1 * 1 * 2 =   2         2 * 1 * 2 =   4         3 * 1 * 2 =   6         4 * 1 * 2 =   8         5 * 1 * 2 =  10         6 * 1 * 2 =  12         7 * 1 * 2 =  14         8 * 1 * 2 =  16         9 * 1 * 2 =  18
1 * 2 * 2 =   4         2 * 2 * 2 =   8         3 * 2 * 2 =  12         4 * 2 * 2 =  16         5 * 2 * 2 =  20         6 * 2 * 2 =  24         7 * 2 * 2 =  28         8 * 2 * 2 =  32         9 * 2 * 2 =  36
1 * 3 * 2 =   6         2 * 3 * 2 =  12         3 * 3 * 2 =  18         4 * 3 * 2 =  24         5 * 3 * 2 =  30         6 * 3 * 2 =  36         7 * 3 * 2 =  42         8 * 3 * 2 =  48         9 * 3 * 2 =  54
1 * 4 * 2 =   8         2 * 4 * 2 =  16         3 * 4 * 2 =  24         4 * 4 * 2 =  32         5 * 4 * 2 =  40         6 * 4 * 2 =  48         7 * 4 * 2 =  56         8 * 4 * 2 =  64         9 * 4 * 2 =  72
1 * 5 * 2 =  10         2 * 5 * 2 =  20         3 * 5 * 2 =  30         4 * 5 * 2 =  40         5 * 5 * 2 =  50         6 * 5 * 2 =  60         7 * 5 * 2 =  70         8 * 5 * 2 =  80         9 * 5 * 2 =  90
1 * 6 * 2 =  12         2 * 6 * 2 =  24         3 * 6 * 2 =  36         4 * 6 * 2 =  48         5 * 6 * 2 =  60         6 * 6 * 2 =  72         7 * 6 * 2 =  84         8 * 6 * 2 =  96         9 * 6 * 2 = 108
1 * 7 * 2 =  14         2 * 7 * 2 =  28         3 * 7 * 2 =  42         4 * 7 * 2 =  56         5 * 7 * 2 =  70         6 * 7 * 2 =  84         7 * 7 * 2 =  98         8 * 7 * 2 = 112         9 * 7 * 2 = 126
1 * 8 * 2 =  16         2 * 8 * 2 =  32         3 * 8 * 2 =  48         4 * 8 * 2 =  64         5 * 8 * 2 =  80         6 * 8 * 2 =  96         7 * 8 * 2 = 112         8 * 8 * 2 = 128         9 * 8 * 2 = 144
1 * 9 * 2 =  18         2 * 9 * 2 =  36         3 * 9 * 2 =  54         4 * 9 * 2 =  72         5 * 9 * 2 =  90         6 * 9 * 2 = 108         7 * 9 * 2 = 126         8 * 9 * 2 = 144         9 * 9 * 2 = 162


1 * 1 * 3 =   3         2 * 1 * 3 =   6         3 * 1 * 3 =   9         4 * 1 * 3 =  12         5 * 1 * 3 =  15         6 * 1 * 3 =  18         7 * 1 * 3 =  21         8 * 1 * 3 =  24         9 * 1 * 3 =  27
1 * 2 * 3 =   6         2 * 2 * 3 =  12         3 * 2 * 3 =  18         4 * 2 * 3 =  24         5 * 2 * 3 =  30         6 * 2 * 3 =  36         7 * 2 * 3 =  42         8 * 2 * 3 =  48         9 * 2 * 3 =  54
1 * 3 * 3 =   9         2 * 3 * 3 =  18         3 * 3 * 3 =  27         4 * 3 * 3 =  36         5 * 3 * 3 =  45         6 * 3 * 3 =  54         7 * 3 * 3 =  63         8 * 3 * 3 =  72         9 * 3 * 3 =  81
1 * 4 * 3 =  12         2 * 4 * 3 =  24         3 * 4 * 3 =  36         4 * 4 * 3 =  48         5 * 4 * 3 =  60         6 * 4 * 3 =  72         7 * 4 * 3 =  84         8 * 4 * 3 =  96         9 * 4 * 3 = 108
1 * 5 * 3 =  15         2 * 5 * 3 =  30         3 * 5 * 3 =  45         4 * 5 * 3 =  60         5 * 5 * 3 =  75         6 * 5 * 3 =  90         7 * 5 * 3 = 105         8 * 5 * 3 = 120         9 * 5 * 3 = 135
1 * 6 * 3 =  18         2 * 6 * 3 =  36         3 * 6 * 3 =  54         4 * 6 * 3 =  72         5 * 6 * 3 =  90         6 * 6 * 3 = 108         7 * 6 * 3 = 126         8 * 6 * 3 = 144         9 * 6 * 3 = 162
1 * 7 * 3 =  21         2 * 7 * 3 =  42         3 * 7 * 3 =  63         4 * 7 * 3 =  84         5 * 7 * 3 = 105         6 * 7 * 3 = 126         7 * 7 * 3 = 147         8 * 7 * 3 = 168         9 * 7 * 3 = 189
1 * 8 * 3 =  24         2 * 8 * 3 =  48         3 * 8 * 3 =  72         4 * 8 * 3 =  96         5 * 8 * 3 = 120         6 * 8 * 3 = 144         7 * 8 * 3 = 168         8 * 8 * 3 = 192         9 * 8 * 3 = 216
1 * 9 * 3 =  27         2 * 9 * 3 =  54         3 * 9 * 3 =  81         4 * 9 * 3 = 108         5 * 9 * 3 = 135         6 * 9 * 3 = 162         7 * 9 * 3 = 189         8 * 9 * 3 = 216         9 * 9 * 3 = 243


1 * 1 * 4 =   4         2 * 1 * 4 =   8         3 * 1 * 4 =  12         4 * 1 * 4 =  16         5 * 1 * 4 =  20         6 * 1 * 4 =  24         7 * 1 * 4 =  28         8 * 1 * 4 =  32         9 * 1 * 4 =  36
1 * 2 * 4 =   8         2 * 2 * 4 =  16         3 * 2 * 4 =  24         4 * 2 * 4 =  32         5 * 2 * 4 =  40         6 * 2 * 4 =  48         7 * 2 * 4 =  56         8 * 2 * 4 =  64         9 * 2 * 4 =  72
1 * 3 * 4 =  12         2 * 3 * 4 =  24         3 * 3 * 4 =  36         4 * 3 * 4 =  48         5 * 3 * 4 =  60         6 * 3 * 4 =  72         7 * 3 * 4 =  84         8 * 3 * 4 =  96         9 * 3 * 4 = 108
1 * 4 * 4 =  16         2 * 4 * 4 =  32         3 * 4 * 4 =  48         4 * 4 * 4 =  64         5 * 4 * 4 =  80         6 * 4 * 4 =  96         7 * 4 * 4 = 112         8 * 4 * 4 = 128         9 * 4 * 4 = 144
1 * 5 * 4 =  20         2 * 5 * 4 =  40         3 * 5 * 4 =  60         4 * 5 * 4 =  80         5 * 5 * 4 = 100         6 * 5 * 4 = 120         7 * 5 * 4 = 140         8 * 5 * 4 = 160         9 * 5 * 4 = 180
1 * 6 * 4 =  24         2 * 6 * 4 =  48         3 * 6 * 4 =  72         4 * 6 * 4 =  96         5 * 6 * 4 = 120         6 * 6 * 4 = 144         7 * 6 * 4 = 168         8 * 6 * 4 = 192         9 * 6 * 4 = 216
1 * 7 * 4 =  28         2 * 7 * 4 =  56         3 * 7 * 4 =  84         4 * 7 * 4 = 112         5 * 7 * 4 = 140         6 * 7 * 4 = 168         7 * 7 * 4 = 196         8 * 7 * 4 = 224         9 * 7 * 4 = 252
1 * 8 * 4 =  32         2 * 8 * 4 =  64         3 * 8 * 4 =  96         4 * 8 * 4 = 128         5 * 8 * 4 = 160         6 * 8 * 4 = 192         7 * 8 * 4 = 224         8 * 8 * 4 = 256         9 * 8 * 4 = 288
1 * 9 * 4 =  36         2 * 9 * 4 =  72         3 * 9 * 4 = 108         4 * 9 * 4 = 144         5 * 9 * 4 = 180         6 * 9 * 4 = 216         7 * 9 * 4 = 252         8 * 9 * 4 = 288         9 * 9 * 4 = 324


1 * 1 * 5 =   5         2 * 1 * 5 =  10         3 * 1 * 5 =  15         4 * 1 * 5 =  20         5 * 1 * 5 =  25         6 * 1 * 5 =  30         7 * 1 * 5 =  35         8 * 1 * 5 =  40         9 * 1 * 5 =  45
1 * 2 * 5 =  10         2 * 2 * 5 =  20         3 * 2 * 5 =  30         4 * 2 * 5 =  40         5 * 2 * 5 =  50         6 * 2 * 5 =  60         7 * 2 * 5 =  70         8 * 2 * 5 =  80         9 * 2 * 5 =  90
1 * 3 * 5 =  15         2 * 3 * 5 =  30         3 * 3 * 5 =  45         4 * 3 * 5 =  60         5 * 3 * 5 =  75         6 * 3 * 5 =  90         7 * 3 * 5 = 105         8 * 3 * 5 = 120         9 * 3 * 5 = 135
1 * 4 * 5 =  20         2 * 4 * 5 =  40         3 * 4 * 5 =  60         4 * 4 * 5 =  80         5 * 4 * 5 = 100         6 * 4 * 5 = 120         7 * 4 * 5 = 140         8 * 4 * 5 = 160         9 * 4 * 5 = 180
1 * 5 * 5 =  25         2 * 5 * 5 =  50         3 * 5 * 5 =  75         4 * 5 * 5 = 100         5 * 5 * 5 = 125         6 * 5 * 5 = 150         7 * 5 * 5 = 175         8 * 5 * 5 = 200         9 * 5 * 5 = 225
1 * 6 * 5 =  30         2 * 6 * 5 =  60         3 * 6 * 5 =  90         4 * 6 * 5 = 120         5 * 6 * 5 = 150         6 * 6 * 5 = 180         7 * 6 * 5 = 210         8 * 6 * 5 = 240         9 * 6 * 5 = 270
1 * 7 * 5 =  35         2 * 7 * 5 =  70         3 * 7 * 5 = 105         4 * 7 * 5 = 140         5 * 7 * 5 = 175         6 * 7 * 5 = 210         7 * 7 * 5 = 245         8 * 7 * 5 = 280         9 * 7 * 5 = 315
1 * 8 * 5 =  40         2 * 8 * 5 =  80         3 * 8 * 5 = 120         4 * 8 * 5 = 160         5 * 8 * 5 = 200         6 * 8 * 5 = 240         7 * 8 * 5 = 280         8 * 8 * 5 = 320         9 * 8 * 5 = 360
1 * 9 * 5 =  45         2 * 9 * 5 =  90         3 * 9 * 5 = 135         4 * 9 * 5 = 180         5 * 9 * 5 = 225         6 * 9 * 5 = 270         7 * 9 * 5 = 315         8 * 9 * 5 = 360         9 * 9 * 5 = 405


1 * 1 * 6 =   6         2 * 1 * 6 =  12         3 * 1 * 6 =  18         4 * 1 * 6 =  24         5 * 1 * 6 =  30         6 * 1 * 6 =  36         7 * 1 * 6 =  42         8 * 1 * 6 =  48         9 * 1 * 6 =  54
1 * 2 * 6 =  12         2 * 2 * 6 =  24         3 * 2 * 6 =  36         4 * 2 * 6 =  48         5 * 2 * 6 =  60         6 * 2 * 6 =  72         7 * 2 * 6 =  84         8 * 2 * 6 =  96         9 * 2 * 6 = 108
1 * 3 * 6 =  18         2 * 3 * 6 =  36         3 * 3 * 6 =  54         4 * 3 * 6 =  72         5 * 3 * 6 =  90         6 * 3 * 6 = 108         7 * 3 * 6 = 126         8 * 3 * 6 = 144         9 * 3 * 6 = 162
1 * 4 * 6 =  24         2 * 4 * 6 =  48         3 * 4 * 6 =  72         4 * 4 * 6 =  96         5 * 4 * 6 = 120         6 * 4 * 6 = 144         7 * 4 * 6 = 168         8 * 4 * 6 = 192         9 * 4 * 6 = 216
1 * 5 * 6 =  30         2 * 5 * 6 =  60         3 * 5 * 6 =  90         4 * 5 * 6 = 120         5 * 5 * 6 = 150         6 * 5 * 6 = 180         7 * 5 * 6 = 210         8 * 5 * 6 = 240         9 * 5 * 6 = 270
1 * 6 * 6 =  36         2 * 6 * 6 =  72         3 * 6 * 6 = 108         4 * 6 * 6 = 144         5 * 6 * 6 = 180         6 * 6 * 6 = 216         7 * 6 * 6 = 252         8 * 6 * 6 = 288         9 * 6 * 6 = 324
1 * 7 * 6 =  42         2 * 7 * 6 =  84         3 * 7 * 6 = 126         4 * 7 * 6 = 168         5 * 7 * 6 = 210         6 * 7 * 6 = 252         7 * 7 * 6 = 294         8 * 7 * 6 = 336         9 * 7 * 6 = 378
1 * 8 * 6 =  48         2 * 8 * 6 =  96         3 * 8 * 6 = 144         4 * 8 * 6 = 192         5 * 8 * 6 = 240         6 * 8 * 6 = 288         7 * 8 * 6 = 336         8 * 8 * 6 = 384         9 * 8 * 6 = 432
1 * 9 * 6 =  54         2 * 9 * 6 = 108         3 * 9 * 6 = 162         4 * 9 * 6 = 216         5 * 9 * 6 = 270         6 * 9 * 6 = 324         7 * 9 * 6 = 378         8 * 9 * 6 = 432         9 * 9 * 6 = 486


1 * 1 * 7 =   7         2 * 1 * 7 =  14         3 * 1 * 7 =  21         4 * 1 * 7 =  28         5 * 1 * 7 =  35         6 * 1 * 7 =  42         7 * 1 * 7 =  49         8 * 1 * 7 =  56         9 * 1 * 7 =  63
1 * 2 * 7 =  14         2 * 2 * 7 =  28         3 * 2 * 7 =  42         4 * 2 * 7 =  56         5 * 2 * 7 =  70         6 * 2 * 7 =  84         7 * 2 * 7 =  98         8 * 2 * 7 = 112         9 * 2 * 7 = 126
1 * 3 * 7 =  21         2 * 3 * 7 =  42         3 * 3 * 7 =  63         4 * 3 * 7 =  84         5 * 3 * 7 = 105         6 * 3 * 7 = 126         7 * 3 * 7 = 147         8 * 3 * 7 = 168         9 * 3 * 7 = 189
1 * 4 * 7 =  28         2 * 4 * 7 =  56         3 * 4 * 7 =  84         4 * 4 * 7 = 112         5 * 4 * 7 = 140         6 * 4 * 7 = 168         7 * 4 * 7 = 196         8 * 4 * 7 = 224         9 * 4 * 7 = 252
1 * 5 * 7 =  35         2 * 5 * 7 =  70         3 * 5 * 7 = 105         4 * 5 * 7 = 140         5 * 5 * 7 = 175         6 * 5 * 7 = 210         7 * 5 * 7 = 245         8 * 5 * 7 = 280         9 * 5 * 7 = 315
1 * 6 * 7 =  42         2 * 6 * 7 =  84         3 * 6 * 7 = 126         4 * 6 * 7 = 168         5 * 6 * 7 = 210         6 * 6 * 7 = 252         7 * 6 * 7 = 294         8 * 6 * 7 = 336         9 * 6 * 7 = 378
1 * 7 * 7 =  49         2 * 7 * 7 =  98         3 * 7 * 7 = 147         4 * 7 * 7 = 196         5 * 7 * 7 = 245         6 * 7 * 7 = 294         7 * 7 * 7 = 343         8 * 7 * 7 = 392         9 * 7 * 7 = 441
1 * 8 * 7 =  56         2 * 8 * 7 = 112         3 * 8 * 7 = 168         4 * 8 * 7 = 224         5 * 8 * 7 = 280         6 * 8 * 7 = 336         7 * 8 * 7 = 392         8 * 8 * 7 = 448         9 * 8 * 7 = 504
1 * 9 * 7 =  63         2 * 9 * 7 = 126         3 * 9 * 7 = 189         4 * 9 * 7 = 252         5 * 9 * 7 = 315         6 * 9 * 7 = 378         7 * 9 * 7 = 441         8 * 9 * 7 = 504         9 * 9 * 7 = 567


1 * 1 * 8 =   8         2 * 1 * 8 =  16         3 * 1 * 8 =  24         4 * 1 * 8 =  32         5 * 1 * 8 =  40         6 * 1 * 8 =  48         7 * 1 * 8 =  56         8 * 1 * 8 =  64         9 * 1 * 8 =  72
1 * 2 * 8 =  16         2 * 2 * 8 =  32         3 * 2 * 8 =  48         4 * 2 * 8 =  64         5 * 2 * 8 =  80         6 * 2 * 8 =  96         7 * 2 * 8 = 112         8 * 2 * 8 = 128         9 * 2 * 8 = 144
1 * 3 * 8 =  24         2 * 3 * 8 =  48         3 * 3 * 8 =  72         4 * 3 * 8 =  96         5 * 3 * 8 = 120         6 * 3 * 8 = 144         7 * 3 * 8 = 168         8 * 3 * 8 = 192         9 * 3 * 8 = 216
1 * 4 * 8 =  32         2 * 4 * 8 =  64         3 * 4 * 8 =  96         4 * 4 * 8 = 128         5 * 4 * 8 = 160         6 * 4 * 8 = 192         7 * 4 * 8 = 224         8 * 4 * 8 = 256         9 * 4 * 8 = 288
1 * 5 * 8 =  40         2 * 5 * 8 =  80         3 * 5 * 8 = 120         4 * 5 * 8 = 160         5 * 5 * 8 = 200         6 * 5 * 8 = 240         7 * 5 * 8 = 280         8 * 5 * 8 = 320         9 * 5 * 8 = 360
1 * 6 * 8 =  48         2 * 6 * 8 =  96         3 * 6 * 8 = 144         4 * 6 * 8 = 192         5 * 6 * 8 = 240         6 * 6 * 8 = 288         7 * 6 * 8 = 336         8 * 6 * 8 = 384         9 * 6 * 8 = 432
1 * 7 * 8 =  56         2 * 7 * 8 = 112         3 * 7 * 8 = 168         4 * 7 * 8 = 224         5 * 7 * 8 = 280         6 * 7 * 8 = 336         7 * 7 * 8 = 392         8 * 7 * 8 = 448         9 * 7 * 8 = 504
1 * 8 * 8 =  64         2 * 8 * 8 = 128         3 * 8 * 8 = 192         4 * 8 * 8 = 256         5 * 8 * 8 = 320         6 * 8 * 8 = 384         7 * 8 * 8 = 448         8 * 8 * 8 = 512         9 * 8 * 8 = 576
1 * 9 * 8 =  72         2 * 9 * 8 = 144         3 * 9 * 8 = 216         4 * 9 * 8 = 288         5 * 9 * 8 = 360         6 * 9 * 8 = 432         7 * 9 * 8 = 504         8 * 9 * 8 = 576         9 * 9 * 8 = 648


1 * 1 * 9 =   9         2 * 1 * 9 =  18         3 * 1 * 9 =  27         4 * 1 * 9 =  36         5 * 1 * 9 =  45         6 * 1 * 9 =  54         7 * 1 * 9 =  63         8 * 1 * 9 =  72         9 * 1 * 9 =  81
1 * 2 * 9 =  18         2 * 2 * 9 =  36         3 * 2 * 9 =  54         4 * 2 * 9 =  72         5 * 2 * 9 =  90         6 * 2 * 9 = 108         7 * 2 * 9 = 126         8 * 2 * 9 = 144         9 * 2 * 9 = 162
1 * 3 * 9 =  27         2 * 3 * 9 =  54         3 * 3 * 9 =  81         4 * 3 * 9 = 108         5 * 3 * 9 = 135         6 * 3 * 9 = 162         7 * 3 * 9 = 189         8 * 3 * 9 = 216         9 * 3 * 9 = 243
1 * 4 * 9 =  36         2 * 4 * 9 =  72         3 * 4 * 9 = 108         4 * 4 * 9 = 144         5 * 4 * 9 = 180         6 * 4 * 9 = 216         7 * 4 * 9 = 252         8 * 4 * 9 = 288         9 * 4 * 9 = 324
1 * 5 * 9 =  45         2 * 5 * 9 =  90         3 * 5 * 9 = 135         4 * 5 * 9 = 180         5 * 5 * 9 = 225         6 * 5 * 9 = 270         7 * 5 * 9 = 315         8 * 5 * 9 = 360         9 * 5 * 9 = 405
1 * 6 * 9 =  54         2 * 6 * 9 = 108         3 * 6 * 9 = 162         4 * 6 * 9 = 216         5 * 6 * 9 = 270         6 * 6 * 9 = 324         7 * 6 * 9 = 378         8 * 6 * 9 = 432         9 * 6 * 9 = 486
1 * 7 * 9 =  63         2 * 7 * 9 = 126         3 * 7 * 9 = 189         4 * 7 * 9 = 252         5 * 7 * 9 = 315         6 * 7 * 9 = 378         7 * 7 * 9 = 441         8 * 7 * 9 = 504         9 * 7 * 9 = 567
1 * 8 * 9 =  72         2 * 8 * 9 = 144         3 * 8 * 9 = 216         4 * 8 * 9 = 288         5 * 8 * 9 = 360         6 * 8 * 9 = 432         7 * 8 * 9 = 504         8 * 8 * 9 = 576         9 * 8 * 9 = 648
1 * 9 * 9 =  81         2 * 9 * 9 = 162         3 * 9 * 9 = 243         4 * 9 * 9 = 324         5 * 9 * 9 = 405         6 * 9 * 9 = 486         7 * 9 * 9 = 567         8 * 9 * 9 = 648         9 * 9 * 9 = 729
"""