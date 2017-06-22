﻿# Python Geographic Visualizer (GeoVis)

![Map image of global provinces rendered with GeoVis (Data source: GADM v2)](https://raw.github.com/karimbahgat/geovis/master/images/readme_topbanner.png)

**Version: 0.2.0**

**Author: [Karim Bahgat](https://uit.academia.edu/KarimBahgat)**


## Introduction
Python Geographic Visualizer (GeoVis) is a standalone geographic visualization module for the Python programming language intended for easy everyday-use by novices and power-programmers alike. It has one-liners for quickly visualizing a shapefile, building and styling basic maps with multiple shapefile layers, and/or saving to imagefiles. Uses the built-in Tkinter or other third-party rendering modules to do its main work. The current version is functional, but should be considered a work in progress with potential bugs, so use with care. For now, only visualizes shapefiles that are in lat/long unprojected coordinate system. 


## Latest News

- April 15, 2014: New v0.2.0 released, major update. 
  - New features:
    - Symbolize shapefiles based on their attributes and add legend (categorical, equal classes, equal interval, natural breaks)
    - Choose between multiple symbolizer icons: circle, square, pyramid
    - Zoom the map to a region of interest
    - Manually draw basic geometries and write text on map
    - Functions that allow mid-script interactive user-inputs
    - Support for the Pillow version of PIL, and improved PIL quality by using antialiasing
    - Changed to MIT license to be more contributor friendly
  - Incompatible changes with previous version
    - Make and style a layer, then add to map, instead of adding to map directly from file
    - Color now has to be explicitly set and is no longer random by default
    - Support for PyCairo has been temporarily discontinued due to some difficulties, so is likely to have errors
  - Errors fixed
    - Fixed error with interactively saving image from the viewer window in PIL mode.  
- 23 Feb. 2014: A little too quick on the trigger finger for the first release. 
  - Discovered and fixed a crucial import error.   - Also expanded the README file and converted it to markdown, and added autogenerated Wiki documentation. 
- 21 Feb. 2014: First rough version of code released (v0.1.0).
  - Basic functionality
  - One liners for shapefile viewing and map saving
  - Multiple layers custom map creation
  - Customize each shapefile with colors and fillsize


## Table of Contents
- [About](#about)
  - [Dependencies](#dependencies)
  - [System Compatibility](#system-compatibility)
  - [License](#license)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Importing](#importing)
  - [Instant Mapping](#instant-mapping)
  - [Customized Maps](#customized-maps)
- [Advanced Usage](#advanced-usage)
  - [Choosing Your Renderer](#choosing-your-renderer)
  - [Zooming In](#zooming-in)
  - [Playing With Colors](#playing-with-colors)
  - [Batch Map Creation](#batch-map-creation)
- [Help and Documentation](#help-and-documentation)
- [Contributing](#contributing)
- [Thanks To](#thanks-to)


## About

### Dependencies
Technically speaking, GeoVis has no external dependencies, but it is highly recommended that you install the [Aggdraw](http://effbot.org/zone/aggdraw-index.htm), [PIL](http://www.pythonware.com/products/pil/) or [PyCairo](http://cairographics.org/pycairo/) renderer libraries to do the rendering. GeoVis automatically detects which renderer module you have and uses the first it finds in the following order (aggdraw, PIL, pycairo). If you wish to manually choose a different renderer this has to be specified for each session. If none of these are available then GeoVis will default to using the built-in Tkinter Canvas as its renderer, but due to major limitations this is not recommended for viewing larger shapefiles. 

### System Compatibility
Should work on Python version 2.x and Windows. Has not yet been tested on Python 3.x or other OS systems.

### License
Contributors are wanted and needed, so this code is free to share, use, reuse,
and modify according to the MIT license, see license.txt


## Getting Started

### Installation
1. Download the GeoVis repository folder from GitHub.
2. Either a or b:
  - a) Place the geovis folder in you Python site-packages folder for a "permanent" installation.
  - b) Or begin each session by typing `import sys` and `sys.path.append("folder path where the geovis folder is located")`.

### Importing
Assuming you have already installed it as described in the Installation section, GeoVis is imported as:

```python
import geovis
```

To begin using geovis either check out the full list of commands in the [the USER_MANUAL](../master/USER_MANUAL.md), or keep reading below for a basic introduction. 

### Instant Mapping
If you are simply wanting to inspect some shapefile interactively, or for seeing how your processed shapefile turned out, then you do this with a simple one-liner:

```python
geovis.ViewShapefile("C:/shapefile.shp")
```

If you quickly want to show someone else your shapefile over email or on a forum you can just as easily save you map to an image either by clicking the "save image" button in the interactive window viewer or with the following line:

```python
geovis.SaveShapefileImage("C:/shapefile.shp",
                   savepath="C:/output_picture.png")
```

### Customized Maps
It is also possible to build your map from scratch in order to create a more visually appealing map. 

First setup and create a newmap instance:

```python
geovis.SetMapDimensions(width=4000, height=2000)
geovis.SetMapBackground(geovis.Color("blue")
newmap = geovis.NewMap()
```

Next, each shapefile has to be loaded and symbolized into layer instances:

```python
polylayer = geovis.Layer(polypath, fillcolor=geovis.Color("random"))
pointlayer = geovis.Layer(pointpath, fillcolor=geovis.Color("random"))
```

If you wish to, you can also visualize the underlying attributes of your layer by adding one or more classifications. For instance, out point layer can be made to vary from small to large size and green to red color based on its "population" attribute:

```python
pointlayer.AddClassification(symboltype="fillsize", valuefield="population", symbolrange=[0.01,0.2], classifytype="natural breaks", nrclasses=5)
pointlayer.AddClassification(symboltype="fillcolor", valuefield="population", symbolrange=[geovis.Color("green"),geovis.Color("red")], classifytype="natural breaks", nrclasses=5)
```

In which case you will probably want to add a legend so that you can see which symbols represent which values. Let's place it in the top left corner of the map:

```python
pointlayer.AddLegend(layer=pointlayer, upperleft=[0.01,0.01], bottomright=[0.3,0.3])
```

Finally, render the layers to the newmap instance:

```python
newmap.AddToMap(polylayer)
newmap.AddToMap(pointlayer)
```

For a finishing touch, add a top-centered map title:

```python
newmap.AddText(relx=0.5, rely=0.01, text="Example Map Title", textsize=0.10, textanchor="n")
```

And save the map:

```python
newmap.SaveMap("C:/Users/BIGKIMO/Desktop/custombuiltmap.png")
```


## Advanced Usage

### Choosing Your Renderer
If you have more than one renderer and you want to choose which one to use, for instance PIL, you must do this at the beginning of each session (also, if you're going for maximum speed/less quality then enable reducing the number of vectors while you're at it, though this is not recommended for line-shapefiles):

```python
geovis.SetRenderingOptions(renderer="PIL", reducevectors=True)
```

### Zooming In
By default, the map you create will show the entire world. To zoom the map to a particular area or region of interest you simply set the zoomextents of the map, which must be done before you add your layers:

```python
geovis.SetMapZoom(x2x=[-90,90], y2y=[-45,45])
```

### Playing With Colors
There are several ways to play with the colors in your map. The most basic stylizing tool you will want to know about is the Color creator (a wrapper around [Valentin Lab's Colour module](https://pypi.python.org/pypi/colour) with added convenience functionality). You can either create a random color:

```python
randomcolor = geovis.Color("random")
```

Or you can create a specific color the way you imagine it in your head by writing the color name and optionally tweaking the color intensity and brightness (float value between 0 and 1). Let's create a strong (high intensity) but dark (low brightness) red:

```python
strongdarkred = geovis.Color("red", intensity=0.8, brightness=0.2)
```

Alternatively, instead of creating a very specific color you can create a random color that still keeps within certain limits. For instance, specifying a low brightness value and low intensity value but not specifying a color name will produce a random matte-looking color. Better yet, you can set the style argument to "matte" (among many other style names, see the documentation for the full list) which automatically chooses the brightness and intensity for you:

```python
randommattecolor = geovis.Color(style="matte")
```

Assuming you now know how to set your own colors or color styles, these colors are useful since they can be used to specify the color of any number of symbol options passed as keyword arguments to GeoVis' various rendering functions (see the documentation for a full list of changable symbol options). For instance, let's save a shapefile image as before, but this time set the fillcolor of the shapefile polygons/lines/circles to our strong-dark-red that we defined previously. In addition we will increase the outline width to match the strong fillcolor (we leave the outline *color* to its defaul black since this fits with the map):

```python
geovis.SaveShapefileImage("C:/shapefile.shp",
                   savepath="C:/output_picture.png",
                   fillcolor=strongdarkred,
                   outlinewidth=5)
```

### Batch Map Creation
Sometimes it is necessary to quickly create a gallery of images of all your shapefiles in a given directory. GeoVis provides a general utility tool that can help you do this; it loops through, parses, and returns the foldername, filename, and extension of all shapefiles in a folder tree, which in turn can be used as input for the SaveShapefileImage function. So for instance we may write it as:

```python
for eachfolder, eachshapefile, eachfiletype in geovis.ShapefileFolder(r"D:\Test Data\GPS"):
    shapefilepath = eachfolder+eachshapefile+eachfiletype
    savetopath = "C:/Users/BIGKIMO/Desktop/mapgallery/"+eachshapefile+".png"
    geovis.SaveShapefileImage(shapefilepath, savetopath)
```

The filename, parent-folder, and file extension can be played around with to do many other batch operations as well, such as placing each map image next to (in the same folder as) each shapefile. 


## Help and Documentation
This brief introduction has only covered the most essential functionality of GeoVis. 
If you need more information about or are experiencing problems with a particular function you can look up the full documentation of available functions, classes, and arguments by typing `help(geovis)`, or checking out [the USER_MANUAL](../master/USER_MANUAL.md).

If you still need help, you can either [submit an issue](https://github.com/karimbahgat/geovis/issues) here on GitHub, or contact me directly at: karim.bahgat.norway@gmail.com


## Contributing
I welcome any efforts at contributing to this project. Below are a list of current problems and limitations that I hope to change in future releases:

- The shapefiles have to be in lat/long coordinates (i.e. unprojected) in order to be displayed correctly. That is, GeoVis does not yet handle projections or coordinate transformation.
- Currently, zooming to a local scale can be made much more efficient by using spatial indexing such as QuadTree...
- I have not yet figured out how to pass PyCairo rendered images to the Tkinter window for viewing, so for now it results in an error. 
- Currently has not been tested with, and probably won't work in Python 3.x due to syntax changes, so should look into fixing this. 

---

---

---

### Thanks To
GeoVis could not have been accomplished without the excellent work of other open-source modules which it uses behind-the-scenes: 

- Several contributors over at Stackoverflow for their help with various rendering related problems and optimizations.
- Various bloggers whose code examples have in some cases been used directly in GeoVis (these parts of the code are marked with the original source)
- For shapefile reading it uses a modified version of 
[Joel Lawhead's PyShp module](http://code.google.com/p/pyshp/). 
- For color-wizardry it builds on and expands [Valentin Lab's Colour module](https://pypi.python.org/pypi/colour). 
- And offcourse it relies on the rendering of whichever renderer you are using. 
