##Plot for Pitches and Timbre

**Purpose**

Displays a Bar and Scatter plot for Timbres and Pitches for each Segment throughout the track, outputting four plots. In addition, there is a 3D plot for Timbre and Pitches by Segment. These images will be saved to the current directory you are working in when running this program. In total, there are five plots that will be saved.

**Inspiration**

I want to expand on different visualizations on attributes for different tracks and be able to produce animation(s) while the track is playing. By learning on how to plot different attributes in a 2D and a 3D graph, it will help me understand how matplotlib stores data from Echo Nest into functions that their API provides.

**Explanation**

First you need to get the Track ID from the song you want to analyze. Then you can continue making your
graph the way you want it to look using [matplotlib]. After this, I used a scatter and bar plot from 
the [matplotlib] API and fed the data of the mean of pitches and timbre into two different plots. 

```python
import echonest.remix.audio as audio

trackID = <'TRACK_ID_OF_YOUR_FAVORITE_SONG'>
segments = audio.AudioAnalysis(trackID).segments
collect = audio.AudioQuantumList()
collect_t = audio.AudioQuantumList()

for seg in segments:
    collect.append(seg.pitches)
    collect_t.append(seg.timbre)
```

**3D plot**

When creating a 3D plot, you need to first create a variable that will hold the x-axis and the dimensions. With
that variable you need to append the 3 dimensional data (segments, pitches, and timbre) when you iterate through
the segments (x-axis). When we use the scattter function, we need to feed it all of the values that are contained
in the list for segments, pitches, and timbre instead of just feeding it the first value of the list; hence, the 
"strange" syntax in the function.

```python
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
```

**Resources**
  
1. [matplotlib]



[matplotlib]: http://matplotlib.org/

