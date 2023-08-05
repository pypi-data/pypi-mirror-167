import collections
import hashlib
import math
import os
import random
import re
import shutil
import sys
import tarfile
import time
import zipfile
from collections import defaultdict
from pathlib import Path

import pandas as pd
import requests
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import torch
import torchvision
from PIL import Image
from torch import nn
from torch.nn import functional as F
from torch.utils import data
from torchvision import transforms
from torchstat import stat


def compute_num_params(net, shape):
    stat(net, shape)


#mylib = sys.modules[__name__]

def use_svg_display():
    # Use the svg format to display a plot in Jupyter.
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    # Set the figure size for matplotlib.
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize

def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    # Set the axes for matplotlib.
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()#用于画网格线

def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear',
         fmts=('-', 'm--', 'g-.', 'r:'), figsize=None, axes=None):

    if legend is None:
        legend = []

    set_figsize(figsize)
    axes = axes if axes else plt.gca()

    # Return True if `X` (tensor or list) has 1 axis
    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], "__len__"))

    if has_one_axis(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)
    axes.cla()
    for x, y, fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)


class Logger(object):
    def __init__(self,fileN ="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN,"a")
 
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
 
    def flush(self):
        pass


class Timer:
    """Record multiple running times."""
    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """Start the timer."""
        self.tik = time.time()

    def stop(self):
        """Stop the timer and record the time in a list."""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """Return the average time."""
        return sum(self.times) / len(self.times)

    def sum(self):
        """Return the sum of time."""
        return sum(self.times)

    def cumsum(self):
        """Return the accumulated time."""
        return np.array(self.times).cumsum().tolist()

def synthetic_data(w, b, num_examples):
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, torch.reshape(y, (-1, 1))

def linreg(X, w, b):
    return torch.matmul(X, w) + b

def squared_loss(y_hat, y):
    return (y_hat - torch.reshape(y, y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


def load_array(data_arrays, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

def get_fashion_mnist_labels(labels):
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # Tensor Image
            ax.imshow(img.numpy())
        else:
            # PIL Image
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes

def get_dataloader_workers():
    return 4


def load_data_fashion_mnist(batch_size, root, resize=None, download=True):
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))#将图片短边缩放至resize，长宽比保持不变
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(root=root, train=True, transform=trans, download=download)
    mnist_test = torchvision.datasets.FashionMNIST(root=root, train=False, transform=trans, download=download,)
    return (data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=4), 
            data.DataLoader(mnist_test, batch_size, shuffle=True, num_workers=4))


def init_weights(net):
    if isinstance(net, torch.nn.Linear):
        torch.nn.init.normal_(net.weight, mean=0., std=0.01)
        # print(net.weight)
    #此处没写完，后续断更新

#如果net为sequential结构可以使用net.apply(init_weights) ，apply函数是nn.Module中实现的, 递归地调用self.children() 去处理自己以及子模块


# 返回预测正确的个数
def accuracy(y_hat, y):  #@save
    """计算预测正确的数量"""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


# 给定模型net和数据集返回模型在这个数据集上的分类正确率
def evaluate_accuracy(net, data_iter, device=None):  #@save
    """计算在指定数据集上模型的精度"""
    # if isinstance(net, torch.nn.Module):
    #     net.eval()  # 将模型设置为评估模式
    #     if device is None:
    #         device = next(iter(net.parameters())).device
    assert isinstance(net, torch.nn.Module)
    net.eval()
    device = next(iter(net.parameters())).device
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            X = X.to(device)
            y = y.to(device)
            metric.add(accuracy(net(X), y), y.numel())
    return float(metric[0] / metric[1])


# 返回模型net在某个数据集上的平均损失
def evaluate_loss(net, data_iter, loss):
    assert isinstance(net, torch.nn.Module)
    net.eval()
    device = next(iter(net.parameters())).device
    metric = Accumulator(2)  # Sum of losses, no. of examples
    for X, y in data_iter:
        X, y = X.to(device), y.to(device)
        out = net(X)
        y = torch.reshape(y, out.shape)
        l = loss(out, y)
        metric.add(float(l.sum()), y.numel())
    return float(metric[0] / metric[1])


class Accumulator:
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


# 定义一个在动画中绘制数据的实用程序类
class Animator:
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None, ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1, figsize=(3.5, 2.5)):
        use_svg_display()
        #self.fig, self.axes = plt.subplots(nrows, ncols, figsize=figsize)
        self.fig, self.axes = plt.subplots(nrows, ncols)
        if nrows * ncols == 1:
            self.axes = [self.axes,]
        #定义了一个config_axes的函数，用于设置self.axes[0]
        self.config_axes = lambda:set_axes(self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

        self.X, self.Y, self.fmts = None, None, fmts
    # 向图表中添加多个数据点,x期望为一个数表示epoch，y期望为一个列表，里面的元素表示当前epoch的一些指标，一般为train loss, train acc, test acc
    def add(self, x, y):
        if isinstance(y, (int, float)):
            n = 1
            y = [y]
        else:
            n = len(y)
        x = [x]*n
        #创建两个二维list
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        #X与Y中的第i个列表分别对应着一条曲线的横坐标与纵坐标
        for i, (a, b) in enumerate(zip(x, y)):
            self.X[i].append(a)
            self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            # print(x, y)
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        plt.pause(0.001)
        #在jupyter中用下面两句代码
        display.display(self.fig)
        display.clear_output(wait=True)



def visit_params_and_grads(net, epoch=None):
    assert isinstance(net, torch.nn.Module)
    with torch.no_grad():
        if epoch is None:
            for name, param in net.named_parameters():
                print(f'****Params Name:{name}    Params Value:\n{param.data}')
                print(f'****Params Name:{name}    Params Grad:\n{param.grad.data}')
            
        else:
            for name, param in net.named_parameters():
                print(f'****Epoch:{epoch}    Params Name:{name}    Params Value:\n{param.data}')
                print(f'****Epoch:{epoch}    Params Name:{name}    Params Grad:\n{param.grad.data}')


def visit_params(net):
    assert isinstance(net, torch.nn.Module)
    with torch.no_grad():
        state_dict = net.state_dict()
        for key in state_dict:
            print(f'****Params Name:{key}    Params Value:\n{state_dict[key]}')
        

def monitor_grad_hook(module, grad_input, grad_output):
    if grad_output[0] is not None:
        print('loss dui  {}   OUTPUT  Grad_Shape:{}  GRAD:\n{}'.format(module, grad_output[0].shape, grad_output[0]))
    if grad_input[0] is not None:
        print('loss dui  {}   INPUT   Grad_Shape:{}  GRAD:\n{}'.format(module, grad_input[0].shape, grad_input[0]))



def train_epoch_for_classify(net, train_iter, loss, updater, device, 
                epoch=None, visit_params_before_update=False, monitor_grad=False, visit_params_and_grads_after_update=False):
    '''

    Args:

    Returns:

    '''
    assert isinstance(net, torch.nn.Module)
    net.train()
    metric = Accumulator(3)

    for X, y in train_iter:

        X, y = X.to(device), y.to(device)

        y_hat = net(X)
        l = loss(y_hat, y)
        assert isinstance(updater, torch.optim.Optimizer)
        updater.zero_grad()

        if monitor_grad:
            print('----------> next will show all networks inputs and outputs grads:')

        l.backward()

        if visit_params_before_update:
            print('----------> next will show parameters before update:')
            visit_params(net)

        updater.step()

        if visit_params_and_grads_after_update:
            print('----------> next will show parameters after updating and show parameters grads:')
            if epoch is None:
                visit_params_and_grads(net)
            else:
                visit_params_and_grads(net, epoch)

        with torch.no_grad():
            metric.add(float(l * X.shape[0]), accuracy(y_hat, y), y.numel())

    # Return training loss and training accuracy
    return float(metric[0] / metric[2]), float(metric[1] / metric[2])


def train_classify(net, train_iter, val_iter, loss, num_epochs, updater, device=torch.device('cpu'), 
    save_epoch_module_root=None, visit_params_before_update=False, monitor_grad=False, visit_params_and_grads_after_update=False):
    '''该函数提供了分类任务的训练接口, 并且会动态画图展示train_loss, train_acc, test_acc 随着epoch变化的曲线
    Args:
        net:训练的模型
        train_iter:训练数据dataloader
        val_iter:验证数据dataloader
        loss:损失函数
        num_epochs:迭代轮数
        updater:更新参数的优化器
        visit_params_before_update:是否展示在每一次batch更新参数之前的参数值
        monitor_grad:是否展示对中间变量的梯度值
        visit_params_and_grads_after_update:是否展示在每一次batch更新之后的参数值和此次更新所用的梯度值
    Returns:
        train_epoch_loss::List 训练过程中每一轮的平均损失
        train_epoch_acc::List 训练过程中每一轮的准确率
        val_epoch_acc::List 每一轮训练后在验证集上的平均损失
    '''
    assert isinstance(net, torch.nn.Module)

    handles = []
    if monitor_grad:
        for model in net.children():
            handles.append(model.register_full_backward_hook(monitor_grad_hook))

    # animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0, 1],
    #                     legend=['train loss', 'train acc', 'test acc'])

    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0, 1],
                    legend=['train loss', 'train acc', 'test acc'])

    train_epoch_loss, train_epoch_acc, val_epoch_acc = [], [], []

    net.to(device)
    print(f'---------->Training on {device}')

    for epoch in range(num_epochs):
        print(' '*30, 'Current Epoch:{}'.format(epoch))

        train_metrics = train_epoch_for_classify(net, train_iter, loss, updater, device, epoch,
                                                visit_params_before_update, monitor_grad, visit_params_and_grads_after_update)
        print(' '*30,'Current Epoch:{}'.format(epoch))

        if val_iter is not None:
            val_acc = evaluate_accuracy(net, val_iter)
            val_epoch_acc.append(val_acc)
            print('Train loss:{}, Train acc:{}, Val acc:{}'.format(train_metrics[0], train_metrics[1], val_acc))
            animator.add(epoch + 1, train_metrics + (val_acc,))
        else:
            print('Train loss:{}, Train acc:{}'.format(train_metrics[0], train_metrics[1]))             
            animator.add(epoch + 1, train_metrics)

        train_epoch_loss.append(train_metrics[0])
        train_epoch_acc.append(train_metrics[1])
        
        # save module
        if save_epoch_module_root is not None:
            path = Path(save_epoch_module_root)
            if path.is_dir() == False:
                os.makedirs(save_epoch_module_root)
            state = {'net':net.state_dict(), 
                        'updater': updater.state_dict(),
                        'epoch':epoch}
            torch.save(state, save_epoch_module_root + f'epoch-{epoch}-modules')

    if(len(handles) > 0):
        for handle in handles:
            handle.remove()
    
    plt.show()

    return train_epoch_loss, train_epoch_acc, val_epoch_acc


