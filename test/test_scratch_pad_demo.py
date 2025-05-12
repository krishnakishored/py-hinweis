import pytest
import os
import sys
from io import StringIO

# Add src directory to Python path for imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)
from scratch_pad.demo import Demo


def test_demonstrate_enumerate(capsys):
    """Test the demonstrate_enumerate method of Demo class"""
    # Arrange
    demo = Demo()

    # Act
    demo.demonstrate_enumerate()
    captured = capsys.readouterr()

    # Assert
    expected_outputs = [
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
    assert len(actual_outputs) == len(
        expected_outputs
    ), "Number of outputs doesn't match"

    for actual, expected in zip(actual_outputs, expected_outputs):
        assert (
            actual.strip() == expected
        ), f"Expected '{expected}' but got '{actual}'"


def test_demo_initialization():
    """Test Demo class initialization"""
    demo = Demo()
    assert demo.name == "Demo", "Demo name should be 'Demo'"


if __name__ == "__main__":
    pytest.main(["-v"])
