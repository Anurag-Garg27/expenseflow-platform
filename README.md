# ExpenseFlow Platform

ExpenseFlow Platform is a personal expense tracking application that I'm building from scratch to understand how software is developed and deployed in the real world.

The goal of this project is not just to build an expense tracker. I want to experience the complete journey of an application—from writing backend code and testing APIs to containerizing it with Docker, deploying it on AWS, setting up CI/CD, monitoring the application, and maintaining it like a real production system.

Instead of following a complete tutorial, I'm building this project one step at a time while understanding the reason behind every engineering decision.

## Why I'm Building This

As someone preparing for a DevOps career, I wanted a project that would teach me more than just tools.

Through this project, I'm learning:

* Backend development with Python and Flask
* API development and testing
* Database design and integration
* Git and GitHub workflows
* Docker and containerization
* CI/CD with GitHub Actions
* AWS cloud deployment
* Monitoring and logging
* Production-style engineering practices

More importantly, I want to understand how different engineering roles work together throughout the Software Development Lifecycle (SDLC).

## Current Status

🚧 Currently working on **Sprint: Backend-007**

### Completed

* Project foundation
* Flask application setup
* Basic application structure
* Static routes (`/`, `/about`, `/contact`)
* Dynamic routing
* JSON responses using `jsonify()`
* Dynamic expense lookup using expense IDs
* Basic error handling for invalid expense requests

### Next

The next step is to build the **Expense Collection API (`GET /expenses`)**, which will return all available expenses and prepare the project for database integration.

## Repository Structure

```text
expenseflow-platform/
│
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── app.py
└── docs/
```

## Project Roadmap

* [x] Initialize repository
* [x] Build Flask backend foundation
* [x] Create static routes
* [x] Implement dynamic routing
* [x] Return JSON responses
* [x] Implement dynamic expense lookup
* [ ] Build expense collection API
* [ ] Design and integrate the database
* [ ] Create REST APIs
* [ ] Write API tests
* [ ] Containerize the application with Docker
* [ ] Build a CI/CD pipeline
* [ ] Deploy the application on AWS
* [ ] Add monitoring and logging
* [ ] Complete the project documentation

This repository will continue to grow as I keep learning and adding new features. My goal isn't just to finish the project—it's to understand why each piece exists and how everything works together in a real-world software development workflow.
