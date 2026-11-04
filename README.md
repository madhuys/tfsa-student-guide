# tfsa-student-guide

A student-friendly, self-contained TFSA explainer site with a voice-over motion graphic hero.

A static site: plain HTML, CSS and JavaScript, no build step.

## Run

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open http://127.0.0.1:8000/.

## Test

```sh
python3 -m unittest discover -s tests
```

The test checks that every page parses and that every local link and asset it names exists.
