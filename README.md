
# Cinema Ticket Booking API

This project is a FastAPI-based backend for a cinema ticket booking system. It uses PostgreSQL as the database.

---

## Running the Project with Docker

This project is dockerized to run both the FastAPI app and PostgreSQL database easily.

### Prerequisites

- Docker installed on your machine
- Docker Compose installed

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Create `.env` file

Create a `.env` file in the root directory of the project and add the following environment variables:

```
POSTGRESQL_USER=your_db_user
POSTGRESQL_PASS=your_db_password
POSTGRESQL_HOST=db
POSTGRESQL_PORT=5432
POSTGRESQL_NAME=your_db_name
```

> Note: `POSTGRESQL_HOST=db` corresponds to the Docker service name for the database container.

### Step 3: Build and Run Docker Containers

Run the following command to build and start the containers:

```bash
docker compose up --build
```

This command will:

- Build the FastAPI application image
- Pull and start the PostgreSQL database container
- Link the app container with the database container

### Step 4: Access the API

Once running, the FastAPI server will be accessible at:

```
http://localhost:8007
```

You can also visit the automatic API docs (Swagger UI) at:

```
http://localhost:8007/docs
```

---

## Notes

- The database will be created automatically inside the PostgreSQL container based on your `.env` settings.
- Make sure the ports `8007` (app) and `5432` (Postgres) are free on your local machine.
- If you want to stop the project, run:

```bash
docker compose down
```

---

## Files included

- `Dockerfile` for FastAPI app
- `docker-compose.yml` to orchestrate app and DB containers
- `.env` file (not committed to git, should be created manually)
- All source code files

---

## Contact

If you have any issues running the project, please contact the developer.
