
|variable|  description   |
|----|----|
|n_episodes_train| numbers of episode in one epoch train |
|n_way_train| numbers of class in one episode train |
|n_support|numbers of support images, it indicates the k shot|
|n_query|numbers of query images|
|samples_indices|a list ,length is the number of total classes,each object is the indexes of the images of corresponding class|


# mini imagenet
- Each class has 600 images
- Datasets partition 

|type|numbers of classes| 
|---|----| 
|train|64|
|test|20|
|val|16|

