import sys, os

def get_contents(the_file):
    """Return contents of file as list of 'documents' = lines."""
    with open(os.path.join('data', the_file), 'r') as f:
        contents = f.read()
    contents = contents.split('\n')
    return contents

def makeInverseIndex(strlist):
    """Map each word to doc #s of each doc containing that word.

    Task 0.6.6"""
    d = {}
    for i, document in enumerate(strlist):
        for word in document.split():
            if word and word in d:
                d[word].add(i)
            elif word:
                d[word] = {i}
    return d

def orSearch(inverseIndex, query):
    """Return set of doc #s for all docs containing *any* word in query.

    Task 0.6.7"""
    to_return = set()
    for word in query:
        if word in inverseIndex:
            to_return.update(list(inverseIndex[word]))
    return to_return

def andSearch(inverseIndex, query):
    """Return set of doc #s for all docs containing *all* words in query.

    Task 0.6.8"""
    # 1. Populate set initially, with results for first word.
    first_word = query[0]
    if first_word in inverseIndex:
        to_return = set(inverseIndex[first_word])
    else:
        return None
    # 2. Remove those doc #s in which subsequent words are not found.
    for word in query:
        # No need to continue if to_return is empty.
        if to_return and word in inverseIndex:
            to_return.intersection_update(list(inverseIndex[word]))
        else:
            return None
    return to_return
