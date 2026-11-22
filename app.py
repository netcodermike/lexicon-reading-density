import re

def tokens(text):
    return re.findall(r"[^\W\d_]+",text.casefold())

def analyze(data):
    known, passages=data["known"],data["passages"]
    if not isinstance(known,list) or not isinstance(passages,dict) or not passages:
        raise ValueError("Provide a word list and a map of named passages")
    words={word for entry in known for word in tokens(entry)}
    report=[]
    for name,text in passages.items():
        terms=tokens(text)
        unknown=[word for word in terms if word not in words]
        report.append({"name":name,"tokens":len(terms),"unknown_tokens":len(unknown),
                       "unknown_words":sorted(set(unknown))})
    return {"passages":report}

if __name__ == "__main__":
    import json
    from pathlib import Path
    import sys
    try:
        path, = sys.argv[1:]
        result = analyze(json.loads(Path(path).read_text(encoding="utf-8")))
        print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError) as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(2)
