__author__ = 'JoePaxton'

import echonest.remix.audio as audio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
See README.md
Author: Joe Paxton
"""

def main():
    segments = audio.AudioAnalysis('TRVSKVZ1467FC8250D').segments
    collect = audio.AudioQuantumList()
    collect_t = audio.AudioQuantumList()
    
    for seg in segments:
        collect.append(seg.pitches)
        collect_t.append(seg.timbre)
        
    x=0
    y=0    
        
    for i in range(len(collect)): 
        x = i
        y = np.mean(collect[i])
        y_t = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.scatter(x, y)

    plt.title('Scatter Plot of Mean Values for Pitches by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Pitches')
    plt.savefig('Scatter_Plot_Pitches.png',dpi=600)  
    plt.show()
        
    for i in range(len(collect)): 
        x = i        
        y = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.scatter(x, y)

    plt.title('Scatter Plot of Mean Values for Timbre by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Timbre')  
    plt.savefig('Scatter_Plot_Timbre.png',dpi=600) 
    plt.show()    
    
    for i in range(len(collect)): 
        x = i
        y = np.mean(collect[i])
        y_t = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.bar(x, y)

    plt.title('Bar Plot of Mean Values for Pitches by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Pitches')
    plt.savefig('Bar_Plot_Pitches.png',dpi=600) 
    plt.show()    
        
    for i in range(len(collect)): 
        x = i        
        y = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.bar(x, y)

    plt.title('Bar Plot of Mean Values for Timbre by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Timbre')
    plt.savefig('Bar_Plot_Timbre.png',dpi=600)      
    plt.show()
    
    #3D of Timbre and Pitches by Segment
    points = np.zeros((len(segments), 3),dtype=float)    
    
    for i in range(len(segments)):        
        points[i] = ( (i, np.mean(collect[i]), np.mean(collect_t[i])) )    

    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_xlabel('Segments')
    ax.set_ylabel('Pitches')
    ax.set_zlabel('Timbre')
    ax.set_title('3D Timbre and Pitches')
    ax.scatter(points[:, 0], points[:, 1],  points[:, 2], zdir = 'z', c = '.5')    
    plt.savefig('3D_Plot_Pitch_and_Timbre.png',dpi=600) 
    plt.show()    

    return

if __name__ == '__main__':
    main()