def train_epoch_for_regression(net, train_iter, loss, updater, device,
                                epoch=None, visit_params_before_update=False, monitor_grad=False, visit_params_and_grads_after_update=False):
    '''

    '''
    assert isinstance(net, torch.nn.Module)
    net.train()
    metric = Accumulator(2)

    for X, y in train_iter:

        X, y = X.to(device), y.to(device)

        y_hat = net(X)
        l = loss(y_hat, y)
        assert isinstance(updater, torch.optim.Optimizer)
        updater.zero_grad()

        if monitor_grad:
            print('----------> next will show all networks inputs and outputs grads:')

        l.backward()

        if visit_params_before_update:
            print('----------> next will show parameters before update:')
            visit_params(net)

        updater.step()

        if visit_params_and_grads_after_update:
            print('----------> next will show parameters after updating and show parameters grads:')
            if epoch is None:
                visit_params_and_grads(net)
            else:
                visit_params_and_grads(net, epoch)

        with torch.no_grad():
            metric.add(float(l * X.shape[0]), y.numel())

    # Return training loss
    return float(metric[0] / metric[1])


def train_regression(net, train_iter, val_iter, loss, num_epochs, updater, device=torch.device('cpu'),
    save_epoch_module_root=None, visit_params_before_update=False, monitor_grad=False, visit_params_and_grads_after_update=False):
    '''该函数提供了回归任务的训练接口, 并且会动态画图展示train_loss, test_loss 随着epoch变化的曲线
    Args:
        net:训练的模型
        train_iter:训练数据dataloader
        val_iter:验证数据dataloader
        loss:损失函数
        num_epochs:迭代轮数
        updater:更新参数的优化器
        visit_params_before_update:是否展示在每一次batch更新参数之前的参数值
        monitor_grad:是否展示对中间变量的梯度值
        visit_params_and_grads_after_update:是否展示在每一次batch更新之后的参数值和此次更新所用的梯度值
    Returns:
        train_epoch_loss::List 训练过程中每一轮的平均损失
        val_epoch_loss::List 每一轮训练后在验证集上的平均损失
    '''
    handles = []
    if isinstance(net, nn.Module):
        if monitor_grad:
            for model in net.children():
                handles.append(model.register_full_backward_hook(monitor_grad_hook))

    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0, 1],
                        legend=['train loss', 'val loss'])
    
    net.to(device)
    print(f'Training on {device}')

    train_epoch_loss, val_epoch_loss = [], []

    for epoch in range(num_epochs):
        print(' '*30, 'Current Epoch:{}'.format(epoch))

        train_metrics = train_epoch_for_regression(net, train_iter, loss, updater, device, epoch,
                                                visit_params_before_update, monitor_grad, visit_params_and_grads_after_update)
        
        print(' '*30,'Current Epoch:{}'.format(epoch))

        if val_iter is not None:
            val_loss = evaluate_loss(net, val_iter, loss)
            print('Train loss:{}, Val loss:{}'.format(train_metrics, val_loss))
            val_epoch_loss.append(val_loss)
            animator.add(epoch + 1, [train_metrics,val_loss])
        else:
            print('Train loss:{}'.format(train_metrics))
            animator.add(epoch + 1, train_metrics)

        train_epoch_loss.append(train_metrics)
        # save module
        if save_epoch_module_root is not None:
            path = Path(save_epoch_module_root)
            if path.is_dir() == False:
                os.makedirs(save_epoch_module_root)
            state = {'net':net.state_dict(), 
                        'updater': updater.state_dict(),
                        'epoch':epoch}
            torch.save(state, save_epoch_module_root + f'epoch-{epoch}-modules')

    if(len(handles) > 0):
        for handle in handles:
            handle.remove()
    
    plt.show()

    return train_epoch_loss, val_epoch_loss



