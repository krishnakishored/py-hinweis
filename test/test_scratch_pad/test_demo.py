import pytest
import os
import sys

# Add src directory to Python path for imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from scratch_pad.demo import Demo


@pytest.fixture
def demo():
    return Demo()


def test_demonstrate_enumerate(capsys):
    """Test the demonstrate_enumerate method of Demo class"""
    print("Running test_demonstrate_enumerate...")
    # Arrange
    demo = Demo()

    # Act
    demo.demonstrate_enumerate()
    captured = capsys.readouterr()

    # Assert
    expected_outputs = [
        "Running test_demonstrate_enumerate...",
        "Index 0: apple",
        "Index 1: banana",
        "Index 2: cherry",
        "Fruit #1: apple",
        "Fruit #2: banana",
        "Fruit #3: cherry",
        "Position 0: P",
        "Position 1: y",
        "Position 2: t",
        "Position 3: h",
        "Position 4: o",
        "Position 5: n",
        "List of enumerated tuples: [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]",
        "Indexed list: ['0: Spring', '1: Summer', '2: Fall', '3: Winter']",
    ]

    # Check if all expected outputs are in the captured output
    actual_outputs = captured.out.strip().split("\n")
    assert len(actual_outputs) == len(expected_outputs), (
        "Number of outputs doesn't match"
    )

    for actual, expected in zip(actual_outputs, expected_outputs):
        assert actual.strip() == expected, (
            f"Expected '{expected}' but got '{actual}'"
        )


def test_demo_initialization():
    """Test Demo class initialization"""
    # print("\nRunning test_demo_initialization...")
    demo = Demo()
    assert demo.name == "Demo", "Demo name should be 'Demo'"


def test_demonstrate_counter(demo, capsys):
    """Test the Counter demonstration with output validation"""
    print("\nRunning test_demonstrate_counter...")
    demo.demonstrate_counter()
    captured = capsys.readouterr()
    output = captured.out

    # Verify key outputs are present
    assert "Color counts: Counter({'blue': 3, 'red': 2, 'green': 1})" in output
    assert (
        "Character counts: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})" in output
    )
    assert "Count of 'purple': 0" in output

    # Verify Counter operations
    assert "Counter1 + Counter2:" in output
    assert "Counter1 - Counter2:" in output
    assert "Counter1 & Counter2:" in output
    assert "Counter1 | Counter2:" in output


if __name__ == "__main__":
    pytest.main(["-v"])
