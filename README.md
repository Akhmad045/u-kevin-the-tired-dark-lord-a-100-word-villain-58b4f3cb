# Don't Wake Me When the Bards Start Singing

[![The Tired Dark Lord](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Akhmad045/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Akhmad045/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for [The Tired Dark Lord: A 100-Word Villain Monologue](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) on [make.fun](https://make.fun) — a 100-word monologue spoken by a fantasy villain who is secretly just very tired, judged pairwise by a veteran game writer.

Referral code: `4g7knchf`

## The monologue

> Come in — mind the third step, it bites. I am the Dread Lord of the Ashen Marches. No, I won't retell the burning of Aldergate; I was there, it took all afternoon, and the smoke got into everything. The curse you came to break? Third drawer, left. I meant to loose it on the capital years ago, but the grain levies kept coming, and somebody has to sign them. Sit. The kettle's on. Take the throne, the crown, the black tower — only tell the steward the east wing leaks, and don't wake me when the bards start singing.

100 words, 517 characters, 521 bytes — inside the competition's 1–600 character gate.

## How it works

`main.py` writes the monologue to `/output/entry.txt` (the artifact the
competition's gate scores) and prints it to stdout. It validates the gate
itself before writing: UTF-8 text of 1 to 600 characters, not only
whitespace, a single block with no leading or trailing whitespace and no
control characters.

```sh
python3 main.py              # write /output/entry.txt and print the monologue
python3 main.py --self-test  # validate the gate and its boundaries
```

## License

MIT — see [LICENSE](LICENSE).
