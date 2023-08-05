import torch
class CNNscheduler:
        def __init__(self, optimizer) -> None:
            self.scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, 0.5)
        def update(self, epoch):
            if (epoch > 100) & (epoch % 10 == 9):
                self.scheduler.step()
        def load_state_dict(self, state_dict):
            self.scheduler.load_state_dict(state_dict)
        def state_dict(self):
            return self.scheduler.state_dict()
        def get_last_lr(self):
            return self.scheduler.get_last_lr()
class SNNscheduler(CNNscheduler):
    def __init__(self, optimizer) -> None:
        super(SNNscheduler, self).__init__(optimizer)
        self.scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, [30, 60, 80, 100], gamma=0.2)
    def update(self, epoch):
        self.scheduler.step()

optimizer = torch.optim.Adam(torch.nn.Conv2d(2, 3,1,1).parameters(), lr=5e-4, weight_decay=5e-4)
lr_scheduler = SNNscheduler(optimizer)
for epoch in range(150):
    print(epoch, lr_scheduler.get_last_lr())
    lr_scheduler.update(epoch)