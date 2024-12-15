const bookList = document.getElementById('book-list');
const bookForm = document.getElementById('book-form');
const refreshButton = document.getElementById('refresh-button');
const authorSelect = document.getElementById('author');
const authorForm = document.getElementById('author-form');

// تابع برای دریافت و نمایش کتاب‌ها
async function fetchBooks() {
    try {
        const response = await fetch('/api/books/');
        const books = await response.json();
        bookList.innerHTML = books.map(book => `
            <div>
                <h1>کتاب‌ها</h1>
                <h3>${book.title}</h3>
                <p>${book.description}</p>
                <p>تاریخ انتشار: ${book.published_date}</p>
                <p>نویسنده: ${book.author_name ? book.author_name : 'نامشخص'}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error fetching books:', error);
    }
}


// تابع برای افزودن کتاب جدید
bookForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const published_date = document.getElementById('published_date').value;
    const author = document.getElementById('author').value;

    try {
        await fetch('/api/books/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description, published_date, author }),
        });
        fetchBooks(); // به‌روزرسانی لیست کتاب‌ها
        bookForm.reset(); // ریست کردن فرم
    } catch (error) {
        alert('عدم توانایی در افزودن کتاب. لطفاً دوباره تلاش کنید.');
    }
});

// تابع برای حذف کتاب
async function deleteBook(id) {
    if (confirm('آیا مطمئن هستید که می‌خواهید این کتاب را حذف کنید؟')) {
        try {
            await fetch(`/api/books/${id}/`, { method: 'DELETE' });
            fetchBooks(); // به‌روزرسانی لیست کتاب‌ها
        } catch (error) {
            alert('عدم توانایی در حذف کتاب. لطفاً دوباره تلاش کنید.');
        }
    }
}

// تابع برای افزودن نویسنده جدید
authorForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const name = document.getElementById('author-name').value;
    const biography = document.getElementById('author-biography').value;

    try {
        await fetch('/api/authors/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, biography }),
        });
        fetchAuthors(); // به‌روزرسانی لیست نویسندگان
        authorForm.reset(); // ریست کردن فرم
    } catch (error) {
        alert('عدم توانایی در افزودن نویسنده. لطفاً دوباره تلاش کنید.');
    }
});

// دکمه بارگذاری مجدد
refreshButton.addEventListener('click', fetchBooks);

// بارگذاری نویسندگان برای فرم
async function fetchAuthors() {
    try {
        const response = await fetch('/api/authors/');
        const authors = await response.json();
        authorSelect.innerHTML = authors.map(author => `
            <option value="${author.id}">${author.name}</option>
        `).join('');
    } catch (error) {
        alert('عدم توانایی در دریافت نویسندگان. لطفاً دوباره تلاش کنید.');
    }
}

// بارگذاری اولیه داده‌ها
fetchBooks();
fetchAuthors();
