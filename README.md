You don't want to use this code for anything, it's just something I'm doing for the heckuv it.

It does a small headlines thing. I wanted to see if I could learn a bit about scraping and throw together as useful site for myself.

The code is a mess, not meant to be perfect or used by anyone else. I didn't want to spend too much time on it, just enough to learn a little and have a working site.



Some stuff so I remember what I did to get things to work in case I need to redo things.

```
git remote add origin git@github-news:Blake-/news.git
git branch --set-upstream-to=origin/main main
```

gives me something like this:

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github-news:Blake-/news.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

then had to set up ssh to use the key for just this

Somewhere in there I added that pub to the repo too

```
Host github-news
    HostName github.com
    User blake-
    IdentityFile ~/.ssh/github-news-repo
    IdentitiesOnly yes
```


```
python3 manage.py runserver
```

