from statistics import mode
import os
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class Reshape(nn.Module):
    def __init__(self, *args):
        super(Reshape, self).__init__()
        self.shape = args

    def forward(self, x):
        # print(x.shape,x.view(x.shape[0], -1).shape)
        return x.view(x.shape[0], -1)

def cal_accuracy(y, pred_y):
    res = pred_y.argmax(axis=1)
    tp = np.array(y)==np.array(res)
    acc = np.sum(tp)/ y.shape[0]
    return acc

class BaseNN:
    def __init__(self, save_fold=None):
        self.model = nn.Sequential()
        self.batchsize = None
        self.layers = []
        self.layers_num = 0
        self.optimizer = 'SGD'
        self.x = None
        self.y = None
        self.res = None
        self.save_fold = "checkpoints"
        if save_fold != None:
            self.save_fold = save_fold

    def add(self, layer=None, activation=None, optimizer=None, **kw):
        self.layers_num += 1
        self.layers.append(layer)
        if layer == 'Linear':
            self.model.add_module('Reshape', Reshape(self.batchsize))
            self.model.add_module('Linear' + str(self.layers_num), nn.Linear(kw['size'][0], kw['size'][1]))
            print("增加全连接层，输入维度:{},输出维度：{}。".format(kw['size'][0], kw['size'][1]))
        elif layer == 'Reshape':
            self.model.add_module('Reshape', Reshape(self.batchsize))
        # elif layer == 'ReLU':
        #     self.model.add_module('ReLU' + str(self.layers_num), nn.ReLU())
        #     print("增加ReLU层。")
        elif layer == 'Conv2D':
            self.model.add_module('Conv2D' + str(self.layers_num), nn.Conv2d(kw['size'][0], kw['size'][1], kw['kernel_size']))
            print("增加卷积层，输入维度:{},输出维度：{},kernel_size: {} ".format(kw['size'][0], kw['size'][1], kw['kernel_size']))
        elif layer == 'MaxPool':
            self.model.add_module('MaxPooling' + str(self.layers_num), nn.MaxPool2d(kw['kernel_size']))
            print("增加最大池化层,kernel_size: {} ".format(kw['kernel_size']))
        elif layer == 'AvgPool':
            self.model.add_module('MaxPooling' + str(self.layers_num), nn.AvgPool2d(kw['kernel_size']))
            print("增加平均池化层,kernel_size: {} ".format(kw['kernel_size']))
        
        # 激活函数
        if activation == 'ReLU':
            self.model.add_module('ReLU' + str(self.layers_num), nn.ReLU())
            print("使用ReLU激活函数。")
        elif activation == 'Softmax':
            self.model.add_module('Softmax'+str(self.layers_num), nn.Softmax())
            print('使用Softmax激活函数。')

        # 优化器
        if optimizer != None:
            self.optimizer = optimizer


    def load_dataset(self, x, y):
        self.x = Variable(torch.tensor(np.array(x)).to(torch.float32))
        self.y = Variable(torch.tensor(np.array(y)).long())

        self.batchsize = self.x.shape[0]

    def train(self, lr=0.1, epochs=30, save_fold=None, filename='basenn.pkl', checkpoint=None):
        if checkpoint:
            if not os.path.exists(checkpoint):
                print("未找到{}文件！".format(checkpoint))
                return 
            self.model = torch.load(checkpoint)

        loss_fun = nn.CrossEntropyLoss()  # 使用交叉熵作为损失函数
        if self.optimizer == 'SGD':
            optimizer = torch.optim.SGD(self.model.parameters(), lr=lr,momentum=0.9)  # 使用SGD优化器
        elif self.optimizer == 'Adam':
            optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        elif self.optimizer == 'Adagrad':
            optimizer = torch.optim.Adagrad(self.model.parameters(), lr=lr)
        elif self.optimizer == 'ASGD':
            optimizer = torch.optim.ASGD(self.model.parameters(), lr=lr)  
        print("使用 {} 优化器。".format(self.optimizer))
        for epoch in range(epochs):  
            y_pred = self.model(self.x)
            acc = cal_accuracy(self.y, y_pred)
            # print(y_pred, self.y)
            loss = loss_fun(y_pred, self.y)
            print("{epoch:%d  Loss:%.4f  Accuracy:%.4f}" % (epoch, loss, acc))
            optimizer.zero_grad()  # 将梯度初始化为零，即清空过往梯度
            loss.backward()  # 反向传播，计算当前梯度
            optimizer.step()  # 根据梯度更新网络参数

        if save_fold:
            self.save_fold = save_fold
            print(self.save_fold)
        if not os.path.exists(self.save_fold):
            os.mkdir(self.save_fold)

        model_path = os.path.join(self.save_fold, filename)
        print("保存模型中...")
        torch.save(self.model, model_path)
        print("保存模型{}成功！".format(model_path))

    def inference(self, data, show=False, checkpoint=None):
        data  = Variable(torch.tensor(np.array(data)).to(torch.float32))
        if checkpoint:
            self.model = torch.load(checkpoint)

        with torch.no_grad():
            res = self.model(data)
        res = np.array(res)
        if show:
            print("推理结果为：",res)
        self. res = res
        return res

    def print_model(self):
        # print('模型共{}层'.format(self.layers_num))
        print(self.model)

    def save(self, model_path='basenn.pkl'):
        print("保存模型中...")
        torch.save(self.model, model_path)
        print("保存模型{}成功！".format(model_path))
    
    def load(self,model_path):
        print("载入模型中...")
        self.model = torch.load(model_path)
        print("载入模型{}成功！".format(model_path))

    def print_result(self, result=None):
        res_idx = self.res.argmax(axis=1)
        res = {}
        for i,idx in enumerate(res_idx):
            res[i] ={"预测值":idx,"置信度":self.res[i][idx]} 
        print("推理结果为：", res)
        return res
