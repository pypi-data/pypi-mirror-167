aprompt
=======

**A**dvanced **Prompt**s replace the built-in
`input()` with colored and optimized prompts.
Note that using aprompt inside an IDE will
probably not work. Run your scripts from the
terminal.


Features
--------

### Prompts
- [x] text
- [x] password
- [x] code
- [x] amount
- [x] select
- [x] multi-select
- [x] sort
- [x] path _(beta)_
- [ ] datetime
- [ ] time


### Other
- [x] custom formatter _(not documented yet)_
- [x] custom prompts _(not documented yet)_
- [ ] detailed docs


Usage
-----

```python
import aprompt as ap

name = ap.prompt(
    "Please enter your name.",
    ap.prompts.text()
)

age = ap.prompt(
    "Please enter your age.",
    ap.prompts.amount(
        minimum = 0,
        maximum = 150,
    )
)

password = ap.prompt(
    "Please enter your password.",
    ap.prompts.text(hide = True)
)

language = ap.prompt(
    "What language do you prefer?",
    ap.prompts.select(
        "English",
        "Chinese",
        "French",
        "Japanese",
        "German",
    )
)

can_code_in = ap.prompt(
    "In what languages can you code in? (Choose 3 or more)",
    ap.prompts.select(
        "c",
        "c++",
        "c#",
        "python",
        "ruby",
        "javascript",
        "java",
        "pascal",
        "haskell",
        "rust",
        "go",
        "lua",
        "swift",
        "R",
        "bash",
        sort = True,
        multiple = True,
        require = lambda x: x >= 3,
    )
)

...
```