# HiRISE-image-labeling
This project investigates using different machine learning algorithms to correctly label landmarks from the HiRISE mars orbital images.

# Downloading the Data

NASA's HiRISE labeled image data set is publicly available. You can read more about from their [data library page](https://data.nasa.gov/Space-Science/Mars-orbital-image-HiRISE-labeled-data-set-version/egmv-36wq/about_data) and you can download it from [Zenodo](https://zenodo.org/records/4002935). You can also follow the bellow instructions.

The download is broken up between two zip files. You can download them using wget.
`wget https://zenodo.org/records/4002935/files/hirise-map-proj-v3.zip?download=1
wget hirise-map-proj-v3_2.zip?download=1`

You can then use unzip to unzip the files.
`unzip 'hirise-map-proj-v3.zip?download=1' -d data
unzip 'hirise-map-proj-v3_2.zip?download=1' -d data`

Verify that the data folder has the files. I find one of the quick was to do this is to check the size, which should be 2.3 GB.
`du -sh data`

Once you are satisfied you have succesfully downloaded all the data, go ahead and remove the zip files.
`rm 'hirise-map-proj-v3.zip?download=1'
rm 'hirise-map-proj-v3_2.zip?download=1'`
