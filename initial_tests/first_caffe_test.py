__author__ = 'stefjanssen'

import caffe
import numpy as np
data_path = "../../Nus-wide/1k/"

image = caffe.io.load_image("")

image_width = 240
image_height = 218

def load_images():
    train_file = open(data_path + "train.txt", 'r')
    all_images = np.asarray([])
    all_labels = np.asarray([])
    for line in file:
        temp_arr = line.split(" ")
        print temp_arr
        if temp_arr[0] != "":
            image = caffe.io.load_image(data_path + temp_arr[0])
            all_images = np.concatenate((all_images, image), axis=0)
            labels = [int(l) for l in temp_arr[1:]]
            all_labels.concatenate((all_labels, labels), axis=0)

    print "shape of data: "
    print np.shape(all_images)
    print "shape of labels: "
    print np.shape(all_labels)


if __name__ == "__main__":
    load_images()