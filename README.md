# Lexicon Reading Density

Compare unknown word density across text passages against an editable reference vocabulary.

![Sample run from Lexicon Reading Density](docs/demo.webp)

## Run

Install Python 3.11 or newer. Run these commands from the repository root.

```sh
python app.py sample.json
```

Replace `sample.json` with a JSON file following the same structure. The app prints a JSON report to standard output.

Word matching ignores case and punctuation. Unknown token counts include repeats. Listed unknown words are unique.

## Verify

Run `python check.py` with Python 3.11 or newer after the build step when applicable. The check verifies the bundled scenario and confirms that an invalid input returns an error.
