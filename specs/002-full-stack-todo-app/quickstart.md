# Quickstart: Full-Stack Web Todo Application

This guide provides instructions on how to set up and run the project locally.

## Prerequisites

- Python 3.9+
- Node.js 16+
- `pip` and `npm`

## Backend Setup (FastAPI)

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up environment variables:**
    -   Create a `.env` file in the `backend` directory.
    -   Add the following variables:
        ```
        DATABASE_URL="your_neon_database_url"
        SECRET_KEY="your_jwt_secret"
        ALGORITHM="HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES=30
        ```

6.  **Run the backend server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The backend will be running at `http://localhost:8000`.

## Frontend Setup (Next.js)

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Set up environment variables:**
    -   Create a `.env.local` file in the `frontend` directory.
    -   Add the following variables:
        ```
        NEXT_PUBLIC_API_URL="http://localhost:8000"
        ```

4.  **Run the frontend server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:3000`.

## Running the Application

1.  Start the backend server.
2.  Start the frontend server.
3.  Open your browser and navigate to `http://localhost:3000`.
