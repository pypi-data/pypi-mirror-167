# Pokemon Card Recognizer

Recognize a Pokemon Card in an image or video.

```python
from card_recognizer.api.card_recognizer import CardRecognizer, Mode 
recognizer = CardRecognizer(
    mode=Mode.PULLS_VIDEO
)
pulls = recognizer.exec("/path/to/video")
```

Example analysis of a booster pack opening video:

![](https://github.com/prateekt/pokemon-card-recognizer/blob/75409e8ecdc32256dfc4a0a8243782152fdd406b/example2.png?raw=true)
![](https://github.com/prateekt/pokemon-card-recognizer/blob/75409e8ecdc32256dfc4a0a8243782152fdd406b/example.png?raw=true)

Benchmarks: https://docs.google.com/presentation/d/1tpEXNj3jZj0f76kt5cbCCsY58cTygakf7PuKHGJaEC8/edit?usp=sharing


    
