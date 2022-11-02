# SmartIV-yolov5

[数据集下载](https://pan.baidu.com/s/1EV20XavJ-DA8zOEisS67QA?pwd=1jyo)
[说明文档下载](https://pan.baidu.com/s/1-mv87wrFQ4DAKt-SUVnW5A?pwd=r8q7)

1.参考链接：[YOLOV5](https://github.com/ultralytics/yolov5)

2.权重下载：[best.pth](https://pan.baidu.com/s/1AdYGT6f3Gut25tCYgeCSlA?pwd=kr6o)

```
└── yolov5
	......
    ├── models
    ├── README.md
    ├── requirements.txt
    ├── Tools  -->可视化工具文件
    ├── runs
        ├── train
            ├── exp
                └── weights
                    ├── best.pt
                    └── last.pt
	......

```

3.运行：`python detect_task1.py`

4.保存json结果：`task_result/smartIV/`

5.docker 镜像安装：

​**5.1 镜像下载链接**：[task1_smartiv.tar](https://pan.baidu.com/s/1JhJivCzbmod1IY6yaoVisg?pwd=p9o1)
​    

**5.1 加载镜像：**(加载需要一会儿时间)

```
docker load < task1_smartiv.tar
```

![image-20221101114630511](README.assets/image-20221101114630511.png)

加载成功如下图所示：

![image-20221101115704711](README.assets/image-20221101115704711.png)

 

**5.2 查看镜像：**

```
docker images
```

![image-20221101103218388](README.assets/image-20221101103218388.png)

 

**5.3 容器创建**：将本地测试图片链接到docker环境的`/root/app/task1`路径下（可参考下一条具体示例）

```python
docker run --name <容器名称> --gpus all -it -v <本地存放测试图片文件位置>:/root/app/task1  task1_smartiv:v2
```

**示例**：假设容器名为test，本地测试图片存放路径为`/home/wmj/Docker_envs/local_file/imgs`

![image-20221101104252070](README.assets/image-20221101104252070.png)

将其链接到docker环境下的`task1`文件夹,docker内路径为`/usr/src/app/task1`，具体命令如下：

```
docker run --name test --gpus all -it -v /home/wmj/Docker_envs/local_file/imgs:/usr/src/app/task1  task1_smartiv:v2
```

![image-20221101104915032](README.assets/image-20221101104915032.png)

**5.4 文件说明**：容器创建后默认进入`/usr/src/app/`文件夹下，只需要关注4个文件:

| 1    | detect_task1.py | 主要运行文件                                   |
| ---- | --------------- | ---------------------------------------------- |
| 2    | best.pt         | 训练好的模型权重                               |
| 3    | task1           | 存放测试图片，与之前的本地路径的imgs文件夹链接 |
| 4    | task1_result    | 内有子文件夹smartIV，存放测试结果.json文件     |

![image-20221101105902008](README.assets/image-20221101105902008.png)

​				

**5.5 运行：** `在/usr/src/app/`路径下，运行如下命令:

```
python detect_task1.py --weights best.pt --source task1
```

![image-20221101111317461](README.assets/image-20221101111317461.png)

**5.6 结果查看：** 将生成的`.json`文件自动创建并放置于`/usr/src/app/task1_result/smartIV`下

![image-20221101110637584](README.assets/image-20221101110637584.png)

**5.7 文件转移**：如果想将结果文件从docker镜像迁移出来保存至本地，可以将docker镜像内的文件或者文件夹放到`task1`文件夹下，然后在本地的`/home/wmj/Docker_envs/local_file/imgs`就可以看到了。
