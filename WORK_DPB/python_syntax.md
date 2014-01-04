## Python syntax notes

 1. To add to a set `S`:

        S.add('new_item')

 1. To subtract from a set `S`:

        S.remove('remove_me')

 2. To replace `S` with its union or intersection with another set, `T`:

        S.update(T)
        S.intersection_update(T)

 1. To copy a set by value:

        T = S.copy()

[end]
