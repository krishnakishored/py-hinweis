## Setting up pytest

1. Install pytest:
```bash
pip install pytest
```

2. Project structure:
```
py-hinweis/
    ├── tests/
    │   ├── __init__.py
    │   ├── test_demo.py
    │   └── notes.md
    ├── src/
    │   └── demo.py
    └── requirements.txt
```

## Running Tests

1. Run all tests:
```bash
pytest
```

2. Run tests with verbose output:
```bashß
pytest -v
```

3. Run specific test file:
```bash
pytest tests/test_demo.py
## Run specific test function:
uv run pytest test/test_arrays_and_strings.py::test_first_unique_char
```

4. Run tests matching a pattern:
```bash
pytest -k "demo"
```

5. Show print outputs:
```bash
pytest -s
```

## Writing Tests

1. Test file naming:
   - Files must start with `test_` or end with `_test.py`
   - Test functions must start with `test_`

2. Assertions:
```python
assert value == expected, "Optional failure message"
```

3. Fixtures:
```python
@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
```

4. Capturing output:
```python
def test_print_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
```

## Best Practices

1. One assertion per test when possible
2. Use descriptive test names
3. Group related tests in classes
4. Use appropriate fixtures for setup/teardown
5. Keep tests independent
6. Follow AAA pattern (Arrange-Act-Assert)

## Using uv (Fast Python Package Installer)

### Installation

On macOS, install uv using Homebrew:
```bash
brew install uv
```

## UV Package Manager Commands

### Installation
| Platform | Command |
|----------|---------|
| macOS    | `brew install uv` |

### Basic Commands
| Category | Command | Description |
|----------|---------|-------------|
| **Virtual Environment** | `uv venv` | Create a new virtual environment |
| | `uv venv .venv` | Create virtual environment in .venv directory |
| **Package Management** | `uv pip install package_name` | Install a package |
| | `uv pip install -r requirements.txt` | Install dependencies from requirements.txt |
| | `uv pip install --dev pytest pytest-cov` | Install development dependencies |
| | `uv pip freeze > requirements.txt` | Generate requirements.txt |
| | `uv pip compile requirements.txt` | Create/update uv.lock file |
| | `uv pip sync` | Sync environment with lock file |

### Running Python
| Command | Description |
|---------|-------------|
| `uv run python script.py` | Run a Python script |
| `uv run python` | Start Python REPL |
| `uv run pytest` | Run pytest |
| `uv run mypy` | Run type checker |

### Advanced Features
| Feature | Command | Description |
|---------|---------|-------------|
| Parallel Install | `uv pip install --parallel requirements.txt` | Install packages in parallel |
| Cache Management | `uv pip install --cache-dir .cache/uv` | Use specific cache directory |
| Binary Preference | `uv pip install --prefer-binary package_name` | Prefer pre-compiled wheels |

### Development Workflow
| Task | Command | Description |
|------|---------|-------------|
| Project Setup | `uv pip install -e .` | Install project in editable mode |
| Lock File | `uv pip compile requirements.txt` | Generate deterministic lock file |
| Clean Install | `uv pip sync` | Install exact versions from lock file |
| Uninstall All | `uv pip uninstall --all` | Remove all packages |

### Best Practices
- Always use uv.lock for deterministic builds
- Commit both requirements.txt and uv.lock
- Use `--dev` flag for development dependencies
- Use `uv pip sync` instead of install for reproducible environments

## GitHub SSH Setup

### Generating SSH Keys
1. Generate new SSH key:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
- Use RSA alternatively if ed25519 is not supported:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

2. Start SSH agent:
```bash
eval "$(ssh-agent -s)"
```

3. Add SSH key to agent:
```bash
ssh-add ~/.ssh/id_ed25519
```

### Adding SSH Key to GitHub
1. Copy public key:
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

2. Add to GitHub:
   - Go to GitHub → Settings → SSH and GPG keys
   - Click "New SSH key"
   - Paste your key and save

### Testing Connection
```bash
ssh -T git@github.com
```

### Using SSH URLs
- Change remote URL from HTTPS to SSH:
```bash
git remote set-url origin git@github.com:username/repository.git
```
```sh
# update .git/config 
[remote "origin"]
	url = git@github-krishnakishored:krishnakishored/py-hinweis.git
	fetch = +refs/heads/*:refs/remotes/origin/*

# github-krishnakishored is a setup in ~/.ssh/config
```

- Verify remote URL:
```bash
git remote -v
```

### Best Practices
1. Use unique SSH keys for different services
2. Keep private keys secure and never share them
3. Use SSH config file (~/.ssh/config) for multiple accounts
4. Regularly rotate SSH keys for security
5. Back up your SSH keys securely