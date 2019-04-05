#Loading the file and returning the data

import nibabel as nib
img = nib.load('data/anon_sub-01_T1w.nii')
data = img.get_data()


#.Rotating and flipping data with numpy

import numpy as np
datarot1 = np.rot90(data, 1)
datarot2 = np.rot90(data, 3)
dataflip = np.fliplr(datarot1)

#Setting up a plot with subplots

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=[18, 6])
fig.subplots_adjust(wspace =-0.5, hspace = 1)


#Creating a function to plot each slice with correct titles

pos = 0
    
def show_slices(slices): 
    for i, dataslice  in enumerate(slices):
        
        axes[i].cla()
        
        axes[0].set_yticks([])
        axes[1].set_yticks([])
        axes[2].set_yticks([])
        axes[0].set_xticks([])
        axes[1].set_xticks([])
        axes[2].set_xticks([])
        axes[0].set_title('Sagittal', fontsize=25, color='r')
        axes[1].set_title('Coronal', fontsize=25, color='r')
        axes[2].set_title('Transversal', fontsize=25, color='r')
        axes[0].set_ylabel('Slice {}'.format(pos),fontsize=25, color="r")
        axes[i].imshow(dataslice, cmap='gray', origin='lower')

#Setting up the animation  
        
def animate(i):
    global pos
    pos += 1       

    slice_0 = dataflip[:, :, pos]
    slice_1 = datarot1[:, pos, :]
    slice_2 = datarot2[pos, :, :] 
    (show_slices([slice_0, slice_1, slice_2]))
    

#Animating and saving

import matplotlib.animation as animation

anim = animation.FuncAnimation(fig, animate, frames=190, interval=250)


#Uncomment the folowing for saving

#anim.save('video.mp4', writer='ffmpeg')
        