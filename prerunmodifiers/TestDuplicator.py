from robot.api import SuiteVisitor


class TestDuplicator(SuiteVisitor):
    """
    Parameters are passed to this prerunmodifier as a list, where even argument is a tag and an odd one - a mapping keyword.

    Example:

    Simple cool test
    [Tags]    S1    S2    S3
    Log    Some cool test

    After prerunmodifier there will be three tests:

    Simple cool test: S1
    [Tags]    S1    S2    S3
    Precondition for S1
    Log    Some cool test

    Simple cool test: S2
    [Tags]    S1    S2    S3
    Precondition for S2
    Log    Some cool test

    Simple cool test: S3
    [Tags]    S1    S2    S3
    Precondition for S3
    Log    Some cool test

    """

    def __init__(self, *tags_and_keywords):
        if len(tags_and_keywords) % 2:
            raise Exception('Invalid number of arguments for TestDublicator')

        self.kws = {tags_and_keywords[i]: tags_and_keywords[i+1] for i in range(0, len(tags_and_keywords), 2)}

    def start_suite(self, suite):
        if not suite.tests:
            return None
        dublicated_tests = list()
        for test in suite.tests:
            dublicated_tests.extend(self._dublicate(test))
        suite.tests = dublicated_tests

    def _dublicate(self, test):
        result = list()
        for tag, kw in self.kws.items():
            if tag in test.tags:
                modified_test = test.deepcopy()
                modified_test.name += ": " + tag
                t = modified_test.keywords[0].deepcopy()
                t.name, t.args = kw, ()
                modified_test.keywords.insert(0, t)
                modified_test.keywords[1].type = "kw"
                result.append(modified_test)
        if not len(result):
            return test
        return result
