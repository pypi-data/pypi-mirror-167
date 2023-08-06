import cv2
import os




def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree

def classify_hist_with_split(image1, image2, size=(256, 256)):
    # RGB每个通道的直方图相似度
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

def Laplacian(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    return cv2.Laplacian(img,cv2.CV_64F).var()



def keyexact(video_file, key_savefile):
    cap = cv2.VideoCapture(video_file)  # 返回一个capture对象
    num_img = int(cap.get(7))  # 视频帧数据
    img_total = [0] * num_img

    # cap.set(cv2.CAP_PROP_POS_FRAMES,0)  #设置要获取的帧号
    # _,img_total[0]=cap.read()  #read方法返回一个布尔值和一个视频帧。若帧读取成功，则返回True

    key_frame_num = []
    ref_id_frame = 0
    id_frame = 0
    step = 1
    S_Up = 0.80  # 0.86 0.6 003biansumohu   0.88 0.6Horse01
    S_Down = 0.6
    Clear_threshold = 50
    Global_S_threshold = 0.86

    # 若相似度小了，往前找
    def compute_frame_X(id_min, id_max):
        # if(id_min==id_max):
        #     return id_min
        max_id = id_max
        min_id = id_min
        new_id = int((min_id + max_id) / 2)
        if (new_id == min_id or new_id == max_id):
            return id_max  # 左大，右小，说明全新视角开始
        cap.set(cv2.CAP_PROP_POS_FRAMES, new_id)
        _, img_total[new_id] = cap.read()
        if (Laplacian(img_total[new_id]) > Clear_threshold and S_Up > classify_hist_with_split(img_total[ref_id_frame],
                                                                                               img_total[
                                                                                                   new_id]) > S_Down):
            return new_id
        elif (Laplacian(img_total[new_id]) > Clear_threshold and classify_hist_with_split(img_total[ref_id_frame],
                                                                                          img_total[new_id]) >= S_Up):
            return compute_frame_X(new_id, max_id)
        elif (Laplacian(img_total[new_id]) > Clear_threshold and classify_hist_with_split(img_total[ref_id_frame],
                                                                                          img_total[new_id]) <= S_Down):
            return compute_frame_X(min_id, new_id)
        elif (Laplacian(img_total[new_id]) <= Clear_threshold):
            return max_id

    # 若相似度大了，往后找
    def compute_frame_D(id_min, step):
        new_id0 = id_min
        new_id1 = id_min + step
        if (new_id1 >= num_img):
            return id_min
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, new_id1)
            _, img_total[new_id1] = cap.read()
            if (Laplacian(img_total[new_id1]) > Clear_threshold and S_Up > classify_hist_with_split(
                    img_total[ref_id_frame], img_total[new_id1]) > S_Down):
                return new_id1
            elif (Laplacian(img_total[new_id1]) > Clear_threshold and classify_hist_with_split(img_total[ref_id_frame],
                                                                                               img_total[
                                                                                                   new_id1]) <= S_Down):
                return compute_frame_X(new_id0, new_id1)
            elif (Laplacian(img_total[new_id1]) > Clear_threshold and classify_hist_with_split(img_total[ref_id_frame],
                                                                                               img_total[
                                                                                                   new_id1]) >= S_Up):
                return compute_frame_D(new_id1, step)
            elif (Laplacian(img_total[new_id1]) <= Clear_threshold):
                return compute_frame_D(new_id1, step)


    # step.1 寻找第1帧, 清晰度达标就加入关键帧
    while id_frame<num_img and len(key_frame_num)==0:
        cap.set(cv2.CAP_PROP_POS_FRAMES,id_frame)
        _,img_total[id_frame]=cap.read()
        if(Laplacian(img_total[id_frame])>Clear_threshold):
            key_frame_num.append(id_frame)
            ref_id_frame = id_frame
        id_frame = id_frame+1

    # if(id_frame>=num_img):
    #     exit("视频清晰度低，关键帧过少!")

    # step.2 寻找第2帧，确定初始step
    while id_frame<num_img and  len(key_frame_num)==1:
        cap.set(cv2.CAP_PROP_POS_FRAMES,id_frame)
        _,img_total[id_frame]=cap.read()
        if(Laplacian(img_total[id_frame])>Clear_threshold and S_Up > classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])>S_Down):
            key_frame_num.append(id_frame)
            ref_id_frame = id_frame
            step = key_frame_num[-1] - key_frame_num[-2]
        id_frame = id_frame+1

    # if(id_frame>=num_img):
    #     exit("视频相似度不够，关键帧过少!")

    # step.3 寻找其它帧
    id_frame = id_frame - 1 + step
    while id_frame<num_img:
        print(id_frame)
        cap.set(cv2.CAP_PROP_POS_FRAMES,id_frame)
        _,img_total[id_frame]=cap.read()
        if(Laplacian(img_total[id_frame])>Clear_threshold and S_Up>classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])>S_Down):
            key_frame_num.append(id_frame)
            ref_id_frame = id_frame
            # step = key_frame_num[-1] - key_frame_num[-2]

        elif(Laplacian(img_total[id_frame])>Clear_threshold and classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])<=S_Down):
            id_frame = compute_frame_X(ref_id_frame, id_frame)
            key_frame_num.append(id_frame)
            ref_id_frame = id_frame
            if(S_Up>classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])>S_Down):  # 如果出现大面积模糊情况，会导致步长突变，导致后面关键帧过少。主要是相似度函数并不完美，并非完全线性变化。
                step = key_frame_num[-1] - key_frame_num[-2]

        elif(Laplacian(img_total[id_frame])>Clear_threshold and classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])>=S_Up):
            id_frame= compute_frame_D(id_frame,step)
            key_frame_num.append(id_frame)
            if(S_Up>classify_hist_with_split(img_total[ref_id_frame], img_total[id_frame])>S_Down):  # 如果出现大面积模糊情况，会导致步长突变，导致后面关键帧过少。主要是相似度函数并不完美，并非完全线性变化。
                step = key_frame_num[-1] - key_frame_num[-2]
            ref_id_frame = id_frame


        id_frame = id_frame + step



    # step.4 全局去重
    key_ison=[1]*len(key_frame_num)
    # for i in range(len(key_frame_num)):
    #     if(key_ison[i]==1):
    #         j=i+2    #相邻的图像不用再比较
    #         while j<len(key_frame_num):
    #             if(key_ison[j]==1):
    #                 if(classify_hist_with_split(img_total[key_frame_num[i]], img_total[key_frame_num[j]])>=Global_S_threshold):
    #                     key_ison[j]=0
    #             j=j+1

    # step.5 save key frame
    img_save_dir = key_savefile
    if (not os.path.exists(img_save_dir)):
        os.makedirs(img_save_dir)
    New_key_frame_num = []
    for i in range(len(key_frame_num)):
        if(key_ison[i]==1):
            New_key_frame_num.append(key_frame_num[i])
            # cv2.imwrite(img_save_dir + str(key_frame_num[i]).zfill(8)+'.jpg', img_total[key_frame_num[i]])
            cv2.imwrite(img_save_dir + str(i).zfill(8) + '.jpg', img_total[key_frame_num[i]])

    return len(New_key_frame_num)


if __name__ == '__main__':
    video_path = '/home/luo/桌面/video/'
    video_name = '024'
    video_type = '.mp4'
    video_file = video_path + video_name + video_type
    key_savefile = '/home/luo/桌面/video/'
    keyexact(video_file, key_savefile)