def predict(net, test_iter, n = 6):
    for x, y in test_iter:
        y_hat = net(x).argmax(axis=1)
        truelabels = get_fashion_mnist_labels(y)
        prelabels = get_fashion_mnist_labels(y_hat)
        titles = ['true:'+true+'\n' + 'pre:'+pred for true, pred in zip(truelabels, prelabels)]
        show_images(x[0:n].reshape(n, 28, 28), num_rows=1, num_cols=n, titles=titles)



def get_k_fold_data(k, i, x, y):
    '''在K折交叉验证过程中返回第i折的数据,包含训练数据和验证数据
    Args:
        k:折数
        i:获取第i折数据
        x:x为tensor类型的训练数据
        y:y为tensor类型的标签
    Returns:
        x_train:第i折的训练数据
        y_train:第i折的训练数据标签
        x_valid:第i折的验证数据
        y_valid:第i折的验证数据标签
    '''
    assert k > 1
    fold_size = x.shape[0] // k
    x_train, y_train = None, None
    for j in range(k):
        idx = slice(j*fold_size, (j+1)*fold_size)
        x_part, y_part = x[idx, :], y[idx]
        if j == i:
            x_valid, y_valid = x_part, y_part
        elif x_train is None:
            x_train, y_train = x_part, y_part
        else:
            x_train = torch.cat([x_train, x_part], dim=0)
            y_train = torch.cat([y_train, y_part], dim=0)
    return x_train, y_train, x_valid, y_valid



def try_gpu(i=0):
    '''如果存在，则返回gpu(i)，否则返回cpu()
    Args:
        i:gpu编号
    Returns:
        返回相应的设备
    '''
    if torch.cuda.device_count() >= i+1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')


def try_all_gpus():
    '''返回所有可用的GPU，如果没有GPU，则返回[cpu(),]'''
    devices = [torch.device(f'cuda:{i}') for i in range(torch.cuda.device_count())]
    return devices if devices else [torch.device('cpu')]

'----------------------------------------序列数据---------------------------------------------------'

def count_corpus(tokens):
    '''统计词元频率'''
    if len(tokens) == 0 or isinstance(tokens[0], list):
        tokens = [token for line in tokens for token in line]
    return collections.Counter(tokens)

class Vocab:
    def __init__(self, tokens, min_freq=0, reserved_tokens=None):
        '''我们可以选择增加一个列表，用于保存那些被保留的词元，
        例如：填充词元（“<pad>”）；序列开始词元（“<bos>”）；序列结束词元（“<eos>”）
        '''
        if reserved_tokens is None:
            reserved_tokens = []
        # 按出现频率排序
        counter = count_corpus(tokens)
        self._token_freas = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        # 未知词元的索引为0
        self.idx_to_token = ['<unk>'] + reserved_tokens
        self.token_to_idx = {token: idx for idx, token  in enumerate(self.idx_to_token)}
        for token, freq in self._token_freas:
            if freq < min_freq:
                break
            if token not in self.token_to_idx:
                self.idx_to_token.append(token)
                self.token_to_idx[token] = len(self.idx_to_token) - 1
    
    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        '''根据tokens 返回对应的 idx'''
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk())
        return [self.token_to_idx.get(token, self.unk()) for token in tokens]
    
    def to_tokens(self, idxs):
        '''根据idxs 返回对应的 token'''
        if not isinstance(idxs, (list, tuple)):
            return self.idx_to_token[idxs]
        return [self.idx_to_token[idx] for idx in idxs]
    
    def unk(self):
        return 0

    def token_freqs(self):
        return self._token_freas


