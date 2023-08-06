import torch

#Reshape((1, 28, 28))
#Reshape((28 * 28,))
#Reshape((28 * 28))
class Reshape(torch.nn.Module):
    def __init__(self, shape):
        super().__init__()
        self.shape = shape
        if type(self.shape) == int:
            self.shape = [self.shape]

    def forward(self, x):
        return x.view((-1, *self.shape))
        
#https://en.wikipedia.org/wiki/Dot_product
class DotProduct(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, user_id, movie_id):
        #print(user_id.shape) #torch.Size([1, 1, 100])
        #print(user_id.shape) #torch.Size([1, 1, 100])
        dot_product = (user_id * movie_id).sum(2)
        #print(dot_product.shape) #torch.Size([1, 1])
        return dot_product
        
class RNNLastOutput(torch.nn.Module):
    def __init__(self, input_size=1, hidden_size=32, batch_first=True):
        super().__init__()
        self.rnn = torch.nn.LSTM(input_size=input_size, hidden_size=hidden_size, batch_first=batch_first)
        #self.rnn = torch.nn.GRU(input_size 32, hidden_size=32, batch_first=True)

    def forward(self, x):
        #print(x.shape) #torch.Size([2, 7, 1])
        output, _ = self.rnn(x)
        #print(output.shape) #torch.Size([2, 7, 32])
        x = output[:,-1]
        #print(x.shape) #torch.Size([2, 32])
        return x
