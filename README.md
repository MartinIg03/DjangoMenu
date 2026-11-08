# DjangoMenu

# DjangoMenu – Virtuoso Digital Menu

## About the Project

DjangoMenu is a web-based digital restaurant menu developed using **Python and Django**. The project is inspired by the Virtuoso bar and provides visitors with an interactive and visually engaging way to explore its menu.

The application is designed to make browsing food and drinks simple, convenient and accessible from different devices, including smartphones, tablets and desktop computers.

**Disclaimer:** This project is an independent concept inspired by Virtuoso. It is not the bar's official menu or website.

## Features

### 1. Interactive Digital Menu
- Browse menu items organized into different categories.
- Select a category to open its corresponding menu.
- View individual dishes and their descriptions.
- Check prices displayed in euros (€).
- View photographs of selected dishes.

### 2. Bulgarian and English Language Support
The application supports two languages:
- Bulgarian (BG)
- English (EN)

Visitors can switch between languages using the language selector. The application can also automatically select an initial language based on the visitor's browser language.

Menu categories, dish names, descriptions and informational content support both languages.

### 3. Photo Gallery
The main page features a visual photo gallery that showcases the venue through uploaded photographs.

Images are automatically arranged according to their proportions, creating a collage-style presentation.

### 4. About Us
Visitors can access an **About Us** section to learn more about the venue.

This section can contain additional information, descriptions and relevant external links.

### 5. Content Management (Admin Panel)
The application includes a Django administration panel that allows authorized administrators to manage the menu without directly modifying the source code.

Administrators can:

- **Categories:** Create and organize menu categories, add Bulgarian and English names, and provide additional notes.
- **Dishes:** Add new dishes, edit names and descriptions, assign categories, upload photographs and set prices.
- **Visibility:** Control which dishes are displayed to visitors.
- **Ordering:** Arrange the order in which categories and dishes appear.
- **Gallery:** Upload and organize photographs displayed on the main page.
- **About Us:** Update the informational content in both supported languages.

## How to Use the Application

### For Visitors

1. Open the digital menu through its website address.
2. Browse the available menu categories.
3. Select a category to view its contents.
4. Explore the available dishes, descriptions, photographs and prices.
5. Use the BG/EN buttons to change the display language.
6. Select the About Us section to learn more about the venue.

No registration or account is required to browse the public menu.

### For Administrators

1. Navigate to the administration page by adding `/admin/` to the website address.
2. Log in using your Django administrator credentials.
3. Select the section you want to manage.
4. Add, edit or remove menu content as required.
5. Save your changes.

Changes to the menu are reflected on the public website through the Django application.

## Technology Stack

The project uses the following technologies:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Backend framework and application logic |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Interactive functionality and language switching |
| Bootstrap 5 | UI components and responsive elements |
| SQLite | Database (configured development backend) |
| Pillow | Image processing support |

## Project Structure

```text
DjangoMenu/
│
├── config/              # Django project configuration
│
├── menu/                # Main application
│   ├── models.py        # Categories, dishes, gallery and About Us
│   ├── views.py         # Application logic
│   ├── urls.py          # Application routes
│   ├── admin.py         # Admin panel configuration
│   ├── templates/       # HTML templates
│   └── static/          # CSS, JavaScript and static images
│
├── Gallary/             # Gallery-related project assets
│
├── manage.py            # Django management utility
└── README.md            # Project documentation
```

## Running the Project Locally

To run the project on your local machine:

**1. Clone the repository**

```bash
git clone https://github.com/MartinIg03/DjangoMenu.git
cd DjangoMenu
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

**3. Install the dependencies**

Install the packages specified by the project's dependency configuration.

For a Pipenv setup:

```bash
pipenv install
```

**4. Apply database migrations**

```bash
python manage.py migrate
```

**5. Create an administrator account**

```bash
python manage.py createsuperuser
```

**6. Start the development server**

```bash
python manage.py runserver
```

**7. Open the application**

Visit:

- Public menu: http://127.0.0.1:8000/
- Administration panel: http://127.0.0.1:8000/admin/

## Project Purpose

The purpose of DjangoMenu is to demonstrate how a traditional restaurant menu can be transformed into a modern digital experience.

It combines Django's backend capabilities with an interactive frontend, bilingual content management and a visual presentation to create a practical digital menu solution.

The application also demonstrates the use of Django models, database relationships, template rendering, static and media files, and administrative content management.  