# 隐变量自回归模型训练数据准备
# 方法一：随机采样
def seq_data_iter_random(text_idxs, batch_size, num_steps):
    '''
    参数batch_size指定了每个小批量中子序列样本的数目， 
    参数num_steps是每个子序列中预定义的时间步数。
    '''
    # 从随机偏移量开始对序列进行分区，随机范围包括num_steps-1
    text_idxs = text_idxs[random.randint(0, num_steps-1):]
    # 减去1，是因为我们需要考虑标签, 得到了子序列个数
    num_subseqs = (len(text_idxs) - 1) // num_steps
    # 长度为num_steps的子序列的起始索引
    sub_seq_initial_indices = list(range(0, num_subseqs*num_steps, num_steps))
    # 在随机抽样的迭代过程中，
    # 来自两个相邻的、随机的、小批量中的子序列不一定在原始序列上相邻
    random.shuffle(sub_seq_initial_indices)

    num_batchs = num_subseqs // batch_size
    for i in range(0, num_batchs*batch_size, batch_size):
        initial_indices_per_batch = sub_seq_initial_indices[i:i+batch_size]
        X = [text_idxs[j:j+num_steps] for j in initial_indices_per_batch]
        Y = [text_idxs[j+1:j+1+num_steps] for j in initial_indices_per_batch]
        yield torch.tensor(X), torch.tensor(Y)


# 方法二：顺序分区
# 不理解
def seq_data_iter_sequential(text_idxs, batch_size, num_steps):  #@save
    """使用顺序分区生成一个小批量子序列"""
    # 从随机偏移量开始划分序列
    offset = random.randint(0, num_steps-1)
    num_tokens = ((len(text_idxs) - offset - 1) // batch_size) * batch_size
    Xs = torch.tensor(text_idxs[offset: offset + num_tokens])
    Ys = torch.tensor(text_idxs[offset + 1: offset + 1 + num_tokens])
    Xs, Ys = Xs.reshape(batch_size, -1), Ys.reshape(batch_size, -1)
    num_batches = Xs.shape[1] // num_steps
    for i in range(0, num_steps * num_batches, num_steps):
        X = Xs[:, i: i + num_steps]
        Y = Ys[:, i: i + num_steps]
        yield X, Y
        

# 整合以上两个分区函数
class SeqDataLoader:
    def __init__(self, text_idxs, batch_size, num_steps, use_random_iter=False, max_tokens=-1):
        if use_random_iter:
            self.data_iter_fn = seq_data_iter_random
        else:
            self.data_iter_fn = seq_data_iter_sequential
        self.text_idxs = text_idxs
        self.batch_size = batch_size
        self.num_steps = num_steps
    def __iter__(self):
        return self.data_iter_fn(self.text_idxs, self.batch_size, self.num_steps)


def predict_seqdata(prefix, num_preds, net, vocab, device):
    hidden = net.begin_state(batch_size=1, device=device)
    outputs = [vocab[prefix[0]]]
    get_inputs = lambda: torch.tensor([outputs[-1]], device=device).reshape((-1, 1)) 
    for y in prefix[1:]:
        _, hidden = net(get_inputs(), hidden)
        outputs.append(vocab[y])
    for _ in range(num_preds):
        y, hidden = net(get_inputs(), hidden)
        outputs.append(int(y.argmax(dim=1).reshape(1)))
    return ''.join([vocab.to_tokens(i) for i in outputs])



def truncate_pad(line, num_steps, padding_token):
    '''
    截断或填充文本序列
    '''
    if len(line) > num_steps:
        return line[:num_steps]
    return line + [padding_token] * (num_steps - len(line))


def build_array(lines, vocab, num_steps):
    lines = [vocab[line] for line in lines]
    lines = [line + [vocab['<eos>']] for line in lines]
    array = torch.tensor([truncate_pad(line, num_steps, vocab['<pad>']) for line in lines])
    valid_len = (array != vocab['<pad>']).type(torch.int32).sum(1)

    return array, valid_len


def load_data(source, target, batch_size, num_steps):
    src_vocab = Vocab(source, min_freq=2, reserved_tokens=['<pad>', '<bos>', '<eos>']) 
    tar_vocab = Vocab(target, min_freq=2, reserved_tokens=['<pad>', '<bos>', '<eos>']) 
    src_array, src_valid_len = build_array(source, src_vocab, num_steps)
    tar_array, tar_valid_len = build_array(target, tar_vocab, num_steps)
    data_arrays = (src_array, src_valid_len, tar_array, tar_valid_len)
    data_iter = load_array(data_arrays, batch_size)
    return data_iter, src_vocab, tar_vocab



class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        raise NotImplementedError


class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
    def init_state(self, enc_outputs):
        raise NotImplementedError
    def forward(self, x, state):
        raise NotImplementedError


class EncoderDecoder(nn.Module):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
    def forward(self, enc_x, dec_x):
        enc_outputs = self.encoder(enc_x)
        dec_state = self.decoder.init_state(enc_outputs)
        return self.decoder(dec_x, (dec_state, dec_state))



def grad_clipping(net, theta):
    if isinstance(net, nn.Module):
        params = [p for p in net.parameters() if p.requires_grad]
    else:
        params = net.params
    norm = torch.sqrt(sum(torch.sum((p.grad ** 2)) for p in params))
    if norm > theta:
        for p in params:
            p.grad[:] *= theta / norm



def train_epoch_seqdata(net, train_iter, loss, updater, device, use_random_iter):
    state, timer = None, Timer()
    metrics = Accumulator(2)
    for X, Y in train_iter:
        if state is None or use_random_iter:
            state = net.begin_state(batch_size=X.shape[0], device=device)
        else:
            if isinstance(state, (list, tuple)):
                for s in state:
                    s.detach_()
            else:
                state.detach_()
        y = Y.T.reshape(-1)
        X, y = X.to(device), y.to(device)
        y_hat, state = net(X, state)

        l = loss(y_hat, y)
        updater.zero_grad()
        l.backward()
        grad_clipping(net, 1)
        updater.step()
        
        metrics.add(float(l * y.numel()), int(y.numel()))
    return math.exp(metrics[0] / metrics[1]), metrics[1] / timer.stop()



def train_seqdata(net, num_epochs, train_iter, loss, updater, device, use_random_iter=False):
    animator = Animator(xlabel='epoch', ylabel='perplexity', legend=['train'], xlim=[1, num_epochs])
    if isinstance(net, nn.Module):
        net.to(device)
    for epoch in range(num_epochs):
        ppl, speed = train_epoch_seqdata(net, train_iter, loss, updater, device, use_random_iter)
        if (epoch+1) % 10 == 0:
            animator.add(epoch+1, ppl)
            # with torch.no_grad():
            #     print(predict('time traveller', 50, net, vocab, mb.try_gpu()))

    print(f'困惑度:{ppl:.1f},  {speed:.1f} 词元/秒')

    plt.show()


class RNNModel(nn.Module):
    def __init__(self, rnn_layer, vocab_size):
        super().__init__()
        self.rnn = rnn_layer
        self.vocab_size = vocab_size
        self.num_hiddens = self.rnn.hidden_size
        if not self.rnn.bidirectional:
            self.num_directions = 1
            self.linear = nn.Linear(self.num_hiddens, self.vocab_size)
        else:
            self.num_directions = 2
            self.linear = nn.Linear(self.num_hiddens*2, self.vocab_size)
        
    def forward(self, x, state):
        x = F.one_hot(x.T, self.vocab_size).to(torch.float32)
        y, state = self.rnn(x, state)
        out = self.linear(y.reshape(-1, self.num_hiddens*self.num_directions))
        return out, state
    
    def begin_state(self, batch_size, device):
        if not isinstance(self.rnn, nn.LSTM):
            return torch.zeros((self.num_directions*self.rnn.num_layers, batch_size, self.num_hiddens), device=device)
        else:
            return (torch.zeros((self.num_directions*self.rnn.num_layers, batch_size, self.num_hiddens), device=device),
                    torch.zeros((self.num_directions*self.rnn.num_layers, batch_size, self.num_hiddens), device=device))



def sequence_mask(x, valid_len, value=0):
    '''在decoder的过程中，会有‘pad’那个序列对应的隐状态传入全连接层做预测，
    这样会导致在算损失的时候也要考虑这部分，为了不考虑这部分，可以把这部分对应的预测变为0，这样再算交叉熵损失的时候这部分就会为0
    这个函数对于二维或者三维的数据x都可以用
    '''
    maxlen = x.size(1) # len of seq
    mask = torch.arange((maxlen), dtype=torch.float32, device=x.device)[None, :] < valid_len[:, None]
    x[~mask] = value
    return x

#-----------------------------------------------------attention------------------------------

def show_heatmaps(matrices, xlabel, ylabel, titles=None, figsize=(2.5, 2.5),
                  cmap='Reds'):
    """显示矩阵热图
    其输入matrices的形状是 （要显示的行数，要显示的列数，查询的数目，键的数目）
    """
    use_svg_display()
    num_rows, num_cols = matrices.shape[0], matrices.shape[1]
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize,
                                 sharex=True, sharey=True, squeeze=False)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            pcm = ax.imshow(matrix.detach().numpy(), cmap=cmap)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
            if j == 0:
                ax.set_ylabel(ylabel)
            if titles:
                ax.set_title(titles[j])
    fig.colorbar(pcm, ax=axes, shrink=0.6)


