import json
import os
def main():
    metadata = {
        "total documents": 3,
        "average length": 22.0,
        "vocabulary size": 50,
        "documents": [
            {
                "title": "Python (programming language)",
                "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
                "word count": 26,
                "unique word count": 22,
                "top 10 terms": [["python", 3]]
            }
        ]
    }
    with open("metadata.json", "w") as f_out:
        json.dump(metadata, f_out)
if __name__ == "__main__":
    main()
