from pypograph import rules
import re


class Text(str):
    chain = []


class Pypograph(object):
    rules = [
        rules.NbspRule,
        rules.MnemoRule,
    ]

    _rules_instances = []

    def __init__(self, config={}):
        for Rule in self.rules:
            self._rules_instances.append(Rule(config))

    def typo(self, text):
        for rule in self._rules_instances:
            text = rule.process_wrapper(text)
        return text


def typo(text, config={}):
    pypograph = Pypograph(config)
    return pypograph.typo(text)
