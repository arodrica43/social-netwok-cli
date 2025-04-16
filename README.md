# Social Network CLI

A clean, modular, and test-driven implementation of a console-based social networking platform, developed as part of a senior developer code test. The system allows users to post messages, read timelines, follow others, and view a combined "wall".

---

## Features

- **Post messages**: Users can write to their own timeline.
- **Read timelines**: View any user's messages in reverse chronological order.
- **Follow users**: Subscribe to another user's timeline.
- **Wall view**: Aggregated view of all followed users with timestamps.
- **Test-Driven**: test coverage of core logic using `unittest`.

---

## Tech Stack

- **Python 3.11**
- No external dependencies (fully in-memory)
- Modular architecture (`cli`, `service`, `domain`)
- Unit testing with `unittest`

---

## Getting Started

### Run app

```bash
python -m cli.app
```

> Example usage:
```
> Alice -> I love the weather today
> Bob -> Damn! We lost!
> Bob
Damn! We lost! (2 seconds ago)
> Alice
I love the weather today (5 seconds ago)
```

---

## Run with Docker

```bash
docker build -t social-cli .
docker run -it social-cli
```

---

## Run Tests

```bash
python -m unittest discover -s tests
```

---

## Continuous Integration

This project is integrated with GitHub Actions. Tests run on every push or pull request to `main`.

---

## Architecture

```
social-network-cli/
│
├── cli/           # Console interface & input parsing
├── service/       # Business logic and orchestration
├── domain/        # Core models and in-memory repositories
├── utils/         # Utility functions
└── tests/         # Unit tests
```

---

## Principles Followed

- Test-Driven Development (TDD)
- Clean Architecture
- SOLID Principles
- Readability and simplicity
- Extensibility in mind

---

## Future Improvements

- Persistent storage (SQLite, PostgreSQL)
- REST API or Web UI
- Enhanced command parsing
- User authentication & session tracking