def masked_softmax(x, valid_lens):
    '''
    x: 传入的scores:batch * num_query * num_key
    valid_lens:有效的键值对个数
    '''
    if valid_lens is None:
        return nn.functional.softmax(x, dim=-1)
    else:
        shape = x.shape
        if valid_lens.dim() == 1:
            valid_lens = torch.repeat_interleave(valid_lens, shape[1], dim=0)
        else:
            valid_lens = valid_lens.reshape(-1)
        x = sequence_mask(x.reshape(-1, shape[-1]), valid_lens, value=-1e6)
    
    return nn.functional.softmax(x.reshape(shape), dim=-1)


# 带有mask的损失
class MaskedSoftmaxLoss(nn.CrossEntropyLoss):
    # pred的形状：(batch_size,num_steps,vocab_size)
    # label的形状：(batch_size,num_steps)
    # valid_len的形状：(batch_size,)
    def forward(self, pred, label, valid_len):
        weights = torch.ones_like(label)
        weights = sequence_mask(weights, valid_len)
        self.reduction = 'none' # 指定none则算完交叉熵不会自动求sum或者mean，可以指定成sum或者mean
        unweighted_loss = super().forward(pred.permute(0, 2, 1),label)#unweighted_loss:batch_size * num_steps
        weighted_loss = (unweighted_loss * weights).mean(dim = 1)
        return weighted_loss


#加性注意力（additive attention）
class AdditiveAttention(nn.Module):
    def __init__(self, key_size, query_size, num_hiddens, dropout):
        super().__init__()
        self.w_k = nn.Linear(key_size, num_hiddens, bias=False)
        self.w_q = nn.Linear(query_size, num_hiddens, bias=False)
        self.w_v = nn.Linear(num_hiddens, 1, bias=False)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, queries, keys, values, valid_lens):
        '''
        queries:batch * num_query * query_size
        keys:batch * num_key * key_size
        values:batch * num_key * 值的维度
        valid_lens:有效的键值对个数
        '''
        queries, keys = self.w_q(queries), self.w_k(keys) # queries:batch*num_query*num_hiddens, keys:batch*num_keys*num_hiddens
        #以下增加维度可以巧妙地利用广播机制实现一个样本的每个query都和这个样本对应的每个key相加
        queries = queries.unsqueeze(2) #batch*num_query*1*num_hiddens
        keys = keys.unsqueeze(1) #batch*1*num_keys*num_hiddens
        features = torch.tanh(queries + keys) #batch*num_query*num_key*num_hiddens
        scores = self.w_v(features).squeeze(-1) #batch*num_query*num_key
        self.attention_weights = masked_softmax(scores, valid_lens) #batch*num_query*num_key
        return torch.bmm(self.dropout(self.attention_weights), values) #batch*num_query*值的维度


#缩放点积注意力（scaled dot-product attention）
class DotProductAttention(nn.Module):
    def __init__(self, dropout):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
    def forward(self, queries, keys, values, valid_lens=None):
        # queries的形状：(batch_size，查询的个数，d)
        # keys的形状：(batch_size，“键－值”对的个数，d)
        # values的形状：(batch_size，“键－值”对的个数，值的维度)
        # valid_lens:有效的键值对个数
        d = queries.shape[-1]
        scores = torch.bmm(queries, keys.transpose(1, 2)) / math.sqrt(d) #batch*num_query*num_key
        self.attention_weights = masked_softmax(scores, valid_lens) #batch*num_query*num_key
        return torch.bmm(self.dropout(self.attention_weights), values)#batch*num_query*值的维度


