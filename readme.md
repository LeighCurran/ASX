[![buy me a coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20us%20a%20coffee-green.svg?style=for-the-badge)](https://www.buymeacoffee.com/leighcurran)
![Maintenance](https://img.shields.io/maintenance/yes/2021.svg?style=for-the-badge)

ASX is a package to pull data from https://www.asx.com.au/asx/1/share.

## Requirements
- Install Python 3.9 (for all users)
- Pip install requests

## Usage

Connect to ASX API:

    import asx
    ASX = asx.api()
    ASX.getdata(Symbol)