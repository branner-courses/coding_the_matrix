## (see text)

    In [127]: from random import randint
    
    In [128]: def movie_review(name):
        reviews = ['See it!', 'Don\'t see it!', 'Mnyeh...']
        return name + ': ' + reviews[randint(0, len(reviews)-1)]
       .....: 
    
    In [129]: movie_review('Jaws')
    Out[129]: 'Jaws: Mnyeh...'
    
    In [130]: movie_review('Jaws')
    Out[130]: 'Jaws: See it!'
    
    In [131]: movie_review('Jaws')
    Out[131]: 'Jaws: Mnyeh...'
    
    In [132]: movie_review('Jaws')
    Out[132]: "Jaws: Don't see it!"

[end]
