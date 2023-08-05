import sys
sys.path.append("/home/shb/SpikingNeuralNetwork/") 

from SNN.datasets import CIFAR10DVS
from SNN.utils.transformer import EventReorder
import argparse
import os
import shutil
import time
import math
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
from torch.autograd import Variable
import torch.optim
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import copy
import numpy as np 
import random

parser = argparse.ArgumentParser(description='PyTorch ALTP')
parser.add_argument('--dataset', default='MNIST', type=str, help='dataset = [MNIST]')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('-b', '--batch-size', default=40, type=int,
                    metavar='N', help='mini-batch size (default: 40)')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 1e-4)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-load', default='', type=str, metavar='PATH',
                    help='path to training mask (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--lr', '--learning-rate', default=0.0005, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('-j', '--workers', default=1, type=int, metavar='N',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    help='number of data loading workers (default: 4)')
parser.add_argument('--epochs', default=120, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('--steps', default=100, type=int, metavar='N',
                    help='number of time steps to run')
parser.add_argument('--vth', default=2, type=float, metavar='vth',
                    help='threshold')
parser.add_argument('--leak', default=1, type=float, metavar='leak',
                    help='leaky parameter')
parser.add_argument('--repeat', default=3, type=int,
                    metavar='N', help='repeat (default: 1)')
parser.add_argument('--count', default=1, type=int,
                    help='count (default: 1)')  # 时间窗口内的脉冲是计数还是百分比（per)  处在后per为0
parser.add_argument('--per', default=0.25, type=float,
                    metavar='per', help='per (default: 0.25)')
parser.add_argument('--avgtimes', default=4, type=float,
                    metavar='avgtimes', help='avgtimes (default: 9)')

parser.add_argument('--hz', default=5, type=int, metavar='hz',
                    help='scale update hz')
parser.add_argument('--device', default=0, type=int, metavar='device',
                    help='device id for gpu')
parser.add_argument('--gpus', default='0', type=str,
                    help='id(s) for CUDA_VISIBLE_DEVICES')
parser.add_argument('--change', type=int, nargs='+', default=[30, 60, 80, 100],
                    help='Decrease learning rate at these epochs.')
parser.add_argument('--lr_gama', type=int, nargs='+', default=[0.2, 0.2, 0.2, 0.2],
                    help='lr change gama times at each point.')
parser.add_argument('--seed', type=int, help='manual seed')
parser.add_argument('--sign', type=int, help='scale sign')
parser.add_argument('--data_path', default='/home/shb/datasets/CIFAR10DVS', type=str,
                    help='data_set_path')        

def SNNpadding(img, border=None, fill=0):
    # CHWT
    if isinstance(border, tuple):
        if len(border) == 2:
            left, top = right, bottom = border
        elif len(border) == 4:
            left, top, right, bottom = border
    else:
        left = top = right = bottom = border
    return np.pad(img, ((0, 0), (top, bottom), (left, right), (0, 0)), mode='constant', constant_values=fill)

class RandomCrop(object):
    """Crop the given DVS at a random location.
    input ndarray
    """

    def __init__(self, size, padding=None, pad_if_needed=False, fill=0, padding_mode='constant'):
        if isinstance(size, tuple):
            self.size = size
        else:
            self.size = (int(size), int(size))
        self.padding = padding
        self.pad_if_needed = pad_if_needed
        self.fill = fill
        self.padding_mode = padding_mode

    @staticmethod
    def get_params(img, output_size):
        """Get parameters for ``crop`` for a random crop.

        Args:
            img : Image to be cropped CHWT.
            output_size (tuple): Expected output size of the crop.

        Returns:
            tuple: params (i, j, h, w) to be passed to ``crop`` for random crop.
        """
        h, w = img.shape[1], img.shape[2]
        th, tw = output_size
        if w == tw and h == th:
            return 0, 0, h, w

        i = random.randint(0, h - th)
        j = random.randint(0, w - tw)
        return i, j, th, tw

    def __call__(self, img):
        """
        Args:
            img (ndarray): CHWT to be cropped.

        Returns:
            img (ndarray): Cropped image.
        """
        if self.padding is not None:
            img = SNNpadding(img, self.padding, self.fill)

        i, j, h, w = self.get_params(img, self.size)

        return img[:, i:i+h, j:j+w, :].copy()

    def __repr__(self):
        return self.__class__.__name__ + '(size={0}, padding={1})'.format(self.size, self.padding)

class RandomTranspose(object):
    """Horizontally flip the given ndarray randomly with a given probability.

    Args:
        p (float): probability of the image being flipped. Default value is 0.5
    """

    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, img):
        """
        Args:
            img (ndarray): CHWT to be transpose.

        Returns:
            img (ndarray): transposed image.
        """
        if random.random() < self.p:
            return img.swapaxes(1, 2).copy()
        return img

    def __repr__(self):
        return self.__class__.__name__ + '(p={})'.format(self.p)

