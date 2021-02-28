# AmongUsHelper

AmongUsHelper helps you to guess who the imposter is.

## Quick Start

1. Install requirements
```
$ pip install -r requirements.txt
```

2. Edit `data.txt`
```
# participants
white, black, purple, yellow, orange, brown, cyan, lime, blue, red;

# black has been killed
dead black;
# black said purple didn't kill black
black trust purple;
# white said cyan killed black
white doubt cyan;
cyan doubt white;
# skipped
skip;

dead red;
# yellow and brown said neither lime nor white killed red
yellow, brown trust lime, white;
# orange has been ejected
eject orange;

# no one has been killed
dead none;
eject yellow;
```

3. Run `main.py`
```
$ python main.py
```

Then possible combinations of impostors will be output.
