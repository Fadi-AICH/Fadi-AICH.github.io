---
layout: post
title: "Civiscore — Public Service Evaluation Platform"
date: 2025-05-22
permalink: /projects/civiscore/
categories: [Projects, Software, Full-Stack]
tags: [FastAPI, React, MySQL, JWT, Docker, GitHub-Actions, GlobeGL]
external_image: https://raw.githubusercontent.com/Fadi-AICH/Civiscore/main/image.png
hide_banner: true
case_study: true
toc: true
excerpt: "Team-built participatory platform for evaluating public services with FastAPI, React, MySQL, JWT authentication, interactive geospatial visualization, Docker and CI/CD."
---

<div class="case-kicker">Full Stack · REST API · Data Visualization · Team Project</div>
<p class="case-lead"><strong>Civiscore</strong> is a participatory web platform designed to let citizens evaluate public services and explore aggregated service-quality information geographically. It was developed as a <strong>team project</strong> by Fadi AICH, Ilyasse ELHAMDOUCHI and Anas EL BADRE, combining a FastAPI backend, relational data model, React interface and interactive 3D globe.</p>

<div class="case-summary">
  <div><b>FastAPI</b><span>REST backend and Swagger documentation</span></div>
  <div><b>React</b><span>responsive client application</span></div>
  <div><b>MySQL</b><span>relational persistence with SQLAlchemy</span></div>
  <div><b>Docker + CI/CD</b><span>reproducible services and automated pipeline</span></div>
</div>

<div class="case-flow"><span>React UI</span><i>→</i><span>REST API</span><i>→</i><span>FastAPI</span><i>→</i><span>SQLAlchemy</span><i>→</i><span>MySQL</span><i>→</i><span>Statistics / Globe</span></div>

<div class="case-note"><strong>Product idea:</strong> combine citizen-generated evaluations with a visual geographic interface so service data is not limited to tables or isolated reviews.</div>

## 1. User-facing concept

The platform is designed around three main user needs:

- discover public services;
- submit evaluations based on defined criteria;
- understand aggregated results through statistics and geospatial visualization.

The interface includes an interactive globe powered by `globe.gl`, giving the project a visual exploration layer on top of the underlying CRUD application.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/Civiscore/main/image.png" alt="Civiscore application"><figcaption><strong>Main Civiscore interface.</strong> The application combines conventional service data with interactive geographic exploration.</figcaption></figure>

## 2. Application architecture

The project uses a clear frontend/backend separation:

- **React.js** handles the interactive user interface;
- **Axios** communicates with the REST API;
- **FastAPI** exposes application and authentication endpoints;
- **SQLAlchemy** maps application entities to the relational database;
- **MySQL** stores users, services, evaluations, criteria and related data;
- **Docker Compose** starts the main services consistently.

This separation makes the frontend replaceable without rewriting the backend business logic, while the API can be inspected independently through Swagger.

## 3. Authentication and authorization

Authentication is handled using JWT-based flows. The API includes signup/login endpoints and role-aware user management.

The security design matters because the platform distinguishes between anonymous visitors, authenticated users and administrative operations. Authentication protects operations that modify persistent platform data while public exploration can remain accessible where appropriate.

Representative API routes documented in the repository include:

- `POST /api/v1/auth/signup`
- `POST /api/v1/auth/login`
- service CRUD under `/api/v1/services/`
- evaluation CRUD and statistics endpoints;
- user-management endpoints;
- evaluation-criteria and score endpoints.

## 4. Domain model

The application revolves around entities such as users, public services, evaluations and evaluation criteria. The relational model keeps those responsibilities explicit instead of storing the platform state in loosely structured frontend data.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/Civiscore/main/image1.jpg" alt="Civiscore UML class diagram"><figcaption><strong>Class/domain diagram.</strong> The model shows the core entities and their relationships, providing the structural basis for the FastAPI/SQLAlchemy backend.</figcaption></figure>

## 5. User and administrator workflows

The application distinguishes between user-facing evaluation flows and administrative capabilities. The use-case design documents how registered users search, consult and evaluate services while administrators manage platform data and governance operations.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/Civiscore/main/image2.jpg" alt="Civiscore user administrator use cases"><figcaption><strong>User/admin use cases.</strong> This view documents the authenticated workflows and separates normal citizen actions from administrative responsibilities.</figcaption></figure>

Visitors also have a separate set of actions that do not require authentication.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/Civiscore/main/image3.jpg" alt="Civiscore visitor use cases"><figcaption><strong>Visitor use cases.</strong> Public browsing is modeled independently from the actions available to registered users.</figcaption></figure>

## 6. Evaluations and statistics

The backend provides CRUD operations for evaluations as well as statistics endpoints for individual services and overall platform summaries. This means aggregated metrics are calculated from backend data rather than being static values embedded in the UI.

The repository documents endpoints such as service-level and overall statistics, along with voting support for evaluations.

## 7. Geospatial visualization

`globe.gl` provides the 3D geographic interface. This turns location-linked service data into an explorable visualization and demonstrates integration between application data and a more specialized frontend library built on the Three.js ecosystem.

The value of this feature is not only visual polish: it gives users a different way to navigate country/service information than a standard list or dashboard.

## 8. Dockerized development and deployment

The repository separates backend and frontend Docker builds and includes a `docker-compose.yml` for local orchestration. A developer can configure environment variables and start the services together rather than manually reproducing each runtime setup.

The documented local architecture exposes:

- FastAPI backend on port 8000;
- React frontend on port 3000;
- MySQL as the application database.

## 9. Testing and quality

The repository documents testing at several layers:

- backend tests with pytest and Pydantic validation;
- frontend component/interaction tests;
- integration scenarios such as registration, evaluation and voting.

The project README reports test coverage above 80%. I present that here as a repository-documented project metric rather than an independently re-measured value on this portfolio page.

## 10. CI/CD

A GitHub Actions workflow is documented for:

1. Python/JavaScript linting;
2. backend and frontend tests;
3. Docker image builds;
4. continuous deployment.

The project also has a public deployment configured at **civiscore.vercel.app**.

## 11. Team project context

This is intentionally presented as a team project, not as solo work. The repository credits:

- **Fadi AICH**
- **Ilyasse ELHAMDOUCHI**
- **Anas EL BADRE**

For a portfolio, that distinction matters: the project demonstrates collaboration on a multi-component application in addition to technical implementation.

## 12. What this project demonstrates

Civiscore shows experience outside a pure security lab:

- API design with FastAPI;
- relational data modeling;
- JWT-based authentication;
- React application development;
- geospatial / 3D visualization;
- Dockerized application architecture;
- automated testing and CI/CD;
- collaborative software development.

## 13. Potential extensions

The repository identifies future directions including:

- real-time notifications with WebSockets;
- internationalization;
- CSV/PDF export;
- gradual service decomposition where justified by scale.

<div class="case-actions"><a href="https://github.com/Fadi-AICH/Civiscore" target="_blank">GitHub repository ↗</a><a href="https://civiscore.vercel.app/" target="_blank">Live application ↗</a><a href="{{ '/projects/' | relative_url }}">All projects</a></div>
