# URL Shortener

## 🛠 Tools & Technologies Used
- Python 3
- Flask (web framework)
- SQLite3 (for lightweight database storage)

## 📌 About the Project
A simple, functional, and persistent URL shortening web service built using Python and Flask.

It allows users to shorten any valid URL and then redirect to the original URL using the generated short code.

## ✅ Key Features
- Modular and logically organized codebase
- Persistent storage of URLs using SQLite3
- Protection against SQL injection (uses parameterized queries)
- Clean, RESTful API routes

## ⚠️ Current Limitations
- No user interface (API-only)
- Not fault-tolerant (runs locally; no error handling for DB/server failures)
- No caching layer (every request hits the database)
- Not scalable (SQLite is not suitable for high-concurrency or high-traffic)
- No concurrency control (simultaneous users might generate the same short code)
- Security vulnerabilities (no input validation or rate limiting)
- No logging or monitoring implemented

## 📌 Conclusion
This project is a solid proof-of-concept for a URL shortener with basic persistence and functionality. While it demonstrates core principles like modularity and SQL safety, it is **not yet production-ready**. Improving scalability, fault-tolerance, security, and observability would be necessary for deployment.

---

## 💡 Future Improvements
- Replace SQLite with PostgreSQL or a scalable database
- Add input validation and rate limiting
- Implement caching (e.g., with Redis) for frequently accessed URLs
- Add structured error handling and logging
- Deploy with production-ready tools (e.g., gunicorn + nginx, Docker)

