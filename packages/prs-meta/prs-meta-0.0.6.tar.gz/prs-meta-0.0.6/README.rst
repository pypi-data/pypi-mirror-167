prs meta
========

A wrapper for pyreadstat to easily read, create, and adjust .sav files

documentation: https://prs-meta.readthedocs.io/en/latest/prs.html

**Installation**
----------------

``pip install prs-meta``

**Usage**
---------

Create from df::

    from prs.meta import Meta
    
    df = pd.DataFrame({'my_column': [1,2,3]})
    M = Meta(df)
    M.view('my_column')


