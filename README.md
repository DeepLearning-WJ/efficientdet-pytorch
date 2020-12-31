## Efficientdet：Scalable and Efficient Object 目标检测模型在 Pytorch 当中的实现
---

<!-- vim-markdown-toc GFM -->

* [所需环境](#所需环境)
* [文件下载](#文件下载)
* [注意事项](#注意事项)
* [训练步骤](#训练步骤)
* [mAP 目标检测精度计算更新](#map-目标检测精度计算更新)
* [Reference](#reference)

<!-- vim-markdown-toc -->

### 所需环境

torch

### 文件下载
- 训练所需的 pth 可以在百度网盘下载。
- 包括 Efficient-d0 到 d7 所有权重。

### 注意事项
- **1、训练前一定要注意权重文件与 Efficientdet 版本的对齐！**
- **2、注意修改训练用到的 voc_classes.txt 文件！**
- **3、注意修改预测用到的 voc_classes.txt 文件！**

### 训练步骤
1. 本文使用 VOC 格式进行训练。
2. 训练前将标签文件放在 VOCdevkit 文件夹下的 VOC2007 文件夹下的 Annotation 中。
3. 训练前将图片文件放在 VOCdevkit 文件夹下的 VOC2007 文件夹下的 JPEGImages 中。
4. 在训练前利用 voc2efficientdet.py 文件生成对应的 txt。
5. 再运行根目录下的 voc_annotation.py，运行前需要将 classes 改成你自己的 classes。

    ```python
    classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    ```
6. 就会生成对应的 2007_train.txt，每一行对应其图片位置及其真实框的位置。
7. 在训练前需要修改 model_data 里面的 voc_classes.txt 文件，需要将 classes 改成你自己的 classes。
8. 修改 train.py 文件下的 phi 可以修改 efficientdet 的版本，训练前注意权重文件与 Efficientdet 版本的对齐。
9. 运行 train.py 即可开始训练。

### mAP 目标检测精度计算更新
- 更新了 get_gt_txt.py、get_dr_txt.py 和 get_map.py 文件。
- get_map 文件克隆自 https://github.com/Cartucho/mAP

### Reference

- https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch
- https://github.com/Cartucho/mAP
