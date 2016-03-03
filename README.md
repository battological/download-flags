Download the flags of every country from Wikipedia.

You can probably just download the script and run it, but if you're having trouble, the following should work:

```
git clone https://github.com/battological/download-flags.git
cd download-flags
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python download_flags.py
```