class PositionalEncoding(nn.Module):
    """位置编码"""
    def __init__(self, num_hiddens, dropout, max_len=1000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(dropout)
        # 创建一个足够长的P
        self.P = torch.zeros((1, max_len, num_hiddens))
        X = torch.arange(max_len, dtype=torch.float32).reshape(
            -1, 1) / torch.pow(10000, torch.arange(
            0, num_hiddens, 2, dtype=torch.float32) / num_hiddens)
        self.P[:, :, 0::2] = torch.sin(X)
        self.P[:, :, 1::2] = torch.cos(X)

    def forward(self, X):
        X = X + self.P[:, :X.shape[1], :].to(X.device)
        return self.dropout(X)

class MultiHeadAttention(nn.Module):
    def __init__(self, key_size, query_size, value_size, num_hiddens, num_heads, dropout=0, bias=False):
        super().__init__()
        self.num_heads = num_heads
        self.attention = DotProductAttention(dropout = dropout)
        self.w_q = nn.Linear(query_size, num_hiddens, bias=bias)
        self.w_k = nn.Linear(key_size, num_hiddens, bias=bias)
        self.w_v = nn.Linear(value_size, num_hiddens, bias=bias)
        self.w_o = nn.Linear(num_hiddens, num_hiddens, bias=bias)
    def forward(self, queries, keys, values, valid_lens):
        #以queries为例，这里可以理解为先使用w_q将queries从query_size变到大概num_heads个头的总长度，
        #然后再把总长度切开，形成num_heads个头
        queries = transpose_qkv(self.w_q(queries), self.num_heads)   
        keys = transpose_qkv(self.w_k(keys), self.num_heads)
        values = transpose_qkv(self.w_v(values), self.num_heads)

        if valid_lens is not None:
            valid_lens = torch.repeat_interleave(valid_lens, repeats=self.num_heads, dim=0)
        output = self.attention(queries, keys, values, valid_lens)#(batch*num_heads)*num_query*num_hiddens/num_heads
        output_concat = transpose_output(output, self.num_heads) # batch * num_query * num_hiddens
        return self.w_o(output_concat)


def transpose_qkv(x, num_heads):
    '''
    x可以是query，key，value，为了多头注意力的并行，用来将这三个量变换形状
    '''
    # 输入X的形状:(batch_size，查询或者“键－值”对的个数，num_hiddens)
    # 输出X的形状:(batch_size，查询或者“键－值”对的个数，num_heads，num_hiddens/num_heads)
    x = x.reshape(x.shape[0], x.shape[1], num_heads, -1)
    # 输出X的形状:(batch_size，num_heads，查询或者“键－值”对的个数, num_hiddens/num_heads)
    x = x.permute(0, 2, 1, 3)
    # 最终输出的形状:(batch_size*num_heads,查询或者“键－值”对的个数,num_hiddens/num_heads)
    return x.reshape(-1, x.shape[2], x.shape[3])


def transpose_output(X, num_heads):
    """逆转transpose_qkv函数的操作"""
    X = X.reshape(-1, num_heads, X.shape[1], X.shape[2])
    X = X.permute(0, 2, 1, 3)
    return X.reshape(X.shape[0], X.shape[1], -1)


#--------------------------------------------动态学习率------------------------------------
# 预热+余弦学习率调度器
class CosineScheduler:
    '''会在epoch==warmup_steps时达到base_lr'''
    def __init__(self, max_update, base_lr=0.01, final_lr=0,
               warmup_steps=0, warmup_begin_lr=0):
        self.base_lr_orig = base_lr
        self.max_update = max_update
        self.final_lr = final_lr
        self.warmup_steps = warmup_steps
        self.warmup_begin_lr = warmup_begin_lr
        self.max_steps = self.max_update - self.warmup_steps

    def get_warmup_lr(self, epoch):
        increase = (self.base_lr_orig - self.warmup_begin_lr) \
                       * float(epoch) / float(self.warmup_steps)
        return self.warmup_begin_lr + increase

    def __call__(self, epoch):
        if epoch < self.warmup_steps:
            return self.get_warmup_lr(epoch)
        if epoch <= self.max_update:
            self.base_lr = self.final_lr + (
                self.base_lr_orig - self.final_lr) * (1 + math.cos(
                math.pi * (epoch - self.warmup_steps) / self.max_steps)) / 2
        return self.base_lr


#---------------------------------------目标检测相关------------------------------------------
def box_corner_to_center(boxes):
    """从（左上，右下）转换到（中间，宽度，高度）"""
    x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    w = x2 - x1
    h = y2 - y1
    boxes = torch.stack((cx, cy, w, h), axis=-1)
    return boxes

def box_center_to_corner(boxes):
    """从（中间，宽度，高度）转换到（左上，右下）"""
    cx, cy, w, h = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    x1 = cx - 0.5 * w
    y1 = cy - 0.5 * h
    x2 = cx + 0.5 * w
    y2 = cy + 0.5 * h
    boxes = torch.stack((x1, y1, x2, y2), axis=-1)
    return boxes

def bbox_to_rect(bbox, color):
    # 将边界框(左上x,左上y,右下x,右下y)格式转换成matplotlib格式：
    # ((左上x,左上y),宽,高)
    return plt.Rectangle(
        xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1],
        fill=False, edgecolor=color, linewidth=2)


def multibox_prior(img, sizes, ratios):
    """生成以每个像素为中心具有不同形状的锚框"""
    in_height, in_width = img.shape[-2:]
    device, num_sizes, num_ratios = img.device, len(sizes), len(ratios)
    boxes_per_pixel = (num_sizes + num_ratios - 1)
    size_tensor = torch.tensor(sizes, device=device)
    ratio_tensor = torch.tensor(ratios, device=device)
    # 生成锚框的所有中心点
    # 这里以0 1 2为例，中心点是0.5和1.5所以要加上0.5, /in_height是为了进行归一化
    center_h = (torch.arange(in_height, device=device) + 0.5) / in_height
    center_w = (torch.arange(in_width, device=device) + 0.5) / in_width
    shift_y, shift_x = torch.meshgrid(center_h, center_w, indexing='ij')
    shift_y, shift_x = shift_y.reshape(-1), shift_x.reshape(-1)#此时shift_y和shift_x一对一地形成了所有中心点下标
    # 生成“boxes_per_pixel”个高和宽，
    # 之后用于创建锚框的四角坐标(xmin,xmax,ymin,ymax)
    # w为一行，其中每个元素为不同的锚框的宽度
    w = torch.cat((sizes[0] * torch.sqrt(in_height * ratio_tensor[:] / in_width),
                     size_tensor[1:] * torch.sqrt(in_height * ratio_tensor[0] / in_width)))
    # h为一行，其中每个元素为不同的锚框的高度
    h = torch.cat((sizes[0] * torch.sqrt(in_width / ratio_tensor[:] / in_height), 
                     size_tensor[1:] * torch.sqrt(in_width / ratio_tensor[0] / in_height)))
    # 除以2来获得半高和半宽
    anchor_manipulations = torch.stack((-w, -h, w, h)).T.repeat(in_height * in_width, 1) / 2
    # 每个中心点都将有“boxes_per_pixel”个锚框，
    # 所以生成含所有锚框中心的网格，重复了“boxes_per_pixel”次
    out_grid = torch.stack([shift_x, shift_y, shift_x, shift_y],
                dim=1).repeat_interleave(boxes_per_pixel, dim=0)
    output = out_grid + anchor_manipulations
    # 只能返回一张图片的所有锚框
    return output.unsqueeze(0) # 1 * 锚框个数 * 4(左上和右下下标)



