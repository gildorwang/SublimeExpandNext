# SublimeExpandNext

## What it does
A replacement of the built-in expand command (`ctrl+d`) which does not work when I have modified `word_separators` to make some special characters become valid word contents.
This plugin will expand properly to include the special characters in the word.

## Features
1. Expands to whole word when there's no selection, or selects the next occurrence when something is already selected, just like the built-in command `find_under_expand`.
2. Easier to control if it should match whole word, or also accept part of a word, with the `whole_word` parameter.
3. When `skip_last` is true, it has the same behavior as the built-in command `find_under_expand_skip`.

## How to use
1. Put `expand_next.py` under the packages folder (e.g. `Data\Packages\User`).
2. Modify the keymap to use this:

````json
{ "keys": ["alt+e"], "command": "expand_next", "args": {"skip_last": false, "whole_word": true}},
{ "keys": ["alt+shift+e"], "command": "expand_next", "args": {"skip_last": true, "whole_word": true}},
{ "keys": ["alt+o"], "command": "expand_next", "args": {"skip_last": false, "whole_word": false}},
{ "keys": ["alt+shift+o"], "command": "expand_next", "args": {"skip_last": true, "whole_word": false}},
````

## License
[MIT License](https://github.com/gildorwang/SublimeExpandNext/blob/master/LICENSE)

## Notice
The code to escape regex properly is inspired by plugin [WordHighlight](https://github.com/SublimeText/WordHighlight) when I noticed it continued to work correctly after I introduced special characters.
