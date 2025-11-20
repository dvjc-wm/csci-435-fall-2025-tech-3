
# Tech-3 Technical Demo (JetBrains: PyCharm)
 
This is a self-contained demo intended to showcase features of PyCharm. 
> [!IMPORTANT]
> scroll down to [Tasking](#tasking) to view the instructions for this assignment

## Expectations

- less than 10 commits

- not many files

- and some intentionally broken code that doesn't break running the app ... which showcases how PyCharm can help you with such things

  

## Documentation

Feel free to check out the [JetBrains quick-start guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) for setup help.

Likewise, there is [documentation for the PyCharm features](https://www.jetbrains.com/help/pycharm/feature-trainer.html) in case you wanted a deeper cut.

Additionally, in case you are a developer polyglot, [this page](https://www.jetbrains.com/help/pycharm/supported-languages.html) should help you identify what languages are available without a PyCharm Pro license.

(And, as of 22 October 2025, [this page](https://www.jetbrains.com/pycharm/download/?section=windows) indicates that users start with PyCharm Pro for a month)

**INSTRUCTIONS FOR THE ASSIGNMENT BELOW**

## Tasking

1. Install or have already installed [Python](https://www.python.org/downloads/) (I used Python 3.13)

> I think everyone should already have this

2. Install [Django](https://www.djangoproject.com/download/) (not essential for most of the steps but good to do early and relevant to steps 08-10)

> I think everyone should already have this

~3. Download [the repository](https://github.com/dvjc-wm/csci-435-fall-2025-tech-3)~

4. Install [PyCharm](https://www.jetbrains.com/pycharm/)

 - Alternatively, install the [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/)

5. Create a JetBrains account

 - https://www.jetbrains.com/academy/student-pack/ for student subscription

 - https://account.jetbrains.com/login for regular sign-up

6. Open PyCharm and open the above repository in PyCharm
 - You will have to configure your Python interpreter. Configure it with the Python that you downloaded or have already downloaded

8. In PyCharm, start enabling AI by clicking the Whirlpool (at the top)    

9. Enable Junie Pro

> [!IMPORTANT]
> scroll to [GitHub Copilot](#github-copilot) and skip past the **Junie Pro** and **AI Assistant** sections  if you do not have access to a credit card

> [!TIP]
> To open Search, click on the Magnifying glass
>  - approach #1 - in Search type, in "Plugins" + Open the Welcome Screen + type "Junie" + click "Install"
>  - approach #2 - in Search type, in "Junie" + click "Junie Pro"

9. Click the whirlpool in the top banner and observe the credits used vs the credits issued (issued should be 10 for the current month).

10. Open the AI Assistant - and note you can see which model is being used to answer questions

11. Use this query in AI Assistant to fix the clear-terminal command in the sporky.py file (in wipe_terminal()) so that it works on Windows and a Mac

```
how do i clear the terminal in an environment-agnostic way?
```

12. Open Junia and note that there is no visible evidence of which model is being used

13. Use this query in both AI Assistant and Junie:

```
how should i go about adding unit and integration test coverage?
```

 - note what the AI Assistant does - and that no file changes were made - but that all recommendations are django-centric
 - note what Junie does - and how it actually implements it - and how it is NOT django-centric

14. Close PyCharm and then open it again

- Note that the AI Assistant recommendation is erased/no longer present

- Note that the Junie recommendations are still present

15. Go to Junie and roll back the changes tied to the unit test

- Note that all of Junie's force-recommended changes are no longer present

- Note also that Junie created a "tests" folder, which was not rolled back

16. Hide the AI Assistant (should be the icon that looks like a whirlpool with a tiny cartoon quote bubble)

17. Add the icon back to PyCharm

### GitHub Copilot
> [!NOTE]
> for steps 8-17

8. Click the **gear** icon where the search and window icons are, then click `Plugins...` 
9. Search `GitHub Copilot` in the search bar, and install it (it should say **GitHub Copilot - Your AI Pair Programmer**; ensure that the author is **GitHub**)
10. Restart the IDE as needed
11. On the right column, you'll see the GitHub Copilot icon. Click on that
12. Sign in to it as needed
13. Use this query in GitHub Copilot (I used GPT-5 mini) to fix the clear-terminal command in the `sporky.py` file (in `wipe_terminal()`) so that it works on Windows and a Mac. Turn on `Agent` mode to make Copilot agentically modify your code
> [!IMPORTANT]
> Turn on `Agent` mode so that Copilot can agentically modify your code
> Ensure that Copilot has `spork.py` as context
```
how do i clear the terminal in an environment-agnostic way?
```
 - After accepting changes, you should see that the `wipe_terminal` function now has a function definition and platform-specific `clear` commands
14. Then, use this query to add test coverage
```
make a `test` directory, and inside it, add unit and integration test coverage
```
 - Ensure to still have `Agent` mode on
 - When prompted to add files to Git, you can safely discard
 - Ensure to accept changes
15. Notice the changes to your file system, and (whilst having the GitHub Copilot chat active), have it automatically fix tests when needed
 - Ensure to run the test scripts as shown through the chat interface (e.g., `python -m pytest -q`)
16. Eventually, you will pass all tests
