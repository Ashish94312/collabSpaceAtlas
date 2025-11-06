#  ![CollabSpace Atlas](favicon.ico) CollabSpace Atlas

[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)](https://opensource.org/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-blue)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **"A unified map of Artificial Intelligence knowledge."**

CollabSpace Atlas is a Django-based content management platform designed to centralize AI research, simplify learning, and connect researchers, students, and practitioners through structured, accessible AI insights. Built with an open-access approach, the platform requires no authentication—all content is freely accessible to facilitate knowledge sharing and collaboration.

---

## 🎯 Vision & Purpose

CollabSpace Atlas is designed to be the **go-to hub** where researchers, students, and AI enthusiasts can:

- 📰 **Read deep, human-written explainers** on complex AI topics
- 📚 **Explore curated research papers** from top venues (arXiv, NeurIPS, CVPR, ICLR, etc.)
- 🤖 **Access AI-generated summaries** that make cutting-edge research more digestible
- 🤝 **Collaborate** through discussions, reviews, and knowledge sharing

### The Problem We're Solving

AI research is growing exponentially, but:
- New papers are published daily across multiple platforms
- Technical jargon and dense content make research inaccessible to many
- There's no centralized place to discover, understand, and discuss AI research
- Finding relevant papers and understanding their significance is time-consuming

### Our Solution

CollabSpace Atlas bridges this gap by:
1. **Curating** the most important and impactful AI research papers
2. **Summarizing** complex papers using AI to make them accessible
3. **Explaining** fundamental concepts through human-written, educational content
4. **Connecting** a community of learners, researchers, and practitioners

---

## ✨ Key Features

- 🏠 **Homepage** with featured AI subfields (ML, NLP, CV, RL, Robotics)
- 🔍 **Search & Filter** functionality (keywords, topics, difficulty)
- 📄 **Markdown-based Content** with rich metadata and frontmatter support
- 📝 **Research Paper Support** with specialized templates
- 🌐 **No Authentication Required** - open access for everyone
- 📱 **Responsive Design** for all devices
- 🗂️ **Topic Organization** - hierarchical topic structure with subtopics
- 📊 **Interactive Roadmaps** - visualize learning paths and connections

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.8
- **Content:** Markdown with YAML frontmatter
- **Database:** SQLite (default, easily switchable to PostgreSQL)
- **Rendering:** Python-Markdown with extensions (optional pymdown-extensions)
- **Deployment:** Any Django-compatible hosting (Heroku, Railway, Render, etc.)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/collabSpaceAtlas.git
   cd collabSpaceAtlas
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000`
   - No signup or login required - start exploring immediately!

### Optional: Enhanced Markdown Support

For enhanced markdown rendering (math equations, syntax highlighting, emojis), install optional dependencies:

```bash
pip install pymdown-extensions
```

This is optional - the application works without it, but provides better rendering features.

---

## 📁 Project Structure

```
collabSpaceAtlas/
├── content/                    # Content directory
│   ├── topics/                # Content organized by topic
│   │   ├── ml/               # Machine Learning content
│   │   ├── stats/            # Statistics content
│   │   ├── deep-learning/    # Deep Learning content
│   │   └── _roadmap.md       # Topic roadmaps
│   ├── templates/            # Content templates
│   │   ├── basic-template.md
│   │   └── research-paper-template.md
│   └── README.md             # Content guidelines
├── collabSpaceAtlas/         # Django app
│   ├── content_loader.py     # Loads markdown content
│   ├── markdown_renderer.py  # Renders markdown to HTML
│   ├── models.py            # Database models
│   ├── views.py             # View handlers
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
├── collabSpace/             # Django project settings
│   ├── settings.py
│   └── urls.py
├── manage.py                # Django management script
├── requirements.txt          # Python dependencies
└── README.md               # This file
```

---

## 📝 Adding Content

### Creating a New Content File

1. **Create a markdown file** in the appropriate topic folder:
   ```
   content/topics/ml/intro-to-ml.md
   ```

2. **Use the frontmatter format:**
   ```markdown
   ---
   title: "Introduction to Machine Learning"
   slug: "intro-to-ml"
   topic: "ml"
   difficulty: "beginner"
   estimated_time: 60
   tags: ["machine-learning", "basics"]
   status: "published"
   ---
   
   # Your content here
   
   Write your markdown content below the frontmatter...
   ```

3. **The system will automatically detect and display the content** on the next page load.

### Content Templates

Templates are available in `content/templates/`:
- `basic-template.md` - Standard educational content
- `research-paper-template.md` - Research papers and comparisons

### Frontmatter Fields

- `title` (required): Display title
- `slug` (optional): URL slug (defaults to filename)
- `topic` (optional): Topic category
- `difficulty`: "beginner", "intermediate", "advanced"
- `estimated_time`: Reading time in minutes
- `tags`: Array of tags
- `status`: "published" or "draft"
- `summary`: Brief description

---

## 🤝 Contributing

We welcome contributions from everyone! Whether you're a developer, researcher, writer, or designer, there's a place for you here.

### How You Can Help

#### 🖋️ Content Contributions
- **Write explainer articles** on AI topics (beginner-friendly guides)
- **Curate and add research papers** with metadata
- **Review and improve** existing summaries
- **Translate content** to make it accessible globally
- **Create roadmaps** for learning paths

#### 💻 Code Contributions
- **Frontend:** UI/UX improvements, new features, bug fixes
- **Backend:** Django views, content loading, markdown rendering
- **DevOps:** CI/CD setup, deployment automation, monitoring
- **Documentation:** Improve docs, add examples, write tutorials

#### 🐛 Bug Reports & Feature Requests
- Found a bug? Open an issue with details
- Have an idea? Suggest a feature with use cases

### Contribution Workflow

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/collabSpaceAtlas.git
   cd collabSpaceAtlas
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes**
   - Follow Python/Django conventions
   - Write clear, self-documenting code
   - Test your changes locally
   - Update documentation if needed

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your meaningful commit message"
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Fill out the PR description
   - Reference related issues
   - Request review from maintainers

### Contribution Guidelines

- ✅ **Be respectful** and inclusive in all interactions
- ✅ **Test** your changes before submitting
   ```bash
   python manage.py test
   python manage.py runserver  # Test manually
   ```
- ✅ **Document** your code and updates
- ✅ **Keep PRs focused** — one feature/fix per PR when possible
- ✅ **Follow** existing code style and patterns

### Content Writing Guidelines

When contributing articles or summaries:

- Use **clear, accessible language** — explain technical terms
- Include **examples and analogies** to aid understanding
- Structure content with **headings, lists, and code blocks**
- Add **references and links** to original sources
- Follow our **content templates** (see `/content/templates/`)
- Use proper frontmatter format

### First-Time Contributors

New to open source? We're beginner-friendly! Start with:
- Fixing typos in documentation
- Adding new content examples
- Improving existing content
- Reporting bugs with reproduction steps

### 🚀 Contributing to Our Other Projects

We're building multiple open-source tools to transform how people collaborate and learn. If you're interested in collaborative editing and real-time document creation, check out our other project:

#### [CollabSpace - Real-time Document Editor](https://github.com/Ashish94312/collabSpace) 📝

**CollabSpace** is a real-time collaborative document editor that competes with Google Docs and Notion. Built with React, Node.js, and WebSockets, it offers:

- **Real-time Collaboration** - Multiple users editing simultaneously
- **Rich Text Editing** - Full formatting, images, and media support
- **Multi-page Documents** - Create complex documents with multiple pages
- **WebSocket Integration** - Instant synchronization across all users
- **JWT Authentication** - Secure user management
- **Image Handling** - Drag & drop, resize, and manage images

**Why Contribute to CollabSpace?**
- 🎯 **Impact** - Help build an open-source alternative to proprietary tools
- 🚀 **Modern Stack** - Work with React, Node.js, WebSockets, and Prisma
- 🤝 **Community** - Join a growing community of contributors
- 📚 **Learning** - Gain experience with real-time collaboration systems
- 💡 **Innovation** - Help shape the future of collaborative editing

**Easy Ways to Get Started:**
- Fix bugs and improve error handling
- Enhance mobile responsiveness
- Add new editor features
- Improve WebSocket reconnection logic
- Add documentation and examples
- Star the repository and share with others!

👉 **Check it out:** [https://github.com/Ashish94312/collabSpace](https://github.com/Ashish94312/collabSpace)

Every contribution matters - whether it's here at CollabSpace Atlas or at CollabSpace, your help makes a difference! 🌟

---

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Creating Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Django Admin (Optional)

If you need admin access for development:

```bash
python manage.py createsuperuser
```

Then visit: `http://127.0.0.1:8000/admin`

### Adding New Features

The architecture is designed to be extensible:
- Add new topic types by creating folders in `content/topics/`
- Create custom templates for different content formats
- Extend `ContentLoader` for additional metadata parsing
- Add new views in `views.py` for specialized content displays
- Customize markdown rendering in `markdown_renderer.py`

---

## 🌐 Related Projects

We're also working on other exciting projects:

### [CollabSpace](https://github.com/Ashish94312/collabSpace) 🔗

A real-time collaborative document editor built with React, Node.js, and WebSockets. CollabSpace allows multiple users to edit documents simultaneously with features like rich text editing, image handling, page management, and real-time synchronization.

**Key Features:**
- Real-time collaboration with WebSockets
- Rich text editing capabilities
- Multi-page document support
- Image upload and management
- User authentication and document sharing

Check it out: https://github.com/Ashish94312/collabSpace

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to all contributors who help make AI research more accessible
- Inspired by the open-source community's commitment to knowledge sharing
- Built with ❤️ for researchers, students, and AI enthusiasts worldwide

---

## 📞 Connect With Us

- **GitHub Issues:** [Report bugs or request features](https://github.com/your-username/collabSpaceAtlas/issues)
- **Contributions:** [See our contributors](https://github.com/your-username/collabSpaceAtlas/graphs/contributors)

---

## 🌟 Star Us!

If you find CollabSpace Atlas useful, please consider giving us a ⭐ on GitHub!

---

## 🚧 Roadmap

### Current Phase: MVP Development

### Upcoming Features
- 🤖 Conversational Assistant for paper Q&A
- 📊 Enhanced Knowledge Graph Visualization
- 💬 Discussion threads per paper
- 📚 Collections and curated lists
- 🎯 Smart Recommendations
- 📥 Auto-ingestion from arXiv API
- 🔍 Advanced search with filters

---

**Ready to contribute?** Jump into the issues and start making a difference! 🚀

---

_Made with ❤️ by the open source community_