# 显示以图像中一个像素为中心的所有锚框
def show_bboxes(axes, bboxes, labels=None, colors=None):
    """显示所有边界框"""
    def _make_list(obj, default_values=None):
        if obj is None:
            obj = default_values
        elif not isinstance(obj, (list, tuple)):
            obj = [obj]
        return obj
    
    labels = _make_list(labels)
    colors = _make_list(colors, ['b','g','r','m','c'])
    for i, bbox in enumerate(bboxes):
        color = colors[i % len(colors)]
        rect = bbox_to_rect(bbox.detach().numpy(),color)
        axes.add_patch(rect)
        if labels and len(labels) > i:
            text_color = 'k' if color == 'w' else 'w'
            axes.text(rect.xy[0], rect.xy[1], labels[i], va='center',
                     ha='center', fontsize=9, color=text_color,
                     bbox=dict(facecolor=color, lw=0))


# 交并比(IoU)
def box_iou(boxes1,boxes2):
    # 左上右下形式坐标
    # boxes1：(boxes1的数量,4),
    # boxes2：(boxes2的数量,4),
    """计算两个锚框或边界框列表中成对的交并比"""
    box_area = lambda boxes: ((boxes[:,2] - boxes[:,0]) *
                             (boxes[:,3] - boxes[:,1]))
    areas1 = box_area(boxes1) # 锚框1的面积
    areas2 = box_area(boxes2) # 锚框2的面积
    inter_upperlefts = torch.max(boxes1[:,None,:2],boxes2[:,:2]) 
    inter_lowerrights = torch.min(boxes1[:,None,2:],boxes2[:,2:])
    inters = (inter_lowerrights - inter_upperlefts).clamp(min=0)
    # inter_areasand and union_areas的形状:(boxes1的数量,boxes2的数量)
    inter_areas = inters[:,:,0] * inters[:,:,1] # 交集的面积
    union_areas = areas1[:,None] + areas2 - inter_areas # 并集的面积
    return inter_areas / union_areas # num_box1 * num_box2



# 将真实边界框分配给锚框
def assign_anchor_to_bbox(anchors,ground_truth,device,iou_threshold=0.5):
    """将最接近的真实边界框分配给锚框"""
    num_anchors, num_gt_boxes = anchors.shape[0], ground_truth.shape[0]
    jaccard = box_iou(anchors,ground_truth) # 计算所有的锚框和真实边缘框的IOU
    anchors_bbox_map = torch.full((num_anchors,), -1, dtype=torch.long, device=device)    
    max_ious, indices = torch.max(jaccard, dim=1)#indices为每一个锚框对应的真实的边界框的标号, max_ious为每一个锚框对应的真实边界框的iou
    anc_i = torch.nonzero(max_ious >= iou_threshold).reshape(-1) #找到所有iou值>0.5的锚框的下标
    box_j = indices[max_ious >= iou_threshold]#找到所有iou值>0.5的锚框对应的真实边界框
    anchors_bbox_map[anc_i] = box_j
    #到现在上面的每一个iou>=0.5的锚框都分配了一个真实的边界框，但是此时并不一定每个真实边界框都分配到了一个锚框，
    #所以下面的代码要对每一个真实边界框进行遍历,并未其分配一个锚框
    col_discard = torch.full((num_anchors,),-1)
    row_discard = torch.full((num_gt_boxes,),-1)
    for _ in range(num_gt_boxes):
        max_idx = torch.argmax(jaccard, dim=None) # 找IOU最大的锚框,找的是全局最大的锚框
        box_idx = (max_idx % num_gt_boxes).long()
        anc_idx = (max_idx / num_gt_boxes).long()
        anchors_bbox_map[anc_idx] = box_idx
        jaccard[:,box_idx] = col_discard # 把最大Iou对应的锚框在 锚框-类别 矩阵中的一列删掉
        jaccard[anc_idx,:] = row_discard # 把最大Iou对应的锚框在 锚框-类别 矩阵中的一行删掉
    return anchors_bbox_map#返回每一个分配了边界框的锚框对应的真实边界框的下标

def offset_boxes(anchors, assigned_bb, eps=1e-6):
    """对锚框偏移量的转换"""
    c_anc = box_corner_to_center(anchors)
    c_assigned_bb = box_corner_to_center(assigned_bb)
    offset_xy = 10 * (c_assigned_bb[:, :2] - c_anc[:, :2]) / c_anc[:, 2:]
    offset_wh = 5 * torch.log(eps + c_assigned_bb[:, 2:] / c_anc[:, 2:])
    offset = torch.cat([offset_xy, offset_wh], axis=1)
    return offset # 尽量使得 offset 让 machine learning 算法好预测


