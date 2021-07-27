import torchvision.datasets.folder as datasets
import os.path as osp
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
import os


class ImageFolderFewShot(datasets.ImageFolder):
    """A generic data loader where the images are arranged in this way: ::
        root/dog/xxx.png
        root/dog/xxy.png
        root/dog/xxz.png
        root/cat/123.png
        root/cat/nsdf3.png
        root/cat/asd932_.png
    Args:
        root (string): Root directory path.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        loader (callable, optional): A function to load an image given its path.
     Attributes:
        classes (list): List of the class names.
        class_to_idx (dict): Dict with items (class_name, class_index).
        imgs (list): List of (image path, class_index) tuples
    """

    def __init__(self, root, transform=None, target_transform=None):
        super(ImageFolderFewShot, self).__init__(root, transform=transform, target_transform=target_transform)
        self.labels = [sample[1] for sample in self.samples]


# ROOT_PATH = '../../data/Mini-imagenet'


class MyDatasets(Dataset):
    def __init__(self, csv_path, imageSize, transform):
        # csv_path = osp.join(ROOT_PATH, setname + '.csv')
        lines = [x.strip() for x in open(csv_path, 'r').readlines()][1:]
        dataDir = os.path.dirname(csv_path)

        data = []
        label = []
        lb = -1

        self.wnids = []
        self.class_idx_to_sample_idx = {}

        for idx, l in enumerate(lines):
            name, wnid = l.split(',')
            path = osp.join(dataDir, name)
            if wnid not in self.wnids:
                self.wnids.append(wnid)
                lb += 1
                self.class_idx_to_sample_idx.update({lb: []})
            data.append(path)
            label.append(lb)
            self.class_idx_to_sample_idx[lb].append(idx)

        self.classes = self.wnids

        self.data = data
        self.labels = label
        self.transform = transform



    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        path, label = self.data[i], self.labels[i]
        image = self.transform(Image.open(path).convert('RGB'))
        return image, label