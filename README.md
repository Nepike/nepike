## Maksim Shchuchkin

Backend developer, Python. MIPT — applied mathematics and physics, bachelor's in 2026, now in the
master's programme at the Kurchatov school (КНТ).

Most of what I write has to keep running afterwards. The two projects below are the ones I actually
maintain; the rest of this profile is coursework and experiments, labelled as such.

### What I work on

**[knt-portal](https://github.com/Nepike/knt-portal)** — the student portal of my faculty, live at
[knt-mipt.ru](https://knt-mipt.ru). Django 6 on PostgreSQL, WebSockets over Channels, background
work in Celery, files in S3-compatible storage, Docker Compose, deployed by a push to `main`, 511
tests. Twelve applications, 500+ registered users, one developer — me. It is the second generation:
the first ran for two years and is kept as
[knt-portal-legacy](https://github.com/Nepike/knt-portal-legacy).

**[thesis-remote-robotics-lab](https://github.com/Nepike/thesis-remote-robotics-lab)** — a server
that lets people drive real robots over the network: device locking, priority command queues,
cancellable server-side group manoeuvres, and ArUco navigation that fuses several overhead cameras
into an unscented Kalman filter and plans with A\*. asyncio and FastAPI on one side, robot firmware
in C++ on the other. Bachelor's thesis at the Kurchatov Institute robotics laboratory, graded 10/10.

### Also worth opening

| | |
|---|---|
| [work-postovalova-site](https://github.com/Nepike/work-postovalova-site) | A commissioned Django site whose contact form is triaged from a Telegram group — inline buttons write straight back to the database |
| [edu-hate-lang-compiler](https://github.com/Nepike/edu-hate-lang-compiler) | A small statically-typed language: lexer, recursive-descent parser, type checking during the parse, and a POLIZ interpreter. 2 900 lines of C++, no parser generators |
| [edu-input-action-registry](https://github.com/Nepike/edu-input-action-registry) | A C++17 core behind a leftist heap of polymorphic actions, exposed to Python with pybind11 and driven from a PySide6 application |
| [edu-machine-learning-labs](https://github.com/Nepike/edu-machine-learning-labs) | Eight labs from classical scikit-learn to PyTorch: CNN, autoencoder, character-level transformer, GAN |
| [allgohome](https://github.com/Nepike/allgohome) | EKF, UKF and a particle filter running side by side on the same noisy camera, with A\* and a waypoint controller — the prototype the thesis procedure grew from |
| [datspulse-client-ants](https://github.com/Nepike/datspulse-client-ants) | An operator console built during a hex-grid strategy contest: live arena map, hand-planned paths, batch move submission |

Repository names carry a prefix: `work-` is commissioned, `thesis-` is the diploma, `edu-` is
university or school coursework. Everything without a prefix is my own.

### Stack

Python · Django · asyncio · FastAPI · PostgreSQL · Redis · Celery · Channels · Docker · nginx ·
Linux · GitHub Actions · C++ · pybind11 · HTML / CSS / JS · Tailwind · HTMX

### Contacts

Telegram [@pikethemax](https://t.me/pikethemax) · maxventilator@gmail.com
