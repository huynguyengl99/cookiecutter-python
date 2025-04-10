# ✨ Python & Django Cookiecutter Templates

A curated collection of modern, flexible, and production-ready **Cookiecutter templates** for building Python and Django
applications with ease and best practices baked in.

Whether you're crafting a CLI utility, a PyPI package, or a full-blown Django REST API, this project provides **four
distinct templates** to jumpstart your development journey.

---

## 🚀 Available Templates

1. **Python App (`py`)** – A modern, general-purpose Python application structure
2. **Python Package (`pypackage`)** – A template for building and publishing packages to PyPI
3. **Django REST App (`drf`)** – A fully-configured DRF app with optional Celery, WebSockets, and cloud support
4. **DRF Package (`drf_package`)** – A clean structure for reusable DRF extensions and components

---

## 🔧 Requirements

- **Python** 3.8 or higher
- **Cookiecutter** – [Install it here](https://cookiecutter.readthedocs.io/en/stable/README.html#installation)

> Additional requirements are included in the generated project’s `README.md`, tailored to the selected template.

---

## ⚙️ Usage

```bash
# Install Cookiecutter
pip install cookiecutter

# Then run from GitHub template
cookiecutter gh:huynguyengl99/cookiecutter-python
```

> 💡 During setup, you’ll be prompted to choose your template type and fill in relevant project details.


---

### 🧭 Template Selection Prompt

When you run the command, Cookiecutter will prompt you to select one of the available templates:

```
Select a template
1 - Python app (A cookiecutter template for a normal python app)
2 - Python package (A cookiecutter template for a python package)
3 - DRF (A cookiecutter template for a django rest framework app)
4 - DRF package (A cookiecutter template for a drf package)
Choose from [1/2/3/4] (1):
```

> Press the corresponding number to select your desired template.

---

## ✨ Template Highlights

### 🐍 Python App (`py`)

- Dependency management with [UV](https://github.com/astral-sh/uv)
- Docker-ready setup
- Pre-commit hooks for consistent code quality
- Testing with `pytest`
- Code formatting via `Ruff`

---

### 📦 Python Package (`pypackage`)

- PyPI-ready project structure
- Docs setup for ReadTheDocs
- GitHub Actions CI/CD pipelines
- Open source license options
- Versioning and test framework built-in

---

### 🌐 Django REST App (`drf`)

- DRF project layout following modern best practices
- PostgreSQL database integration
- Optional: Google Login, Celery, WebSockets
- Email provider support (SendGrid, Mailgun, etc.)
- API documentation via Swagger & ReDoc

---

### 🧩 DRF Package (`drf_package`)

- Lightweight yet powerful structure for reusable APIs
- PostgreSQL support
- PyPI publishing setup
- Test scaffolding for DRF components
- Optional WebSocket integration

---

## 🛠️ Configuration Options

Each template offers tailored configuration prompts:

<details>
<summary><strong>Python App (`py`)</strong></summary>

- Project & repository name
- Description, author name/email

</details>

<details>
<summary><strong>Python Package (`pypackage`)</strong></summary>

- GitHub + PyPI usernames
- License selection
- Docker support
- Versioning options

</details>

<details>
<summary><strong>Django REST App (`drf`)</strong></summary>

- PostgreSQL version & timezone
- Cloud deployment options (AWS, GCP, Azure)
- Email service provider
- Google login, Celery, WebSocket toggles
- API casing (camelCase support)

</details>

<details>
<summary><strong>DRF Package (`drf_package`)</strong></summary>

- All the essentials for a PyPI-ready DRF extension
- PostgreSQL and WebSocket integration

</details>

---

## 🗂️ Directory Structures

### Python App (`py`)

```
project_name/
├── pyproject.toml
├── docker-compose.yml
├── Dockerfile
├── ruff.toml
├── README.md
└── project_slug/
    └── __init__.py  # + your code here
```

### Python Package (`pypackage`)

```
project_name/
├── pyproject.toml
├── LICENSE
├── docs/
├── tests/
├── README.md
└── project_slug/
    └── __init__.py  # + package modules
```

### Django REST App (`drf`)

```
project_name/
├── pyproject.toml
├── docker-compose.yml
├── Dockerfile
├── scripts/
│   └── manage.sh
├── README.md
└── project_slug/
    ├── config/
    ├── accounts/
    ├── core/
    └── status/
```

### DRF Package (`drf_package`)

```
project_name/
├── pyproject.toml
├── LICENSE
├── docs/
├── tests/
├── README.md
└── project_slug/
    └── __init__.py  # + your DRF components
```

---

## 🧪 Development Workflow

Each template includes tools and docs for:

- Setting up your local dev environment
- Running tests and checking coverage
- Managing dependencies
- Formatting/linting
- Performing migrations
- Docker-based development

---

## 🤝 Contributing

Contributions, bug reports, and ideas are welcome!
Feel free to fork, submit issues, or open a Pull Request.

---

## 📄 License

MIT License – see the `LICENSE` file for full details.
