from PIL import Image
import os

'''
使用python3
调用Image库拼接多张图片合成pdf
'''


def rea(pdf_name, imagesDirPath):
    # 获取目录所有文件名
    file_list = os.listdir(imagesDirPath)
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)
    pic_name.sort()
    # 按文件名的数字进行排序 即 1.png  2.png
    pic_name.sort(key=lambda x: int(x[:-4]))  ##文件名按数字排序

    new_pic = []
    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)
    for x in pic_name:
        if "png" in x:
            new_pic.append(x)
    print("图片文件：", new_pic)
    # 根据文件路径打开第一张图片资源作为被拼接的图片
    firstImagePath = imagesDirPath + "/" + new_pic[0]
    print(firstImagePath)
    im1 = Image.open(firstImagePath)

    # 处理第一张图片 把PNG格式转换成的四通道转成RGB的三通道
    if im1.mode == "RGBA":
        # print(firstImagePath, '转换成RGB')
        im1 = im1.convert('RGB')
    else:
        print('im1 mode not is RGBA')

    # 拼接的图片数组中移除第一个
    new_pic.pop(0)
    for i in new_pic:
        # 根据文件路径打开图片资源
        imagePath = imagesDirPath + "/" + i
        print(imagePath)
        img = Image.open(imagePath)
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":
            # print(imagePath, '转换成RGB')
            img = img.convert('RGB')
            im_list.append(img)
        else:
            print('im1 mode not is RGBA')
            im_list.append(img)
    # 调用Image库拼接图片输出为pdf
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)


if __name__ == '__main__':
    pdf_name = input("请输入合成PDF文件名称：")
    imagesDirPath = input("请输入合成的图片目录：")
    # pdf_name = 'didi'
    # imagesDirPath = '/Users/huzekang/Downloads/jvmbook'
    if ".pdf" in pdf_name:
        rea(pdf_name=pdf_name, imagesDirPath=imagesDirPath)
    else:
        rea(pdf_name="{}.pdf".format(pdf_name), imagesDirPath=imagesDirPath)
