# ccmclient

a command line client for cc mixter that makes use of the cc mixter api. 

>ccMixter is a produsage community music site that promotes remix culture and makes >samples, remixes, and a cappella 
tracks licensed under Creative Commons available for >download and re-use in creative works. 
Visitors are able to listen to, sample, mash-up, or >interact with music in a variety 
of ways including the download and use of tracks and >samples in their own remixes.
>[https://en.wikipedia.org/wiki/CcMixter](wikipedia)

downloads the uploads from given [cc mixter](http://ccmixter.org/) artist name or selection criterias. 

based on given filter arguments (which is in the simplest form might be just a username) user generated content 
gets downloaded (files like .mp3, .flac, .mid) and packaged uploads (for example .zip files) get extracted. already 
downloaded files will not get downloaded again.

after download, just drag and drop files into your DAW without the need to manually search and select on the website, 
then download and extract the artists content.


## Install and use on win, osx, linux 

### Python

you need [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed. 

then just clone or download this repository and install the needed python packages from requirements.txt `pip3 install -r requirements.txt`

or simply use pip

        python -m pip install pyccmc

### Binaries

Binary, executable files can be found at [tigabeatz.net](https://tigabeatz.net)

## Use

### simple guided downloader

open a terminal and execute

    ccmclient

the script will ask for 

- to run in secret mixter or interactive query mode 
  
- if in secret mixter mode, you will be asked for
  - the secret mixters artist name
  - a limit to restrict the number of downloads (default = 10)

- if in itq mode, you will be asked for 
  -  to fill the ccmixter api parameters (a previously selected list of options). 
     each option, or parameter, has a short description.
  - and after a preview of what gets downloaded, you will be asked to start the download 

alternatively, execute the ccmclient.exe / binary with command line parameters like 
`ccmclient --artist tigabeatz --limit 0` or `ccmcclient.exe --help` 

usage examples:

- download everything uploaded by artist `ccmclient --artist tigabeatz --limit 0`
- download based on a custom query `ccmclient --query "{\"user\":\"tigabeatz\"}"`
- simply use the guided downloader with `ccmclient.py` (see "simple guided downloader" )

by default, the files are written to a directory structure 
from where you start the tool like `<request>\<artist>\<upload name>\<files>`

#### command line options

| -h, --help | show help and exit                                                                                                                 |
| ---------- |------------------------------------------------------------------------------------------------------------------------------------|
| --artist   | an artists name                                                                                                                    |
| --limit    | maximum allowed results                                                                                                            |
| --dryrun   | set to True if you do not want to download. prints out metadata of the query                                                       |
| --itq      | interactive query builder, download by manually search                                                                             |
| --proxy    | http(s):\\\\url:port                                                                                                               |
| --query    | json with cc mixter api   parameters        {\\"user\\":\\"tigabeatz\\";\\"limit\\":\\"1\\"}      (you must escape " with \\")     |
| --folder   | where to store your requests data, default to this scripts folder                                                                  |
| --logfile  | logfile location, default to this scripts folder                                                                                   |
| --index    | file to store history of downloaded files, defaults to this scripts folder                                                         |
| --test | check if this tool is working                                                                                                      |


## further reading

- [ccmixter thread](http://ccmixter.org/thread/4155)
