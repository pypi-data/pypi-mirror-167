from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QDialog,QMainWindow
from PyQt5.QtGui import QIcon, QColor, QPainter, QPixmap
from PyQt5 import uic
import vis_gui
from videotoply import *
import time

class videoPlayer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('video_2.ui', baseinstance=self)  # 加载designer设计的ui程序
        # 播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.ui.wgt_player)
        # 按钮
        self.ui.btn_select.clicked.connect(self.open)
        self.ui.btn_play_pause.clicked.connect(self.playPause)
        self.ui.btn_ana_video.clicked.connect(self.keyframe_exact)
        self.ui.btn_rec_ply.clicked.connect(self.reconstitute)
        self.ui.btn_open3d_ply.clicked.connect(self.open3d)
        self.ui.btn_select_ckpt.clicked.connect(self.select_ckpt)
        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.ui.sld_duration.sliderMoved.connect(self.updatePosition)
        # 资源图片
        '''self.ui.btn_select.setIcon(QIcon('../icon/hide.png'))
        self.ui.btn_play_pause.setIcon(QIcon('../icon/play.png'))'''
        # self.ui.wgt_player.setStyleSheet("QWidget { background-color: QColor(0,0,0) }" )
        # self.ui.btn_select.setStyleSheet('QPushButton{background:url(../icon/hide.png) no-repeat center}') # StyleSheet使用CSS语法
        # self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
        self.ckpt_filename = "./checkpoints/model_000007.ckpt"
    # 打开视频文件
    def open(self):
        file = QFileDialog.getOpenFileUrl()[0]
        self.player.setMedia(QMediaContent(file))
        self.filename = str(file)[26:-2]
        self.player.play()
        # self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/pause.png) no-repeat center}')
    # 播放视频
    def playPause(self):
        if self.player.state()==1:
            self.player.pause()
            # self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
        elif self.player.state()==2 or self.ui.sld_duration.value()!=0:
            self.player.play()
            # self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/pause.png) no-repeat center}')
    # 视频总时长获取
    def getDuration(self, d):
        '''d是获取到的视频总时长（ms）'''
        self.ui.sld_duration.setRange(0, d)
        self.ui.sld_duration.setEnabled(True)
        self.displayTime(d)
    # 视频实时位置获取
    def getPosition(self, p):
        self.ui.sld_duration.setValue(p)
        self.displayTime(self.ui.sld_duration.maximum()-p)
    # 显示剩余时间
    def displayTime(self, ms):
        minutes = int(ms/60000)
        seconds = int((ms-minutes*60000)/1000)
        self.ui.lab_duration.setText('{}:{}'.format(minutes, seconds))
        # if ms==0:
        #     self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.ui.sld_duration.maximum()-v)
    # 自定义paintEvent，绘制背景图
    def paintEvent(self, event):
        painter = QPainter(self)
        # painter.drawPixmap(self.ui.rect(), QPixmap('../icon/bg_1.jpg'))

    #新增加函数,可实时输出txt到textBrowser界面
    def printf(self,mes):
        self.ui.textBrowser.append(mes)
        self.cursot = self.ui.textBrowser.textCursor()
        self.ui.textBrowser.moveCursor(self.cursot.End)
        QApplication.processEvents()

    def video_parameter(self):
        cap = cv2.VideoCapture(self.filename)
        V_W = int(cap.get(3))
        V_H = int(cap.get(4))
        V_speed = int(cap.get(5))
        V_picnum = int(cap.get(7))
        time.sleep(3)
        self.printf("视频分析完毕!\n视频主要参数:")
        self.printf("宽X高:  "+str(V_W)+'X'+str(V_H))
        self.printf("帧数:  "+str(V_picnum))
        self.printf("帧速率:  "+ str(V_speed)+'帧/秒')



    def keyframe_exact(self):
        self.printf("开始分析视频......")
        self.video_parameter()
        self.printf("开始提取关键帧......")
        self.output_file, self.num_key = key_exact(self.filename)
        self.printf("关键帧提取完毕!\n关键帧数量:  " + str(self.num_key))

    def select_ckpt(self):
        self.ckpt_filename, _ = QFileDialog.getOpenFileName(self, "选取文件", r"checkpoints/", "All File(*)")
        self.ui.line_ckpt.setText(self.ckpt_filename)


    def reconstitute(self):
        self.printf("开始三维重建......")
        time.sleep(3)
        self.printf("开始计算相机参数......")
        pic_sfm(self.output_file)
        self.printf("开始进行深度多视角重建......")
        self.plyfile = sfm_ply(self.filename, self.output_file, self.ckpt_filename)
        self.printf("三维重建完毕......")
        self.printf("点云路径: " + self.plyfile)

    def open3d(self):
        vis_gui.main()

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('icon/ground3d.jpg'))
    myPlayer = videoPlayer()
    myPlayer.ui.show()
    app.exec()
