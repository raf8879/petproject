# 📝 SiteWomen

**SiteWomen** is a learning project designed to practice web development skills using Django.  

## 🚀 Features
- User registration and authentication  
- User profile management  
- Adding and editing content  
- Social authentication (GitHub, VK)  
- CAPTCHA support for bot protection  

## 🛠 Technologies Used
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** PostgreSQL  
- **Caching:** Redis  
- **Authentication:** Django Social Auth  
- **Additional Tools:** Django Debug Toolbar, Captcha  

## 🔧 Installation and Setup

### 1️⃣ Clone the repository:
bash
git clone https://github.com/raf8879/petproject.git
cd petproject


2️⃣ Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3️⃣ Set up the .env file
Create a .env file in the project root and add the following:

DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=sitewomen_db
DB_USER=sitewomen
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST_PASSWORD=your_email_password
SOCIAL_AUTH_GITHUB_SECRET=your_github_secret
SOCIAL_AUTH_VK_OAUTH2_SECRET=your_vk_secret



4️⃣ Apply migrations and run the server:
python manage.py migrate
python manage.py runserver

Open in your browser:
👉 http://127.0.0.1:8000



🔗 Contact
👨‍💻 Author: Rafael Dzhabrailov
📩 Email: rafaelrafael8879@gmail.com
🔗 LinkedIn: www.linkedin.com/in/rafael-dzhabrailov-756716330