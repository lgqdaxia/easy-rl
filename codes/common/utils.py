#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2021-03-12 16:02:24
LastEditor: John
LastEditTime: 2022-07-20 23:53:34
Discription: 
Environment: 
'''
import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import json

from matplotlib.font_manager import FontProperties  # 导入字体模块

def chinese_font():
    ''' 设置中文字体，注意需要根据自己电脑情况更改字体路径，否则还是默认的字体
    '''
    try:
        font = FontProperties(
        fname='/System/Library/Fonts/STHeiti Light.ttc', size=15) # fname系统字体路径，此处是mac的
    except:
        font = None
    return font

def plot_rewards_cn(rewards, ma_rewards, cfg, tag='train'):
    ''' 中文画图
    '''
    sns.set()
    plt.figure()
    plt.title(u"{}环境下{}算法的学习曲线".format(cfg.env_name,
              cfg.algo_name), fontproperties=chinese_font())
    plt.xlabel(u'回合数', fontproperties=chinese_font())
    plt.plot(rewards)
    plt.plot(ma_rewards)
    plt.legend((u'奖励', u'滑动平均奖励',), loc="best", prop=chinese_font())
    if cfg.save:
        plt.savefig(cfg.result_path+f"{tag}_rewards_curve_cn")
    # plt.show()


def plot_rewards(rewards, ma_rewards, cfg, tag='train'):
    sns.set()
    plt.figure()  # 创建一个图形实例，方便同时多画几个图
    plt.title("learning curve on {} of {} for {}".format(
        cfg.device, cfg.algo_name, cfg.env_name))
    plt.xlabel('epsiodes')
    plt.plot(rewards, label='rewards')
    plt.plot(ma_rewards, label='ma rewards')
    plt.legend()
    if cfg.save_fig:
        plt.savefig(cfg.result_path+"{}_rewards_curve".format(tag))
    plt.show()


def plot_losses(losses, algo="DQN", save=True, path='./'):
    sns.set()
    plt.figure()
    plt.title("loss curve of {}".format(algo))
    plt.xlabel('epsiodes')
    plt.plot(losses, label='rewards')
    plt.legend()
    if save:
        plt.savefig(path+"losses_curve")
    plt.show()

def save_results_1(dic, tag='train', path='./results'):
    ''' 保存奖励
    '''
    for key,value in dic.items():
        np.save(path+'{}_{}.npy'.format(tag,key),value)
    print('Results saved！')
    
def save_results(rewards, ma_rewards, tag='train', path='./results'):
    ''' 保存奖励
    '''
    np.save(path+'{}_rewards.npy'.format(tag), rewards)
    np.save(path+'{}_ma_rewards.npy'.format(tag), ma_rewards)
    print('Result saved!')


def make_dir(*paths):
    ''' 创建文件夹
    '''
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def del_empty_dir(*paths):
    ''' 删除目录下所有空文件夹
    '''
    for path in paths:
        dirs = os.listdir(path)
        for dir in dirs:
            if not os.listdir(os.path.join(path, dir)):
                os.removedirs(os.path.join(path, dir))

def save_args(args):
    # save parameters    
    args_dict = vars(args)   
    with open(args.result_path+'params.json', 'w') as fp:
        json.dump(args_dict, fp)   
    print("Parameters saved!")
    