# 标记锚框的类和偏移量
def multibox_target(anchors, labels):
    """使用真实边界框标记锚框"""
    batch_size, anchors = labels.shape[0], anchors.squeeze(0)
    batch_offset, batch_mask, batch_class_labels = [], [], []
    device, num_anchors = anchors.device, anchors.shape[0]
    for i in range(batch_size):
        label = labels[i,:,:]
        anchors_bbox_map = assign_anchor_to_bbox(anchors,label[:,1:],device)   
        class_labels = torch.zeros(num_anchors, dtype=torch.long,device=device)  
        assigned_bb = torch.zeros((num_anchors,4), dtype=torch.float32,device=device)   
        indices_true =torch.nonzero(anchors_bbox_map >= 0)# 分配了真实边界框的锚框下标
        bb_idx = anchors_bbox_map[indices_true] #分配了边界框的锚框对应的真实边界框的下标
        class_labels[indices_true] = label[bb_idx,0].long() + 1 #所有锚框对应的类别，0表示背景，>0表示物体, (num_anchors,)
        assigned_bb[indices_true] = label[bb_idx, 1:] #所有锚框对应的真实的边界框的坐标，num_anchors * 4
        bbox_mask = ((anchors_bbox_map >= 0).float().unsqueeze(-1)).repeat(1,4) # num_anchors * 4,没有分配真实边界框的锚框对应4个0,分配的对应4个1   
        offset = offset_boxes(anchors, assigned_bb) * bbox_mask#乘上bbox_mask是因为有的锚框对应的真实边界框坐标全是0，为了把这部分去掉, num_anchors*4
        batch_offset.append(offset.reshape(-1))
        batch_mask.append(bbox_mask.reshape(-1))
        batch_class_labels.append(class_labels)
    bbox_offset = torch.stack(batch_offset) #batch_size * (num_anchors*4)
    bbox_mask = torch.stack(batch_mask) #batch_size * (num_anchors*4)
    class_labels = torch.stack(batch_class_labels) #batch_size * num_anchors
    # bbox_offset返回每一个锚框到真实标注框的offset偏移
    # bbox_mask为0表示背景锚框，就不用了，>0表示对应真实的物体
    # class_labels为锚框对应类的编号
    return (bbox_offset, bbox_mask, class_labels)


# 应用逆偏移变换来返回预测的边界框坐标
def offset_inverse(anchors,offset_preds):
    """根据带有预测偏移量的锚框来预测边界框"""
    anc = box_corner_to_center(anchors)
    pred_bbox_xy = (offset_preds[:,:2] * anc[:,2:] / 10) + anc[:,:2]
    pred_bbox_wh = torch.exp(offset_preds[:,2:] / 5) * anc[:, 2:]
    pred_bbox = torch.cat((pred_bbox_xy, pred_bbox_wh), axis=1)
    predicted_bbox = box_center_to_corner(pred_bbox)
    return predicted_bbox # 将锚框用偏移量进行偏移，得到预测的边界框


def nms(boxes, scores, iou_threshold):
    #boxes为所有的预测框， scores为每个预测框对应的预测类别概率最大的值
    """对预测边界框的置信度进行排序"""
    B = torch.argsort(scores, dim = -1, descending=True)#得到从大到小的预测概率所对应的预测框下标
    keep = []
    while B.numel()>0: # 直到把所有框都访问过了，再退出循环
        i = B[0] # B中的预测概率最大值的下标（对应着相应的预测框）
        keep.append(i)
        if B.numel() == 1: break
        # 所有的iou大于阈值的全部去掉    
        iou = box_iou(boxes[i,:].reshape(-1,4),
                     boxes[B[1:],:].reshape(-1,4)).reshape(-1)
        inds = torch.nonzero(iou <= iou_threshold).reshape(-1) #得到所有<阈值的下标
        B = B[inds + 1]#+1是因为得到这些与最大概率预测框的iou小于阈值的预测框的在B中的下标，然后把B更新成小于阈值的预测框
    return torch.tensor(keep, dtype=torch.long, device=boxes.device)#返回未被抑制的预测框的下标


# 将非极大值抑制应用于预测边界框
def multibox_detection(cls_probs,offset_preds,anchors,nms_threshold=0.5,pos_threshold=0.009999999):
    #cls_probs:每一个预测框对每一类的预测概率，batch * num_classes * num_predicted_bb
    #offset_preds:batch * num_anchors * 4
    device, batch_size = cls_probs.device, cls_probs.shape[0]
    anchors = anchors.squeeze(0)
    num_classes, num_anchors = cls_probs.shape[1], cls_probs.shape[2]
    out = []
    for i in range(batch_size):
        cls_prob, offset_pred = cls_probs[i], offset_preds[i].reshape(-1,4) # num_anchors * 4 
        predicted_bb = offset_inverse(anchors,offset_pred) # 把预测框拿出来
        #下面conf得到不考率背景的每一个预测框的对每一类物体的最大概率值和相应的下标,classid这里变成用0代表第一类物体了
        #不考虑背景是因为在抑制的时候防止因为背景框把物体检测的框抑制了
        conf, class_id = torch.max(cls_prob ,dim = 0)
        background_indices = torch.nonzero(class_id == 0).reshape(-1)# 背景预测框的下标
        non_background_indices = torch.nonzero(class_id != 0).reshape(-1)# 非背景预测框的下标
        non_back_predictbb = predicted_bb[non_background_indices]
        non_back_conf = conf[non_background_indices]
        keep = nms(non_back_predictbb, non_back_conf, nms_threshold)
        # 获取被抑制的预测框
        non_keep = []
        for idx, _ in enumerate(non_back_predictbb):
            if idx not in keep:
                non_keep.append(idx)
        # 将被抑制的预测框的类别设置为0
        class_id[non_background_indices[non_keep]] = 0
        # 下面就是把所有预测框重新排列了一下，前面放的没有被抑制的，后面放的被抑制的
        all_sorted_indices = torch.cat((non_background_indices[keep],  #非背景框
                                        non_background_indices[non_keep],#背景框
                                        background_indices), dim=0)#背景框
        class_id = class_id[all_sorted_indices]
        conf = conf[all_sorted_indices]
        predicted_bb = predicted_bb[all_sorted_indices]
        # pos_threshold是一个用于非背景预测的阈值, 如果有预测目标概率小于pos那个值则被视为背景
        below_min_idx = (conf < pos_threshold)
        class_id[below_min_idx] = 0
        conf[below_min_idx] = 1 - conf[below_min_idx] # 增加背景的置信度
        # 返回预测的信息，共num_anchors行，每一行6个信息，分别为：类别，预测概率值，4个左上右下坐标
        pred_info = torch.cat((class_id.unsqueeze(1), conf.unsqueeze(1), predicted_bb), dim=1)
        out.append(pred_info)
    return torch.stack(out)