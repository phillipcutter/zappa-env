# Zappa Env

Zappa-env is a simple package that allows you to call Zappa commands from a custom virtualenv for build purposes

## Installing & Usage

Install zappa
`pip install zappa-env`

Run your Zappa commands with `zappa-env` followed by your virtualenv and Zappa command
`zappa-env my-virtual-env zappa update prod`

## Requirements

Zappa-env currently assumes that your virtualenvs are installed with the `virtualenvwrapper` package and located in `$HOME/.virtualenvs/`. Currently this is unable to be changed unless you modify the source code.

## Why?

The reason I made this project was because I was getting annoyed activating a special deployment virtualenv just to deploy or package my Zappa repo. This small project combines the `workon virtualenv` and zappa commands so I can run my Zappa commands in just one line.

## Contributions

Submit an issue or pull request and I'll do my best to merge the PR or help with the issue.

## To-do

- [ ] Support running zappa commands with a requirements.txt file (eliminates need for virtualenvs)
- [ ] Support Anaconda
- [ ] Support stock Python virtualenvs
