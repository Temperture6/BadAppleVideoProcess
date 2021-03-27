import os, time
from PIL import Image


def list_file(filepath):
    # 列出全部文件
    fl = list(os.walk(filepath))[0][2]

    # 跳帧挑选
    filelist = []

    for i in range(0, len(fl), 2):
        filelist.append(fl[i])

    return filelist


def process_picture(path_, filelist, savepath):

    # 删除文件以重新开始
    if os.path.exists(savepath):
        os.remove(savepath)

    start = time.time()
    f = open(savepath, "a+")
    # 按路径处理图片
    for file in filelist:
        text_ = '{8,8,'
        img = Image.open(path_ + "/" + file)
        img = img.convert('L')
        pixels = img.load()

        for w in range(img.width):
            text_ = text_ + 'B'
            for h in range(img.height - 1, -1, -1):
                if pixels[w, h] <= 100:
                    # 黑色
                    text_ = text_ + '1'
                else:
                    # 白色
                    text_ = text_ + '0'
            text_  = text_ + ','

        text_ = text_ + '},'

        print(text_, file=f)
    f.close()
    end = time.time()
    print("处理完成，处理了{0}张图片，用时{1}秒".format(len(filelist), end - start))

    return


if __name__ == "__main__":
    path = "./pic"
    process_picture(path, list_file(path), "data.txt")
