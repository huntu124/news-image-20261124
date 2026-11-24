# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/huntu124/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/huntu124/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One-image digest of 24 November 2026's world news: a deterministic
newspaper-style "front page" (1024x1024 JPEG) rendered with Pillow from a
fixed list of eight stories of the day — mine blasts ablaze on three oil
tankers in the Strait of Hormuz, the Israeli drone strike at a Khan Younis
police post, the Russia–Ukraine clash at the UN Security Council over Black
Sea shipping, US agencies eyeing Iran in the tanker cyberattacks, the report
of a Russian nuclear weapon planned for space, the Solomon Islands flipping
allegiance back to Australia, the UN deputy chief's warning on Gaza, and
Nvidia's Jensen Huang returning to the spotlight as shares rally.

## Run it

```sh
python3 main.py
```

The program writes `$MAKEFUN_OUTPUT_DIR/entry.png` (defaults to `/output`),
re-rendering the shipped `news-2026-11-24.jpg` byte-identically when Pillow
is available, and copying the shipped file otherwise. Deterministic: two
runs produce identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0n4jr1g6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
