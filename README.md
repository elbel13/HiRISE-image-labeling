# HiRISE-image-labeling
This project investigates using different machine learning algorithms to correctly label landmarks from the HiRISE mars orbital images.

# Downloading the Data

NASA's HiRISE labeled image data set is publicly available. You can read more about from their [data library page](https://data.nasa.gov/Space-Science/Mars-orbital-image-HiRISE-labeled-data-set-version/egmv-36wq/about_data) and you can download it from [Zenodo](https://zenodo.org/records/4002935). You can also follow the bellow instructions.

The download is broken up between two zip files. You can download them using wget.
`wget https://zenodo.org/records/4002935/files/hirise-map-proj-v3.zip?download=1
wget hirise-map-proj-v3_2.zip?download=1`

You can then use unzip to unzip the files.
```
unzip 'hirise-map-proj-v3.zip?download=1' -d data
unzip 'hirise-map-proj-v3_2.zip?download=1' -d data
```

Verify that the data folder has the files. I find one of the quick was to do this is to check the size, which should be 2.3 GB.
```
du -sh data
```

Once you are satisfied you have succesfully downloaded all the data, go ahead and remove the zip files.
```
rm 'hirise-map-proj-v3.zip?download=1'
rm 'hirise-map-proj-v3_2.zip?download=1'
```

# Create Anoconda Environment

This repo has a `requirements.txt` file, which is intended for use in creating an Anocanda environment with all the necessary project dpendencies. If you need to install Anocanda, do so on their [download page](https://www.anaconda.com/download). If you already have Anoconda installed, you can use the following command to create the Anoconda environment:
```
conda create --name hirise-images --file requirements.txt
```

You can then start the environment with the following command:
```
conda activate hirise-images
```

# Running the Notebook Server

There are several options for running the notebook server. The simplest one is to run the server on your local machine. However, if you're using a seperate lab server (as I am), it may be more helpful to set up the server to run on start up. I will explore both options.

## Running the Server Locally

To run the server on your local machine, navigate to the `notebooks` folder and run the following command:
```
jupyter notebook
```

The notbook server will start up, and it will launch the browser window for you to access the Notbook server. If you need to open it up manually, search the output for the urls that look something like the following:
```
http://localhost:8888/tree?token=<Acess Token Here>
http://127.0.0.1:8888/tree?token=<Access Token Here>
```
You can copy either of these urls into your browser's address box to navigate to the Notebook server.

## Running the Server Remotely

To run the server remotely, you have several options. One option would be to set up public key authentication, adjust your server's firewall correctly, and access your server's url over your local network or the internet. I found a simpler yet secure solution to be create an SSH tunnel with port forwarding. For more details on this method, you can check out this [article on Medium](https://medium.com/@apbetahouse45/how-to-run-jupyter-notebooks-on-remote-server-part-1-ssh-a2be0232c533), and to learn more about tunneling applications through SSH check out this [Redhat article](https://www.redhat.com/sysadmin/ways-use-ssh).

First, on the server, navigate to the `notebooks` folder and run the following command:
```
jupyter notebook --no-browser
```
The server will generate various lines of output, including instructions for accessing the server locally. Take note of this output as we will use it after setting up tunneling.

On your local machine, run the following command to open the tunnel with port forwarding:
```
ssh -NL 8888:localhost:8888 <UserName>@<Server-IP/FQDN>
```

Now that the tunnel is open, go back to the output generated on the server and find the URLs that look something like this:
```
http://localhost:8888/tree?token=<Acess Token Here>
http://127.0.0.1:8888/tree?token=<Access Token Here>
```

Copy either of those URLs into your local browser to access the Notebook server.