class RandomHorizontalFlip(object):
    """Horizontally flip the given ndarray randomly with a given probability.

    Args:
        p (float): probability of the image being flipped. Default value is 0.5
    """

    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, img):
        """
        Args:
            img (ndarray): Image to be flipped.

        Returns:
            ndarray: Randomly flipped image.
        """
        if random.random() < self.p:
            return np.flip(img, 2).copy()
        return img

    def __repr__(self):
        return self.__class__.__name__ + '(p={})'.format(self.p)


args = parser.parse_args()

os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus

def setRandom():
    if args.seed is None:
        args.seed = random.randint(1, 10000)
    print('seed:', args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    np.random.seed(args.seed)
    random.seed(args.seed)
    # cudnn.benchmark = False
    # cudnn.deterministic = True
    cudnn.benchmark = True


def main():
    device = torch.device(f'cuda:{args.device}')
    torch.cuda.set_device(device)
    seed1 = 44
    seed2 = 85
    seed3 = 63
    torch.manual_seed(seed1)
    torch.cuda.manual_seed(seed2)
    torch.cuda.manual_seed_all(seed3)
    np.random.seed(seed1)
    random.seed(seed2)
    cudnn.benchmark = False
    cudnn.deterministic = True
    
    print('\n'+'='*15+'settings'+'='*15)
    print('pid:', os.getpid())
    print('lr: ', args.lr)
    print('change lr point:', args.change)
    print('change gama', args.lr_gama)
    print('batchsize:',args.batch_size)
    print('epochs:', args.epochs)
    print('steps:', args.steps)
    print('vth:', args.vth)
    print('leak:{}'.format(args.leak))
    print('hz:{}'.format(args.hz))
    print('repeat:{}'.format(args.repeat))
    print('count={}'.format(args.count))
    print('per={}'.format(args.per))
    print('='*15+'settings'+'='*15+'\n')

    best_prec1 = 0
    ep = []
    lRate = []   
    tp1_5_loss_tr = []
    tp1_5_loss_eval = []

    model = SNN(args)

    print(model)
    
    model.to(device)
    
    criterion = torch.nn.MSELoss(reduction='sum')
    criterion_en = torch.nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay) #

    # optionally resume from a checkpoint
    if args.resume:
        if os.path.isfile(args.resume):
            print("=> loading checkpoint '{}'".format(args.resume))
            checkpoint = torch.load(args.resume, map_location=device)
            args.start_epoch = checkpoint['epoch']
            best_prec1 = checkpoint['best_prec1']
            model.load_state_dict(checkpoint['state_dict'])
            optimizer.load_state_dict(checkpoint['optimizer'])
            print("=> loaded checkpoint '{}' (epoch {})"
                  .format(args.resume, checkpoint['epoch']))
            args.warmup = 0
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))

    # Dataloader
    time_read1 = time.time()
    normalize = transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], std=[0.557, 0.549, 0.5534])
    transform_train = transforms.Compose([
        # RandomTranspose(1),
        # RandomCrop(128, padding=16),
        # RandomHorizontalFlip(),
        # EventReorder((0, 2, 1, 3))
        # transforms.ToTensor(),
        # normalize,
    ])
    train_data = CIFAR10DVS(args.data_path, download=False, step=args.steps, subSet="Train",
                transform=transform_train, target_transform=None)
    train_loader = torch.utils.data.DataLoader(train_data,
                                               batch_size=args.batch_size, shuffle=True,
                                               num_workers=args.workers,
                                               pin_memory=True)
    time_read1 = time.time() - time_read1
    print('read data of testing takes %dh %dmin' %
          (time_read1/3600, (time_read1 % 3600)/60))

    time_read1 = time.time()
    transform_test = transforms.Compose([
        # transforms.ToTensor(),
        # normalize,
    ])
    val_data = CIFAR10DVS(args.data_path, step = args.steps, subSet="Test", 
                        transform=transform_test)
    val_loader = torch.utils.data.DataLoader(val_data,  # val_data for testing
                                             batch_size=int(args.batch_size/2), shuffle=False,
                                             num_workers=args.workers,
                                             pin_memory=False)
    time_read1 = time.time() - time_read1
    print('read data of testing takes %dh %dmin' %
          (time_read1/3600, (time_read1 % 3600)/60))
    print('read dataset done')
    if args.evaluate:
        validate(val_loader, model, criterion, criterion_en, time_steps=args.steps, leak=args.leak, device=device)
        return

    for epoch in range(args.start_epoch, args.epochs):
        for name, wmax, wmin, wmean in getALTPw(model):
            print(name, wmax, wmin, wmean)
        if epoch % args.hz == 0 and args.hz < args.epochs:
            args.sign = 1
        else:
            args.sign = 0

        start = time.time()
        args.lr = adjust_learning_rate(optimizer, epoch, args.lr)
        lRate.append(args.lr)
        ep.append(epoch)

        # train for one epoch
        tp1_5_loss_tr.append(train(train_loader, model, criterion, criterion_en, optimizer, epoch, 
                            time_steps=args.steps, leak=args.leak, device=device))

        # evaluate on validation set
        modeltest = model
        tp1_5_loss_eval.append(validate(val_loader, modeltest, criterion, criterion_en, 
                                time_steps=args.steps, leak=args.leak, device=device))
        prec1 = tp1_5_loss_eval[-1][0]

        # remember best prec@1 and save checkpoint
        is_best = prec1 > best_prec1
        best_prec1 = max(prec1, best_prec1)
        save_checkpoint({
            'epoch': epoch + 1,
            'state_dict': model.state_dict(),
            'best_prec1': best_prec1,
            'optimizer': optimizer.state_dict(),
        }, is_best, epoch, prec1)
        time_use = time.time() - start
        print('time used this epoch: %d h%dmin%ds' %(time_use//3600,(time_use%3600)//60,time_use%60))

        if args.sign:
            print('\n'+'='*15+'scale'+'='*15)            
            for name, scale in getScales(model):
                print(name, scale)
            print('='*15+'scale'+'='*15+'\n')


    for k in range(0, args.epochs - args.start_epoch):
        print('Epoch: [{0}/{1}]\t'
              'LR:{2}\t'
              'Prec@1 {top1:.3f} \t'
              'Prec@5 {top5:.3f} \t'
              'En_Loss_Eval {losses_en_eval: .4f} \t'
              'Prec@1_tr {top1_tr:.3f} \t'
              'Prec@5_tr {top5_tr:.3f} \t'
              'En_Loss_train {losses_en: .4f}'.format(
            ep[k], args.epochs, lRate[k], top1=tp1_5_loss_eval[k][0], top5=tp1_5_loss_eval[k][1], losses_en_eval=tp1_5_loss_eval[k][2], 
            top1_tr=tp1_5_loss_tr[k][0], top5_tr=tp1_5_loss_tr[k][1], losses_en=tp1_5_loss_tr[k][2]))
    print('best_acc={}'.format(best_prec1))



def grad_cal(scale, IF_in):
    out = scale * IF_in.gt(0).type(torch.cuda.FloatTensor)
    return out

def ave(output, input):
    c = input >= output
    if input[c].sum() < 1e-3:
        return 1
    return output[c].sum()/input[c].sum()


def train(train_loader, model, criterion, criterion_en, optimizer, epoch, time_steps, leak, device):
    # switch to train mode
    model.train()

    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()
    top5 = AverageMeter()

    top1_tr = AverageMeter()
    top5_tr = AverageMeter()
    losses_en = AverageMeter()


    end = time.time()
    start_end = end 
    for i, (input, target) in enumerate(train_loader):
        # if args.warmup != 0 and args.warm_iter < args.warmup:
        #     adjust_warmup_lr(optimizer, args.warm_iter, args.warmup)
        #     args.warm_iter += 1
        # measure data loading time
        data_time.update(time.time() - end)
        input, target = input.to(device), target.to(device)
        # input, targets_a, targets_b, lam = mixup_data(input, target, 1.)
        label = target.clone()
        # labels_b = targets_b.clone()

        optimizer.zero_grad()  # Clear gradients w.r.t. parameters

        output = model(input, steps=time_steps, l=leak)
        
        targetN = output.data.clone().zero_().to(device)
        targetN.scatter_(1, target.unsqueeze(1), 1)
        targetN = Variable(targetN.type(torch.cuda.FloatTensor))

        # targetN_b = output.data.clone().zero_().to(device)
        # targetN_b.scatter_(1, targets_b.unsqueeze(1), 1)
        # targetN_b = Variable(targetN_b.type(torch.cuda.FloatTensor))

        # loss = mixup_criterion(criterion, output.cpu(), targetN_a.cpu(), targetN_b.cpu(), lam)
        # loss_en = mixup_criterion(criterion_en, output.cpu(), labels_a.cpu(), labels_b.cpu(), lam)
        loss = criterion(output.cpu(), targetN.cpu())
        loss_en = criterion_en(output.cpu(), label.cpu())

        # measure accuracy and record loss
        prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
        losses.update(loss.item(), input.size(0))
        top1.update(prec1.item(), input.size(0))
        top5.update(prec5.item(), input.size(0))

        prec1_tr, prec5_tr = accuracy(output.data, target, topk=(1, 5))
        losses_en.update(loss_en.item(), input.size(0))
        top1_tr.update(prec1_tr.item(), input.size(0))
        top5_tr.update(prec5_tr.item(), input.size(0))

        # compute gradient and do SGD step
        loss.backward(retain_graph=False)
        optimizer.step()


        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()
    
    
    print('Epoch: [{0}] Prec@1 {top1_tr.avg:.3f} Prec@5 {top5_tr.avg:.3f} Entropy_Loss {loss_en.avg:.4f}'
          .format(epoch, top1_tr=top1_tr, top5_tr=top5_tr, loss_en=losses_en))
    time_use = end - start_end
    print('train time: %d h%dmin%ds' %(time_use//3600,(time_use%3600)//60,time_use%60))

    return top1_tr.avg, top5_tr.avg, losses_en.avg

def validate(val_loader, model, criterion, criterion_en, time_steps, leak, device):
    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()
    top5 = AverageMeter()
    losses_en_eval = AverageMeter()

    # switch to evaluate mode
    model.eval()

    end = time.time()
    with torch.no_grad():
        for i, (input, target) in enumerate(val_loader):
	        # measure data loading time
            data_time.update(time.time() - end)
            input_var = input.to(device)
            labels = Variable(target.to(device))
            target = target.to(device)
            output = model.tst(input_var, steps=time_steps, l=leak)

            targetN = output.data.clone().zero_().to(device)
            targetN.scatter_(1, target.unsqueeze(1), 1)
            targetN = Variable(targetN.type(torch.cuda.FloatTensor))
            loss = criterion(output.cpu(), targetN.cpu())
            loss_en = criterion_en(output.cpu(), labels.cpu())
	        # measure accuracy and record loss
            prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
            losses.update(loss.item(), input.size(0))
            top1.update(prec1.item(), input.size(0))
            top5.update(prec5.item(), input.size(0))
            losses_en_eval.update(loss_en.item(), input.size(0))

            # measure elapsed time
            batch_time.update(time.time() - end)
            end = time.time()

    print('Test: Prec@1 {top1.avg:.3f} Prec@5 {top5.avg:.3f} Entropy_Loss {losses_en_eval.avg:.4f}'
          .format(top1=top1, top5=top5, losses_en_eval=losses_en_eval))

    return top1.avg, top5.avg, losses_en_eval.avg


def save_checkpoint(state, is_best, epoch, prec1, filename='checkpoint_latest.pth.tar'):
    path = "./ckp/"
    if not os.path.exists(path):
        os.mkdir(path)
    torch.save(state,path + filename)
    if is_best:
        shutil.copyfile(path + filename, path + "best_" + str(epoch) + '_' + str(prec1) + '_' + filename)


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def adjust_learning_rate(optimizer, epoch, lr):
    """Sets the learning rate to the initial LR decayed by 10 every 30 epochs"""
    if epoch in args.change:
        id = args.change.index(epoch)
        lr *= args.lr_gama[id]
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr
    return lr

def adjust_warmup_lr(optimizer, citer, warmup):
    print('warm up:', args.lr * (citer + 1.) / warmup)
    for param_group in optimizer.param_groups:
        param_group['lr'] = args.lr * (citer + 1.) / warmup

def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].reshape(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res

class Neuron(nn.Module):
    def __init__(self, response_func, threshold, leak, _scale=1, pool=False, out=False, name="neuron") -> None:
        super(Neuron, self).__init__()
        self.response_func = response_func
        self.threshold = threshold
        self.leak = leak
        self.name = name
        self._scale = torch.nn.parameter.Parameter(torch.tensor(_scale), requires_grad=False)
        self.pool = pool
        self.out = out
    
    def reset(self, soma_in, mem, soma_out):
        # torch.autograd.Variable(torch.zeros((batch_size, *self.in_shape), device=device), requires_grad=False)  # will not add in optimizer
        self.soma_in = soma_in
        self.mem = mem
        self.soma_out = soma_out

    def snn_forward(self, response_func_input):
        soma_in = self.response_func(response_func_input)
        self.soma_in += soma_in
        self.mem += soma_in
        # 后面再修改threshold， gt成一个函数
        ex_membrane = nn.functional.threshold(self.mem, self.threshold, 0)
        self.mem = self.mem - ex_membrane # hard reset
        # generate spike
        soma_out = ex_membrane.gt(0).type(torch.cuda.FloatTensor)
        if not self.pool:
            self.mem = self.leak * self.mem
        self.soma_out += soma_out
        return soma_out
    
    def updateScale(self, sign):
        if sign:
            self._scale.data = 0.6 * ave(self.soma_out, self.soma_in) + 0.4 * self._scale.data
        self.scale = grad_cal(self._scale.data, self.soma_in)

    def forward(self, sum_x):
        sum_y = self.response_func(sum_x)
        out = torch.mul(sum_y, self.scale)
        return out - out.detach() + self.soma_out.detach()
 
class ALTP_D(nn.Module):
    def __init__(self, shape, ones=True, bias: bool = False, device=None) -> None:
        factory_kwargs = {'device': device}
        super(ALTP_D, self).__init__()
        self.shape = shape
        self.ones = ones
        self.weight = torch.nn.parameter.Parameter(torch.empty(shape, **factory_kwargs))
        if bias:
            self.bias = torch.nn.parameter.Parameter(torch.empty(shape, **factory_kwargs))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self) -> None:
        if self.ones:
            torch.nn.init.normal_(self.weight, mean=0.2339, std=0.3971) # from s150's ckp
        else:
            torch.nn.init.zeros_(self.weight)
        if self.bias is not None:
            torch.nn.init.zeros_(self.bias)

    def forward(self, input: torch.Tensor):
        re = input.mul(self.weight.relu())
        if self.bias is not None:
            re = re.add(self.bias)
        return re

    def extra_repr(self) -> str:
        return 'shape={}, bias={}'.format(self.shape, self.bias is not None)

class ResponseFunc(nn.Module):
    def __init__(self, separate, share_func) -> None:
        super(ResponseFunc, self).__init__()
        self.separate = separate
        self.share_func = share_func

    def forward(self, x):
        out = self.separate(x)
        return self.share_func(out.detach())+out

def getScales(model: nn.Module):
    re = []
    for name, m in model.named_modules():
        if isinstance(m, Neuron):
            re.append((name, m._scale))
    return re

def getALTPw(model: nn.Module):
    re = []
    for name, m in model.named_modules():
        if isinstance(m, ALTP_D):
            re.append((name, m.weight.max(), m.weight.min(), m.weight.mean()))
    return re

def mixup_data(x, y, alpha=1.0, use_cuda=True):
    '''Returns mixed inputs, pairs of targets, and lambda'''
    if alpha > 0:
        lam = np.random.beta(alpha, alpha)
    else:
        lam = 1

    batch_size = x.size()[0]
    if use_cuda:
        index = torch.randperm(batch_size).cuda()
    else:
        index = torch.randperm(batch_size)

    mixed_x = lam * x + (1 - lam) * x[index, :]
    y_a, y_b = y, y[index]
    return mixed_x, y_a, y_b, lam

def mixup_criterion(criterion, pred, y_a, y_b, lam):
    return lam * criterion(pred, y_a) + (1 - lam) * criterion(pred, y_b)


class SNN(nn.Module):
    def __init__(self, args) -> None:
        super(SNN, self).__init__()
        device = torch.device(f'cuda:{args.device}')
        self.maxpool4 = nn.AvgPool2d(kernel_size=3)
        conv11 = nn.Conv2d(in_channels=2, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        # share11 = ALTP((args.batch_size, 64, 32, 32), device)
        self.neuron11 = Neuron(conv11, args.vth, args.leak)
        conv12 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        # share12 = ALTP((args.batch_size, 64, 32, 32), device)
        self.neuron12 = Neuron(conv12, args.vth, args.leak)
        avgpool1 = nn.AvgPool2d(kernel_size=2)
        self.neuronp1 = Neuron(avgpool1, 0.75, args.leak, pool=True)
        
        conv21 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1, bias=False)
        self.neuron21 = Neuron(conv21, args.vth, args.leak)
        conv22 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1, bias=False)
        self.neuron22 = Neuron(conv22, args.vth, args.leak)
        conv23 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1, bias=False)
        self.neuron23 = Neuron(conv23, args.vth, args.leak)
        self.avgpool2 = nn.MaxPool2d(kernel_size=2)

        fc0 = nn.Linear(256 * 10 * 10, 1024, bias=False)
        shareF0 = ALTP_D((1024), device=device)
        self.neuronf0 = Neuron(ResponseFunc(fc0, shareF0), args.vth, args.leak)
        self.classifier = nn.Linear(1024, 10, bias=False)
        self.classifier.threshold = args.vth
        
        self._weight_init()

    def forward(self, input_x, steps, l=1):
        self.reset_mem()
        total_input = 0
        with torch.no_grad():
            for i in range(steps * args.repeat):
                # Poisson input spike generation
                eventframe_input = input_x[:, :, :, :, i % steps].float()
                eventframe_input = args.avgtimes * self.maxpool4(eventframe_input)
                total_input += eventframe_input
                spike = self.neuron11.snn_forward(eventframe_input)
                spike = self.neuron12.snn_forward(spike)
                spike = self.neuronp1.snn_forward(spike)
                spike = self.neuron21.snn_forward(spike)
                spike = self.neuron22.snn_forward(spike)
                spike = self.neuron23.snn_forward(spike)

                fc_in = self.avgpool2(spike).view(input_x.size(0), -1)

                spike = self.neuronf0.snn_forward(fc_in)
            self.updateScale(args.sign)
        with torch.enable_grad():
            spike = self.neuron11(total_input)
            spike = self.neuron12(spike)
            spike = self.neuronp1(spike)
            spike = self.neuron21(spike)
            spike = self.neuron22(spike)
            spike = self.neuron23(spike)

            fc_in = self.avgpool2(spike).view(input_x.size(0), -1)

            character = self.neuronf0(fc_in)
            out = self.classifier(character)
        return out / self.classifier.threshold / steps
    
    def tst(self, input_x, steps=100, l=1):
        # 注意这里没有reset 
        # 效果跑完再和上面合并，并且out可以测试分开conv和集中conv的效果，上面训练也可以改成集中conv
        self.reset_mem()
        out = 0
        with torch.no_grad():
            for i in range(steps * args.repeat):
                # Poisson input spike generation
                eventframe_input = (input_x[:, :, :, :, (i % steps)]).float()
                eventframe_input = args.avgtimes * self.maxpool4(eventframe_input)
                spike = self.neuron11.snn_forward(eventframe_input)
                spike = self.neuron12.snn_forward(spike)
                spike = self.neuronp1.snn_forward(spike)
                spike = self.neuron21.snn_forward(spike)
                spike = self.neuron22.snn_forward(spike)
                spike = self.neuron23.snn_forward(spike)

                fc_in = self.avgpool2(spike).view(input_x.size(0), -1)

                spike = self.neuronf0.snn_forward(fc_in)
                out += self.classifier(spike)
            return out / self.classifier.threshold / steps
        

    def updateScale(self, sign):
        for m in self.modules():
            if isinstance(m, Neuron):
                m.updateScale(sign)

    def reset_mem(self):
        for m in self.modules():
            if isinstance(m, Neuron):
                m.reset(0, 0, 0)
        

    def _weight_init(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.in_channels
                variance1 = math.sqrt(2.0 / n)
                m.weight.data.normal_(0, variance1)
                # define threshold
                # m.threshold = args.vth

            elif isinstance(m, nn.Linear):
                size = m.weight.size()
                fan_in = size[1]  # number of columns
                variance2 = math.sqrt(2.0 / fan_in)
                m.weight.data.normal_(0.0, variance2)
                # define threshold
                # m.threshold = args.vth 


if __name__ == '__main__':
    main()
