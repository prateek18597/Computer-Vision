import cv2
import sys
import numpy as np
import math


file = open("list.txt","r")
names=[line.strip() for line in open('list.txt')]
img=[]
# for item in names:
image=cv2.imread("./img/lake.tif",0)
img.append(image)


def low_pass_filter(X_matrix,size):
	X=np.zeros((len(X_matrix)-size+1,len(X_matrix[0])-size+1))
	
	for j in range(0,len(X_matrix)-size+1,1):
		for k in range(0,len(X_matrix[0])-size+1,1):
			temp=0;
			for m in range(0,size,1):
				for n in range(0,size,1):
					temp+=X_matrix[j+m][k+n];
			X[j][k]=temp//9;

	return X;

image=np.array(image)
i=low_pass_filter(image,3)
i1=low_pass_filter(image,5)
i2=low_pass_filter(image,7)

print(i)
# print(image.shape)
cv2.imshow("Original",np.array(image, dtype = np.uint8))
cv2.imshow("3X3",np.array(i, dtype = np.uint8))
cv2.imshow("5X5",np.array(i1, dtype = np.uint8))
cv2.imshow("7X7",np.array(i2, dtype = np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()