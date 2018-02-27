# Psychic-Poker

Psychic Poker Player solution


# Requirements 
```
Python abc package
Python 2.7
```

# To Run

### Sample Run

```
python main.py
```

### Run in Docker

First build docker image in directory

```
docker build -t psychicpoker .
```

Then run docker image

```
docker run --name psychicpoker psychicpoker
```

### Run Tests

Enter tests directory and run

```
python test_card.py
```

# Sample output

```
Hand TH JH QC QD QS  Deck QH KH AH 2S 6S  Best Hand AH TH JH QH KH  (straight-flush)  
Hand 2H 2S 3H 3S 3C  Deck 2D 3D 6C 9C TH  Best Hand 2D 3D 3H 3S 3C  (four-of-a-kind)  
Hand 2H 2S 3H 3S 3C  Deck 2D 9C 3D 6C TH  Best Hand 2D 2H 2S 3H 3S  (full-house) 
Hand 2H AD 5H AC 7H  Deck AH 6H 9H 4H 3C  Best Hand AH 2H 5H 6H 7H  (flush)  
Hand AC 2D 9C 3S KD  Deck 5S 4D KS AS 4C  Best Hand AC 2D 3S 4D 5S  (straight)  
Hand KS AH 2H 3C 4H  Deck KC 2C TC 2D AS  Best Hand 2C 2D 2H TC KC  (three-of-a-kind) 
Hand AH 2C 9S AD 3C  Deck QH KS JS JD KD  Best Hand JS JD QH KS KD  (two-pairs) 
Hand 6C 9C 8C 2D 7C  Deck 2H TC 4C 9S AH  Best Hand 2H 2D 6C 7C 8C  (one-pair) 
Hand 3D 5S 2H QD TD  Deck 6S KH 9H AD QH  Best Hand  (high-card) 
```


