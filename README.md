# E-commerce API

This is a backend API for a sample e-commerce application built with FastAPI and MongoDB.

## Features

-   **Product APIs:** Create and list products with filtering and pagination.
-   **Order APIs:** Create orders and retrieve orders by user with pagination.
-   **Database:** MongoDB Atlas integration using Motor (async driver).
-   **Deployment:** Optimized for Railway with a `Procfile`.

## Setup and Running Locally

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd ecommerce-api
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up MongoDB URI:**
    Create a `.env` file in the `ecommerce-api` directory and add your MongoDB Atlas connection string:
    ```
    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority
    ```
    Replace `<username>`, `<password>`, `<cluster-url>`, and `<database-name>` with your actual MongoDB Atlas credentials.

4.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## API Documentation

Once the application is running, you can access the interactive API documentation (Swagger UI) at:

-   `http://127.0.0.1:8000/docs`
-   `http://127.0.0.1:8000/redoc`

## Deployment on Railway

1.  **Create a new project on Railway** and connect your GitHub repository.
2.  **Railway will automatically detect** the `Procfile` and set up the build and start commands.
3.  **Add a `MONGO_URI` environment variable** in your Railway project settings. This variable should contain your MongoDB Atlas connection string.

    Example:
    `MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority`

4.  **Deploy the application.** Railway will handle the rest.

Your API will be accessible at the URL provided by Railway (e.g., `https://your-project-name.up.railway.app`).