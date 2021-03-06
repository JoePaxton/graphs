##Plot for Pitches and Timbre

**Purpose**

Displays a Bar and Scatter plot for Timbres and Pitches for each Segment throughout the track (in our case it is Worldstar by Childish Gambino) outputting four plots. In addition, there is a 3D plot for Timbre and Pitches by Segment. These images will be saved to the current directory you are working in when running this program. In total, there are five plots that will be saved.

**Inspiration**

I want to expand on different visualizations on attributes for different tracks and be able to produce animation(s) while the track is playing. By learning on how to plot different attributes in a 2D and a 3D graph, it will help me manipulate animations and plots from [matplotlib] so I can store data from Echo Nest into functions that their API provides.

**Explanation**

First you need to get the Track ID from the song you want to analyze. Then you can continue making your
graph the way you want it to look using [matplotlib]. After the code below, I used a scatter and bar plot from 
the [matplotlib] API and fed the data of the mean of pitches and timbre into two different plots. 
See how I implemented [researchmodule.py] to create my graphs.

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

When creating a 3D plot, you need to first create a variable that will hold the x-axis in our case and the 
dimensions in the zeros function provided by numpy. With that variable you need to append the 3 dimensional
data (segments, pitches, and timbre) when you iterate through the segments (x-axis). When we use the scattter
function, we need to feed it all of the values that are contained in the list for segments, pitches, and timbre
instead of just feeding it the first value of the list; hence, the "strange" syntax in the indices within the
scatter function. The savefig function saves the 3D plot in the current directory you are working in. The first parameter is the name of the .png image and the second parameter 'dpi' is simply dots per inch. For resolution purposes dpi=600 seemed to be the best looking, in my opinion.

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
I used [matplotlib 3D] examples in order to figure out how to feed Echo Nest data into a 3D plot.


**Resources**
  
1. [matplotlib]
2. [matplotlib 3D]


[matplotlib]: http://matplotlib.org/
[researchmodule.py]: https://github.com/JoePaxton/graphs/blob/master/researchmodule.py
[matplotlib 3D]: http://matplotlib.org/faq/howto_faq.html#how-to-search-examples
