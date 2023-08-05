def calculate(pagecount, pagesize):
    MegaBytes = pagecount * pagesize
    return  "{:.2f} MB / {:.2f} GB / {:.2f} TB".format(MegaBytes, MegaBytes / 1024, MegaBytes / 1024 ** 2)
