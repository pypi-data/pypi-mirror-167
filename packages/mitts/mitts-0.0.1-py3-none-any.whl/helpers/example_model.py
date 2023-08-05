import numpy as np
import torch as T

device = T.device("cpu")  # apply to Tensor or Module

# Modified from james mccaffrey a-minimal-pytorch-complete-example
# -----------------------------------------------------------

class Net(T.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hid1 = T.nn.Linear(4, 7)  # 4-7-3
        self.oupt = T.nn.Linear(7, 3)
        # (initialize weights)

    def forward(self, x):
        z = T.tanh(self.hid1(x))
        z = self.oupt(z)  # no softmax. see CrossEntropyLoss()
        return z


# -----------------------------------------------------------

# 0. get started
print("\nBegin minimal PyTorch Iris demo ")
T.manual_seed(1)
np.random.seed(1)

# 1. set up training data
print("\nLoading Iris train data ")

train_x = np.array([
    [5.0, 3.5, 1.3, 0.3],
    [4.5, 2.3, 1.3, 0.3],
    [5.5, 2.6, 4.4, 1.2],
    [6.1, 3.0, 4.6, 1.4],
    [6.7, 3.1, 5.6, 2.4],
    [6.9, 3.1, 5.1, 2.3]], dtype=np.float32)

train_y = np.array([0, 0, 1, 1, 2, 2], dtype=np.int64)

print("\nTraining predictors:")
print(train_x)
print("\nTraining class labels: ")
print(train_y)

train_x = T.tensor(train_x, dtype=T.float32).to(device)
train_y = T.tensor(train_y, dtype=T.long).to(device)

# 2. create network
net = Net().to(device)  # could use Sequential()

# 3. train model
max_epochs = 100
lrn_rate = 0.04
loss_func = T.nn.CrossEntropyLoss()  # applies softmax()
optimizer = T.optim.SGD(net.parameters(), lr=lrn_rate)

print("\nStarting training ")
net.train()
indices = np.arange(6)
for epoch in range(0, max_epochs):
    np.random.shuffle(indices)
    for i in indices:
        X = train_x[i].reshape(1, 4)  # device inherited
        Y = train_y[i].reshape(1, )
        optimizer.zero_grad()
        oupt = net(X)
        loss_obj = loss_func(oupt, Y)
        loss_obj.backward()
        optimizer.step()
    # (monitor error)
print("Done training ")
