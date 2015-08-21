git-at-pomona.github.io !["status"](https://travis-ci.org/PomonaCS051/PomonaCS051.github.io.svg)
========

## About

This site is dedicated to documenting the use of GitHub and Git in the CS051
lab environments at Pomona College for Fall 2015. Our original proposal for the
trial can be found here: [CS051 Proposal: GitHub + Eclipse](https://github.com/rwoll/CS051Proposal).

## Contributing

We're currently working on putting the materials to this site together, so if
you have any feedback, concerns, or suggestions please create an issue through
GitHub or fork the repository, make your edits and then make a PR. (Spelling
and grammar corrections are always appreciated!)

## Building the Site

The static site is generated with the [Jekyll](http://jekyllrb.com). To build
the site locally, clone the repository, then `cd` into the cloned repo.  
Install Jekyll (assuming you have Ruby installed):
```
gem install jekyll
```  
Then run:  
```
jekyll serve
```
Finally, view the site at `http://localhost:4000`. As you make changes to the
content of the site, jekyll will watch and attempt to rebuild. If you adjust
the `_config.yml` file, you will have to rebuild with `jekyll serve`. 

## Contributers

This project is currently maintained by [@rwoll](https://github.com/rwoll)
and [@ericthewry](https://github.com/ericthewry).
