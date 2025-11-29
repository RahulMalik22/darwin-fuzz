# 🧬 Contributing to Darwin

First off, thank you for considering contributing to Darwin! It's people like you that make this tool a powerful engine for security research and optimization algorithms.

---

## 📋 Table of Contents

* [Getting Started](#-getting-started)
* [How to Contribute](#%EF%B8%8F-how-to-contribute)
* [Development Workflow](#-development-workflow)
* [Reporting Bugs](#-reporting-bugs)
* [Suggesting Enhancements](#-suggesting-enhancements)
* [Code Review Process](#-code-review-process)
* [Style Guidelines](#-style-guidelines)
* [Community Guidelines](#-community-guidelines)

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:
- **Python 3.7+** installed
- **C++ compiler** (GCC 7+, Clang 5+, or MSVC 2019+)
- **CMake 3.12+** for building C++ components
- **Git** for version control

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub by clicking the "Fork" button.

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/darwin-fuzz.git
   cd darwin-fuzz
   ```

3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/darwin-fuzz.git
   ```

4. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

5. **Build the C++ core**:
   ```bash
   mkdir build && cd build
   cmake ..
   make
   cd ..
   ```

6. **Run tests to verify setup**:
   ```bash
   pytest tests/
   ```

---

## 🛠️ How to Contribute

We love pull requests! Here's the workflow we recommend:

### 1. Create a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/amazing-mutation-strategy
```

**Branch naming conventions:**
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `perf/description` - Performance improvements

### 2. Make Your Changes

- Write clean, readable code
- Follow our [Style Guidelines](#-style-guidelines)
- Add comments for complex logic
- Keep commits atomic and focused

### 3. Add Tests

**This is crucial!** If you add code, please add corresponding test cases:

```bash
# Add your tests in the tests/ directory
tests/
├── test_mutation.py
├── test_crossover.py
└── test_your_feature.py
```

Run tests locally:
```bash
pytest tests/ -v
```

### 4. Update Documentation

If you change APIs or add features, update the relevant documentation:
- `README.md` - Main project documentation
- `docs/` - Detailed guides and API references
- Code docstrings - Inline documentation

### 5. Verify Build

Ensure the C++ core compiles without warnings:

```bash
cd build
cmake .. && make
# Should complete with 0 warnings
```

For more verbose output:
```bash
cmake .. && make VERBOSE=1
```

### 6. Commit Your Changes

Write meaningful commit messages:

```bash
git add .
git commit -m "feat: add adaptive mutation rate controller

- Implements dynamic mutation based on population diversity
- Adds tests for edge cases
- Updates documentation with usage examples"
```

**Commit message format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `perf:` - Performance improvement
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 7. Push and Create Pull Request

```bash
git push origin feature/amazing-mutation-strategy
```

Then go to GitHub and create a Pull Request with:
- Clear title describing the change
- Detailed description of what and why
- Reference any related issues (e.g., "Fixes #123")
- Screenshots/videos if UI changes

---

## 🔄 Development Workflow

### Keeping Your Fork Updated

Regularly sync with the upstream repository:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Working on Multiple Features

If you're working on multiple features simultaneously:

```bash
# Start new feature from updated main
git checkout main
git pull upstream main
git checkout -b feature/new-idea
```

---

## 🐛 Reporting Bugs

We use [GitHub Issues](https://github.com/ORIGINAL-OWNER/darwin-fuzz/issues) to track bugs. If you find one, please report it!

### Before Submitting a Bug Report

1. **Check existing issues** - Someone might have already reported it
2. **Try the latest version** - The bug might be fixed already
3. **Gather information** - Collect logs, error messages, and system info

### A Good Bug Report Includes

**Title:** Clear, descriptive summary (e.g., "Segmentation fault when evolving with population size 1")

**Description:**
```markdown
## Environment
- OS: Ubuntu 22.04 LTS
- Python Version: 3.10.12
- Darwin Version: 1.2.3
- C++ Compiler: GCC 11.4.0

## Steps to Reproduce
1. Run command `python darwin_solver.py --cities 60 --population 1`
2. Click "Start Evolution"
3. Observe crash after 5 generations

## Expected Behavior
Should handle edge case gracefully or show warning about minimum population size.

## Actual Behavior
Program crashes with:
```
Segmentation fault (core dumped)
```

## Logs/Screenshots
[Attach relevant logs, stack traces, or screenshots]

## Additional Context
This only happens with population size 1. Works fine with size 2+.
```

---

## 💡 Suggesting Enhancements

We welcome feature suggestions! Please open a GitHub Issue with:

**Title:** Feature request: [Your idea]

**Description:**
- **Problem Statement:** What problem does this solve?
- **Proposed Solution:** How would you implement it?
- **Alternatives Considered:** What other approaches did you think about?
- **Additional Context:** Use cases, examples, mockups

---

## 🔍 Code Review Process

### What Happens After You Submit a PR?

1. **Automated Checks:** CI/CD runs tests and linters
2. **Maintainer Review:** A core maintainer reviews your code
3. **Feedback Loop:** Address any requested changes
4. **Approval:** Once approved, your PR will be merged!

### Review Expectations

- **Response Time:** We aim to provide initial feedback within 3-5 days
- **Be Patient:** Complex PRs may take longer to review
- **Be Receptive:** Reviewers are here to help improve the code

### What Reviewers Look For

✅ Code correctness and logic  
✅ Test coverage  
✅ Documentation completeness  
✅ Performance implications  
✅ Security considerations  
✅ Compatibility with existing features  

---

## 🎨 Style Guidelines

To keep the codebase clean and consistent, please adhere to these standards:

### Python Style

**Follow PEP 8** - Use tools like `black` and `flake8`:

```bash
# Auto-format code
black darwin_solver.py

# Check style
flake8 darwin_solver.py
```

**Key conventions:**
- Use `snake_case` for functions and variables
- Use `PascalCase` for class names
- Maximum line length: 88 characters (Black default)
- Use type hints where appropriate

**Example:**
```python
def calculate_fitness(tour: List[int], distances: np.ndarray) -> float:
    """Calculate total distance of a tour.
    
    Args:
        tour: List of city indices representing the tour order
        distances: 2D array of distances between cities
        
    Returns:
        Total tour distance as a float
    """
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    return total_distance
```

### C++ Style

**Follow the Google C++ Style Guide** with these specific requirements:

- Use `std::` namespace explicitly (no `using namespace std;`)
- Prioritize memory safety and RAII principles
- Ensure compatibility with O3 optimization
- Use modern C++17 features where appropriate

**Key conventions:**
- Use `PascalCase` for class names
- Use `snake_case` for function and variable names
- Use `SCREAMING_SNAKE_CASE` for constants
- Maximum line length: 80 characters

**Example:**
```cpp
#include <vector>
#include <algorithm>

class GeneticAlgorithm {
private:
    std::vector<std::vector<int>> population_;
    const double MUTATION_RATE = 0.02;
    
public:
    std::vector<int> tournament_selection(
        const std::vector<std::vector<int>>& population,
        const std::vector<double>& fitness,
        int tournament_size
    ) {
        // Implementation with clear logic
        std::uniform_int_distribution<> dist(0, population.size() - 1);
        // ... rest of implementation
    }
};
```

### Documentation Style

**Python Docstrings** - Use Google style:
```python
def function(arg1: int, arg2: str) -> bool:
    """Short description of function.
    
    Longer description if needed, explaining the purpose
    and any important details.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When arg1 is negative
    """
```

**C++ Comments** - Use Doxygen style:
```cpp
/**
 * @brief Short description of function
 * 
 * Longer description if needed.
 * 
 * @param arg1 Description of arg1
 * @param arg2 Description of arg2
 * @return Description of return value
 */
```

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
feat(mutation): add adaptive mutation rate

Implements dynamic mutation rate that adjusts based on
population diversity. This improves convergence speed
while maintaining exploration capability.

- Adds diversity metric calculation
- Adjusts mutation rate between 0.01 and 0.05
- Includes unit tests for edge cases

Closes #42
```

---

## 👥 Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- **Be Respectful:** Treat everyone with respect and kindness
- **Be Constructive:** Provide helpful, actionable feedback
- **Be Patient:** Remember that everyone was a beginner once
- **Be Open-Minded:** Different perspectives lead to better solutions

### Getting Help

- **Documentation:** Check `README.md` and `docs/` first
- **GitHub Issues:** Search existing issues or create a new one
- **Discussions:** Use GitHub Discussions for questions and ideas

### Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub's contributor graph
- Release notes for significant contributions

---

## 🏆 Types of Contributions

We welcome all types of contributions:

- 🐛 **Bug Reports & Fixes**
- ✨ **New Features**
- 📝 **Documentation Improvements**
- 🎨 **UI/UX Enhancements**
- ⚡ **Performance Optimizations**
- 🧪 **Test Coverage**
- 🌐 **Translations**
- 💡 **Ideas & Suggestions**

---

## 📚 Additional Resources

- [README.md](README.md) - Project overview and setup
- [LICENSE](LICENSE) - Project license
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [docs/](docs/) - Detailed documentation
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community standards

---

## ❓ Questions?

If you have questions about contributing, feel free to:
- Open a [GitHub Discussion](https://github.com/ORIGINAL-OWNER/darwin-fuzz/discussions)
- Comment on relevant issues
- Reach out to maintainers

---

<div align="center">

**Thank you for contributing to Darwin!** 🧬

<sub>Built with ❤️ by the Chaos Architects</sub>

</div>