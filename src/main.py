from typing import Iterator
from trie import Trie


def main() -> None:
    document: str = "src/input.txt"
    buffer_size: int = 4096
    keywords: Trie = chunk_to_words(doc_to_chunk(document, buffer_size))
    print(keywords)


def chunk_to_words(chunk: Iterator[list[str]]) -> Trie:
    keywords = Trie()
    for word in [word for words in chunk for word in words]:
        keywords.add(word)
    return keywords


def doc_to_chunk(filepath: str, buffer_size: int) -> Iterator[list[str]]:
    position: int = 0
    try:
        with open(filepath) as f:
            while True:
                words: list[str] = []
                buffer = f.read(buffer_size)
                if not buffer:
                    print("End of file reached...")
                    break
                position += 1
                words.extend(buffer.split())
                if len(buffer) == buffer_size:
                    last_segment: str = words.pop()
                    if len(last_segment) > 0:
                        f.seek(position * buffer_size, 0)
                yield words
    except FileNotFoundError:
        print(f"File [{filepath}] not found.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
