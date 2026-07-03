# 🖼️Image to PDF Converter 

<p align="center">
  Convert one or multiple images into a single PDF using a simple and responsive web interface built with Flask.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

## 📌 Overview

Image to PDF Converter is a lightweight web application that allows users to upload one or multiple image files and merge them into a single PDF document. Built using Flask and Pillow, it provides a clean and user-friendly interface for quick image-to-PDF conversion.

---

## ✨ Features

- 📂 Upload one or multiple images
- 📄 Merge all images into a single PDF
- ⚡ Fast image processing
- 🎨 Simple and responsive UI
- 📥 Automatic PDF download
- 🖼️ Supports JPG, JPEG, and PNG images

---

## 🛠️ Tech Stack

Category| Technologies
Backend| Python, Flask
Frontend| HTML5, CSS3, JavaScript
Image Processing| Pillow
Server| Flask Development Server

---

## 📁 Project Structure

image-to-pdf-converter/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
├── outputs/
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/yourusername/image-to-pdf-converter.git

cd image-to-pdf-converter

### 2. Create a Virtual Environment (Optional)

Windows

python -m venv venv

venv\Scripts\activate

Linux / macOS

python3 -m venv venv

source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

▶️ Running the Project

Start the Flask server.

python app.py

Open your browser and visit:

http://127.0.0.1:5000

---

🚀 How It Works

1. Open the application.
2. Upload one or more image files.
3. Click Convert to PDF.
4. Images are processed using Pillow.
5. A single PDF is generated.
6. The PDF is downloaded automatically.

---

🔄 Workflow

User
   │
   ▼
Upload Images
   │
   ▼
Flask Backend
   │
   ▼
Pillow Processes Images
   │
   ▼
Generate PDF
   │
   ▼
Return PDF
   │
   ▼
Automatic Download

---

📦 Dependencies

- Flask
- Pillow

Install them using:

pip install -r requirements.txt

---

📸 Supported Formats

- JPG
- JPEG
- PNG

---

🌟 Future Enhancements

- Drag & Drop Upload
- Image Preview
- Rearrange Images Before Conversion
- Rotate Images
- Delete Selected Images
- PDF Compression
- Multiple Page Sizes (A4, Letter, Legal)
- Password-Protected PDF
- Dark Mode
- Progress Bar
- WebP & HEIC Support
- Deploy on Render or Railway
- User Authentication
- Conversion History

---

🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

git checkout -b feature-name

3. Commit your changes

git commit -m "Add feature"

4. Push the branch

git push origin feature-name

5. Open a Pull Request

---

📄 License

This project is licensed under the MIT License.

---

👩‍💻 Author

Ritika Singh Chandel

If you found this project useful, don't forget to ⭐ the repository
