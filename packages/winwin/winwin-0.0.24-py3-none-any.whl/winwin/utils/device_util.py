# -*- coding: utf-8 -*-
# @Time    : 2022-09-13 11:39
# @Author  : zbmain


# devices
class devices():
    import torch
    torch = torch.device(torch.cuda.is_available() and 'cuda' or 'cpu')
    '''torch方式'''
    tensorflow = 'GPU:0'
    '''tensorflow方式'''
