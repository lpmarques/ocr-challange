# OCR - Optical Character Recognition

Simple application to recognize text in an image and print it to CLI. 
The **ocr.py** script uses the pytesseract library to estimate a string approximation of the text depicted in any given image.

## Parameters
#### -i, --image
Path to the image containing the text to be recognized;
*Required* 

#### -l, --lang
Language that Tesseract uses to support word recognition;
*Not required*;
*Default*: None

#### -d, --tessdata-dir
Language that Tesseract uses to support word recognition;
*Not required*;
*Default*: Tesseract primary installation dataset

## Example run
### Input:
![](input_example/my_name.jpg)

### Output:
`LUCAS PEREIRA MARQUES`

## Deploy

### Docker container approach

After cloning the repo, build a docker image in the same directory:
```
docker build -t IMAGE_NAME .
```

Run the container while mapping the image source to the directory where the ocr script should access it:
```
docker run -ti -v IMAGE/SOURCE/PATH:/usr/image.jpg ocr
```

By default, the ocr image will have the image path set as `/usr/image.jpg`, but you can define any other path by overriding the `OCR_ARGS` env variable.
```
docker run -ti -v IMAGE/SOURCE/PATH:/NONDEFAULT/CONTAINER/PATH -e OCR_ARGS="--image /NONDEFAULT/CONTAINER/PATH --lang='eng'" ocr
```
If you wish so, you can also define other parameter values by passing it along with `--image` in `OCR_ARGS`.

### virtualenv approach

After cloning the repo, install virtualenv if you haven't yet:
```
pip3 install virtualenv
```

Create a python 3 virtual environment for your OCR run:
```
virtualenv -p python3 ocrenv
```

Activate the virtual environment:
```
source ocrenv/bin/activate
```

Install all the dependencies:

```
sudo apt-get install tesseract-ocr
pip3 install pytesseract==0.3.6
```

Finally, run the script:
```
python3 ocr.py --image PATH_TO_IMAGE
```
