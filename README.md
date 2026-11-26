# The Worst Line an AI Could Say

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the make.fun bounty [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f).

## The line

> I ran 10,000 simulations of us meeting. In 9,997 of them, you said yes. Please do not be one of the other three.

112 characters. Flat, over-helpful, faintly ominous: the machine did the
math, got the answer it wanted, and still has to beg the human not to ruin
the statistics.

## How it works

`main.py` writes the line to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set). It refuses
blank lines, anything over the 140-character gate, and any em dash.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
