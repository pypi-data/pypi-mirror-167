# Bellybutton Image Segmentation (bellybuttonseg)

This is a machine-learning-based image segmentation package, designed for ease of use.
Bellybutton uses a convolutional neural network, trained on images and paired user-generated masks, and outputs individually ID'd regions.
Using the package requires no coding; by editing a text file, users can edit hyper-parameters, modify data augmentation (e.g. rotate images), specify outputs and filetypes, and run training and prediction.


## Quickstart guide

### Install Bellybutton

Create a new python environment (e.g. using anaconda: shorturl.at/elRTZ)
 
```
conda create --name bellybuttonenv

```

Activate this environment (e.g. using anaconda)
 
```
conda activate bellybuttonenv

```

Download Bellybutton package 
 
```
pip install bellybuttonseg
```

### Run Bellybutton on an example dataset

Create the example directory. When this line is run, you will be prompted to select a location for the example dataset to be saved.
```
python3 -c 'from bellybuttonseg import createdir; createdir.createdir(example=1)'

```

Note that the directory you selected now has a new folder: example_project_[DATASETINFO]. Inside there folders that hold images (train, test, predict), masks, areas of interest, and outputs. We have chosen [INSERT DATASET INFO]...

[optional] Edit hyper-parameters by opening and editing [new directory]/base_parameters.txt. A complete list of parameters and their meanings is included further in this readme. 

Run Bellybutton on this dataset. When this line is run, you will be prompted to select the base folder for your project, in this case select example_project_[DATASETINFO] that you just created.

```
python3 -c 'from bellybuttonseg import createdir; createdir.runBB()'

```

The algorithm should run and you can track its progress on the command line. A new folder (whose name is based on the date and time) will be created inside example_project_[DATASETINFO]/outputs/ that will store results. Once training and prediction are completed, peruse the results inside this folder. Note that a new used_parameters.txt file has been created inside this outputs folder that stores the parameters used.

To run Bellybutton again using different parameters, edit the base_parameters.txt before executing the above code line again.


### Run Bellybutton on your own dataset

Create a directory (note: this is a slightly different line of code than creating the example directory.) When this line is run, you will be prompted to select a location AND prompted to enter a name for this project.

```
python3 -c 'import bellybuttonseg; bellybuttonseg.createdir()'

```

Move your images, masks, and (optionally) areas of interest into the appropriate folders created in this new directory.

Edit the parameters inside the parameters.txt file if desired.

Run Bellybutton on your data. Again, you will be prompted to select your project folder.

```
python3 -c 'import bellybuttonseg; bellybuttonseg.runBB()'

```

Results will be stored inside a new folder inside [yourproject]/outputs/.

Enjoy!


## Adjustable Parameters

[to be filled out]




