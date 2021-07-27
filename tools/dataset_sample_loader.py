
from torch.utils.data import TensorDataset, Dataset, DataLoader, Sampler
import torch

class MyDataset(Dataset):
    def __init__(self):
        super(MyDataset, self).__init__()
        self.data = torch.tensor(list(range(100)))

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)




class MySampler(Sampler):
    def __init__(self, data_source, indices):
        super(MySampler, self).__init__(data_source)
        self.indices = indices

    def __iter__(self):
        return iter(self.indices)

    def __len__(self):
        return len(self.indices)

if __name__ == "__main__":
    labels = torch.randint(5, (100,))
    data = torch.rand(size=(100, 1))
    dataset = TensorDataset(data, labels)

    for cls in range(5):
        # dataset = MyDataset()
        indices, = torch.where(labels == cls)
        my_sampler = MySampler(dataset, indices)
        loader = DataLoader(dataset,
                            batch_size=10,
                            sampler=my_sampler,
                            drop_last=False)
        print('cls:', cls)

        for id, batch_data in enumerate(loader):
            # Do you training / evaluating here
            print('id:', id)
            print(batch_data)
            # pass