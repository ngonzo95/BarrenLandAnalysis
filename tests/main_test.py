from main import main as unit


def test_happyPathTestExample1(monkeypatch):
    mock = MockInputOutput()
    monkeypatch.setattr('builtins.input', mock.mock_input)
    monkeypatch.setattr('builtins.print', mock.mock_print)

    mock.stdInString = "{\"0 292 399 307\"}"
    unit()
    assert len(mock.printCalls) == 1
    assert mock.printCalls[0] == "116800 116800"


def test_happyPathTestExample2(monkeypatch):
    mock = MockInputOutput()
    monkeypatch.setattr('builtins.input', mock.mock_input)
    monkeypatch.setattr('builtins.print', mock.mock_print)

    mock.stdInString = ("{\"48 192 351 207\", \"48 392 351 407\", "
                        + "\"120 52 135 547\", \"260 52 275 547\"}")
    unit()

    assert len(mock.printCalls) == 1
    assert mock.printCalls[0] == "22816 192608"

def test_whenExceptionOccursPrintsMessage(monkeypatch):
    mock = MockInputOutput()
    monkeypatch.setattr('builtins.input', mock.mock_input)
    monkeypatch.setattr('builtins.print', mock.mock_print)

    mock.stdInString = ("{\"48 192 351 207\", \"48 392 351 407\", "
                        + "\"120 52 135 547\", \"260 52 275 \"}")
    unit()

    assert len(mock.printCalls) == 1
    assert mock.printCalls[0] == "Rectangle at position 3 is misformatted"


class MockInputOutput:
    def __init__(self):
        self.stdInString = ""
        self.printCalls = []

    def mock_print(self, str):
        self.printCalls.append(str)

    def mock_input(self):
        return self.stdInString
