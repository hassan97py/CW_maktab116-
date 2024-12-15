const categoryList = document.getElementById('category-list');
const subcategoryList = document.getElementById('subcategory-list');
const errorMessage = document.getElementById('error-message');
const categoryContainer = document.getElementById('category-container');
const subcategoryContainer = document.getElementById('subcategory-container');
const backButton = document.getElementById('back-button');

// Fetch Categories
async function fetchCategories() {
    try {
        const response = await fetch('/api/categories/');
        if (!response.ok) throw new Error('Failed to load categories.');
        const categories = await response.json();
        displayCategories(categories);
    } catch (error) {
        errorMessage.textContent = error.message;
    }
}

// Display Categories
function displayCategories(categories) {
    categoryList.innerHTML = '';
    categories.forEach(category => {
        const li = document.createElement('li');
        li.textContent = category.name;
        li.onclick = () => fetchSubcategories(category.id);
        categoryList.appendChild(li);
    });
}

// Fetch Subcategories
async function fetchSubcategories(categoryId) {
    try {
        const response = await fetch(`/api/categories/${categoryId}/subcategories/`);
        if (!response.ok) throw new Error('No subcategories available.');
        const subcategories = await response.json();
        displaySubcategories(subcategories);
    } catch (error) {
        errorMessage.textContent = error.message;
    }
}

// Display Subcategories
function displaySubcategories(subcategories) {
    categoryContainer.style.display = 'none';
    subcategoryContainer.style.display = 'block';
    subcategoryList.innerHTML = '';
    subcategories.forEach(subcategory => {
        const li = document.createElement('li');
        li.textContent = subcategory.name;
        subcategoryList.appendChild(li);
    });
}

// Back Button Functionality
backButton.onclick = () => {
    subcategoryContainer.style.display = 'none';
    categoryContainer.style.display = 'block';
    errorMessage.textContent = '';
};

// Initial Fetch
fetchCategories();

// Add Category Functionality
document.getElementById('add-category-button').onclick = async () => {
    const name = document.getElementById('new-category-name').value;
    if (!name) return alert('لطفاً نام دسته را وارد کنید.');

    try {
        const response = await fetch('/api/categories/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name })
        });
        if (!response.ok) throw new Error('خطا در افزودن دسته.');
        fetchCategories(); // بروزرسانی لیست دسته‌ها
    } catch (error) {
        alert(error.message);
    }
};
