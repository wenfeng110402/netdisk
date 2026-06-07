# CloudDisk

A cloud storage backend API built with FastAPI, integrated with Cloudflare R2, and designed to work with a Next.js frontend.

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional, for containerized deployment)
- Cloudflare R2 account

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd netdisk
   ```

2. **Set up environment variables**
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

### Docker Deployment

1. **Configure environment variables**
   ```bash
   cp backend/.env.example backend/.env
   # Edit .env with your configuration
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **View logs**
   ```bash
   docker-compose logs -f backend
   ```

4. **Stop services**
   ```bash
   docker-compose down
   ```

## Project Structure

```
netdisk/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── models/      # Database models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # Business logic
│   │   ├── websocket/   # WebSocket handlers
│   │   ├── middleware/  # Custom middleware
│   │   ├── utils/       # Utility functions
│   │   ├── config.py    # Configuration
│   │   ├── database.py  # Database setup
│   │   └── main.py      # Application entry
│   ├── tests/           # Test files
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
├── frontend/            # Next.js frontend (to be implemented)
├── docs/                # Documentation
├── docker-compose.yml
└── README.md
```

## Configuration

All configuration is managed through environment variables. See `backend/.env.example` for available options.

Key configurations:
- Database connection
- Cloudflare R2 credentials
- OAuth provider credentials (Google, GitHub)
- User quotas and limits
- JWT settings
- CORS origins

## API Documentation

Once the server is running, access interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT
