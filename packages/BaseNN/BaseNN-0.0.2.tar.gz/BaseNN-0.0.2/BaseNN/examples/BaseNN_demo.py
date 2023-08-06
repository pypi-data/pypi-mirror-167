from BaseNN import BaseNN
import numpy as np
import cv2
import os

def cal_accuracy(y, pred_y):
    res = pred_y.argmax(axis=1)
    tp = np.array(y)==np.array(res)
    acc = np.sum(tp)/ y.shape[0]
    return acc

def read_data(path):
    data = []
    label = []
    dir_list = os.listdir(path)

    # 将顺序读取的文件保存到该list中
    for item in dir_list:
        tpath = os.path.join(path,item)

        # print(tpath)
        for i in os.listdir(tpath):
            # print(item)
            img = cv2.imread(os.path.join(tpath,i))
            imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # print(img)
            data.append(imGray)
            label.append(int(item))
    x = np.array(data)
    y = np.array(label)

    x = np.expand_dims(x, axis=1)
    return x, y

def only_infer_demo():
    # 测试数据
    test_path = '../dataset/iris/iris_test.csv'
    test_x = np.loadtxt(test_path, dtype=float, delimiter=',',skiprows=1,usecols=range(0,4))
    test_y = np.loadtxt(test_path, dtype=int, delimiter=',',skiprows=1,usecols=4)

    model = BaseNN()
    checkpoint = 'iris_ckpt/basenn.pkl'
    result = model.inference(data=test_x, checkpoint=checkpoint)
    model.print_result(result)

def normal_train_demo():
    model = BaseNN()
    # 训练数据
    train_path = '../dataset/iris/iris_training.csv'
    x = np.loadtxt(train_path, dtype=float, delimiter=',',skiprows=1,usecols=range(0,4)) # [120, 4]
    y = np.loadtxt(train_path, dtype=int, delimiter=',',skiprows=1,usecols=4)
    model.add(layer='Linear',size=(4, 10),activation='ReLU') # [120, 10]
    model.add(layer='Linear',size=(10, 5), activation='ReLU') # [120, 5]
    model.add(layer='Linear', size=(5, 3), activation='Softmax') # [120, 3]
    model.load_dataset(x, y)
    model.save_fold = 'iris_ckpt'
    model.train(lr=0.01, epochs=100)

def continue_train_demo():
    model = BaseNN()
    # 训练数据
    train_path = '../dataset/iris/iris_training.csv'
    x = np.loadtxt(train_path, dtype=float, delimiter=',',skiprows=1,usecols=range(0,4)) # [120, 4]
    y = np.loadtxt(train_path, dtype=int, delimiter=',',skiprows=1,usecols=4)
    model.load_dataset(x, y)
    model.save_fold = 'checkpoints'
    checkpoint = 'iris_ckpt/basenn.pkl'
    model.train(lr=0.01, epochs=1000, checkpoint=checkpoint)


def iris_train_test():
    # 训练数据
    train_path = '../dataset/iris/iris_training.csv'
    x = np.loadtxt(train_path, dtype=float, delimiter=',',skiprows=1,usecols=range(0,4)) # [120, 4]
    y = np.loadtxt(train_path, dtype=int, delimiter=',',skiprows=1,usecols=4)
        # 测试数据
    test_path = '../dataset/iris/iris_test.csv'
    test_x = np.loadtxt(test_path, dtype=float, delimiter=',',skiprows=1,usecols=range(0,4))
    test_y = np.loadtxt(test_path, dtype=int, delimiter=',',skiprows=1,usecols=4)
    # 声明模型
    model = BaseNN()
    model.add(layer='Linear',size=(4, 10),activation='ReLU') # [120, 10]
    model.add(layer='Linear',size=(10, 5), activation='ReLU') # [120, 5]
    model.add(layer='Linear', size=(5, 3), activation='Softmax') # [120, 3]
    model.load_dataset(x, y)
    # model.print_model()
    model.train(lr=0.01, epochs=5000, save_fold='iris_ckpt')
    res = model.inference(test_x)
    model.print_result() # 输出字典格式结果
    # 计算分类正确率
    print("分类正确率为：",cal_accuracy(test_y, res))

def mnist_train():
    # 读取数据
    train_x, train_y = read_data("../dataset/cls/mnist/training_set")

    model = BaseNN() #声明模型 
    model.load_dataset(train_x, train_y) # 载入数据
    model.add('Conv2D', size=(1, 6),kernel_size=( 5, 5), activation='ReLU') 
    model.add('AvgPool', kernel_size=(2,2)) 
    model.add('Conv2D', size=(6, 16), kernel_size=(5, 5), activation='ReLU')
    model.add('AvgPool', kernel_size=(2,2)) 
    model.add('Linear', size=(256, 120), activation='ReLU') 
    model.add('Linear', size=(120, 84), activation='ReLU') 
    model.add('Linear', size=(84, 10), activation='Softmax')
    model.add(optimizer='SGD')
    model.save_fold = 'mn_ckpt'
    checkpoint = 'mn_ckpt/basenn.pkl'
    # model.train(lr=0.1, epochs=30, checkpoint=checkpoint) # 继续训练
    model.train(lr=0.1, epochs=30) # 直接训练


def mnist_test(one_img):
    # one_img: 布尔值，True时推理一张图片，返回推理结果字典；False时推理整个验证集，返回准确率
    # 读取数据
    test_x, test_y = read_data("../dataset/cls/mnist/val_set")
    # 模型
    model = BaseNN() # 声明模型
    checkpoint = 'mn_ckpt/basenn.pkl' # 载入模型
    if one_img== False:     # 推理整个验证集
        result = model.inference(data=test_x, checkpoint=checkpoint)
        # model.print_result(result)
        acc = cal_accuracy(test_y, result)  # 计算准确率
        print(acc)
        # 训练集准确率：0.9896
        # 验证集准确率：0.9901
    else: # 推理一张图片
        result = model.inference(data=[test_x[0]], checkpoint=checkpoint)
        model.print_result(result)

if __name__=="__main__":
    normal_train_demo()
    # only_infer_demo()
    # continue_train_demo()
    # iris_train_test()
    # mnist_train()
    # mnist_test(False)