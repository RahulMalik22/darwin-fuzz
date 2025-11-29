# Darwin-Fuzz Project Structure

This document explains the organization of the Darwin-Fuzz repository.

## 📁 Current Structure

```
darwin-fuzz/
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # Main project documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Community guidelines
├── CHANGELOG.md            # Version history
├── requirements.txt        # Python dependencies
├── CMakeLists.txt         # C++ build configuration
├── docs/                  # Documentation
│   ├── installation.md    # Setup guide
│   ├── api.md            # API reference (TODO)
│   └── architecture.md   # Technical details (TODO)
├── examples/             # Example implementations
│   └── simple_fuzzer.py  # Basic example
├── src/                  # Source code (TODO)
│   ├── python/          # Python modules
│   └── cpp/             # C++ engine
├── tests/               # Test suite (TODO)
│   ├── test_engine.py
│   └── test_integration.py
└── build/               # Build artifacts (gitignored)
```

## 📂 Directory Purposes

### Root Files

- **README.md**: Main entry point for the project
- **LICENSE**: Legal licensing (MIT)
- **CONTRIBUTING.md**: How to contribute
- **CODE_OF_CONDUCT.md**: Community standards
- **CHANGELOG.md**: Version history and changes
- **requirements.txt**: Python package dependencies
- **CMakeLists.txt**: C++ build configuration

### `/docs` - Documentation

Contains comprehensive documentation:
- Installation guides
- API references
- Architecture explanations
- Tutorials and guides

### `/examples` - Example Code

Working examples demonstrating Darwin-Fuzz usage:
- Simple fuzzing examples
- Advanced use cases
- Integration examples
- Performance benchmarks

### `/src` - Source Code

#### `/src/python`
Python implementation:
- High-level API
- Orchestration logic
- Visualization tools
- Analysis modules

#### `/src/cpp`
C++ engine:
- Genetic algorithm core
- Performance-critical operations
- Pybind11 bindings

### `/tests` - Test Suite

Automated tests:
- Unit tests for individual components
- Integration tests for full workflows
- Performance benchmarks
- Regression tests

### `/build` - Build Artifacts

Generated during compilation (gitignored):
- Compiled binaries
- CMake cache
- Temporary build files

## 🔨 Planned Structure

As the project grows, we'll add:

```
darwin-fuzz/
├── benchmarks/          # Performance benchmarks
├── scripts/            # Utility scripts
│   ├── setup.sh       # Installation automation
│   └── test.sh        # Testing automation
├── .github/           # GitHub specific
│   ├── workflows/     # CI/CD pipelines
│   └── ISSUE_TEMPLATE/
└── docker/            # Docker configurations
```

## 🎯 File Naming Conventions

### Python Files
- **Modules**: `lowercase_with_underscores.py`
- **Classes**: Defined with `PascalCase` inside modules
- **Tests**: `test_feature_name.py`

### C++ Files
- **Headers**: `feature_name.hpp`
- **Implementation**: `feature_name.cpp`
- **Tests**: `test_feature_name.cpp`

### Documentation
- **Markdown**: `lowercase-with-dashes.md`
- **Config**: `UPPERCASE` or `lowercase.ext`

## 🚀 Development Workflow

1. **Clone Repository**
   ```bash
   git clone https://github.com/RahulMalik22/darwin-fuzz.git
   cd darwin-fuzz
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Add code to appropriate directory
   - Update relevant documentation
   - Add tests for new features

4. **Test Changes**
   ```bash
   pytest tests/
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat: description of changes"
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to GitHub
   - Open Pull Request
   - Wait for review

## 📝 Notes

- **Build artifacts**: Never commit files in `/build`
- **Virtual environments**: Keep `venv/` or `env/` local
- **IDE files**: Add IDE-specific files to `.gitignore`
- **Large files**: Use Git LFS if needed for datasets

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.
