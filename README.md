
# Tech-3 Technical Demo (JetBrains: PyCharm)
 
This is a self-contained demo intended to showcase features of PyCharm.  

## Expectations

- less than 10 commits

- not many files

- and some intentionally broken code that doesn't break running the app ... which showcases how PyCharm can help you with such things

  

## Documentation

Feel free to check out the [JetBrains quick-start guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) for setup help.

Likewise, there is [documentation for the PyCharm features](https://www.jetbrains.com/help/pycharm/feature-trainer.html) in case you wanted a deeper cut.

Additionally, in case you are a developer polyglot, [this page](https://www.jetbrains.com/help/pycharm/supported-languages.html) should help you identify what languages are available without a PyCharm Pro license.

(And, as of 22 October 2025, [this page](https://www.jetbrains.com/pycharm/download/?section=windows) indicates that users simply start with PyCharm Pro for a month)

## Tasking

### install or have already installed [Python](https://www.python.org/downloads/) (I used Python 3.13)

I think everyone should already have this

### install [Django](https://www.djangoproject.com/download/) (not essential for most of the steps but good to do early and relevant to steps 08-10)

I think everyone should already have this

### download [the repository](https://github.com/dvjc-wm/csci-435-fall-2025-tech-3)

### install [PyCharm](https://www.jetbrains.com/pycharm/)

Alternatively, install the [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/)

### create a JetBrains account

https://www.jetbrains.com/academy/student-pack/ for student subscription

https://account.jetbrains.com/login for regular sign-up

### Open PyCharm and open the above repository in PyCharm

### In PyCharm, enable AI by clicking the (Whirlpool at the top)

### Enable Junie Pro

Note: to open Search, click on the Magnifying glass

 - approach #1 - in Search type, in "Plugins" + Open the Welcome Screen + type "Junie" + click "Install"
 - approach #2 - in Search type, in "Junie" + click "Junie Pro"

### Click the whirlpool in the top banner and observe the credits used vs the credits issued (issued should be 10 for the current month).

### Open the AI Assistant - and note you can see which model is being used to answer questions

### use this query in AI Assistant to fix the clear-terminal command in the sporky.py file (in wipe_terminal()) so that it works on Windows and a Mac

```
how do i clear the terminal in an environment agnostic way?
```

### Open Junia and note that there is no visible evidence which model is being used

### use this query in both AI Assistant and Junie:

```
how should i go about adding unit and integration test coverage?
```

 - note what the AI Assistant does - and that no file changes were made - but that all recommendations are django-centric
 - note what Junie does - and how it actually implements it - and how it is NOT django-centric

### close PyCharm and then open it again

- Note that the AI Assistant recommendation is erased/no longer present

- Note that the Junie recommendations are still present

### Go to Junie and roll-back the changes tied to the unit test

### Hide the AI Assistant (should be the icon that looks like a whirlpool with a tiny cartoon quote bubble)

### Add the icon back to the PyCharm