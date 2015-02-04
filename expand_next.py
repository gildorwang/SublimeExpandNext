# expand_next.py
import sublime, sublime_plugin, re

def escape_regex(str):
  # Sublime text chokes when regexes contain \', \<, \>, or \`.
  # Call re.escape to escape everything, and then unescape these four.
  str = re.escape(str)
  for c in "'<>`":
    str = str.replace('\\' + c, c)
  return str

def is_found(region):
  return not (region is None or (region.a == -1 and region.b == -1))

class ExpandNextCommand(sublime_plugin.TextCommand):
  def __init__(self, p):
    super(ExpandNextCommand, self).__init__(p)
  #/__init__

  def run(self, edit, skip_last = False, whole_word = False):
    last_selection = None
    view = self.view

    selections = view.sel()
    last_selection = selections[-1]

    # If the last selection is empty, expand to the current word. In other
    # words, just do the usual Cmd+D operation.
    if last_selection.empty():
      view.window().run_command('find_under_expand')
      return
    #/if

    regex = None
    word = view.substr(last_selection)
    if whole_word:
      regex = r'(?<!\w)' + escape_regex(word) + r'(?!\w)'
    else:
      regex = escape_regex(word)
    #/if

    # print("the regex is '{0}'".format(regex))

    last_point = max(last_selection.a, last_selection.b)
    next_find = view.find(regex, last_point)
    # print("next_find {0}".format(next_find))
    if not is_found(next_find):
      # print("not found; starting again from head")
      next_find = view.find(regex, 0)

      while is_found(next_find) and selections.contains(next_find):
        # print("found {0} already in selections".format(next_find))
        next_find = view.find(regex, next_find.b)
      #/while
    #/if

    if is_found(next_find):
      # print("found {0}".format(next_find))

      if skip_last:
        selections.subtract(last_selection)
      #/if

      selections.add(next_find)
      view.show(next_find)
    #/if
  #/run
#/ExpandNextCommand
