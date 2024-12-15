// Fetch categories from the API
async function fetchCategories() {
    try {
        const response = await fetch('/api/categories/');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching categories:', error);
        return [];
    }
}

// Populate the category dropdown
async function populateCategories() {
  const categories = await fetchCategories();
  const categorySelect = document.getElementById("category-select");

  categories.forEach((category) => {
    const option = document.createElement("option");
    option.value = category.id;
    option.textContent = category.name;
    categorySelect.appendChild(option);
  });
}

// Fetch subcategories for a given category ID
async function fetchSubcategories(categoryId) {
    try {
        const response = await fetch(`/api/categories/${categoryId}/subcategories/`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching subcategories:", error);
        return [];
    }
}


document.getElementById('add-category-btn').addEventListener('click', async () => {
  const categoryName = document.getElementById('new-category-input').value;
  if (!categoryName) {
      alert('Category name cannot be empty!');
      return;
  }

  try {
      const response = await fetch('/api/categories/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: categoryName }),
      });

      if (response.ok) {
          alert('Category added successfully!');
          populateCategories(); // Refresh categories
      } else {
          console.error('Error adding category:', response.statusText);
      }
  } catch (error) {
      console.error('Error adding category:', error);
  }
});



// Display subcategories in the list
async function displaySubcategories(categoryId) {
  const subcategories = await fetchSubcategories(categoryId);
  const subcategoryList = document.getElementById("subcategory-list");

  subcategoryList.innerHTML = ""; // Clear the list

  subcategories.forEach((subcategory) => {
    const li = document.createElement("li");
    li.textContent = subcategory.name;
    subcategoryList.appendChild(li);
  });
}

// Add event listener to the category select dropdown
const categorySelect = document.getElementById("category-select");
categorySelect.addEventListener("change", async () => {
  const categoryId = categorySelect.value;
  await displaySubcategories(categoryId);
});

// Call the function to populate the categories dropdown
populateCategories();
