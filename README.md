# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Akhmad045/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Akhmad045/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for the [make.fun bounty "The Tired Dark Lord: A 100-Word Villain Monologue"](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb): one monologue of about 100 words, spoken by a fantasy villain who is secretly just very tired.

## The monologue

> You have caught me mid-sentence, which is rude, and mid-tea, which is worse. The teapot, by the way, holds my soul — do mind the handle. Three centuries I have kept this tower: the ravens fed, the curses filed, the heroes buried in the east garden, alphabetically. You want the amulet? It is on the shelf, behind the jam. Take it. Take it all. Only — when the villagers cheer your name tonight, remember who sharpened the swords they cheered with. Now. If you are going to strike, strike. I have a kettle to watch.

95 words / 514 characters / 518 bytes — one breath, no trailing newline in the output file.

The speaker is a lich three centuries into keeping his tower, interrupted mid-tea by a hero. He never says he is tired: the weariness lives in the interruptions, the domestic deflections (the teapot, the jam, the kettle) and the way he gives the hero the amulet just to get on with his afternoon — while still being a villain with a history (the drowned-out heroes in the east garden) and a scheme (he sharpened the very swords the villagers will cheer with). The sting lands in the last line.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # validates the gate and the written file
```

`main.py` writes exactly the monologue above to `/output/entry.txt` (UTF-8, no trailing newline) and read-checks the file it wrote. `--self-test` also checks the gate's rejection cases: empty, whitespace-only, over 600 characters, multi-line, carriage return, leading/trailing whitespace, and control characters.

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
